# Exercício 1: Usando a tabela estoque, crie uma CTE que calcule o preço médio por categoria. Depois, na consulta principal, mostre todos os produtos com:
# nome, preco, categoria, preco_medio_categoria e uma coluna chamada diferenca (preco - preco_medio_categoria) ordenado pelos produtos com maior diferença positiva primeiro

WITH medias_categorias AS (
	SELECT
		cat1.nome_categoria,
        round(avg(e1.preco), 2) AS preco_medio_categoria -- round só para a tabela final ficar mais bonitinha.
    FROM estoque e1
    LEFT JOIN categorias cat1 ON cat1.id=e1.categoria_id
    GROUP BY cat1.nome_categoria
)

SELECT
	e.id,
    e.nome,
	cat.nome_categoria,
    e.preco,
	mc.preco_medio_categoria,
    e.preco-mc.preco_medio_categoria AS diferenca
FROM estoque e
LEFT JOIN categorias cat ON cat.id=e.categoria_id
LEFT JOIN medias_categorias mc ON mc.nome_categoria=cat.nome_categoria
ORDER BY diferenca DESC;

#versão sem o LEFT JOIN com categorias na CTE. Link feito na consulta principal pelo id da categoria.
WITH medias_categorias AS (
	SELECT
		e1.categoria_id,
        round(avg(e1.preco), 2) AS preco_medio_categoria -- round só para a tabela final ficar mais bonitinha.
    FROM estoque e1
    GROUP BY e1.categoria_id
)

SELECT
	e.id,
    e.nome,
	cat.nome_categoria,
    e.preco,
	mc.preco_medio_categoria,
    e.preco-mc.preco_medio_categoria AS diferenca
FROM estoque e
LEFT JOIN categorias cat ON cat.id=e.categoria_id
LEFT JOIN medias_categorias mc ON mc.categoria_id=e.categoria_id
ORDER BY diferenca DESC;

# versão com LEFT JOIN com categorias na query principal. Qual das 3 é melhor? Eu imagino que jogar o left join pra dentro da CTE é melhor pq deixa a query principal mais limpa. Mas e o gasto computacional?
WITH medias_categorias AS (
	SELECT
		cat1.id,
        cat1.nome_categoria,
        round(avg(e1.preco), 2) AS preco_medio_categoria -- round só para a tabela final ficar mais bonitinha.
    FROM estoque e1
    LEFT JOIN categorias cat1 ON cat1.id=e1.categoria_id
    GROUP BY cat1.nome_categoria
)

SELECT
	e.id,
    e.nome,
	mc.nome_categoria,
    e.preco,
	mc.preco_medio_categoria,
    e.preco-mc.preco_medio_categoria AS diferenca
FROM estoque e
LEFT JOIN medias_categorias mc ON mc.id=e.categoria_id
ORDER BY diferenca DESC;


#Exercício 2. Crie um relatório com 3 CTEs: vendas_2025: vendas do ano 2025; total_ano: soma total das vendas em 2025; vendas_por_mes: total e percentual de cada mês em relação ao ano. Mostre: mês, total_mes, percentual

WITH vendas_2025 AS (
	SELECT
		*
	FROM vendas v1
    WHERE year(v1.data_venda) = 2025
),
	total_ano_2025 AS (
	SELECT
		SUM(v2025.preco_venda) AS soma_venda
    FROM vendas_2025 v2025
),
	vendas_por_mes AS ( -- essa tabela não cobre todos os meses, seria necessário uma tabela de calendário, mas como em um cenário real temos vendas todos os meses, não seria um problema.
	SELECT
		month(v2.data_venda) AS num_mes,
        monthname(v2.data_venda) AS nome_mes,
        SUM(v2.preco_venda) AS total_mes,
        round((SUM(v2.preco_venda)/MAX(ta2025.soma_venda))*100,2) AS percentual_mes -- aqui usei o MAX para soma_venda estar dentro de uma função de agregação.
    FROM vendas v2
    CROSS JOIN total_ano_2025 ta2025
    GROUP BY month(v2.data_venda), monthname(v2.data_venda)
    ORDER BY percentual_mes DESC -- ordenando por mês que mais contribuiu no percentual.
)

SELECT * FROM vendas_por_mes;


#Exercício 3. Sem usar Window Functions, crie um ranking dos produtos mais caros do estoque (do mais caro para o mais barato).
#Extra: Depois mostre apenas os top 3 de cada categoria.

WITH ranking_produtos AS (
	SELECT
		e1.nome,
        e1.preco,
        cat1.nome_categoria
    FROM estoque e1
    LEFT JOIN categorias cat1 ON cat1.id = e1.categoria_id
    ORDER BY cat1.nome_categoria, e1.preco DESC
)
SELECT
	rp1.nome,
    rp1.preco,
    rp1.nome_categoria,
    count(rp2.nome)+1 AS ranking
FROM ranking_produtos rp1
LEFT JOIN ranking_produtos rp2 
	ON rp1.nome_categoria = rp2.nome_categoria 
    AND rp2.preco > rp1.preco
GROUP BY rp1.nome, rp1.preco, rp1.nome_categoria
HAVING count(rp2.nome)+1 < 4 -- única mudança em relação ao exercício 8. Filtrei os grupos (veículos) no TOP 3 de suas categorias.
ORDER BY rp1.nome_categoria, ranking;


#Exercício 4 - Crie uma CTE chamada status_vendas que classifique cada venda: 'Recente' se data_venda for no último trimestre de 2025; 'Antiga' se for antes disso; 'Futura' se for depois (não há, mas para exercício)

WITH status_venda AS (
	SELECT
		*,
        CASE
			WHEN year(v1.data_venda)=2025 AND month(v1.data_venda) BETWEEN 10 AND 12 THEN 'Recente'
            WHEN (year(v1.data_venda)=2025 AND month(v1.data_venda) BETWEEN 1 AND 9) OR year(v1.data_venda) < 2025 THEN 'Antiga'
            WHEN year(v1.data_venda) > 2025 THEN 'Futura'
        END AS classificacao
    FROM vendas v1
)
SELECT * FROM status_venda;


#Exercício 5. Sem usar Window Functions, calcule para cada produto do estoque: O preço do produto, O preço médio da sua categoria, A diferença (preco - media_categoria)
#A posição no ranking dentro da categoria (1 = mais caro da categoria)

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
