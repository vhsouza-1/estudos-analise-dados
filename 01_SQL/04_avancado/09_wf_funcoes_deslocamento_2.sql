#FUNÇÕES DE DESLOCAMENTO (Nível 2.0)

#Nível 11-13: Fundamentos revisados

#Exercício 11 - LAG com duas colunas
#Liste todas as vendas ordenadas por data. Para cada venda, mostre: Data, produto, valor, Valor da venda anterior, Data da venda anterior, 
#Diferença de dias entre a venda atual e a anterior (use DATEDIFF), Diferença de valor entre a venda atual e a anterior

WITH vendas_estoque_datas AS (
	SELECT
		v.data_venda,
		e.nome,
		v.preco_venda,
		coalesce(LAG(v.preco_venda, 1) OVER(ORDER BY v.data_venda), '-') AS preco_venda_anterior,
		coalesce(LAG(v.data_venda, 1) OVER(ORDER BY v.data_venda), '-') AS data_venda_anterior,
		-- DATEDIFF(v.preco_venda, LAG(v.data_venda, 1) OVER(ORDER BY v.data_venda)) AS diferenca_dias, -> coluna inteira deu null quando fiz direto na query principal, com a CTE deu certo. Precisa separar então né?
		v.preco_venda - LAG(v.preco_venda, 1) OVER(ORDER BY v.data_venda) AS diferenca_preco
	FROM vendas v
	LEFT JOIN estoque e ON e.id = v.id_produto
)

SELECT
	ved.data_venda,
    ved.nome,
    ved.preco_venda,
    ved.preco_venda_anterior,
    ved.data_venda_anterior,
    coalesce(datediff(ved.data_venda, ved.data_venda_anterior), '-') AS diferenca_dias_format,
    coalesce(ved.diferenca_preco, '-') AS diferenca_preco_format
FROM vendas_estoque_datas ved;

#Exercício 12 - LEAD com valor padrão
#Liste os produtos ordenados por data de entrada. Para cada produto, mostre: Nome, preço, data_entrada, Preço do próximo produto (LEAD)
#Uma coluna chamada "tendencia" que diga: 'Subindo' se preço do próximo for maior, 'Descendo' se preço do próximo for menor, 'Estável' se igual, 'Último' se não houver próximo

WITH estoque_parcial AS (
	SELECT
		e.nome,
		e.preco,
		e.data_entrada,
		LEAD(e.preco, 1) OVER(ORDER BY e.data_entrada) AS preco_proximo_produto
	FROM estoque e
)

SELECT
	ep.nome,
    ep.preco,
    ep.data_entrada,
    coalesce(ep.preco_proximo_produto, '-') AS preco_proximo_produto_format,
    CASE
		WHEN ep.preco_proximo_produto > ep.preco THEN 'Subindo' 
        WHEN ep.preco_proximo_produto < ep.preco THEN 'Descendo'
        WHEN ep.preco_proximo_produto = ep.preco THEN 'Estável'
        ELSE 'Último' -- isso aqui cobre todos os casos de último?
    END AS tendencia
FROM estoque_parcial ep;

#Exercício 13 - FIRST_VALUE e LAST_VALUE juntos
#Para cada categoria, mostre: Nome da categoria, Nome do primeiro produto que entrou, Preço do primeiro produto
#Nome do último produto que entrou (use o frame correto!), Preço do último produto, Variação percentual entre o primeiro e o último preço.

#Jeito 1, mais clean, mas meio gambiarra?
SELECT DISTINCT -- distinct aqui funciona bem porque todas as linhas da query para estoque ficam iguais.
	cat.nome_categoria,
    FIRST_VALUE(e.nome) OVER(PARTITION BY cat.nome_categoria ORDER BY e.data_entrada) AS primeiro_produto,
    FIRST_VALUE(e.preco) OVER(PARTITION BY cat.nome_categoria ORDER BY e.data_entrada) AS preco_primeiro_produto,
    LAST_VALUE(e.nome) OVER(PARTITION BY cat.nome_categoria ORDER BY e.data_entrada ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS ultimo_produto,
	LAST_VALUE(e.preco) OVER(PARTITION BY cat.nome_categoria ORDER BY e.data_entrada ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS preco_ultimo_produto
FROM estoque e
LEFT JOIN categorias cat ON cat.id=e.categoria_id;
-- GROUP BY cat.nome_categoria <- não da certo pq não da pra combinar group by com WF.

#Jeito 2, maior, mas mais correto tecnicamente, certo? Qual o melhor? QUal costuma ser usado no dia-a-dia.
WITH estoque_analise_categoria AS (
SELECT 
	cat.nome_categoria,
    FIRST_VALUE(e.nome) OVER(PARTITION BY cat.nome_categoria ORDER BY e.data_entrada) AS primeiro_produto,
    FIRST_VALUE(e.preco) OVER(PARTITION BY cat.nome_categoria ORDER BY e.data_entrada) AS preco_primeiro_produto,
    LAST_VALUE(e.nome) OVER(PARTITION BY cat.nome_categoria ORDER BY e.data_entrada ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS ultimo_produto,
	LAST_VALUE(e.preco) OVER(PARTITION BY cat.nome_categoria ORDER BY e.data_entrada ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS preco_ultimo_produto
FROM estoque e
LEFT JOIN categorias cat ON cat.id=e.categoria_id
)

SELECT 
	eac.nome_categoria,
    eac.primeiro_produto,
    eac.preco_primeiro_produto,
    eac.ultimo_produto,
    eac.preco_ultimo_produto
FROM estoque_analise_categoria eac
GROUP BY eac.nome_categoria;

#Nível 14-16: Aplicações práticas avançadas

#Exercício 14 - Detectando padrões sazonais
#Usando a tabela estoque, crie uma consulta que mostre, para cada mês/ano: Mês/ano, Total de preços no mês
#Total do mesmo mês do ano anterior (use LAG com offset 12, mesmo que não tenha dados), Diferença percentual
#Classificação: 'Crescimento' se positivo, 'Queda' se negativo, 'Primeiro registro' se não houver anterior

WITH estoque_simulação AS ( -- criei essa tabela para testar a query principal mais adequadamente.
	SELECT date('2024-01-01') AS data_mesano, 72000 AS total_mes UNION ALL
	SELECT date('2024-02-01'), 43000 UNION ALL
	SELECT date('2024-03-01'), 92000 UNION ALL
	SELECT date('2024-04-01'), 67000 UNION ALL
	SELECT date('2024-05-01'), 39000 UNION ALL
	SELECT date('2024-06-01'), 58000 UNION ALL
	SELECT date('2024-07-01'), 46000 UNION ALL
	SELECT date('2024-08-01'), 78000 UNION ALL
	SELECT date('2024-09-01'), 31000 UNION ALL
	SELECT date('2024-10-01'), 89000 UNION ALL
	SELECT date('2024-11-01'), 54000 UNION ALL
	SELECT date('2024-12-01'), 62000 
),
estoque_mes AS (
	SELECT
		date(concat(year(e.data_entrada), '-', month(e.data_entrada), '-01')) AS data_mesano,
		SUM(e.preco) AS total_mes
	FROM estoque e
	GROUP BY data_mesano
),
estoque_completo AS (
	SELECT
		*
	FROM estoque_simulação
    UNION ALL
    SELECT 
		*
	FROM estoque_mes
),
analise_parcial AS (
SELECT
	date_format(ec.data_mesano, '%m/%Y') AS data_format,
    ec.total_mes,
    coalesce(LAG(ec.total_mes, 12) OVER(ORDER BY ec.data_mesano), '-') AS total_mes_ano_anterior,
    coalesce(concat(round(((ec.total_mes/LAG(ec.total_mes, 12) OVER(ORDER BY ec.data_mesano))-1)*100, 2), '%'), '-') AS dif_percentual
FROM estoque_completo ec
)
SELECT
	*,
    CASE
		WHEN ap.total_mes_ano_anterior = '-' THEN 'Primeiro Registro'
        WHEN ap.total_mes > ap.total_mes_ano_anterior THEN 'Crescimento'
        WHEN ap.total_mes < ap.total_mes_ano_anterior THEN 'Queda'
        ELSE 'Igual'
    END AS classificacao
FROM analise_parcial ap;

#Exercício 15 - Análise de variação por categoria
#Para cada categoria, calcule a evolução dos preços dos produtos (ordenados por data_entrada):
#Categoria, produto, preço, data, Preço anterior na categoria (LAG), Diferença absoluta, Diferença percentual, Acumulado de variação desde o primeiro produto (some as diferenças percentuais acumuladas)

WITH estoque_cat_analise AS (
SELECT
	cat.nome_categoria,
    e.nome,
    e.preco,
    e.data_entrada,
    coalesce(LAG(e.preco) OVER(PARTITION BY cat.nome_categoria ORDER BY e.data_entrada), '-') AS preco_anterior_cat,
    coalesce(e.preco - LAG(e.preco) OVER(PARTITION BY cat.nome_categoria ORDER BY e.data_entrada), '-') AS dif_absoluta,
    round(((e.preco/LAG(e.preco) OVER(PARTITION BY cat.nome_categoria ORDER BY e.data_entrada))-1)*100, 2) AS dif_percentual
FROM estoque e
LEFT JOIN categorias cat ON cat.id=e.categoria_id
ORDER BY cat.nome_categoria, e.data_entrada
)

SELECT
	eca.nome_categoria,
    eca.nome,
    eca.preco,
    eca.data_entrada,
    eca.preco_anterior_cat,
    coalesce(eca.dif_absoluta, '-') AS dif_absoluta_format,
    coalesce(SUM(eca.dif_percentual) OVER(PARTITION BY eca.nome_categoria ORDER BY eca.data_entrada), '-') AS acumulado_dif_percentual_format
FROM estoque_cat_analise eca;

#Exercício 16 - Comparação com o mais caro da categoria
#Para cada produto, mostre: Nome, categoria, preço, Preço do produto mais caro da categoria, Diferença para o mais caro, Percentual que representa do mais caro
#Uma coluna "distancia" que classifique: 'Muito próximo' se > 90% do mais caro, 'Próximo' se entre 70% e 90%, 'Distante' se < 70%.

WITH estoque_categoria_analise AS (
SELECT
	e.nome,
    cat.nome_categoria,
    e.preco,
    MAX(e.preco) OVER(PARTITION BY cat.nome_categoria) AS maior_preco_cat,
    MAX(e.preco) OVER(PARTITION BY cat.nome_categoria) - e.preco AS diferenca,
    round((e.preco/MAX(e.preco) OVER(PARTITION BY cat.nome_categoria))*100, 2) AS pct_maiorpreco
FROM estoque e
LEFT JOIN categorias cat ON cat.id=e.categoria_id
)
SELECT
	eca.nome,
    eca.nome_categoria,
    eca.preco,
    eca.maior_preco_cat,
    eca.diferenca,
    eca.pct_maiorpreco,
    CASE
		WHEN eca.pct_maiorpreco > 90 THEN 'Muito próximo'
        WHEN eca.pct_maiorpreco BETWEEN 70 AND 90 THEN 'Próximo'
        WHEN eca.pct_maiorpreco < 70 THEN 'Distante'
    END AS distancia
FROM estoque_categoria_analise eca;

#Nível 17-20: Desafios analíticos complexos

#Exercício 17 - Dias desde a última venda (customer journey)
#Usando a tabela vendas, imagine que cada venda é de um cliente diferente (nomes na coluna cliente_nome). Crie um relatório que mostre:
#Data da venda, cliente, valor, Data da última venda (de qualquer cliente) - use LAG, Dias desde a última venda
#Média móvel de vendas dos últimos 30 dias (considere intervalo de dias, não número de vendas)
#Classificação do intervalo: 'Frequente' se intervalo < 30 dias, 'Normal' se intervalo entre 30 e 60 dias, 'Esporádico' se intervalo > 60 dias.
WITH vendas_analise AS (
SELECT
	v.data_venda,
    v.cliente_nome,
    v.preco_venda,
    FIRST_VALUE(v.data_venda) OVER(ORDER BY v.data_venda DESC) AS data_ultima_venda, -- aqui usei FIRST VALUE no lugar de LAST VALUE.
    round(AVG(v.preco_venda) OVER(ORDER BY v.data_venda RANGE BETWEEN INTERVAL 29 DAY PRECEDING AND CURRENT ROW), 2) AS media_movel_30d, -- 29 DAYS	pq o current row é o dia 30.
    -- para query principal
    LAG(v.data_venda, 1) OVER (ORDER BY v.data_venda) AS data_venda_anterior
FROM vendas v
)

SELECT
	va.data_venda,
    va.cliente_nome,
    va.preco_venda,
    coalesce(va.data_ultima_venda, '-') AS data_ultima_venda_format,
    coalesce(datediff(va.data_venda, va.data_venda_anterior), '-') AS distancia_dias_format,
    va.media_movel_30d,
    CASE
		WHEN datediff(va.data_venda, va.data_venda_anterior) < 30 THEN 'Frequente'
        WHEN datediff(va.data_venda, va.data_venda_anterior) BETWEEN 30 AND 60 THEN 'Normal'
        WHEN datediff(va.data_venda, va.data_venda_anterior) > 60 THEN 'Esporádico'
        ELSE 'Primeira Venda'
    END AS classificacao_intervalo
FROM vendas_analise va;

#Exercício 18 - Análise de performance de produtos (versão completa)
#Combine todas as tabelas para criar um relatório de performance por produto: Para cada produto (da tabela estoque), mostre:
#Nome do produto, categoria, Preço atual, Data de entrada, Preço do produto anterior na mesma categoria (por data), Preço do próximo produto na mesma categoria (por data)
#Primeiro preço da categoria, Último preço da categoria, Média dos preços da categoria, Posição no ranking de preço da categoria (DENSE_RANK)
#Classificação composta: 'Líder' se for o mais caro da categoria, 'Seguidor' se for mais caro que a média mas não o líder, 'Médio' se estiver entre -1 desvio e +1 desvio da média, 'Defasado' se for mais barato que a média - 1 desvio

WITH estoque_categorias_analise AS (
	SELECT
		e.nome,
		cat.nome_categoria,
		e.preco,
		e.data_entrada,
		LAG(e.preco, 1) OVER(PARTITION BY cat.nome_categoria ORDER BY e.data_entrada) AS preco_produto_anterior,
		LEAD(e.preco, 1) OVER(PARTITION BY cat.nome_categoria ORDER BY e.data_entrada) AS preco_produto_ulterior,
		FIRST_VALUE(e.preco) OVER(PARTITION BY cat.nome_categoria ORDER BY e.data_entrada) AS primeiro_preco_cat,
		FIRST_VALUE(e.preco) OVER(PARTITION BY cat.nome_categoria ORDER BY e.data_entrada DESC) AS ultimo_preco_cat,
		avg(e.preco) OVER(PARTITION BY cat.nome_categoria) AS preco_medio_categoria,
		DENSE_RANK() OVER(PARTITION BY cat.nome_categoria ORDER BY e.preco DESC) AS ranking_categoria,
		-- para uso na query principal
		STDDEV(e.preco) OVER(PARTITION BY cat.nome_categoria) AS desviop_medcat,
        MAX(e.preco) OVER(PARTITION BY cat.nome_categoria) AS mais_caro_categoria
	FROM estoque e
	LEFT JOIN categorias cat ON cat.id=e.categoria_id
)

SELECT
	eca.nome,
    eca.nome_categoria,
    eca.preco,
    eca.data_entrada,
    coalesce(eca.preco_produto_anterior, '-') AS preco_produto_anterior_format,
    coalesce(eca.preco_produto_ulterior, '-') AS preco_produto_ulterior_format,
    eca.primeiro_preco_cat,
    eca.ultimo_preco_cat,
    eca.preco_medio_categoria,
    eca.ranking_categoria,
    CASE -- esses ranges estão corretos? Do 'Seguidor' e do 'Médio'
		WHEN eca.preco = eca.mais_caro_categoria THEN 'Líder'
		WHEN eca.preco BETWEEN (eca.preco_medio_categoria-eca.desviop_medcat) AND (eca.preco_medio_categoria+eca.desviop_medcat) THEN 'Médio'
        WHEN eca.preco > eca.preco_medio_categoria THEN 'Seguidor' 
        WHEN eca.preco < (eca.preco_medio_categoria-eca.desviop_medcat) THEN 'Defasado'
    END AS classificacao_composta
FROM estoque_categorias_analise eca;

#Exercício 19 - Simulação de tendências (Window Functions aninhadas)
#Este é um desafio avançado! Crie uma consulta que simule uma análise de tendência usando LAG dentro de uma expressão: Para cada mês (agregado por data_entrada), calcule:
#Mês/ano, Total do mês, Média dos últimos 3 meses, Projeção para o próximo mês (use a média dos últimos 3 meses como projeção)
#Compare a projeção com o valor real do próximo mês (você precisará de LEAD para acessar o próximo real), Erro percentual da projeção: |(real - projeção)/real| * 100

WITH estoque_ano_mes AS (
SELECT
	date(concat(year(e.data_entrada), '-', month(e.data_entrada), '-01')) AS data_anomes,
    SUM(e.preco) AS total_mes
FROM estoque e
GROUP BY data_anomes
),
estoque_am_cmm AS ( -- estoque ano mes com média móvel
SELECT
	date_format(eam.data_anomes, '%m-%Y') AS data_formatada,
    eam.total_mes,
	round(avg(eam.total_mes) OVER(ORDER BY eam.data_anomes ROWS BETWEEN 2 PRECEDING AND CURRENT ROW), 2) AS media_movel_3m
FROM estoque_ano_mes eam
)
SELECT
	eac.data_formatada,
    eac.total_mes,
    eac.media_movel_3m,
    eac.media_movel_3m AS projecao_prox_mes,
    coalesce(LEAD(eac.total_mes, 1) OVER(ORDER BY eac.data_formatada), '-') AS valor_real_prox_mes, -- |(real - projeção)/real| * 100
    coalesce(concat(round(((eac.media_movel_3m/LEAD(eac.total_mes, 1) OVER(ORDER BY eac.data_formatada))-1)*100, 2), '%'), '-') AS erro_percentual_projecao 
    -- não deixei como valor absoluto pois quis representar que quando o erro é negativo a projeção errou pra menos e quando é positivo, errou pra mais. Mas poderia ser ao contrário também dependendo da convenção assumida na análise
FROM estoque_am_cmm eac;

#Exercício 20 - Desafio final - Dashboard executivo com storytelling Crie um relatório completo que conte a "história" dos dados da empresa, combinando todas as 3 partes das Window Functions: #Para cada categoria, mostre: 
#Métricas gerais: Nome da categoria, Total de produtos, Preço médio, Preço total do estoque

#Evolução temporal (baseado em data_entrada): Data do primeiro produto, Data do último produto, Preço do primeiro produto, Preço do último produto, Variação percentual (primeiro → último)

#Destaques:, Produto mais caro (nome e preço), Produto mais barato (nome e preço), Produto com maior aumento em relação ao anterior na categoria (maior diferença positiva usando LAG), 
#Produto com maior queda em relação ao anterior na categoria (maior diferença negativa)

#Análise de ranking: Quantos produtos estão acima da média da categoria, Quantos produtos estão abaixo da média, Produto na posição mediana da categoria (dica: use NTILE(2) ou calcule a posição do meio)


WITH estoque_categoria AS (
SELECT 
	-- Métricas gerais
    cat.nome_categoria,
    count(e.id) OVER(PARTITION BY cat.nome_categoria) AS qnt_produtos,
    ROUND(avg(e.preco) OVER(PARTITION BY cat.nome_categoria), 2) AS media_preco_cat,
    sum(e.preco) OVER(PARTITION BY cat.nome_categoria) AS preco_total_cat, -- no enunciado dá a entender que de todo o estoque, mas acho que faz mais sentido ser por categoria
    -- Evolução temporal
    FIRST_VALUE(e.data_entrada) OVER(PARTITION BY cat.nome_categoria ORDER BY e.data_entrada) AS data_primeiro_produto,
    FIRST_VALUE(e.data_entrada) OVER(PARTITION BY cat.nome_categoria ORDER BY e.data_entrada DESC) AS data_ultimo_produto,
    FIRST_VALUE(e.preco) OVER(PARTITION BY cat.nome_categoria ORDER BY e.data_entrada) AS preco_primeiro_produto,
    FIRST_VALUE(e.preco) OVER(PARTITION BY cat.nome_categoria ORDER BY e.data_entrada DESC) AS preco_ultimo_produto,
    round(((FIRST_VALUE(e.preco) OVER(PARTITION BY cat.nome_categoria ORDER BY e.data_entrada DESC)/FIRST_VALUE(e.preco) OVER(PARTITION BY cat.nome_categoria ORDER BY e.data_entrada))-1)*100, 2) AS variacao_percentual,
    -- destaques:
    -- produto mais caro
    concat(FIRST_VALUE(e.nome) OVER(PARTITION BY cat.nome_categoria ORDER BY e.preco DESC), ' - Preco: ', FIRST_VALUE(e.preco) OVER(PARTITION BY cat.nome_categoria ORDER BY e.preco DESC)) AS produto_mais_caro,
    -- produto mais barato
    concat(FIRST_VALUE(e.nome) OVER(PARTITION BY cat.nome_categoria ORDER BY e.preco ASC), ' - Preco: ', FIRST_VALUE(e.preco) OVER(PARTITION BY cat.nome_categoria ORDER BY e.preco ASC)) AS produto_mais_barato
FROM estoque e
LEFT JOIN categorias cat ON cat.id=e.categoria_id
),
destaque_indice AS (
	SELECT
		cat.nome_categoria,
        e.nome,
        coalesce(e.preco-LAG(e.preco) OVER(PARTITION BY cat.nome_categoria ORDER BY e.data_entrada), 0) AS indice_diferenca_entrada
    FROM estoque e
    LEFT JOIN categorias cat ON cat.id=e.categoria_id
),
calculo_medias_p AS (
SELECT
	e.nome,
    e.preco,
    cat.nome_categoria,
    avg(e.preco) OVER(PARTITION BY cat.nome_categoria) AS media_categoria
FROM estoque e
LEFT JOIN categorias cat ON cat.id=e.categoria_id
),
calculo_medias AS (
SELECT
	cmp.nome_categoria,
    count(
		CASE
			WHEN cmp.preco > cmp.media_categoria THEN 1
        END
    ) OVER(PARTITION BY cmp.nome_categoria) AS qnt_acima_medcat,
    count(
		CASE
			WHEN cmp.preco < cmp.media_categoria THEN 1
        END
    ) OVER(PARTITION BY cmp.nome_categoria) AS qnt_abaixo_medcat
FROM calculo_medias_p cmp
),
estoque_categoria_ntile AS (
SELECT
	e.nome,
    e.preco,
    cat.nome_categoria,
	NTILE(2) OVER(PARTITION BY cat.nome_categoria ORDER BY e.preco DESC) AS NTILE_2
FROM estoque e
LEFT JOIN categorias cat ON cat.id=e.categoria_id
),
calculo_pos_media AS (
SELECT
	ect.nome_categoria,
	FIRST_VALUE(ect.nome) OVER(PARTITION BY ect.nome_categoria) AS pos_mediana
FROM estoque_categoria_ntile ect
WHERE ect.ntile_2 = 2
)
SELECT DISTINCT
	ec.nome_categoria,
    ec.qnt_produtos,
    ec.media_preco_cat,
    ec.preco_total_cat,
    ec.data_primeiro_produto,
    ec.data_ultimo_produto,
    ec.preco_primeiro_produto,
    ec.preco_ultimo_produto,
    ec.variacao_percentual,
    ec.produto_mais_caro,
    ec.produto_mais_barato,
    FIRST_VALUE(di.nome) OVER(PARTITION BY di.nome_categoria ORDER BY indice_diferenca_entrada DESC) AS produto_maior_diferenca,
    FIRST_VALUE(di.nome) OVER(PARTITION BY di.nome_categoria ORDER BY indice_diferenca_entrada) AS produto_menor_diferenca,
    cm.qnt_acima_medcat,
    cm.qnt_abaixo_medcat,
    cpm.pos_mediana
FROM estoque_categoria ec
LEFT JOIN destaque_indice di ON di.nome_categoria=ec.nome_categoria
LEFT JOIN calculo_medias cm ON cm.nome_categoria=ec.nome_categoria
LEFT JOIN calculo_pos_media cpm ON cpm.nome_categoria=ec.nome_categoria