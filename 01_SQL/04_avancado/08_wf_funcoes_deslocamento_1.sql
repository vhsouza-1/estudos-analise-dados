#EXERCÍCIOS - FUNÇÕES DE DESLOCAMENTO

#Nível 1-3: Fundamentos

#Exercício 1 - LAG simples
#Liste todas as vendas da tabela vendas ordenadas por data. Mostre: Data da venda, Valor da venda, Valor da venda anterior (use LAG), Diferença entre a venda atual e a anterior

SELECT
	v.data_venda,
    e.nome,
    v.preco_venda,
    LAG(v.preco_venda, 1, '-') OVER(ORDER BY v.data_venda) AS preco_venda_anterior,
    v.preco_venda - LAG(v.preco_venda, 1, '-') OVER(ORDER BY v.data_venda) AS diferenca
FROM vendas v
LEFT JOIN estoque e ON e.id=v.id_produto; -- LEFT JOIN com estoque só para ver o nome do produto.

#Exercício 2 - LEAD simples
#Ainda na tabela vendas, mostre: Data da venda, Valor da venda, Valor da próxima venda (use LEAD), Data da próxima venda

SELECT
	v.data_venda,
    e.nome,
    v.preco_venda,
    LEAD(v.preco_venda, 1, '-') OVER(ORDER BY v.data_venda) AS preco_prox_venda,
    LEAD(v.data_venda, 1, '-') OVER(ORDER BY v.data_venda)
FROM vendas v
LEFT JOIN estoque e ON e.id=v.id_produto;

#Exercício 3 - FIRST_VALUE na prática
#Para cada produto na tabela estoque, ordenado por data de entrada, mostre: Nome, preço, data_entrada, Preço do primeiro produto que entrou no estoque (no geral, sem partição), Diferença entre o preço atual e esse primeiro preço.

SELECT
	e.nome,
    e.preco,
    e.data_entrada,
    FIRST_VALUE(e.preco) OVER(ORDER BY e.data_entrada) AS preco_1st_produto,
    e.preco - FIRST_VALUE(e.preco) OVER(ORDER BY e.data_entrada) AS diferenca
FROM estoque e
ORDER BY e.data_entrada;

#Nível 4-6: Aplicações práticas

#Exercício 4 - Comparação com o primeiro da categoria
#Para cada produto, mostre: Nome, preço, categoria, data_entrada, Preço do primeiro produto que entrou naquela categoria, Diferença percentual entre o preço atual e esse primeiro preço.

SELECT
	e.nome,
    e.preco,
    cat.nome_categoria,
    e.data_entrada,
    FIRST_VALUE(e.preco) OVER(PARTITION BY cat.nome_categoria ORDER BY e.data_entrada) AS preco_produto1,
    concat(round(((e.preco/FIRST_VALUE(e.preco) OVER(PARTITION BY cat.nome_categoria ORDER BY e.data_entrada))-1)*100, 2), '%') AS diferenca_percentual
FROM estoque e
LEFT JOIN categorias cat ON cat.id=e.categoria_id;

#Exercício 5 - LAG com offset maior
#Analise a evolução dos preços no estoque. Para cada produto ordenado por data de entrada, mostre: Nome, preço, data_entrada
#Preço do produto que entrou 2 posições antes, Preço do produto que entrou 3 posições antes, Média desses dois valores anteriores

WITH estoque_precos_anteriores AS (
SELECT
	e.data_entrada,
    e.nome,
    e.preco,
    LAG(e.preco, 2, '-') OVER(ORDER BY e.data_entrada) AS preco_anterior2,
    LAG(e.preco, 3, '-') OVER(ORDER BY e.data_entrada) AS preco_anterior3
FROM estoque e
ORDER BY e.data_entrada
)

SELECT
	*,
    (epa.preco_anterior2 + epa.preco_anterior3)/2 AS media_precos_anteriores23 -- fiz CTE só pro código ficar mais legível
FROM estoque_precos_anteriores epa;

#Exercício 6 - LAST_VALUE (cuidado com o frame!)
#Liste os produtos ordenados por data de entrada. Para cada um, mostre: Nome, preço, data_entrada, Preço do último produto que entrou no estoque (use LAST_VALUE com o frame correto!), Diferença entre o preço atual e esse último preço

SELECT
	e.nome,
    e.preco,
    e.data_entrada,
    LAST_VALUE(e.preco) OVER() AS last_value_teste, -- por que isso dá certo?
    FIRST_VALUE(e.preco) OVER(ORDER BY e.data_entrada DESC) AS lastvalue_simuladocom_firstvalue, -- isso costuma ser utilizado? 
    LAST_VALUE(e.preco) OVER(ORDER BY e.data_entrada ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) last_value_sintaxe_correta, -- essa sintaxe é realmente necessária?
    e.preco - LAST_VALUE(e.preco) OVER() AS diferenca -- aqui usei essa sintaxe pq percebi que os 3 resultados eram iguais
FROM estoque e;

#Nível 7-10: Desafios analíticos

#Exercício 7 - Detectando quedas e subidas
#Usando a tabela vendas, crie uma consulta que identifique tendências: Data, valor, Valor anterior, Diferença, Variação percentual
#Classificação: 'Subida' se valor > anterior, 'Queda' se valor < anterior, 'Estável' se igual. Flag 'pico' se for maior que o anterior E maior que o próximo (use LEAD também)

WITH vendas_tendencias AS (
SELECT
	v.data_venda,
    v.preco_venda,
    LAG(v.preco_venda, 1, '-') OVER(ORDER BY v.data_venda) AS preco_venda_anterior,
    v.preco_venda - LAG(v.preco_venda, 1, '-') OVER(ORDER BY v.data_venda) AS diferenca_preco,
    coalesce(concat(round(((v.preco_venda/LAG(v.preco_venda, 1, '-') OVER(ORDER BY v.data_venda))-1)*100, 2), '%'), '-') AS variacao_percentual,
    --
    LEAD(v.preco_venda, 1, '-') OVER(ORDER BY v.data_venda) AS preco_venda_ulterior
FROM vendas v
)

SELECT
	vt.data_venda,
    vt.preco_venda,
    vt.preco_venda_anterior,
    vt.diferenca_preco,
    vt.variacao_percentual,
    CASE
		WHEN vt.preco_venda > vt.preco_venda_anterior THEN 'Subida'
        WHEN vt.preco_venda < vt.preco_venda_anterior THEN 'Queda'
        ELSE 'Estável'
    END AS classificacao_venda,
    CASE
		WHEN vt.preco_venda > vt.preco_venda_anterior AND vt.preco_venda > vt.preco_venda_ulterior THEN 'Pico'
        ELSE '-'
    END AS flag_pico
    
FROM vendas_tendencias vt;

#utilizei a CTE tanto para deixar a query principal mais limpa, quanto para separar as WF do CASE WHEN. Fiz certo?

#Exercício 8 - Comparação com início e fim do período
#Para cada categoria, crie um relatório que mostre: Nome da categoria, Nome do produto, Preço, Data de entrada, Preço do primeiro produto da categoria (FIRST_VALUE)
#Preço do último produto da categoria (LAST_VALUE com frame correto), Posição no ranking de preço dentro da categoria (DENSE_RANK). Classificação: 'Acima da média' se preço > média da categoria, etc.

WITH estoque_analise_periodo AS (
	SELECT
		cat.nome_categoria,
		e.nome,
		e.preco,
		e.data_entrada,
		FIRST_VALUE(e.preco) OVER(PARTITION BY cat.nome_categoria ORDER BY e.data_entrada) AS preco_primeiro_categoria,
		LAST_VALUE(e.preco) OVER(PARTITION BY cat.nome_categoria ORDER BY e.data_entrada ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS preco_ultimo_categoria, -- usei assim pois você pediu, mas não sei não em hahaha as alternativas que eu dei antes parecem melhores.
		DENSE_RANK() OVER(PARTITION BY cat.nome_categoria ORDER BY e.preco DESC) AS ranking_preco,
        -- media categoria para CASE na quesry principal
        AVG(e.preco) OVER(PARTITION BY cat.nome_categoria) AS preco_medio_categoria
	FROM estoque e
	LEFT JOIN categorias cat ON cat.id=e.categoria_id
)

SELECT
	eap.nome_categoria,
    eap.nome,
    eap.preco,
    eap.data_entrada,
    eap.preco_primeiro_categoria,
    eap.preco_ultimo_categoria,
    eap.ranking_preco,
    CASE
		WHEN eap.preco > eap.preco_medio_categoria THEN 'Acima da Média'
        WHEN eap.preco < eap.preco_medio_categoria THEN 'Abaixo da Média'
        WHEN eap.preco = eap.preco_medio_categoria THEN 'Na Média'
    END AS classificacao
FROM estoque_analise_periodo eap; 

#Aqui eu fiz a mesma coisa, fiz uma CTE parcial qcom tudo que eu iria precisar, ai puxei ela na query principal. Eu acho que ficou bom assim, mas será que to fazendo errado? To com essa duvida, acho que porque eu meio que repito muita coisa da CTE na query principal. Na minha cabeça fica organizado, mas vai que né... Tem algum problema computacional ou sla.

#Exercício 9 - Análise de vendas por produto (mesmo sem LAG ainda!)
#Como ainda não temos vendas repetidas do mesmo produto, vamos simular: crie uma consulta que, para cada produto na tabela estoque, mostre:
#Nome do produto, Preço atual, Preço do produto anterior (na ordenação por preço), Preço do próximo produto (na ordenação por preço). Classificação: 'Mais caro que vizinhos' se preço > anterior E preço > próximo, etc.

WITH estoque_analise_preco AS (
	SELECT
		e.nome,
		e.preco,
		LAG(e.preco, 1, '-') OVER(ORDER BY e.data_entrada) AS preco_anterior, -- você pediu ordenação por preço, mas acho que não faz muito sentido para a classificação...
		LEAD(e.preco, 1, '-') OVER(ORDER BY e.data_entrada) AS preco_ulterior
	FROM estoque e
)
SELECT
	*,
    CASE
		WHEN eap.preco > eap.preco_anterior AND eap.preco > eap.preco_ulterior THEN 'Mais caro que vizinhos'
        ELSE '-'
    END AS classificacao
FROM estoque_analise_preco eap;

#Achei esse exercício meio sem sentido, você começou falando que iriamos simular uma situação, mas ai você me pediu outra coisa.

#Exercício 10 - Desafio final - Relatório completo de evolução
#Combine tudo que você aprendeu nas 3 partes! Crie um relatório que mostre, para cada mês (baseado em data_entrada do estoque):
#Mês/ano (formato 'YYYY-MM'), Total de preços dos produtos que entraram no mês, Total acumulado até o mês, Total do mês anterior (use LAG), Variação percentual em relação ao mês anterior
#Média móvel de 3 meses, Comparação com o primeiro mês com registro, Comparação com o último mês com registro, Ranking do mês em volume de entrada 
#Classificação do mês: 'Recorde' se for o maior total até agora, 'Acima da média' se total > média móvel de 3 meses, 'Abaixo da média' se total < média móvel de 3 meses. 'Normal' caso contrário

WITH estoque_data_anomes AS (
SELECT
	date(concat(year(e.data_entrada), '-', month(e.data_entrada), '-01')) AS data_anomes,
    SUM(e.preco) AS total_preco_mes
FROM estoque e
GROUP BY data_anomes
),
relatorio_estoque_parcial AS (
SELECT
	date_format(ed.data_anomes, '%Y-%m') AS data_anomes_formatado,
    ed.total_preco_mes,
    SUM(ed.total_preco_mes) OVER(ORDER BY data_anomes) AS total_acumulado_mes,
    LAG(ed.total_preco_mes, 1, '-') OVER(ORDER BY data_anomes) AS total_mes_anterior,
    coalesce(concat(round(((ed.total_preco_mes/LAG(ed.total_preco_mes, 1, '-') OVER(ORDER BY data_anomes))-1)*100, 2), '%'), '-') AS varpct_relacao_mesanterior,
    round(AVG(ed.total_preco_mes) OVER(ORDER BY data_anomes RANGE BETWEEN INTERVAL 2 MONTH PRECEDING AND CURRENT ROW), 2) AS media_movel_3m
FROM estoque_data_anomes ed
)
SELECT
	*,
    CASE
		WHEN rep.total_preco_mes >= max(rep.total_preco_mes) OVER(ORDER BY rep.data_anomes_formatado) THEN 'Recorde' -- o único problema aqui é que o mes 3 e 4 ficaram com a flag de recorde. É isso mesmo?
        WHEN rep.total_preco_mes > rep.media_movel_3m THEN 'Acima da Média'
        WHEN rep.total_preco_mes < rep.media_movel_3m THEN 'Abaixo da Média'
        ELSE 'Normal'
    END AS classificacao
FROM relatorio_estoque_parcial rep;
