-- Exercício 21: Listar veículos com a quantidade total de veículos da mesma cor
SELECT
    e.nome AS veiculo,
    e.price AS preco,
    c.nome_cor AS cor,
    tot.total_cores AS veiculos_mesma_cor
FROM estoque e
LEFT JOIN cores c ON c.id = e.cor_id
LEFT JOIN (
    SELECT 
		cor_id, 
        COUNT(*) AS total_cores
    FROM estoque
    WHERE cor_id IS NOT NULL
    GROUP BY cor_id
) tot ON tot.cor_id = e.cor_id
ORDER BY tot.total_cores DESC, e.price DESC;

-- Exercício 22: Veículos com preço acima da média da sua cor
-- (usando tabela derivada para pré-calcular as médias)
SELECT 
    e.nome AS veiculo,
    e.price AS preco,
    c.nome_cor AS cor,
    med.media_cor AS media_da_cor
FROM estoque e
JOIN cores c ON e.cor_id = c.id
JOIN (
    SELECT 
		cor_id, 
        AVG(price) AS media_cor
    FROM estoque
    WHERE cor_id IS NOT NULL
    GROUP BY cor_id
) med ON e.cor_id = med.cor_id
WHERE e.price > med.media_cor
ORDER BY (e.price - med.media_cor) DESC;

-- Exercício 23: Ranking de veículos dentro de cada cor
SELECT 
    e.nome AS veiculo,
    e.price AS preco,
    c.nome_cor AS cor,
    rank_cor.ranking
FROM estoque e
JOIN cores c ON e.cor_id = c.id
JOIN (
    SELECT 
        e1.id,
        e1.cor_id,
        COUNT(*) AS ranking
    FROM estoque e1
    JOIN estoque e2 ON e1.cor_id = e2.cor_id
    GROUP BY e1.id, e1.cor_id
) rank_cor ON e.id = rank_cor.id
ORDER BY c.nome_cor, ranking;

-- Exercício 24: Cores com preço médio acima da média geral
SELECT 
    c.nome_cor AS cor,
    med.media_cor AS preco_medio,
    med.quantidade
FROM cores c
JOIN (
    SELECT 
		cor_id, 
        AVG(price) AS media_cor, 
        COUNT(*) AS quantidade
    FROM estoque
    WHERE cor_id IS NOT NULL
    GROUP BY cor_id
    HAVING AVG(price) > (SELECT AVG(price) FROM estoque)
) med ON c.id = med.cor_id
ORDER BY med.media_cor DESC;

-- Exercício 25: Diferença entre o preço do veículo e a média da sua cor
SELECT 
    e.nome AS veiculo,
    e.price AS preco,
    c.nome_cor AS cor,
    ROUND(med.media_cor, 2) AS media_cor,
    ROUND(e.price - med.media_cor, 2) AS diferenca
FROM estoque e
JOIN cores c ON e.cor_id = c.id
JOIN (
    SELECT 
		cor_id, 
        AVG(price) AS media_cor
    FROM estoque
    WHERE cor_id IS NOT NULL
    GROUP BY cor_id
) med ON e.cor_id = med.cor_id
ORDER BY diferenca DESC;
