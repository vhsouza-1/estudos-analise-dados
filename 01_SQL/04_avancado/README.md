# SQL Avançado - Estudos

Aqui está meus passos no conteúdo avançado em SQL, desenvolvidos durante estudos autodidatas. Nessa parte encontram-se estudos sobre CTEs, Windows Functions e...

- Obs1: diferentemente das outras pastas, aqui encontram todos os exercícios realizados.
- Obs2: o ambiente utilizado foi o MySQL.

## Estrutura 

- ['01_CTEs_fundamentos.sql'](01_CTEs_fundamentos.sql) - CTEs básicas (filtros, médias, somas), múltiplas CTEs, joins, CASE WHEN, CTEs aninhadas, calendário, comparações

- ['02_CTEs_algumas_aplicacoes.sql'](02_CTEs_algumas_aplicacoes.sql) - CTEs com filtros e joins simples, classificações, percentuais, agregações por mês, múltiplas abordagens, rankings (self-join), comparação mês a mês

- ['03_CTEs_alguns_desafios.sql'](03_CTEs_alguns_desafios.sql) - Médias por categoria e relatórios com múltiplas CTEs, rankings sem Window Functions, classificações complexas

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

### CTEs Fundamentais
- CTEs básicas com `WHERE`, `AVG`, `SUM`
- `CROSS JOIN` com CTEs para comparações
- Múltiplas CTEs no mesmo `WITH`
- CTEs com `LEFT JOIN` e `GROUP BY`
- CTEs com `CASE WHEN` para classificação
- CTEs aninhadas (uma CTE usando outra)
- Criação de calendários com `UNION ALL`

### CTEs em Aplicações Práticas
- CTEs com filtros específicos
- CTEs independentes com `CROSS JOIN`
- Cálculo de percentuais com CTEs
- Agregações temporais (mês a mês)
- Múltiplas abordagens: CTE vs subconsulta no `FROM` vs subconsulta no `WHERE`
- Rankings com `SELF JOIN` (sem `WINDOW FUNCTIONS`)
- Análise mês a mês com comparação ao mês anterior

### Desafios com CTEs
- Diferença em relação à média da categoria
- Relatórios com 3+ CTEs encadeadas
- Percentuais de contribuição mensal
- TOP 3 por categoria (ranking com `HAVING`)
- Classificação temporal (`CASE WHEN`)
- Cálculo combinado: média + ranking + diferença
- `SELF JOIN` para posicionamento

---

- Início dos estudos: Fevereiro de 2026
- Autor: Vinícius Henrique Souza
- email: vinicius.h.zlc@gmail.com
- linkedin: https://www.linkedin.com/in/vin%C3%ADcius-henrique-souza-17a077218/
