-- Exercício 16: Veículos com preço acima da média da sua categoria
SELECT 
    e.nome AS veiculo,
    e.price AS preco,
    cat.nome_categoria AS categoria
FROM estoque e
JOIN categorias cat ON e.categoria_id = cat.id
WHERE e.price > (
    SELECT 
		AVG(price) 
    FROM estoque 
    WHERE categoria_id = e.categoria_id
)
ORDER BY cat.nome_categoria, e.price DESC;

-- Exercício 17: Diferença para a média da categoria
SELECT 
    e.nome AS veiculo,
    e.price AS preco,
    cat.nome_categoria AS categoria,
    ROUND(e.price - (
        SELECT 
			AVG(price) 
        FROM estoque 
        WHERE categoria_id = e.categoria_id
    ), 2) AS diferenca_media_categoria
FROM estoque e
JOIN categorias cat ON e.categoria_id = cat.id
ORDER BY diferenca_media_categoria DESC;

-- Exercício 18: Veículos cujo preço é maior que a média da sua cor
SELECT 
    e.nome AS veiculo,
    e.price AS preco,
    c.nome_cor AS cor
FROM estoque e
JOIN cores c ON e.cor_id = c.id
WHERE e.price > (
    SELECT 
		AVG(price) 
    FROM estoque 
    WHERE cor_id = e.cor_id
)
ORDER BY c.nome_cor, e.price DESC;

-- Exercício 19: Categorias onde o veículo mais caro supera em mais de 100% a média da categoria
SELECT DISTINCT
    cat.nome_categoria AS categoria,
    (SELECT MAX(price) FROM estoque WHERE categoria_id = cat.id) AS preco_maximo,
    (SELECT AVG(price) FROM estoque WHERE categoria_id = cat.id) AS preco_medio
FROM categorias cat
WHERE (
    SELECT MAX(price) FROM estoque WHERE categoria_id = cat.id
) > (
    SELECT AVG(price) * 2 FROM estoque WHERE categoria_id = cat.id
);

-- Exercício 20: Cor mais frequente entre os veículos mais caros de cada categoria
SELECT 
    c.nome_cor AS cor,
    COUNT(*) AS frequencia
FROM cores c
JOIN estoque e ON c.id = e.cor_id
WHERE (e.categoria_id, e.price) IN (
    SELECT categoria_id, MAX(price)
    FROM estoque
    GROUP BY categoria_id
)
GROUP BY c.id, c.nome_cor
ORDER BY frequencia DESC
LIMIT 1;