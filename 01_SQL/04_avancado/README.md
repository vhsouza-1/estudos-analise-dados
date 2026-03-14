# SQL Avançado - Estudos (em andamento)

Aqui está meus passos no conteúdo avançado em SQL, desenvolvidos durante estudos autodidatas. Nessa parte encontram-se estudos sobre CTEs, Windows Functions e...

- Obs1: diferentemente das outras pastas, aqui encontram todos os exercícios realizados.
- Obs2: o ambiente utilizado foi o MySQL.

## Estrutura 

- ['01_ctes_fundamentos.sql'](01_ctes_fundamentos.sql) - CTEs básicas (filtros, médias, somas), múltiplas CTEs, joins, CASE WHEN, CTEs aninhadas, calendário, comparações

- ['02_ctes_algumas_aplicacoes.sql'](02_ctes_algumas_aplicacoes.sql) - CTEs com filtros e joins simples, classificações, percentuais, agregações por mês, múltiplas abordagens, rankings (self-join), comparação mês a mês

- ['03_ctes_alguns_desafios.sql'](03_ctes_alguns_desafios.sql) - Médias por categoria e relatórios com múltiplas CTEs, rankings sem Window Functions, classificações complexas
  
- ['04_wf_funcoes_ranking_1.sql'](04_wf_funcoes_ranking_1.sql) - ROW_NUMBER, RANK, DENSE_RANK, NTILE, TOP N por categoria
  
- ['05_wf_funcoes_ranking_2.sql'](05_wf_funcoes_ranking_2.sql) - Rankings com desempate, TOP N por cor/mês, gaps
  
- ['06_wf_funcoes_agregacao_1.sql'](06_wf_funcoes_agregacao_1.sql) - SUM, AVG, COUNT e MAX com Window Functions, médias móveis, frames, RANGE
- ['07_wf_funcoes_agregacao_2.sql'](07_wf_funcoes_agregacao_2.sql) - Múltiplas métricas por categoria, recordes consecutivos, análise de Pareto, Z-score, relatório completo de vendas
- ['08_wf_funcoes_deslocamento_1.sql'](08_wf_funcoes_deslocamento_1.sql) - LAG, LEAD, FIRST_VALUE, LAST_VALUE, comparações temporais, detecção de tendências
- ['09_wf_funcoes_deslocamento_2.sql'](09_wf_funcoes_deslocamento_2.sql) - Análises avançadas com deslocamento, padrões sazonais, customer journey, dashboard executivo com storytelling

## Tabelas

### Tabela 'estoque'

A tabela contém 15 produtos (carros e motos) com as seguintes colunas:

- 'id' - identificador único
- 'nome' - nome do produto
- 'preco' - preço
- 'categoria_id' - id da categoria (referência à tabela categoria)
- 'cor_id' - id da cor (referência à tabela cores)
- 'fabrication' - ano de fabricação
- 'data_entrada' - data de entrada no estoque

### Tabela 'cores'

A tabela contém 6 cores, usadas para referenciar as cores do 'estoque'

- 'id' - identificar único
- 'nome_cor' - nome da cor

### Tabela 'categorias'

A tabela contém 2 categorias (Carro/Moto), usadas para referenciar as categorias do 'estoque'

- 'id' - identificar único
- 'nome_categoria' - nome da categoria

### Tabela 'vendas'

Contém 6 vendas, com as seguintes colunas:

- id_venda - identificador único
- id_produto - id do produto (referência à tabela estoque)
- data_venda - data da venda
- preco_venda - preço da venda
- cliente_nome - nome do cliente

## Conceitos praticados

### Parte 1 - CTEs (Common Table Expressions)
- CTEs básicas com filtros e funções agregadas
- Múltiplas CTEs no mesmo `WITH`
- CTEs aninhadas (uma CTE que referencia outra)
- `CROSS JOIN` com CTEs para comparações com médias globais
- Criação de calendários com `UNION ALL` dentro de CTEs
- CTEs com `CASE WHEN` para classificação de dados
- Rankings com `SELF JOIN` dentro de CTEs (sem Window Functions)
- Análise mês a mês com comparação ao mês anterior
- Múltiplas abordagens para o mesmo problema (CTE vs subconsulta)
- Relatórios com 3 ou mais CTEs encadeadas
- TOP 3 por categoria com `HAVING`

### Parte 2 - Funções de Ranking (Window Functions)
- `ROW_NUMBER()` para numeração sequencial
- `RANK()` e `DENSE_RANK()` para rankings com empates
- Comparação entre as 3 funções de ranking
- `PARTITION BY` para rankings dentro de categorias/grupos
- Critérios de desempate no `ORDER BY` da Window Function
- `NTILE()` para quartis, percentis e distribuição em faixas
- Filtro de TOP N por categoria (com CTE + WHERE)
- Identificação de gaps no ranking
- TOP N por cor, por mês, por data de entrada

### Parte 3 - Funções de Agregação como Window Functions
- `SUM()` como janela acumulada (total acumulado)
- `AVG()` para médias por categoria e médias móveis
- `COUNT()` para contagem progressiva
- `MIN()` e `MAX()` para valores acumulados e amplitude
- Frames: `ROWS UNBOUNDED PRECEDING`, `ROWS BETWEEN`
- Médias móveis com diferentes janelas (3, 5, 7 períodos)
- `RANGE BETWEEN INTERVAL` para análises temporais complexas
- Recordes consecutivos com `MAX()` e `CASE`
- Análise de Pareto (80/20) com percentuais acumulados
- Z-score com `STDDEV()` e classificação estatística

### Parte 4 - Funções de Deslocamento (Window Functions)
- `LAG()` para acessar valores anteriores
- `LEAD()` para acessar valores posteriores
- `FIRST_VALUE()` para primeiro valor da janela
- `LAST_VALUE()` com frame correto (`ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING`)
- LAG com offset maior (2, 3, 12 posições)
- Comparação com primeiro/último da categoria
- Detecção de tendências (subidas, quedas, picos)
- Comparação ano a ano para padrões sazonais
- Dias desde a última venda (customer journey)
- Projeções e simulações de tendências

### Parte 5 - Desafios Analíticos Avançados
- Dashboard gerencial com múltiplas métricas (Exercício 10 - 06_wf_funcoes_agregacao_1)
- Relatório completo de vendas (Exercício 20 - 07_wf_funcoes_agregacao_2)
- Análise de performance completa por produto (Exercício 18 - 09_wf_funcoes_deslocamento_2)
- **Dashboard executivo com storytelling** (Exercício 20 - 09_wf_funcoes_deslocamento_2):
  - Métricas gerais (quantidade, média, total)
  - Evolução temporal (primeiro/último produto, variação percentual)
  - Destaques (mais caro, mais barato, maiores variações)
  - Análise de ranking (acima/abaixo da média, posição mediana)
- Comparação entre abordagens: SELF JOIN (manual) vs Window Functions
- Múltiplas CTEs para organizar consultas complexas
- Otimização e legibilidade de código
- Tratamento de valores nulos com `COALESCE()`
---

- Início dos estudos: Fevereiro de 2026
- Autor: Vinícius Henrique Souza
- email: vinicius.h.zlc@gmail.com
- linkedin: https://www.linkedin.com/in/vin%C3%ADcius-henrique-souza-17a077218/
