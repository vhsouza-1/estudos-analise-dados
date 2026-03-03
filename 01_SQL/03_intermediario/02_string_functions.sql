
-- Funções de String


-- EXERCÍCIO 2: Mascaramento de dados (LGPD style): Primeira letra do primeiro nome + primeira letra do último nome

SELECT
    v.cliente_nome,
    CONCAT(
        UPPER(LEFT(v.cliente_nome, 1)), '. ',
        UPPER(LEFT(SUBSTRING_INDEX(v.cliente_nome, ' ', -1), 1)), '.'
    ) AS iniciais_mascaradas
FROM vendas v;


-- EXERCÍCIO 3: Email fictício corporativo

SELECT
    v.cliente_nome,
    LOWER(CONCAT(
        LEFT(v.cliente_nome, 1),
        '.',
        REPLACE(SUBSTRING_INDEX(v.cliente_nome, ' ', -1), ' ', ''),
        '@empresa.com'
    )) AS email_ficticio
FROM vendas v;


-- EXERCÍCIO 4: Formatação de títulos (Proper Case)

SELECT
    c.nome_cor,
    CONCAT(
        UPPER(LEFT(c.nome_cor, 1)),
        LOWER(SUBSTRING(c.nome_cor, 2))
    ) AS cor_titulo
FROM cores c;



-- EXERCÍCIO 5: Contagem de letras específicas (case insensitive)

SELECT
    e.nome,
    CHAR_LENGTH(e.nome) - CHAR_LENGTH(REPLACE(LOWER(e.nome), 'a', '')) AS quantidade_letras_a
FROM estoque e;


-- EXERCÍCIO 6: Extração de domínio de email 

WITH emails_teste AS (
    SELECT 'joao@gmail.com' AS email
    UNION ALL SELECT 'maria.santos@empresa.com.br'
    UNION ALL SELECT 'carlos@yahoo.co.uk'
) -- WITH veio do enunciado do exercício, fiz apenas a parte do SELECT.
SELECT 
    email,
    SUBSTRING_INDEX(email, '@', 1) AS nome_usuario,
    SUBSTRING_INDEX(email, '@', -1) AS dominio_completo,
    SUBSTRING_INDEX(SUBSTRING_INDEX(email, '@', -1), '.', 1) AS dominio_principal
FROM emails_teste;


-- EXERCÍCIO 7: Detecção de padrões em nomes: Produtos com 'a' como segunda letra

SELECT
    e.nome AS produtos_com_a_segunda_letra
FROM estoque e
WHERE SUBSTRING(e.nome, 2, 1) = 'a';