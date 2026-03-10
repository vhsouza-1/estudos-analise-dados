#Exercício Funções de Ranking 2.0

#Exercícios 11-13 fáceis

#Exercício 11. Ranking com critério de desempate. Liste todos os produtos ordenados por preço (do maior para o menor). Em caso de empate no preço, desempate pelo nome em ordem alfabética. Use ROW_NUMBER().

SELECT
	e.nome,
    e.preco,
    ROW_NUMBER() OVER(ORDER BY e.preco DESC, e.nome) AS ranking -- testei colocar e.nome dentro do OVER e deu certo, testei com e.nome DESC também para confirmar.
FROM estoque e;

#Exercício 12 - Produtos mais antigos. Para cada categoria, liste os produtos ordenados do mais antigo para o mais novo (baseado no ano de fabricação). Use ROW_NUMBER() e mostre a posição de cada produto dentro da sua categoria.

SELECT
	e.nome,
    cat.nome_categoria,
    e.fabrication,
    ROW_NUMBER() OVER(PARTITION BY cat.nome_categoria ORDER BY e.fabrication) AS ranking_categoria -- aqui ta tudo bem pois não existem anos iguais no estoque
FROM estoque e
LEFT JOIN categorias cat ON cat.id=e.categoria_id;

#Exercício 13 - Preços únicos por categoria. 
#Crie um ranking de preços dentro de cada categoria, mas ignore duplicatas de preço (se dois produtos têm o mesmo preço, devem receber o mesmo ranking e o próximo preço deve pular as posições). Use a função adequada.

SELECT
	e.nome,
    e.preco,
    cat.nome_categoria,
    RANK() OVER(PARTITION BY cat.nome_categoria ORDER BY e.preco DESC) AS ranking
FROM estoque e
LEFT JOIN categorias cat ON cat.id=e.categoria_id;

#Exercícios 14-16: Aplicações práticas

#Exercício 14 - Os 3 produtos mais baratos de cada cor. 
#Encontre os 3 produtos com menor preço para cada cor. Mostre nome, preço, cor e o ranking utilizado.

WITH estoque_cores_ranking AS (
	SELECT
		e1.nome,
        e1.preco,
        c1.nome_cor,
        RANK() OVER(PARTITION BY c1.nome_cor ORDER BY e1.preco) AS ranking
    FROM estoque e1
    LEFT JOIN cores c1 ON c1.id=e1.cor_id
)

SELECT
	*
FROM estoque_cores_ranking ecr
WHERE ecr.ranking <=3;

#Exercício 15 - Distribuição por faixas
#Divida os produtos em 3 grupos de acordo com o preço (mais caros, médios, mais baratos). Use NTILE(3) e classifique cada grupo como 'Alto', 'Médio' ou 'Baixo'.

WITH estoque_ranking AS (
	SELECT
		e.nome,
		e.preco,
		NTILE(3) OVER(ORDER BY e.preco DESC) AS faixa
	FROM estoque e
)

SELECT
	ek.nome,
    ek.preco,
    CASE ek.faixa
		WHEN 1 THEN 'Alto'
        WHEN 2 THEN 'Médio'
        WHEN 3 THEN 'Baixo'
    END AS classificacao
FROM estoque_ranking ek;

#Exercício 16 - Comparação com a média da categoria
#Para cada produto, mostre: Nome, preço, categoria; Ranking de preço dentro da categoria (mais caro = 1)
#Uma coluna chamada "comparacao" que diga: 'Acima da média' se o preço for maior que a média da categoria; 'Abaixo da média' se for menor; 'Na média' se for igual

WITH estoque_ranking_medcat AS (
	SELECT
		e1.nome,
        e1.preco,
        cat1.nome_categoria,
        DENSE_RANK() OVER(PARTITION BY cat1.nome_categoria ORDER BY e1.preco DESC) AS ranking,
        AVG(e1.preco) OVER(PARTITION BY cat1.nome_categoria) AS preco_medio_categoria
    FROM estoque e1
    LEFT JOIN categorias cat1 ON cat1.id=e1.categoria_id
)

SELECT
	ekm.nome,
    ekm.preco,
    ekm.nome_categoria,
    ekm.ranking,
    CASE
		WHEN ekm.preco > ekm.preco_medio_categoria THEN 'Acima da média da categoria'
        WHEN ekm.preco = ekm.preco_medio_categoria THEN 'Na média da categoria'
        WHEN ekm.preco < ekm.preco_medio_categoria THEN 'Abaixo da média da categoria'
    END AS comparacao
FROM estoque_ranking_medcat ekm;

#Exercícios 17-20: Desafios

#Exercício 17 - Gaps no ranking
#Identifique se existem "gaps" (saltos) no ranking de preços quando usado RANK(). Para cada produto, mostre:
#Nome, preço, RANK() por preço (geral), DENSE_RANK() por preço, Uma coluna "tem_gap" que diga 'Sim' se a diferença entre RANK e DENSE_RANK for > 0

WITH estoque_rankings AS (
	SELECT
		e1.nome,
        e1.preco,
        RANK() OVER(ORDER BY e1.preco DESC) AS ranking_rank,
        DENSE_RANK() OVER(ORDER BY e1.preco DESC) AS ranking_dense_rank
    FROM estoque e1
)

SELECT
	*,
    CASE
		WHEN ranking_rank - ranking_dense_rank > 0 THEN 'Sim'
        ELSE '-'
    END tem_gap
FROM estoque_rankings;

#Exercício 18 - Top produtos por mês (baseado em data_entrada)
#Usando a tabela estoque, considere a data_entrada. Para cada mês (independente do ano), liste os 2 produtos com maior preço que entraram naquele mês. Mostre mês, nome, preço e ranking.

WITH estoque_ranking_mesentrada AS (
	SELECT
		monthname(e1.data_entrada) AS mes,
        e1.nome,
        e1.preco,
        RANK() OVER(PARTITION BY year(e1.data_entrada), month(e1.data_entrada) ORDER BY e1.preco DESC) AS ranking
    FROM estoque e1
)

SELECT
	*
FROM estoque_ranking_mesentrada
WHERE ranking <= 2;

#Exercício 19 - Quartis com categorização personalizada
#Divida os produtos em 4 quartis de preço (NTILE(4)). Para cada quartil, crie uma classificação: #Quartil 1: 'Premium', Quartil 2: 'Alto', Quartil 3: 'Médio', Quartil 4: 'Entrada'
#Além disso, mostre quantos produtos há em cada quartil (use uma segunda consulta ou CTE para isso).

WITH estoque_quartil AS (
	SELECT
		e1.nome,
		e1.preco,
		NTILE(4) OVER(ORDER BY e1.preco DESC) AS quartil
	FROM estoque e1
),
	estoque_quantidade_quartil AS (
	SELECT
		eq1.quartil,
        count(*) AS qnt_quartil
    FROM estoque_quartil eq1
    GROUP BY eq1.quartil
)

SELECT
	eq.nome,
    eq.preco,
    eq.quartil,
    CASE eq.quartil
		WHEN 1 THEN 'Premium'
        WHEN 2 THEN 'Alto'
        WHEN 3 THEN 'Médio'
        WHEN 4 THEN 'Entrada'
    END AS classificacao,
    eqq.qnt_quartil
FROM estoque_quartil eq
LEFT JOIN estoque_quantidade_quartil eqq ON eqq.quartil=eq.quartil;

#nesse caso, é melhor fazer 2 CTEs e usar o FROM e LEFT JOIN na query principal, ou seria melhor fazer uma única CTE e um JOIN com tabela derivada dentro dela para gerar a segunda CTE?
#Do jeito que eu fiz acredito que é mais legível e organizado, mas é assim que se costuma fazer?

#Exercício 20 - Desafio final - Relatório gerencial
#Crie um relatório que mostre para cada categoria: 
#Nome da categoria, Produto mais caro (nome e preço), Produto mais barato (nome e preço), Segundo produto mais caro (nome e preço), Média de preço da categoria, Quantidade total de produtos na categoria

WITH estoque_ranking_categorias AS (
	SELECT
		e.id,
        e.nome,
		e.preco,
		cat.nome_categoria,
		ROW_NUMBER() OVER(PARTITION BY cat.nome_categoria ORDER BY e.preco DESC) AS ranking_caro,
		ROW_NUMBER() OVER(PARTITION BY cat.nome_categoria ORDER BY e.preco) AS ranking_barato
	FROM estoque e
	LEFT JOIN categorias cat ON cat.id=e.categoria_id
),
	produto_1mais_caro AS (
	SELECT
		erc.nome,
        erc.preco,
        erc.nome_categoria
    FROM estoque_ranking_categorias erc
    WHERE erc.ranking_caro = 1
),
	produto_2mais_caro AS (
	SELECT
		erc.nome,
        erc.preco,
        erc.nome_categoria
    FROM estoque_ranking_categorias erc
    WHERE erc.ranking_caro = 2
),
	produto_1mais_barato AS (
	SELECT
		erc.nome,
        erc.preco,
        erc.nome_categoria
    FROM estoque_ranking_categorias erc
    WHERE erc.ranking_barato = 1
),
	media_e_quantidade_categoria AS (
	SELECT
		erc.nome_categoria,
        avg(erc.preco) AS media_categoria,
        count(erc.id) AS qnt_categoria
    FROM estoque_ranking_categorias erc
    GROUP BY erc.nome_categoria
)

SELECT
	cat.nome_categoria,
    concat(p1c.nome, ': ', p1c.preco) AS mais_caro,
    concat(p2c.nome, ': ', p2c.preco) AS segundo_mais_caro,
    concat(p1b.nome, ': ', p1b.preco) AS mais_barato,
    media_categoria,
    qnt_categoria
FROM categorias cat
LEFT JOIN produto_1mais_caro p1c ON p1c.nome_categoria=cat.nome_categoria
LEFT JOIN produto_2mais_caro p2c ON p2c.nome_categoria=cat.nome_categoria
LEFT JOIN produto_1mais_barato p1b ON p1b.nome_categoria=cat.nome_categoria
LEFT JOIN media_e_quantidade_categoria meq ON meq.nome_categoria=cat.nome_categoria;



