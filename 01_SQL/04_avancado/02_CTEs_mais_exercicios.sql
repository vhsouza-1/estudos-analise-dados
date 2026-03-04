# Exercício 1. Crie uma CTE chamada produtos_caros que selecione produtos com preço > 30000. Na consulta principal, mostre o nome do produto, o preço e qualifique todas as colunas com o alias da CTE.

WITH produtos_caros AS (
	SELECT
		*
    FROM estoque e1
    WHERE e1.preco > 30000
)

SELECT
	pc.nome,
    pc.preco
FROM produtos_caros pc;

#Exercício 2 - Duas CTEs independentes Crie duas CTEs: qtd_carros: quantidade de carros no estoque, qtd_motos: quantidade de motos no estoque
#Depois, faça um CROSS JOIN entre elas para mostrar: "Temos X carros e Y motos".

WITH qtd_carros AS (
	SELECT 
		count(*) AS carros_estoque
    FROM estoque e1
    WHERE e1.categoria_id=1
),
	qtd_motos AS (
	SELECT
		count(*) AS motos_estoque
    FROM estoque e2
    WHERE e2.categoria_id=2
)

SELECT
	concat(
		'Temos ', qc.carros_estoque, ' carros e ', qm.motos_estoque, ' motos'
    ) AS mensagem_produtos_estoque
FROM qtd_carros qc
CROSS JOIN qtd_motos qm;

#Exercício 3 - Crie uma CTE chamada vendas_com_detalhes que junte as tabelas vendas e estoque para mostrar: nome do produto, data da venda e preço da venda.
#Na consulta principal, mostre apenas vendas de produtos da categoria 'Carro'.

WITH vendas_com_detalhes AS (
	SELECT
		e1.nome,
        v1.data_venda,
        v1.preco_venda,
        cat1.nome_categoria
    FROM vendas v1
    LEFT JOIN estoque e1 ON e1.id=v1.id_produto
    LEFT JOIN categorias cat1 ON cat1.id=e1.categoria_id
)

SELECT
	vcd.nome,
    vcd.data_venda,
    vcd.preco_venda
FROM vendas_com_detalhes vcd
WHERE vcd.nome_categoria = 'Carro';


#Exercício 4. Crie uma CTE chamada faixa_precos que adicione uma coluna calculada chamada faixa: 'Econômico' quando preço < 15000. 'Popular' quando preço entre 15000 e 25000. 'Premium' quando preço > 25000
#Depois, mostre quantos produtos e o preço médio em cada faixa. Atenção: Ordene da faixa mais cara para a mais barata.

WITH faixa_precos AS (
	SELECT 
		*,
        CASE
			WHEN e1.preco < 15000 THEN 'Econômico'
            WHEN e1.preco BETWEEN 15000 AND 25000 THEN 'Popular'
            WHEN e1.preco > 25000 THEN 'Premium'
        END AS classificacao
	FROM estoque e1
)

SELECT
	fp.classificacao,
    count(fp.id) AS quantidade,
    avg(fp.preco) AS media_preco
FROM faixa_precos fp
GROUP BY fp.classificacao
ORDER BY
	CASE fp.classificacao
		WHEN 'Premium' THEN 1
        WHEN 'Popular' THEN 2
        WHEN 'Econômico' THEN 3
    END;

#Exercício 5. Crie duas CTEs: faturamento_por_categoria: soma dos preços de venda por categoria (use a tabela vendas com estoque); faturamento_total: soma total de todas as vendas
#Depois, mostre o percentual que cada categoria representa do faturamento total.

WITH faturamento_por_categoria AS (
	SELECT
		cat1.nome_categoria,
        SUM(v1.preco_venda) AS venda_categoria
    FROM vendas v1
    LEFT JOIN estoque e1 ON e1.id=v1.id_produto
    LEFT JOIN categorias cat1 ON cat1.id=e1.categoria_id
    GROUP BY cat1.nome_categoria
),
	faturamento_total AS (
    SELECT
		SUM(v2.preco_venda) AS venda_total
    FROM vendas v2
)

SELECT
	*,
	concat(
		replace(round((fpc.venda_categoria/ft.venda_total) * 100, 2), '.', ','), '%'
	) AS porcentagem_faturamento
FROM faturamento_por_categoria fpc
CROSS JOIN faturamento_total ft;

# Exercício 6. Crie uma CTE chamada entradas_2025 que filtre as entradas do ano de 2025.
#Depois, faça uma segunda CTE chamada entradas_por_mes que agrupe por mês (mostrando o nome do mês, não o número).
#Na consulta principal, mostre o mês e a quantidade, ordenado por mês (janeiro primeiro).

WITH entradas_2025 AS (
	SELECT
		*,
        month(e1.data_entrada) AS num_mes,
        monthname(e1.data_entrada) AS mes_entrada
    FROM estoque e1
    WHERE year(e1.data_entrada) = 2025
),
	entradas_por_mes AS (
	SELECT
		e2025.mes_entrada,
        count(*) AS qtd_entrada
    FROM entradas_2025 e2025
    GROUP BY e2025.mes_entrada, e2025.num_mes
    ORDER BY e2025.num_mes
)

SELECT 
	* 
FROM entradas_por_mes;

#Exercício 7. Resolva a seguinte questão de DUAS formas diferentes (use duas CTEs separadas, uma para cada abordagem): "Quais produtos têm preço acima da média de preços da sua cor?"
#Abordagem A: Usando CTE com JOIN direto; Abordagem B: Usando CTE com subquery no WHERE

# Vou fazer o exercício de 3 formas diferentes: Com CTE, com JOIN direto e com subquery no WHERE. O primeiro jeito é diferente, mas os dois outros jeitos é basicamente o que o enunciado está pedindo, mas fora de uma CTE:

#1. CTE da forma correta:
WITH media_cor AS (
	SELECT 
		c1.id,
        c1.nome_cor,
        avg(e1.preco) AS preco_medio
    FROM estoque e1
    LEFT JOIN cores c1 ON c1.id=e1.cor_id
    GROUP BY c1.nome_cor
)
SELECT
	e.nome,
    mc.nome_cor,
    mc.preco_medio,
    e.preco
FROM estoque e
LEFT JOIN media_cor mc ON mc.id=e.cor_id
WHERE e.preco > mc.preco_medio
ORDER BY e.preco;

#2. JOIN direto:
SELECT
	e.nome,
    mc.nome_cor,
    mc.preco_medio,
    e.preco
FROM estoque e
LEFT JOIN (
	SELECT 
		c1.id,
        c1.nome_cor,
        avg(e1.preco) AS preco_medio
    FROM estoque e1
    LEFT JOIN cores c1 ON c1.id=e1.cor_id
    GROUP BY c1.nome_cor
) mc ON mc.id=e.cor_id
WHERE e.preco > mc.preco_medio
ORDER BY e.preco;

#3. Subquery no WHERE
SELECT
	e.nome,
    c.nome_cor,
    (SELECT avg(e1.preco) FROM estoque e1 WHERE e1.cor_id = e.cor_id) AS preco_medio,
    e.preco
FROM estoque e
LEFT JOIN cores c ON c.id=e.cor_id
WHERE e.preco > (SELECT avg(e1.preco) FROM estoque e1 WHERE e1.cor_id = e.cor_id)
ORDER BY e.preco;

#Exercício 8. Crie uma CTE chamada precos_ordenados que selecione nome, preco e categoria dos produtos, ordenados por preço decrescente dentro de cada categoria.
#Na consulta principal, adicione uma coluna chamada posicao que seja um número sequencial (1, 2, 3...) baseado na ordem

WITH precos_ordenados AS (
	SELECT
		e1.id,
        e1.nome,
        e1.preco,
        cat1.nome_categoria
    FROM estoque e1
    LEFT JOIN categorias cat1 ON cat1.id = e1.categoria_id
    ORDER BY cat1.nome_categoria, e1.preco DESC
)

SELECT
	po1.nome,
    po1.preco,
    po1.nome_categoria,
    count(po2.id) + 1 AS posicao -- conta quantos produtos são mais caros e soma 1 pra fazer o rank (pq se tiver 0 produtos mais caros, significa que o produto é o mais caro, logo posição 1)
FROM precos_ordenados po1
LEFT JOIN precos_ordenados po2 -- self join para comparar a tabela com ela mesma
	ON po2.nome_categoria = po1.nome_categoria -- produtos com a mesma categoria
    AND po2.preco > po1.preco -- produtos com preço maior
GROUP BY po1.nome, po1.preco, po1.nome_categoria -- aqui coloquei todo mundo no group by porque o match é 1:1
ORDER BY po1.nome_categoria, po1.preco DESC
;
#esse aqui fiz com pesquisa, mas a lógica é a seguinte, SELF JOIN para juntar produtos mais caros que o produto analisado, count(...) pra contar quantos são esses produtos e +1 pra ranquear

#Exercício 9. Crie uma CTE chamada vendas_por_mes que mostre, para cada mês de 2025: Mês (número), Total vendido (soma dos preços de venda), Quantidade de vendas
#Crie uma segunda CTE chamada mes_anterior que, para cada mês, mostre o total vendido no mês anterior.
#Na consulta principal, mostre: mês, total_vendido, total_mes_anterior e a diferença (crescimento/queda).

WITH calendario_mes AS (
	SELECT '1' AS mes, monthname('2000-01-01') AS mes_nome UNION ALL
    SELECT '2' AS mes, monthname('2000-02-01') AS mes_nome UNION ALL
    SELECT '3' AS mes, monthname('2000-03-01') AS mes_nome UNION ALL
    SELECT '4' AS mes, monthname('2000-04-01') AS mes_nome UNION ALL
    SELECT '5' AS mes, monthname('2000-05-01') AS mes_nome UNION ALL
    SELECT '6' AS mes, monthname('2000-06-01') AS mes_nome UNION ALL
    SELECT '7' AS mes, monthname('2000-07-01') AS mes_nome UNION ALL
    SELECT '8' AS mes, monthname('2000-08-01') AS mes_nome UNION ALL
    SELECT '9' AS mes, monthname('2000-09-01') AS mes_nome UNION ALL
    SELECT '10' AS mes, monthname('2000-10-01') AS mes_nome UNION ALL
    SELECT '11' AS mes, monthname('2000-11-01') AS mes_nome UNION ALL
    SELECT '12' AS mes, monthname('2000-12-01') AS mes_nome 
), 
	vendas_por_mes AS (
	SELECT
		cm1.mes,
        cm1.mes_nome,
        SUM(v1.preco_venda) AS total_vendido,
        count(v1.id_venda) AS qtd_venda
    FROM calendario_mes cm1
    LEFT JOIN vendas v1 ON month(v1.data_venda) = cm1.mes
	GROUP BY cm1.mes, cm1.mes_nome
),
	mes_anterior AS (
	SELECT
        monthname(concat('2000-',cm2.mes+1,'-01')) AS mes_nome,
        SUM(v2.preco_venda) AS total_mes_anterior
    FROM calendario_mes cm2
    LEFT JOIN vendas v2 ON month(v2.data_venda) = cm2.mes
	GROUP BY cm2.mes, cm2.mes_nome
)

SELECT
	cm.mes_nome,
    coalesce(vpm.total_vendido, '-'),
    coalesce(ma.total_mes_anterior, '-'),
    coalesce(vpm.total_vendido-ma.total_mes_anterior, '-') AS diferenca
FROM calendario_mes cm
LEFT JOIN vendas_por_mes vpm ON vpm.mes_nome=cm.mes_nome
LEFT JOIN mes_anterior ma ON ma.mes_nome=cm.mes_nome;

#Essa query resolve meu problema pois o ano de entrado e de venda são os mesmos, se você mudar de ano imagino que o código seria mais complexo para pegar os casos de dezembro e de janeiro.

#Exercício 10. Usando apenas CTEs não recursivas, resolva: A tabela vendas tem apenas 6 registros. Crie um relatório que mostre, para CADA produto do estoque (todos os 15), quantas vezes foi vendido. 
#Regras: Use pelo menos 2 CTEs; A primeira CTE deve criar uma lista de todos os produtos com seus IDs e nomes; A segunda CTE deve calcular as vendas por produto; Produtos sem venda devem aparecer com 0 

WITH produtos_estoque AS (
	SELECT
		e1.id,
        e1.nome
	FROM estoque e1
),
	contagem_vendas AS (
	SELECT
		pe1.nome,
        count(v1.id_venda) AS qtd_vendas
    FROM produtos_estoque pe1
    LEFT JOIN vendas v1 ON v1.id_produto = pe1.id
    GROUP BY pe1.nome
)

SELECT * FROM contagem_vendas