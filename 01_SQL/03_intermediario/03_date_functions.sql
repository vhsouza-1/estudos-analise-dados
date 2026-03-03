-- EXERCÍCIOS DE FUNÇÕES DE DATA

-- EXERCÍCIO 1: Análise de tempo em estoque

SELECT
    e.nome,
    e.data_entrada,
    DATEDIFF(CURDATE(), e.data_entrada) AS dias_em_estoque,
    CASE -- esse exercício fiz depois de aprender a usar WHEN
        WHEN DATEDIFF(CURDATE(), e.data_entrada) <= 30 THEN 'Menos de 1 mês'
        WHEN DATEDIFF(CURDATE(), e.data_entrada) BETWEEN 31 AND 90 THEN '1-3 meses'
        WHEN DATEDIFF(CURDATE(), e.data_entrada) > 90 THEN 'Mais de 3 meses'
    END AS faixa_tempo
FROM estoque e;


-- EXERCÍCIO 2: Idade do produto na data da venda. Considera fabricação em 01/01 do ano de fabricação

SELECT
    e.nome,
    v.data_venda,
    DATEDIFF(v.data_venda, CONCAT(e.fabrication, '-01-01')) AS idade_na_venda_dias,
    FLOOR(DATEDIFF(v.data_venda, CONCAT(e.fabrication, '-01-01')) / 365) AS idade_na_venda_anos
FROM vendas v
LEFT JOIN estoque e ON e.id = v.id_produto
WHERE DATEDIFF(v.data_venda, CONCAT(e.fabrication, '-01-01')) > 1000;


-- EXERCÍCIO 3: Comparação mês a mês (entradas vs vendas)

SELECT
    MONTHNAME(e.data_entrada) AS mes,
    COUNT(*) AS quant_entrada,
    COUNT(vend.nome_mes) AS quant_venda
FROM estoque e
LEFT JOIN (
    SELECT
        MONTHNAME(v.data_venda) AS nome_mes,
        COUNT(*) AS total_vendas
    FROM vendas v
    GROUP BY MONTHNAME(v.data_venda)
) vend ON vend.nome_mes = MONTHNAME(e.data_entrada)
GROUP BY MONTHNAME(e.data_entrada);


-- EXERCÍCIO 4: Análise por estações do ano (hemisfério sul)

SELECT -- esse exercício eu fiz antes de aprender CASE WHEN, por isso a "gambiarra"
    v.id_venda,
    e.nome,
    v.data_venda,
    (SELECT DISTINCT 'X' FROM vendas v1 
     WHERE v1.id_venda = v.id_venda 
       AND DATE_FORMAT(v1.data_venda, '%m-%d') BETWEEN '09-21' AND '12-20') AS 'Primavera?',
    (SELECT DISTINCT 'X' FROM vendas v1 
     WHERE v1.id_venda = v.id_venda 
       AND (DATE_FORMAT(v1.data_venda, '%m-%d') BETWEEN '12-21' AND '12-31' 
            OR DATE_FORMAT(v1.data_venda, '%m-%d') BETWEEN '01-01' AND '03-20')) AS 'Verão?',
    (SELECT DISTINCT 'X' FROM vendas v1 
     WHERE v1.id_venda = v.id_venda 
       AND DATE_FORMAT(v1.data_venda, '%m-%d') BETWEEN '03-21' AND '06-20') AS 'Outono?',
    (SELECT DISTINCT 'X' FROM vendas v1 
     WHERE v1.id_venda = v.id_venda 
       AND DATE_FORMAT(v1.data_venda, '%m-%d') BETWEEN '06-21' AND '09-20') AS 'Inverno?'
FROM vendas v
LEFT JOIN estoque e ON e.id = v.id_produto;


-- EXERCÍCIO 5: Análise por dia da semana (com filtro de fim de semana)

SELECT
    v.id_venda,
    e.nome,
    v.data_venda,
    DAYOFWEEK(v.data_venda) AS dia_numero,
    DAYNAME(v.data_venda) AS dia_nome
FROM vendas v
LEFT JOIN estoque e ON e.id = v.id_produto
WHERE DAYOFWEEK(v.data_venda) IN (1, 7); -- 1 = domingo e 7 = sábado


-- EXERCÍCIO 6: Relatório completo com formatação brasileira

SET lc_time_names = 'pt_BR'; -- presente no enunciado do exercício

SELECT
    v.id_venda,
    e.nome,
    DATE_FORMAT(v.data_venda, '%d de %M de %Y') AS data_formatada,
    CONCAT(
        UPPER(LEFT(MONTHNAME(v.data_venda), 1)),
        LOWER(SUBSTRING(MONTHNAME(v.data_venda), 2))
    ) AS mes_formatado,
    DATEDIFF(CURDATE(), v.data_venda) AS dias_desde_venda,
    CASE
        WHEN DATEDIFF(CURDATE(), v.data_venda) <= 30 THEN 'Venda recente'
        ELSE 'Venda antiga'
    END AS status_venda
FROM vendas v
LEFT JOIN estoque e ON e.id = v.id_produto;