#Windows Function - Funções de Ranking

#Exercícios 1-3: Básico

#Exercício 1. Ranking simples: Liste todos os produtos com suas respectivas posições no ranking geral de preços (do mais caro para o mais barato). Use ROW_NUMBER().

SELECT 
	e.nome,
    e.preco,
    ROW_NUMBER() OVER(ORDER BY e.preco DESC) AS	ranking
FROM estoque e;

#Exercício 2: Ranking por categoria: Liste os produtos com suas posições dentro de cada categoria (mais caro primeiro).

SELECT
	e.nome,
    e.preco,
    cat.nome_categoria,
    ROW_NUMBER() OVER(PARTITION BY cat.nome_categoria ORDER BY e.preco DESC) AS ranking
FROM estoque e	
LEFT JOIN categorias cat ON cat.id = e.categoria_id
ORDER BY cat.nome_categoria, ranking;

#Exercício 3: Comparação de rankings: Para cada produto, mostre: nome, preco, categoria; ROW_NUMBER() por categoria; RANK() por categoria; DENSE_RANK() por categoria. Explique as diferenças que você observa.

SELECT
	e.nome,
    e.preco,
    cat.nome_categoria,
    ROW_NUMBER() OVER(PARTITION BY cat.nome_categoria ORDER BY e.preco DESC) AS 'ROW_NUMBER p/ categoria', 
    RANK() OVER(PARTITION BY cat.nome_categoria ORDER BY e.preco DESC) AS 'RANK p/ categoria', 
    DENSE_RANK() OVER (PARTITION BY cat.nome_categoria ORDER BY e.preco DESC) AS 'DENSE_RANK p/ categoria' 
FROM estoque e
LEFT JOIN categorias cat ON cat.id = e.categoria_id; -- como não teve nenhum empate, os resultados são idênticos

SELECT
	e.nome,
    e.preco,
    cat.nome_categoria,
    ROW_NUMBER() OVER(ORDER BY e.preco DESC) AS 'ROW_NUMBER', -- ranking sem empates
    RANK() OVER(ORDER BY e.preco DESC) AS 'RANK', -- rank com empate, próximo colocado ao empate pula os números relacionados ao empate
    DENSE_RANK() OVER (ORDER BY e.preco DESC) AS 'DENSE_RANK' -- rank com empate, próximo colocado ao empate não pula números relacionados ao empate.
FROM estoque e
LEFT JOIN categorias cat ON cat.id = e.categoria_id; -- nesse caso que possui empates, os resultados são diferentes.

#Exercícios 4-7: Intermediário

#Exercício 4: Encontre os 2 produtos mais caros de cada categoria.

WITH produtos_ranqueados_categorias AS ( -- CTE necessária pq o ranking é processado depois do where.
	SELECT 
		e.nome,
		e.preco,
		cat.nome_categoria,
		DENSE_RANK() OVER(PARTITION BY cat.nome_categoria ORDER BY e.preco DESC) AS ranking -- usei DENSE_RANK para o caso de empates no primeiro lugar.
	FROM estoque e
	LEFT JOIN categorias cat ON cat.id=e.categoria_id
)

SELECT
	*
FROM produtos_ranqueados_categorias prc
WHERE ranking <= 2
;

#Exercício 5: Quartis de preço: Divida os produtos em 4 grupos (quartis) baseado no preço. Mostre nome, preco e quartil.

SELECT
	e.nome,
    e.preco,
    concat(NTILE(4) OVER(ORDER BY e.preco DESC), '° quartil') AS quartil -- só para ver como fica
FROM estoque e;

#Exercício 6: Dentro vs fora do top 3: Para cada categoria, classifique os produtos como 'Top 3' ou 'Demais' baseado no ranking de preço.

WITH estoque_ranking AS (
	SELECT 
		e.nome,
		e.preco,
		cat.nome_categoria,
		DENSE_RANK() OVER(PARTITION BY cat.nome_categoria ORDER BY e.preco DESC) AS ranking
		
	FROM estoque e
	LEFT JOIN categorias cat ON cat.id = e.categoria_id
)

SELECT
	*,
    CASE
		WHEN er.ranking <=3 THEN 'Top 3'
        ELSE 'Demais' 
    END AS classificacao
FROM estoque_ranking er;

#Qual o gasto computacional de utilizar o dense_rank e o case? Será que ele faz um cálculo para cada linha como uma subquery correlacionada?

#Exercício 7: Maior preço por cor: Para cada cor, qual o produto mais caro? (Dica: use ROW_NUMBER() e filtre)

WITH produtos_rank_cor AS (
	SELECT 
		e.nome,
		e.preco,
		c.nome_cor,
		DENSE_RANK() OVER(PARTITION BY c.nome_cor ORDER BY e.preco DESC) AS ranking -- usei dense_rank no lugar de row_number pois acho mais adequado, caso tenha empate. Poderia ter usado RANK tbm para esse caso.
	FROM estoque e
	LEFT JOIN cores c ON c.id=e.cor_id
)
SELECT
	prc.nome,
    prc.preco,
    prc.nome_cor,
    prc.ranking
FROM produtos_rank_cor prc
WHERE prc.ranking = 1
;

#Exercício 8-10: Avançado

#Exercício 9: Comparação com exercício anterior: Refaça o exercício 5 da lista anterior (ranking manual com SELF JOIN) usando ROW_NUMBER(). Compare a complexidade do código.

# (da lista anterior)Exercício 5. Sem usar Window Functions, calcule para cada produto do estoque: O preço do produto, O preço médio da sua categoria, A diferença (preco - media_categoria)
#A posição no ranking dentro da categoria (1 = mais caro da categoria)

#Minha resolução foi essa:

WITH medias_categorias AS (
	SELECT
		cat1.id,
        cat1.nome_categoria,
        round(avg(e1.preco), 2) AS preco_medio
	FROM estoque e1
    LEFT JOIN categorias cat1 ON cat1.id=e1.categoria_id
    GROUP BY cat1.id, cat1.nome_categoria
),
	estoque_com_media AS ( -- a princípio não ia fazer essa CTE, mas quando tentei fazer tudo da query principal, achei bem confuso.
    SELECT 
		e1.id,
        e1.nome,
		mc.nome_categoria,
		e1.preco,
		mc.preco_medio
	FROM estoque e1
	LEFT JOIN medias_categorias mc ON mc.id=e1.categoria_id
)
SELECT
    ecm1.nome,
	ecm1.preco,
    ecm1.nome_categoria,
    ecm1.preco_medio AS preco_medio_cat,
    ecm1.preco-ecm1.preco_medio AS diferenca,
    count(ecm2.nome) + 1 AS posicao
FROM estoque_com_media ecm1
LEFT JOIN estoque_com_media ecm2 
	ON ecm1.nome_categoria = ecm2.nome_categoria
    AND ecm2.preco > ecm1.preco
GROUP BY ecm1.id, ecm1.nome, ecm1.nome_categoria, ecm1.preco, ecm1.preco_medio -- aqui coloquei todo mundo no group by. Por que deu certo mesmo o ecm1.preco_medio não sendo um match 1 pra 1?
ORDER BY ecm1.nome_categoria, ecm1.preco DESC;

#Resolução com WF:

SELECT
	e.nome,
    e.preco,
    cat.nome_categoria,
    avg(e.preco) OVER (PARTITION BY cat.nome_categoria) AS preco_medio_categoria,
    e.preco - (avg(e.preco) OVER (PARTITION BY cat.nome_categoria)) AS diferenca,
    DENSE_RANK() OVER(PARTITION BY cat.nome_categoria ORDER BY e.preco DESC) AS ranking
FROM estoque e
LEFT JOIN categorias cat ON cat.id=e.categoria_id;

#Basicamente o código é infinitamente mais simples... 


#Exercício 10: Desafio final - relatório completo: Crie um relatório que mostre para cada venda: Data, produto, valor, Ranking da venda por valor (maior venda primeiro)
#Ranking da venda dentro do seu mês, Percentil (NTILE(100)) da venda considerando todas as vendas
#Além disso, adicione uma coluna "flag_top3_mes" que diga 'Sim' se a venda estiver no top 3 do seu mês

WITH vendas_ranking AS (
SELECT 
	v.data_venda,
    e.nome,
    v.preco_venda,
    DENSE_RANK() OVER(ORDER BY v.preco_venda DESC) AS ranking_valor,
    DENSE_RANK() OVER(PARTITION BY month(v.data_venda) ORDER BY v.preco_venda DESC) AS ranking_mes,
    NTILE(100) OVER(ORDER BY v.preco_venda) AS percentil -- aqui no meu caso fica meio estranho, porque tenho poucos entradas na tabela venda.
FROM vendas v
LEFT JOIN estoque e ON e.id=v.id_produto
)
SELECT 
	*,
    CASE
		WHEN vk.ranking_mes <= 3 THEN 'Sim'
        ELSE '-'
    END AS flag_top3_mes
FROM vendas_ranking vk;