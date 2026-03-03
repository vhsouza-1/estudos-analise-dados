-- EXERCÍCIOS DE CASE WHEN


-- EXERCÍCIO 1: Classificação de preços

SELECT 
    e.nome,
    e.preco,
    CASE
        WHEN e.preco < 10000 THEN 'Barato'
        WHEN e.preco BETWEEN 10000 AND 25000 THEN 'Médio'
        WHEN e.preco > 25000 THEN 'Caro'
    END AS classificacao_preco
FROM estoque e
ORDER BY e.preco;


-- EXERCÍCIO 2: CASE no ORDER BY (ordem personalizada)

SELECT
    e.nome,
    e.cor_id,
    c.nome_cor
FROM estoque e
LEFT JOIN cores c ON c.id = e.cor_id
ORDER BY 
    CASE e.cor_id
        WHEN 2 THEN 1  -- Vermelho em primeiro
        WHEN 6 THEN 2  -- Azul em segundo
        WHEN 1 THEN 3  -- Branco em terceiro
        ELSE 4
    END;


-- EXERCÍCIO 3: Agregação condicional (Pivot Table)

SELECT
    COUNT(CASE WHEN e.preco <= 15000 THEN 1 END) AS 'Até 15000',
    COUNT(CASE WHEN e.preco BETWEEN 15001 AND 30000 THEN 1 END) AS '15001 até 30000',
    COUNT(CASE WHEN e.preco > 30000 THEN 1 END) AS 'Acima de 30000'
FROM estoque e;


-- EXERCÍCIO 4: Classificação combinada (múltiplas condições)

SELECT 
    e.id,
    e.nome,
    CONCAT('R$ ', REPLACE(REPLACE(REPLACE(FORMAT(e.preco, 2), '.', '@'), ',', '.'), '@', ',')) AS preco_formatado,
    e.fabrication,
    CASE 
        WHEN e.preco < 15000 AND e.fabrication >= 2015 THEN 'Baixo valor e novo'
        WHEN e.preco < 15000 AND e.fabrication < 2015 THEN 'Baixo valor e antigo'
        WHEN e.preco BETWEEN 15000 AND 30000 AND e.fabrication >= 2015 THEN 'Médio valor e novo'
        WHEN e.preco BETWEEN 15000 AND 30000 AND e.fabrication < 2015 THEN 'Médio valor e antigo'
        WHEN e.preco > 30000 AND e.fabrication >= 2015 THEN 'Alto valor e novo'
        WHEN e.preco > 30000 AND e.fabrication < 2015 THEN 'Alto valor e antigo'
    END AS valor_de_estoque
FROM estoque e
ORDER BY
    CASE valor_de_estoque
        WHEN 'Baixo valor e novo' THEN 1
        WHEN 'Baixo valor e antigo' THEN 2
        WHEN 'Médio valor e novo' THEN 3
        WHEN 'Médio valor e antigo' THEN 4
        WHEN 'Alto valor e novo' THEN 5
        WHEN 'Alto valor e antigo' THEN 6
    END;


-- EXERCÍCIO 5: Comparação com média da categoria

SELECT
    v.id_venda,
    e.nome,
    CONCAT('R$ ', REPLACE(REPLACE(REPLACE(FORMAT(v.preco_venda, 2), '.', '@'), ',', '.'), '@', ',')) AS preco_venda_formatado,
    CONCAT('R$ ', REPLACE(REPLACE(REPLACE(FORMAT(mc.media_categoria, 2), '.', '@'), ',', '.'), '@', ',')) AS media_categoria_formatado,
    CASE
        WHEN v.preco_venda > mc.media_categoria THEN 'Acima da média'
        WHEN v.preco_venda = mc.media_categoria THEN 'Na média'
        WHEN v.preco_venda < mc.media_categoria THEN 'Abaixo da média'
    END AS comparacao_categoria
FROM vendas v
LEFT JOIN estoque e ON e.id = v.id_produto
LEFT JOIN (
    SELECT
        e1.categoria_id,
        AVG(e1.preco) AS media_categoria
    FROM estoque e1
    GROUP BY e1.categoria_id
) mc ON mc.categoria_id = e.categoria_id;


-- EXERCÍCIO 6: Flag de promoção 

SELECT
    e.nome,
    c.nome_cor,
    cat.nome_categoria,
    DATEDIFF(CURDATE(), e.data_entrada) AS dias_em_estoque,
    CONCAT('R$ ', REPLACE(REPLACE(REPLACE(FORMAT(e.preco, 2), '.', '@'), ',', '.'), '@', ',')) AS preco_formatado,
    CASE
        WHEN (DATEDIFF(CURDATE(), e.data_entrada) > 120 OR e.preco > 40000)
            AND e.cor_id <> 2
            AND e.categoria_id <> 2
        THEN 'SIM'
        ELSE 'NÃO'
    END AS 'Promoção?'
FROM estoque e
LEFT JOIN cores c ON c.id = e.cor_id
LEFT JOIN categorias cat ON cat.id = e.categoria_id;


-- EXERCÍCIO 7: Ranking TOP 3 (versão com OR)

SELECT
    v.id_venda,
    e.nome,
    cat.nome_categoria,
    CONCAT('R$ ', REPLACE(REPLACE(REPLACE(FORMAT(v.preco_venda, 2), '.', '@'), ',', '.'), '@', ',')) AS preco_venda_formatado,
    CASE
        WHEN e.preco = (SELECT MAX(e1.preco) FROM estoque e1 WHERE e1.categoria_id = e.categoria_id) THEN 'TOP 1'
        WHEN e.preco = (SELECT e1.preco FROM estoque e1 WHERE e1.categoria_id = e.categoria_id ORDER BY e.preco DESC LIMIT 1 OFFSET 1)
           OR e.preco = (SELECT e1.preco FROM estoque e1 WHERE e1.categoria_id = e.categoria_id ORDER BY e.preco DESC LIMIT 1 OFFSET 2)
        THEN 'TOP 3'
        ELSE 'Demais'
    END AS classificacao
FROM vendas v
LEFT JOIN estoque e ON e.id = v.id_produto
LEFT JOIN categorias cat ON cat.id = e.categoria_id
ORDER BY 
    CASE classificacao
        WHEN 'TOP 1' THEN 1
        WHEN 'TOP 3' THEN 2
        WHEN 'Demais' THEN 3
    END;