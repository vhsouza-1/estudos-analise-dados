-- EXERCÍCIOS DE UNION / UNION ALL


-- EXERCÍCIO 1: Lista combinada (produtos + clientes)

SELECT
    'Produto' AS tipo,
    e.nome AS identificacao
FROM estoque e
UNION ALL
SELECT
    'Cliente',
    v.cliente_nome
FROM vendas v;


-- EXERCÍCIO 2: Timeline completa do sistema

SELECT
    e.data_entrada AS data,
    'Entrada' AS tipo_evento,
    e.nome AS produto
FROM estoque e
UNION ALL
SELECT
    v.data_venda,
    'Venda',
    e.nome
FROM vendas v
LEFT JOIN estoque e ON e.id = v.id_produto
ORDER BY data;


-- EXERCÍCIO 3: Contagem de registros por tabela

SELECT
    'estoque' AS tabela,
    COUNT(*) AS contagem_registros
FROM estoque
UNION ALL
SELECT
    'vendas',
    COUNT(*) 
FROM vendas
UNION ALL
SELECT
    'cores',
    COUNT(*) 
FROM cores
UNION ALL
SELECT
    'categorias',
    COUNT(*) 
FROM categorias
ORDER BY contagem_registros DESC;


-- EXERCÍCIO 4: Produtos vendidos vs não vendidos

SELECT
    'Vendido' AS estado,
    e.nome
FROM vendas v
LEFT JOIN estoque e ON e.id = v.id_produto
UNION ALL
SELECT
    'Não vendido',
    e.nome
FROM estoque e
WHERE e.id NOT IN (SELECT v1.id_produto FROM vendas v1);


-- EXERCÍCIO 5: Lista de anos únicos no sistema

SELECT
    e1.fabrication AS anos
FROM estoque e1
UNION
SELECT
    YEAR(e2.data_entrada)
FROM estoque e2
UNION
SELECT
    YEAR(v.data_venda)
FROM vendas v
ORDER BY anos;


-- EXERCÍCIO 6: Relatório de meses (completando meses sem vendas)

SELECT
    cal.mes_nome,
    COUNT(vcm.id_venda) AS quantidade_vendas,
    CASE
        WHEN SUM(vcm.preco_venda) IS NULL THEN 0
        ELSE SUM(vcm.preco_venda)
    END AS total_vendido
FROM (
    SELECT *, MONTHNAME(data_venda) AS mes_nome
    FROM vendas
) vcm
RIGHT JOIN (
    SELECT '1' AS mes, MONTHNAME('2000-01-01') AS mes_nume UNION ALL 
    SELECT '2', MONTHNAME('2000-02-01') UNION ALL
    SELECT '3', MONTHNAME('2000-03-01') UNION ALL 
    SELECT '4', MONTHNAME('2000-04-01') UNION ALL
    SELECT '5', MONTHNAME('2000-05-01') UNION ALL 
    SELECT '6', MONTHNAME('2000-06-01') UNION ALL
    SELECT '7', MONTHNAME('2000-07-01') UNION ALL 
    SELECT '8', MONTHNAME('2000-08-01') UNION ALL
    SELECT '9', MONTHNAME('2000-09-01') UNION ALL 
    SELECT '10', MONTHNAME('2000-10-01') UNION ALL
    SELECT '11', MONTHNAME('2000-11-01') UNION ALL 
    SELECT '12', MONTHNAME('2000-12-01')
) cal ON cal.mes_nome = vcm.mes_nome -- aqui tive essa sacada de criar um "calendário" para otimizar o processamento
GROUP BY cal.mes_nome;


-- EXERCÍCIO 7: Comparação de abordagens (CASE WHEN vs UNION)

-- Versão com CASE WHEN (mais eficiente - 1 varredura)
SELECT
    e.nome,
    e.preco AS preco_estoque,
    v.preco_venda,
    v.preco_venda - e.preco AS diferenca,
    CASE 
        WHEN (v.preco_venda - e.preco) > 0 THEN 'Acima'
        WHEN (v.preco_venda - e.preco) = 0 THEN 'Igual'
        WHEN (v.preco_venda - e.preco) < 0 THEN 'Abaixo'
    END AS relacao_preco_estoque
FROM vendas v
LEFT JOIN estoque e ON e.id = v.id_produto
ORDER BY 
    CASE relacao_preco_estoque
        WHEN 'Acima' THEN 1
        WHEN 'Igual' THEN 2
        WHEN 'Abaixo' THEN 3
    END;

-- Versão com UNION (3 varreduras - menos eficiente para este caso)

-- Mantida para demonstrar análise comparativa

SELECT e.nome, e.preco, v.preco_venda, v.preco_venda - e.preco AS diferenca, 'Acima' AS relacao
FROM vendas v LEFT JOIN estoque e ON e.id=v.id_produto WHERE (v.preco_venda - e.preco) > 0
UNION ALL
SELECT e.nome, e.preco, v.preco_venda, v.preco_venda - e.preco, 'Igual'
FROM vendas v LEFT JOIN estoque e ON e.id=v.id_produto WHERE (v.preco_venda - e.preco) = 0
UNION ALL
SELECT e.nome, e.preco, v.preco_venda, v.preco_venda - e.preco, 'Abaixo'
FROM vendas v LEFT JOIN estoque e ON e.id=v.id_produto WHERE (v.preco_venda - e.preco) < 0;



-- EXERCÍCIO 8: Distribuição de cores por categoria

SELECT 
    'Carro' AS categoria,
    c.nome_cor AS cor,
    COUNT(*) AS quantidade_por_cor
FROM estoque e
LEFT JOIN cores c ON c.id = e.cor_id
LEFT JOIN categorias cat ON cat.id = e.categoria_id
WHERE cat.nome_categoria = 'Carro'
GROUP BY c.nome_cor
UNION ALL
SELECT 
    'Moto',
    c.nome_cor,
    COUNT(*)
FROM estoque e
LEFT JOIN cores c ON c.id = e.cor_id
LEFT JOIN categorias cat ON cat.id = e.categoria_id
WHERE cat.nome_categoria = 'Moto'
GROUP BY c.nome_cor;