#EXERCÍCIOS CTE (Common Table Expressions)
#(1-3 dificuldade 1)
#Exercício 1. Crie uma CTE chamada produtos_antigos que selecione produtos fabricados antes do ano 2000. Depois, conte quantos são.

WITH produtos_antigos AS (
	SELECT
		e.nome
	FROM estoque e
    WHERE e.fabrication < 2000
)
SELECT
	count(*) AS quantidade_produtos_antigos
FROM produtos_antigos pa;

#Exercício 2. Use uma CTE para calcular o preço médio dos produtos e depois selecione apenas os produtos com preço acima dessa média.

WITH preco_medio_tab AS (
	SELECT
        avg(e1.preco) AS preco_medio
	FROM estoque e1
)
SELECT
	e.nome
FROM estoque e
CROSS JOIN preco_medio_tab pm -- caso interessante de CROSS JOIN, não vi muitos.
WHERE e.preco > pm.preco_medio;


#Exercício 3. Crie uma CTE que calcule o valor total do estoque (preço * quantidade? ops... você não tem quantidade! Mas pode somar os preços como se fosse 1 de cada). Depois mostre esse total.

#Versão usando uma tab "quantidade" para simular o caso completo. Entretanto é redundante para o meu caso.
WITH quantidade_tab AS (
	SELECT 1 AS quantidade
),
	valor_total1 AS (
	SELECT
        SUM(e1.preco * q.quantidade) AS valor_total_estoque
    FROM estoque e1
    CROSS JOIN quantidade_tab q
)
SELECT * FROM valor_total1;

#Versão direta para o meu caso
WITH valor_total2 AS (
	SELECT
		SUM(e2.preco) AS valor_total_estoque
	FROM estoque e2
)
SELECT * FROM valor_total2;

#(4-6 dificuldade 2)
#Exercício 4. Crie duas CTEs: media_por_categoria: media dos preços por categoria; media_geral: média de todos os preços. Depois mostre as categorias que têm media acima da média geral.

WITH media_por_categoria AS (
	SELECT
		cat1.nome_categoria,
        avg(e1.preco) AS preco_medio_categoria
    FROM estoque e1
    LEFT JOIN categorias cat1 ON cat1.id=e1.categoria_id
    GROUP BY cat1.nome_categoria
),
	media_geral AS (
	SELECT 
		avg(e2.preco) AS preco_medio_geral
	FROM estoque e2
)

SELECT
	mpc.nome_categoria
FROM media_por_categoria mpc
CROSS JOIN media_geral mg
WHERE mpc.preco_medio_categoria > mg.preco_medio_geral;


#Exercícios 5. Use CTE para encontrar os produtos que nunca foram vendidos (dica: LEFT JOIN com vendas dentro da CTE).

WITH produtos_nao_vendidos_v1 AS (
	SELECT
        e1.nome
	FROM estoque e1
    LEFT JOIN vendas v1 ON v1.id_produto=e1.id
    WHERE v1.id_venda IS NULL -- versão sem subconsulta, mais leve
), 
	produtos_nao_vendidos_v2 AS (
	SELECT 
		e2.nome
	FROM estoque e2
    WHERE e2.id NOT IN (SELECT id_produto FROM vendas) -- versão com subconsulta
)

SELECT * FROM produtos_nao_vendidos_v1;

#Exercício 6. Crie uma CTE que adicione uma coluna de classificação (usando CASE WHEN) baseada no preço. Depois conte quantos produtos em cada classificação.

WITH estoque_com_classificacao AS (
	SELECT
		*,
		CASE -- usei essa classificação de outro exercício
			WHEN e1.preco > 25000 THEN 'Alto'
			WHEN e1.preco BETWEEN 15000 AND 25000 THEN 'Médio'
			WHEN e1.preco < 15000 THEN 'Baixo'
		END AS classificacao_preco
	FROM estoque e1
)
SELECT
	ecc.classificacao_preco,
    count(ecc.id)
FROM estoque_com_classificacao ecc
GROUP BY ecc.classificacao_preco;

#(7-9 dificuldade 3)
#Exercício 7. Use CTEs aninhadas (uma CTE que usa outra) para encontrar a categoria com a maior média de preço e listar todos os produtos dessa categoria.

WITH categoria_maior_media AS (
	SELECT
		cat1.nome_categoria,
        AVG(e1.preco) AS preco_medio_categoria
    FROM estoque e1
    LEFT JOIN categorias cat1 ON cat1.id=e1.categoria_id
    GROUP BY cat1.nome_categoria
    ORDER BY preco_medio_categoria DESC
    LIMIT 1
),
	produtos_categoria_mm AS ( -- mm de maior média
	SELECT
		e2.nome AS nome_produto
    FROM estoque e2
    LEFT JOIN categorias cat2 ON cat2.id = e2.categoria_id
    LEFT JOIN categoria_maior_media cmm ON cmm.nome_categoria = cat2.nome_categoria
    WHERE cat2.nome_categoria = cmm.nome_categoria
    )

SELECT * FROM produtos_categoria_mm;


# Exercício 8. Crie uma CTE que calcule, para cada mês de 2025, quantos produtos entraram no estoque. Complete os meses sem entrada com 0.

WITH calendario_mes AS (
	SELECT '1' AS mes UNION ALL
    SELECT '2' UNION ALL
    SELECT '3' UNION ALL
    SELECT '4' UNION ALL
    SELECT '5' UNION ALL
	SELECT '6' UNION ALL
    SELECT '7' UNION ALL
    SELECT '8' UNION ALL
    SELECT '9' UNION ALL
    SELECT '10' UNION ALL
    SELECT '11' UNION ALL
    SELECT '12'
)

SELECT
	cm.mes,
    count(e.id)
FROM calendario_mes cm
LEFT JOIN estoque e ON month(e.data_entrada) = cm.mes
where year(e.data_entrada) = 2025
GROUP BY cm.mes;

#Exercício 9. Usando CTEs, compare o preço médio dos produtos com suas respectivas cores com a média geral. Mostre apenas as cores cuja média é superior à geral.

WITH media_cores AS (
	SELECT
		c1.id,
        c1.nome_cor,
        avg(e1.preco) AS preco_medio_cor
    FROM estoque e1
    LEFT JOIN cores c1 ON c1.id=e1.cor_id
    GROUP BY c1.nome_cor
),
	media_geral AS (
	SELECT 
		avg(e2.preco) AS preco_medio_geral 
	FROM estoque e2
)
SELECT
	*
FROM media_cores mc 
CROSS JOIN media_geral mg
WHERE mc.preco_medio_cor > mg.preco_medio_geral