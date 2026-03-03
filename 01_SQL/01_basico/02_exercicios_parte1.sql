# Exercício 1 – Filtro com ordenação

SELECT 
    name AS "Veículo",
    price AS "Preço",
    fabrication AS "Ano de Fabricação"
FROM estoque
WHERE tipo = 'carro' AND fabrication > 2010
ORDER BY price ASC;


#Exercício 2 – LIKE e ordenação

SELECT *
FROM estoque
WHERE name LIKE 'F%';


#Exercício 3 – Operadores lógicos

SELECT name, price
FROM estoque
WHERE color = 'verde' OR color = 'preto'
ORDER BY name ASC;


#Exercício 4 – Contagem por cor

SELECT 
    color AS "Cor",
    COUNT(*) AS "Quantidade"
FROM estoque
GROUP BY color;


#Exercício 5 – Preço médio por tipo

SELECT 
    tipo,
    AVG(price) AS preco_medio
FROM estoque
GROUP BY tipo;


#Exercício 6 – Mínimo e máximo por tipo com diferença

SELECT
    tipo AS "Tipo",
    MIN(price) AS "Menor Preço",
    MAX(price) AS "Maior Preço",
    MAX(price) - MIN(price) AS "Diferença"
FROM estoque
GROUP BY tipo;


#Exercício 7 – Cores com mais de 2 produtos e preço médio > 15000

SELECT 
    color AS "Cor",
    COUNT(*) AS "Quantidade",
    ROUND(AVG(price), 2) AS "Preço Médio",
    MAX(price) AS "Preço Máximo"
FROM estoque
GROUP BY color
HAVING COUNT(*) >= 2 AND AVG(price) > 15000
ORDER BY COUNT(*) DESC;


#Exercício 8 – Anos com pelo menos 2 produtos e maior preço médio

SELECT 
    fabrication AS "Ano de Fabricação", 
    COUNT(*) AS "Quantidade", 
    AVG(price) AS "Preço Médio"
FROM estoque
GROUP BY fabrication
HAVING COUNT(*) >= 2
ORDER BY AVG(price) DESC
LIMIT 1;


#Exercício 9 – Os 3 produtos mais caros

SELECT name AS "Veículo", price AS "Preço"
FROM estoque
ORDER BY price DESC
LIMIT 3;


#Exercício 10 – Segundo produto mais barato

SELECT name AS "Veículo", price AS "Preço"
FROM estoque
ORDER BY price ASC
LIMIT 1 OFFSET 1;


#Exercício 11 – 4º ao 6º lugar no ranking de preços

SELECT name AS "Veículo", price AS "Preço"
FROM estoque
ORDER BY price DESC
LIMIT 3 OFFSET 3;