-- Exercício 10: Quantidade de veículos por cor
SELECT 
    c.nome_cor AS cor,
    COUNT(e.id) AS quantidade
FROM cores c
LEFT JOIN estoque e ON c.id = e.cor_id
GROUP BY c.id, c.nome_cor
ORDER BY quantidade DESC;

-- Exercício 11: Preço médio por categoria
SELECT 
    cat.nome_categoria AS categoria,
    ROUND(AVG(e.price), 2) AS preco_medio,
    MIN(e.price) AS preco_minimo,
    MAX(e.price) AS preco_maximo
FROM categorias cat
LEFT JOIN estoque e ON cat.id = e.categoria_id
GROUP BY cat.id, cat.nome_categoria;

-- Exercício 12: Cor com maior quantidade de veículos
SELECT 
    c.nome_cor AS cor,
    COUNT(e.id) AS quantidade
FROM cores c
LEFT JOIN estoque e ON c.id = e.cor_id
GROUP BY c.id, c.nome_cor
ORDER BY quantidade DESC
LIMIT 1;

-- Exercício 13: Categorias com mais de 3 veículos
SELECT 
    cat.nome_categoria AS categoria,
    COUNT(e.id) AS quantidade
FROM categorias cat
LEFT JOIN estoque e ON cat.id = e.categoria_id
GROUP BY cat.id, cat.nome_categoria
HAVING COUNT(e.id) > 3;

-- Exercício 14: Estatísticas completas por cor (apenas cores com veículos)
SELECT 
    c.nome_cor AS cor,
    COUNT(e.id) AS quantidade,
    ROUND(AVG(e.price), 2) AS preco_medio,
    MIN(e.price) AS preco_minimo,
    MAX(e.price) AS preco_maximo,
    ROUND(AVG(e.fabrication), 0) AS ano_medio
FROM cores c
INNER JOIN estoque e ON c.id = e.cor_id
GROUP BY c.id, c.nome_cor
ORDER BY quantidade DESC, preco_medio DESC;

-- Exercício 15: Comparativo entre categorias (diferença de preço médio)
SELECT 
    cat.nome_categoria AS categoria,
    ROUND(AVG(e.price), 2) AS preco_medio,
    ROUND(AVG(e.price) - (SELECT AVG(price) FROM estoque), 2) AS diferenca_media_geral
FROM categorias cat
LEFT JOIN estoque e ON cat.id = e.categoria_id
GROUP BY cat.id, cat.nome_categoria;