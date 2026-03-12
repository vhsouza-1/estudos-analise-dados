#FUNÇÕES DE AGREGAÇÃO (2.0)

#Nível 11-13: Fundamentos revisados

#Exercício 11 - Total acumulado com duas ordens
#Liste todos os produtos com nome, preço, data_entrada, e duas colunas de total acumulado: 
#acumulado_por_preco: soma acumulada ordenando do mais caro para o mais barato, acumulado_por_data: soma acumulada ordenando da entrada mais antiga para a mais nova
#Compare os resultados e explique por que são diferentes.

SELECT
	e.nome,
    e.preco,
    e.data_entrada,
    SUM(e.preco) OVER(ORDER BY e.preco DESC) AS acumulado_por_preco, -- por algum motivo nos preços iguais o acumulado não se altera...
    SUM(e.preco) OVER(ORDER BY e.data_entrada ASC) AS acumulado_por_data -- nesse todas as linhas são atualizadas, entretanto, os dois chegam no mesmo resultado. Me parece que a acumulado por preço n tem muito sentido...
FROM estoque e;

#Exercício 12 - Média por categoria com detalhe
#Para cada produto, mostre nome, preço, categoria, e a média da categoria. Adicione também: 
#contagem_categoria: quantos produtos existem naquela categoria (use COUNT() OVER), soma_categoria: soma total dos preços da categoria, percentual_categoria: qual percentual do total da categoria aquele produto representa

SELECT
	e.nome,
    e.preco,
    cat.nome_categoria,
    avg(e.preco) OVER(PARTITION BY cat.nome_categoria) AS media_categoria,
    count(e.id) OVER(PARTITION BY cat.nome_categoria) AS contagem_categoria,
    sum(e.preco) OVER(PARTITION BY cat.nome_categoria) AS soma_categoria,
    concat(round(e.preco/sum(e.preco) OVER(PARTITION BY cat.nome_categoria)*100, 2), '%') AS percetual_categoria
FROM estoque e
LEFT JOIN categorias cat ON cat.id=e.categoria_id;

#Exercício 13 - Min e Max acumulados
#Liste os produtos ordenados por data_entrada. Para cada produto, mostre:
#Nome, preço, data_entrada, menor_preco_ate_agora: menor preço visto até aquela data, maior_preco_ate_agora: maior preço visto até aquela data, amplitude_ate_agora: diferença entre o maior e o menor até o momento

SELECT
	e.data_entrada,
    e.nome, 
    e.preco,
    MIN(e.preco) OVER(ORDER BY e.data_entrada) AS menor_preco_ate_agora,
    MAX(e.preco) OVER(ORDER BY e.data_entrada) AS maior_preco_ate_agora,
    (MAX(e.preco) OVER(ORDER BY e.data_entrada))-(MIN(e.preco) OVER(ORDER BY e.data_entrada)) AS amplitude_ate_agora
FROM estoque e;

#Nível 14-16: Aplicações práticas avançadas

#Exercício 14 - Média móvel com diferentes janelas
#Para os produtos ordenados por data_entrada, calcule TRÊS tipos de média móvel:
#media_3d: média do produto atual + 2 anteriores (janela de 3), media_5d: média do produto atual + 4 anteriores (janela de 5), media_7d: média do produto atual + 6 anteriores (janela de 7)
#Mostre nome, preco, data_entrada e as três médias. Como o comportamento muda conforme a janela aumenta?

SELECT
	e.nome,
    e.preco,
    e.data_entrada,
    round(avg(e.preco) OVER(ORDER BY e.data_entrada ROWS BETWEEN 2 PRECEDING AND CURRENT ROW), 2) AS media_3d,
    round(avg(e.preco) OVER(ORDER BY e.data_entrada ROWS BETWEEN 4 PRECEDING AND CURRENT ROW), 2) AS media_5d,
    round(avg(e.preco) OVER(ORDER BY e.data_entrada ROWS BETWEEN 6 PRECEDING AND CURRENT ROW), 2) AS media_7d
FROM estoque e;

#conforme a janela aumenta a amplitude de variação da coluna diminui, pois tende a equivaler a média do estoque a medida que o intervalo tende à quantidade de produtos no estoque.
#a variação da coluna ser menor também serve a formas diferentes de análise. A primeira media variar mais e a terceira variar menos pode carregar insights específicos, mas depende da análise.

#Exercício 15 - Análise de tendência por categoria
#Para cada categoria, calcule uma "média móvel trimestral" (considere 3 meses, baseado em data_entrada). Mostre:
#Categoria, mês/ano (formato 'YYYY-MM'), total de preços no mês, média móvel trimestral.

WITH categorias_mes AS (
	SELECT
		cat.nome_categoria,
		DATE(CONCAT(YEAR(e.data_entrada), '-', MONTH(e.data_entrada), '-01')) AS data_mes,
		SUM(e.preco) AS total_precos
	FROM estoque e
	LEFT JOIN categorias cat ON cat.id=e.categoria_id
	GROUP BY cat.nome_categoria, data_mes
)
SELECT
	cm.nome_categoria,
    date_format(cm.data_mes, '%Y-%m') AS data_formatada,
    cm.total_precos,
    AVG(cm.total_precos) OVER(PARTITION BY cm.nome_categoria ORDER BY cm.data_mes RANGE BETWEEN INTERVAL 2 MONTH PRECEDING AND CURRENT ROW) AS media_movel_trimestral
FROM categorias_mes cm;

#Esse exercício foi relativamente desafiador. Tive que fazer algumas pesquisas, descobri que não da pra ordenar RANGE com MONTH se o ORDER BY não for uma função de data (eu estava tentando ordernar apenas por month(data_entrada))
#também descobri que no MySQL eu posso ordernar por uma função criada no select e usar o alias ainda por cima (caso do data_mes)... muito interessante
#Mas esse exerício foi bem divertido! hehe

#Exercício 16 - Recordes consecutivos
#Identifique produtos que bateram recorde de preço (maior até o momento) em sua categoria e, além disso, verifique se o recorde foi consecutivo (o produto anterior também era recorde). 
#Mostre: Categoria, nome, preço, data_entrada, flag_recorde, flag_recorde_consecutivo; Dica: Use LAG() ou compare com o recorde anterior de alguma forma criativa.

WITH estoque_maxpreco AS (
	SELECT
		cat.nome_categoria,
		e.nome,
		e.preco,
		e.data_entrada,
		max(e.preco) OVER(PARTITION BY cat.nome_categoria ORDER BY e.data_entrada) AS max_preco
	FROM estoque e
	LEFT JOIN categorias cat ON cat.id=e.categoria_id
	ORDER BY cat.nome_categoria, e.data_entrada
)

SELECT
	*,
    CASE
		WHEN em.preco >= em.max_preco THEN 'Sim!'
        ELSE '-'
    END AS flag_recorde,
	CASE
		WHEN em.preco >= em.max_preco THEN '-'
        ELSE 'Consecutivo!'
    END AS flag_recorde_consecutivo
FROM estoque_maxpreco em;

#Aqui não usei LAG() pois é o próximo passo dos estudos, não gosto de pular.

#Nível 17-20: Desafios analíticos complexos

#Exercício 17 - Participação acumulada (Pareto) Crie um relatório que mostre para todos os produtos (ordenados do mais caro para o mais barato):
#Nome, preço, %_individual: percentual que cada produto representa do total geral, %_acumulada: percentual acumulado (soma dos percentuais até aquele produto)
#categoria_pareto: classifique como 'A' se até 80% acumulado, 'B' se até 95%, 'C' se acima de 95%, Contexto: Isso é a Análise de Pareto (80/20) aplicada a produtos.

WITH estoque_pct1 AS (
	SELECT
		e.nome,
		e.preco,
        e.data_entrada,
		e.preco/sum(e.preco) over()*100 AS pct_individual
	FROM estoque e
),

estoque_pct2 AS (
SELECT
	ep1.nome,
    ep1.preco,
    ep1.pct_individual,
    SUM(ep1.pct_individual) OVER(ORDER BY ep1.data_entrada) AS pct_acumulada
FROM estoque_pct1 ep1
)

SELECT
	ep2.nome,
    ep2.preco,
    concat(round(ep2.pct_individual, 2), '%') AS pct_individual_format, 
    concat(round(ep2.pct_acumulada, 2), '%') AS pct_acumulada_format,
    CASE
		WHEN pct_acumulada <= 80 THEN 'A'
        WHEN pct_acumulada <= 95 THEN 'B'
        WHEN pct_acumulada > 95 THEN 'C'
    END AS categoria_pareto
FROM estoque_pct2 ep2;

#Nesse problema tive que separar a segunda CTE para fazer o SUM(pct_individual) pq o MySQL não permite usar o SUM da primeira CTE dentro de outro SUM, por ser wf
#separei a query principal da segunda CTE pra conseguir fazer a formatação das porcentagens e fazer o CASE WHEN sobre a pct_acumulada que é uma WF.

#Exercício 19 - Z-score dos produtos
#Calcule o z-score de cada produto dentro de sua categoria. O z-score indica quantos desvios padrão um valor está acima ou abaixo da média:
#z-score = (preco - media_categoria) / desvio_padrao_categoria
#Mostre nome, categoria, preco, media_categoria, desvio_padrao_categoria, z-score (arredondado para 2 casas) e uma classificação:
#'Muito acima' se z-score > 2, 'Acima' se z-score entre 1 e 2, 'Médio' se z-score entre -1 e 1, 'Abaixo' se z-score entre -2 e -1, 'Muito abaixo' se z-score < -2
#Dica: O MySQL tem a função STDDEV() que pode ser usada como Window Function!

WITH estoque_zscore AS (
	SELECT
		e.nome,
		cat.nome_categoria,
		e.preco,
		round(AVG(e.preco) OVER(PARTITION BY cat.nome_categoria), 2) AS media_categoria,
		round(STDDEV(e.preco) OVER(PARTITION BY cat.nome_categoria), 2) AS desvio_padrao_categoria,
		round((e.preco - AVG(e.preco) OVER(PARTITION BY cat.nome_categoria))/(STDDEV(e.preco) OVER(PARTITION BY cat.nome_categoria)), 2) AS z_score
	FROM estoque e
	LEFT JOIN categorias cat ON cat.id=e.categoria_id
)

SELECT
	*,
    CASE 
		WHEN z_score > 2 THEN 'Muito Acima'
        WHEN z_score BETWEEN 1 AND 2 THEN 'Acima'
        WHEN z_score BETWEEN -1 AND 1 THEN 'Médio'
        WHEN z_score BETWEEN -2 AND -1 THEN 'Abaixo'
        WHEN z_score < -2 THEN 'Muito Abaixo'
    END AS classificacao
FROM estoque_zscore ez;

#Achei esse exercício divertido, gosto muito de lidar com fórmulas (sou físico né haha).

#Exercício 20 - Desafio final - Relatório de performance de vendas
#Combine as tabelas vendas e estoque para criar um relatório completo de performance de vendas:
#Para cada produto vendido, mostre: Nome do produto, categoria, data da venda, valor da venda, Preço original do produto no estoque (para comparação), Diferença entre preço de venda e preço original
#Percentual de desconto/aumento em relação ao original, Média móvel de vendas dos últimos 3 meses (considere apenas vendas deste produto), Comparação com a venda anterior deste mesmo produto (usando LAG)
#Ranking de vendas por valor dentro da sua categoria (usando DENSE_RANK), Percentual que esta venda representa do total vendido da categoria
#Classificação da venda: 'Excelente' se valor > média da categoria + 1 desvio padrão, 'Boa' se valor entre a média e média + 1 desvio, 'Regular' se valor entre a média e média - 1 desvio, 'Ruim' se valor < média - 1 desvio
WITH venda_estoque_parcial AS (
	SELECT
		e.nome,
		cat.nome_categoria,
		v.data_venda,
		v.preco_venda,
		e.preco AS preco_original,
		v.preco_venda-e.preco AS diferenca_preco,
		round(((v.preco_venda/e.preco)-1)*100, 2) AS pct_diferenca,
		round(avg(v.preco_venda) OVER(PARTITION BY e.nome ORDER BY v.data_venda RANGE BETWEEN INTERVAL 2 MONTH PRECEDING AND CURRENT ROW), 2) as media_movel_3m_produto,
		-- não vou fazer a parte do LAG()
		DENSE_RANK() OVER(PARTITION BY cat.nome_categoria ORDER BY v.preco_venda DESC) AS ranking_vendas_categoria,
		round((v.preco_venda/sum(v.preco_venda) OVER(PARTITION BY cat.nome_categoria))*100,2) AS pct_venda_total_categoria,
        -- para o CASE da query princial:
        STDDEV(v.preco_venda) OVER(PARTITION BY cat.nome_categoria) AS desvio_padrao_categoria, 
        avg(v.preco_venda) OVER(PARTITION BY cat.nome_categoria) AS media_preco_categoria
	FROM vendas v
	LEFT JOIN estoque e ON e.id=v.id_produto
	LEFT JOIN categorias cat ON cat.id=e.categoria_id
)

SELECT
	vep.nome,
    vep.nome_categoria,
    vep.data_venda,
    vep.preco_venda,
    vep.preco_original,
    vep.diferenca_preco,
    concat(vep.pct_diferenca, '%') AS pct_diferenca_formatado,
    vep.media_movel_3m_produto,
    vep.ranking_vendas_categoria,
    concat(vep.pct_venda_total_categoria, '%') AS pct_venda_total_categoria_formatado,
    CASE
		WHEN vep.preco_venda > (media_preco_categoria + desvio_padrao_categoria) THEN 'Excelente'
        WHEN vep.preco_venda > (media_preco_categoria)  THEN 'Boa'
        WHEN vep.preco_venda > (media_preco_categoria - desvio_padrao_categoria) THEN 'Regular'
        ELSE 'Ruim' 
    END AS classificacao
FROM venda_estoque_parcial vep

#O CASE WHEN, eu fiz de acordo com as intruções, entretanto, tem um problema. Se o preco_venda for = média_preco_categoria ele cai tanto em 'Boa' quanto 'Regular'...