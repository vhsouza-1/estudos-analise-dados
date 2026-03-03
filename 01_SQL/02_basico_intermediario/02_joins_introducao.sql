-- Exercício 1: Liste todos os veículos com suas respectivas cores
SELECT 
    e.nome AS veiculo,
    e.price AS preco,
    c.nome_cor AS cor
FROM estoque e
INNER JOIN cores c ON e.cor_id = c.id
ORDER BY e.nome;

-- Exercício 2: Liste todos os veículos com suas respectivas categorias
SELECT 
    e.nome AS veiculo,
    e.price AS preco,
    cat.nome_categoria AS categoria
FROM estoque e
INNER JOIN categorias cat ON e.categoria_id = cat.id
ORDER BY e.nome;

-- Exercício 3: Liste todos os veículos com cor e categoria (JOIN duplo)
SELECT 
    e.nome AS veiculo,
    e.price AS preco,
    c.nome_cor AS cor,
    cat.nome_categoria AS categoria
FROM estoque e
INNER JOIN cores c ON e.cor_id = c.id
INNER JOIN categorias cat ON e.categoria_id = cat.id
ORDER BY cat.nome_categoria, e.price DESC;

-- Exercício 4: LEFT JOIN - incluir veículos mesmo sem cor definida
SELECT 
    e.nome AS veiculo,
    e.price AS preco,
    COALESCE(c.nome_cor, '*** SEM COR ***') AS cor
FROM estoque e
LEFT JOIN cores c ON e.cor_id = c.id;

-- Exercício 5: LEFT JOIN - incluir veículos mesmo sem categoria definida
SELECT 
    e.nome AS veiculo,
    e.price AS preco,
    COALESCE(cat.nome_categoria, '*** SEM CATEGORIA ***') AS categoria
FROM estoque e
LEFT JOIN categorias cat ON e.categoria_id = cat.id;

-- Exercício 6: RIGHT JOIN (simulado com LEFT JOIN invertido)
-- Listar todas as cores, mesmo sem veículos associados
SELECT 
    c.nome_cor AS cor,
    COUNT(e.id) AS quantidade_veiculos
FROM cores c
LEFT JOIN estoque e ON c.id = e.cor_id
GROUP BY c.id, c.nome_cor
ORDER BY quantidade_veiculos DESC;

-- Exercício 7: JOIN com filtro - apenas carros
SELECT 
    e.nome AS veiculo,
    e.price AS preco,
    c.nome_cor AS cor
FROM estoque e
INNER JOIN cores c ON e.cor_id = c.id
INNER JOIN categorias cat ON e.categoria_id = cat.id
WHERE cat.nome_categoria = 'Carro'
ORDER BY e.price DESC;

-- Exercício 8: JOIN com filtro - motos vermelhas
SELECT 
    e.nome AS veiculo,
    e.price AS preco
FROM estoque e
INNER JOIN cores c ON e.cor_id = c.id
INNER JOIN categorias cat ON e.categoria_id = cat.id
WHERE cat.nome_categoria = 'Moto' 
  AND c.nome_cor = 'Vermelho'
ORDER BY e.price;

-- Exercício 9: JOIN com filtro de ano
SELECT 
    e.nome AS veiculo,
    e.fabrication AS ano,
    c.nome_cor AS cor,
    cat.nome_categoria AS categoria
FROM estoque e
INNER JOIN cores c ON e.cor_id = c.id
INNER JOIN categorias cat ON e.categoria_id = cat.id
WHERE e.fabrication > 2010
ORDER BY e.fabrication, e.nome;