#Subconsultas Escalares

#Exercício 12 – Produtos com preço acima da média geral

SELECT 
    name AS "Veículo",
    price AS "Preço"
FROM estoque
WHERE price > (SELECT AVG(price) FROM estoque)
ORDER BY price;


#Exercício 13 – Produtos da cor prata com preço acima da média da própria cor

SELECT
    name AS "Veículo",
    price AS "Preço"
FROM estoque
WHERE color = 'prata' 
  AND price > (SELECT AVG(price) FROM estoque WHERE color = 'prata');


#Exercício 14 – Subconsulta no SELECT: diferença para a média geral

SELECT 
    name AS "Veículo", 
    price AS "Preço",
    ROUND(price - (SELECT AVG(price) FROM estoque), 2) AS "Diferença para a Média"
FROM estoque;

#Exercício 15 – Subconsulta no HAVING: tipos com preço médio maior que a média dos carros

SELECT 
    tipo AS "Tipo", 
    COUNT(*) AS "Quantidade", 
    ROUND(AVG(price), 2) AS "Preço Médio"
FROM estoque
GROUP BY tipo
HAVING AVG(price) > (SELECT AVG(price) FROM estoque WHERE tipo = 'carro');

#Subconsultas e agregações
#Exercício 16 – Segundo menor preço da tabela (sem LIMIT/OFFSET)

SELECT name AS "Veículo", price AS "Preço"
FROM estoque
WHERE price = (
    SELECT MIN(price) 
    FROM estoque 
    WHERE price > (SELECT MIN(price) FROM estoque)
);

#Exercício 17 – Produtos mais caros que o mais barato da cor vermelha

SELECT 
    name AS "Veículos",
    price AS "Preço"
FROM estoque
WHERE price > (SELECT MIN(price) FROM estoque WHERE color = 'vermelho')
ORDER BY price;


#Subconsultas Correlacionadas

#Exercício 18 – Mostrar cada produto com a média do seu tipo (correlacionada no SELECT)

SELECT 
    e1.name AS "Veículo",
    e1.tipo AS "Tipo",
    e1.price AS "Preço",
    (SELECT AVG(e2.price) 
     FROM estoque e2 
     WHERE e2.tipo = e1.tipo) AS "Média do Tipo"
FROM estoque e1;

#Exercício 19 – Produtos com preço acima da média do seu próprio tipo

SELECT 
    e1.name AS "Veículo",
    e1.tipo AS "Tipo",
    e1.price AS "Preço"
FROM estoque e1
WHERE e1.price > (
    SELECT AVG(e2.price) 
    FROM estoque e2 
    WHERE e2.tipo = e1.tipo
)
ORDER BY e1.tipo, e1.price DESC;