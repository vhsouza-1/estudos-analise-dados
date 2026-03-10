#EXERCÍCIOS - FUNÇÕES DE AGREGAÇÃO COM WINDOW FUNCTIONS

#Exercício 1-3: Fundamentos

#Exercício 1 - Total acumulado simples
#Liste todos os produtos com nome, preço, e uma coluna chamada total_acumulado que mostre a soma dos preços de todos os produtos até o momento, ordenado por preço (do mais caro para o mais barato). Use ROWS UNBOUNDED PRECEDING.

SELECT
	e.nome,
    e.preco,
    SUM(e.preco) OVER(ORDER BY e.preco DESC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW), -- só para testar a sintaxe ampliada
    SUM(e.preco) OVER(ORDER BY e.preco DESC ROWS UNBOUNDED PRECEDING) AS total_acumulado, -- sintaxe pedida no exercício
    SUM(e.preco) OVER(ORDER BY e.data_entrada DESC ROWS UNBOUNDED PRECEDING) -- faz o total acumulado por data de entrada, acredito que seja uma situação mais próxima do dia-a-dia.
FROM estoque e;

#Exercício 2 - Média por categoria
#Para cada produto, mostre nome, preço, categoria, e a média de preço da sua categoria. 

SELECT
	e.nome,
    e.preco,
    cat.nome_categoria,
    AVG(e.preco) OVER() AS media_total, -- só para comparação.
    AVG(e.preco) OVER(PARTITION BY cat.nome_categoria) AS media_categoria
FROM estoque e
LEFT JOIN categorias cat ON cat.id=e.categoria_id;

#Exercício 3 - Contagem progressiva
#Liste os produtos ordenados por data de entrada (da mais antiga para a mais nova). Adicione uma coluna chamada produtos_ate_agora que mostre quantos produtos já tinham entrado no estoque até aquela data (incluindo o atual).

SELECT
    e.data_entrada,
    e.nome,
    count(e.id) OVER(ORDER BY e.data_entrada ROWS UNBOUNDED PRECEDING) AS produtos_ate_agora -- poderia ser utilizado ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW, como o estoque é fixo, isso replica a coluna id.
FROM estoque e;

#Nível 4-6: Aplicações práticas

#Exercício 4 - Média móvel temporal
#Calcule a média móvel de preços considerando o produto atual e os dois anteriores na ordenação por data de entrada. Mostre nome, preco, data_entrada e a média móvel.

SELECT
	e.nome,
    e.preco,
    e.data_entrada,
    AVG(e.preco) OVER(ORDER BY e.data_entrada ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS media_movel_3
FROM estoque e;

#Exercício 5 - Diferença percentual da média
#Para cada produto, mostre nome, preco, categoria, a média da categoria e a diferença percentual entre o preço do produto e a média da sua categoria. Arredonde para 2 casas decimais.

SELECT
	e.nome,
    e.preco,
    cat.nome_categoria,
    AVG(e.preco) OVER(PARTITION BY cat.nome_categoria) AS media_categoria,
    e.preco-AVG(e.preco) OVER(PARTITION BY cat.nome_categoria) AS diferenca,
    concat(round(((e.preco/AVG(e.preco) OVER(PARTITION BY cat.nome_categoria))-1)*100, 2), '%') AS diferenca_percentual
FROM estoque e
LEFT JOIN categorias cat ON cat.id=e.categoria_id;

#Exercício 6 - Recordes de preço por categoria
#Para cada categoria, identifique quando um produto bateu o recorde de preço dentro daquela categoria até aquele momento (ordenado por data de entrada). 
#Mostre categoria, nome, preco, data_entrada e uma coluna "recorde" que diga 'Sim' ou 'Não'.

SELECT
	e.data_entrada,
    e.categoria_id,
    e.nome,
    e.preco,
	MAX(e.preco) OVER(PARTITION BY e.categoria_id ORDER BY e.data_entrada ROWS UNBOUNDED PRECEDING),
    CASE 
		WHEN e.preco >= MAX(e.preco) OVER(PARTITION BY e.categoria_id ORDER BY e.data_entrada ROWS UNBOUNDED PRECEDING) THEN 'Sim'
        ELSE 'Não'
    END AS recorde
FROM estoque e
ORDER BY e.categoria_id, e.data_entrada;

#Nível 7-10: Desafios analíticos

#Exercício 7 - Total acumulado por mês
#Crie um relatório que mostre, para cada mês (baseado em data_entrada): Mês (nome do mês), Total de preços dos produtos que entraram naquele mês
#Total acumulado até aquele mês (considerando todos os meses anteriores), Média móvel de 2 meses (mês atual + anterior)


WITH estoque_mes AS (
	SELECT
		month(e.data_entrada) AS mes,
        monthname(e.data_entrada) AS nome_mes,
		SUM(e.preco) AS total_mes
	FROM estoque e
	group by month(e.data_entrada), monthname(e.data_entrada)
)

SELECT 
    em.mes,
    em.nome_mes,
    em.total_mes,
    SUM(em.total_mes) OVER(ORDER BY em.mes ROWS UNBOUNDED PRECEDING) AS acumulado_mes, -- percebi que, nesse caso, se eu não escrever nada para o frame, ele é calcualdo como rows unbounded preceding por padrão. É normal deixar sem nada então?
	AVG(em.total_mes) OVER(ORDER BY em.mes ROWS BETWEEN 1 PRECEDING AND CURRENT ROW) AS media_movel_2
FROM estoque_mes em;

#Exercício 8 - Análise de vendas acumuladas. 
#Usando a tabela vendas, crie uma consulta que mostre: Data da venda, Produto vendido, Valor da venda, Total de vendas acumulado no mês (considere apenas vendas do mesmo mês, ordenadas por data)
#Percentual que cada venda representa do total acumulado até ela no mês

SELECT
	v.data_venda,
    e.nome,
    v.preco_venda,
    count(v.id_venda) OVER(PARTITION BY year(v.data_venda), month(v.data_venda) ORDER BY v.data_venda ROWS UNBOUNDED PRECEDING) AS qnt_vendas, -- aqui não precisava do ORDER BY nem do ROWS, mas coloquei para o caso de outro banco de dados.
    SUM(v.preco_venda) OVER(PARTITION BY year(v.data_venda), month(v.data_venda) ORDER BY v.data_venda ROWS UNBOUNDED PRECEDING) AS total_acumulado_mes,
    round((v.preco_venda/SUM(v.preco_venda) OVER(PARTITION BY month(v.data_venda) ORDER BY v.data_venda ROWS UNBOUNDED PRECEDING)*100), 2) AS percentual_venda -- 100% pois só tem uma venda por mês.
FROM vendas v
LEFT JOIN estoque e ON e.id = v.id_produto;

#Exercício 9 - Comparação com períodos anteriores
#Para cada venda na tabela vendas, mostre: Data, Valor, Média das vendas dos 3 dias anteriores (considere dias consecutivos, mesmo que não haja venda em algum dia)
#Diferença entre o valor da venda e essa média, Classificação: 'Acima' se valor > média, 'Abaixo' se valor < média, 'Igual' caso contrário.

WITH vendas_com_medias AS (
	SELECT
		v.data_venda,
		v.preco_venda,
		COALESCE(avg(v.preco_venda) OVER(ORDER BY v.data_venda ASC RANGE BETWEEN INTERVAL 3 DAY PRECEDING AND INTERVAL 1 DAY PRECEDING), 0) AS media_3dias_anteriores,
		v.preco_venda - COALESCE(avg(v.preco_venda) OVER(ORDER BY v.data_venda ASC RANGE BETWEEN INTERVAL 3 DAY PRECEDING AND INTERVAL 1 DAY PRECEDING), 0) AS diferenca
	FROM vendas v
)

SELECT
	*,
	CASE
		WHEN vcm.preco_venda > vcm.media_3dias_anteriores THEN 'Acima'
        WHEN vcm.preco_venda < vcm.media_3dias_anteriores THEN 'Abaixo'
        ELSE 'Igual'
    END AS classificacao
FROM vendas_com_medias vcm;

# Nesse caso o resultado dos exercícios foi um pouco estranho devido aos dados que eu estou utilizando, mas acredito que a lógica esta correta, certo?
#Usei coalesce dentro do WITH pq aquela coluna inteira estava retornando NULL, imagino que pq não existia nenhuma venda no intervalo
#Precisei pesquisar por conta própria como usar o RANGE. Foi tudo bem pq vc me indicou que eu precisava usar RANGE, isso é bom. Sempre indique e seja claro nesses casos.

#Exercício 10 - Desafio final - Dashboard gerencial
#Crie um relatório completo para a diretoria que mostre, por categoria de produto:
#Nome da categoria, Quantidade total de produtos, Preço médio dos produtos, Produto mais caro (nome e preço), Produto mais barato (nome e preço)
#Média móvel de preços considerando os 3 produtos mais recentes (por data_entrada) da categoria #Percentual que o produto mais caro representa do total acumulado da categoria (soma de todos os preços da categoria)
#Uma coluna de "saúde da categoria" que diga: 'Excelente' se a média da categoria > média geral + 20% #'Boa' se média da categoria entre a média geral e +20%
#'Regular' se média da categoria entre -20% e a média geral #'Preocupante' se média da categoria < média geral -20%

WITH estoque_ranking AS (
	SELECT
		e.id,
        e.nome,
        cat.nome_categoria,
        e.preco,
        e.data_entrada,
        ROW_NUMBER() OVER(PARTITION BY cat.nome_categoria ORDER BY e.preco ASC) AS ranking_barato,
		ROW_NUMBER() OVER(PARTITION BY cat.nome_categoria ORDER BY e.preco DESC) AS ranking_caro,
        -- calculo da média movel
        avg(e.preco) OVER(PARTITION BY cat.nome_categoria ORDER BY e.data_entrada ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS media_movel3,
        ROW_NUMBER() OVER(PARTITION BY cat.nome_categoria ORDER BY e.data_entrada DESC) AS indice_media, -- para filtrar a media movel numa das CTEs abaixo
        -- para dar acesso da media total à query princial
        avg(e.preco) OVER() AS media_total
    FROM estoque e
    LEFT JOIN categorias cat ON cat.id=e.categoria_id
),
produtos_mais_caros AS (
	SELECT
		*
    FROM estoque_ranking ek
    WHERE ek.ranking_caro = 1
),
produtos_mais_baratos AS (
	SELECT
		*
    FROM estoque_ranking ek
    WHERE ek.ranking_barato = 1
),
media_movel_categoria AS (
	SELECT
        ek.nome_categoria,
        ek.media_movel3
    FROM estoque_ranking ek
    WHERE ek.indice_media = 1
)

SELECT
	ek.nome_categoria,
    count(ek.id) AS qnt_produtos,
    round(avg(ek.preco),2) AS preco_medio_produtos_formatado,
    concat(pmc.nome, ': ', pmc.preco) AS produto_mais_caro,
    concat(pmb.nome, ': ', pmb.preco) AS produto_mais_barato,
    round(mmc.media_movel3,2) AS media_movel3_formatado,
    concat(round((max(ek.preco)/sum(ek.preco))*100,2), '%') AS percentual_prod_maiscaro,
    CASE
		WHEN avg(ek.preco) > (ek.media_total*1.2) THEN 'Excelente'
        WHEN avg(ek.preco) BETWEEN ek.media_total AND (ek.media_total*1.2) THEN 'Boa'
        WHEN avg(ek.preco) BETWEEN (ek.media_total*0.8) AND ek.media_total THEN 'Regular'
        WHEN avg(ek.preco) < (ek.media_total*0.8) THEN 'Preocupante'
    END saude_da_categoria
FROM estoque_ranking ek
LEFT JOIN produtos_mais_caros pmc ON pmc.nome_categoria=ek.nome_categoria
LEFT JOIN produtos_mais_baratos pmb ON pmb.nome_categoria=ek.nome_categoria
LEFT JOIN media_movel_categoria mmc ON mmc.nome_categoria=ek.nome_categoria
GROUP BY ek.nome_categoria, pmc.nome, pmc.preco, pmb.nome, pmb.preco, mmc.media_movel3, ek.media_total;
