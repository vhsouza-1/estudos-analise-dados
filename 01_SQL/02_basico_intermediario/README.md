# SQL Básico-Intermediário - Estudos

Aqui está uma síntese de meus passos básico-intermdiários em SQL, desenvolvidos durante estudos autodidatas. Nessa parte encontram-se principalmente alguns estudos com JOINs e tabelas derivadas.

- Obs1: aqui encontram-se apenas alguns dos exercícios feitos, buscando uma síntese dos estudos.
- Obs2: o ambiente utilizado foi o MySQL.

Obs2: o ambiente utilizado foi o MySQL.

## Estrutura

- ['tabelas_utilizadas'](01_tabelas_utilizadas.sql) - Criação e inserção dos dados da tabela 'estoque', 'categorias' e 'cores', utilizadas em todos os exercícios
- ['joins_introducao.sql'](02_joins_introducao.sql) - INNER JOIN, LEFT JOIN, filtros com WHERE
- ['joins_agregacao.sql'](03_joins_agregacao.sql) - GROUP BY com JOIN, HAVING, estatísticas
- ['joins_subconsultas.sql'](04_joins_subconsultas.sql) - Subconsultas correlacionadas com JOIN 
- ['tabelas_derivadas.sql'](05_tabelas_derivadas.sql) - Subconsultas no FROM

## Tabelas
### Tabela 'estoque'

A tabela contém 15 produtos (carros e motos) com as seguintes colunas:

- 'id' - identificador único
- 'name' - nome do produto
- 'price' - preço
- 'categoria_id' - id da categoria (referência a tabela categoria)
- 'cor_id' - id da cor (referência a tabela cores)
- 'fabrication' - ano de fabricação

### Tabela 'cores'

A tabela contém 6 cores, usadas para referenciar as cores do 'estoque'

- 'id' - identificar único
- 'nome_cor' - nome da cor

### Tabela 'categorias'

A tabela contém 2 categorias (Carro/Moto), usadas para referenciar as categorias do 'estoque'

- 'id' - identificar único
- 'nome_categoria' - nome da categoria

## Conceitos praticados

### Parte 1 - Introdução aos JOINs
- `INNER JOIN` simples e múltiplo (2+ tabelas)
- `LEFT JOIN` para incluir registros sem correspondência
- Simulação de `RIGHT JOIN` com `LEFT JOIN` invertido
- Filtros com `WHERE` em consultas com JOIN
- `COALESCE` para tratar valores nulos em JOINs

### Parte 2 - Agregações com JOIN
- Funções agregadas combinadas com JOIN (`COUNT`, `AVG`, `MIN`, `MAX`)
- `GROUP BY` com JOIN para estatísticas por categoria/cor
- `HAVING` para filtrar grupos após agregação
- Subconsultas escalares no `SELECT` para comparações

### Parte 3 - Subconsultas com JOIN
- Subconsultas correlacionadas no `WHERE`
- Comparações com média da categoria (`price > média da sua categoria`)
- Comparações com média da cor (`price > média da sua cor`)
- Subconsultas com múltiplas colunas (operador `IN`)
- Subconsultas escalares no `SELECT` para calcular diferenças

### Parte 4 - Tabelas Derivadas (Subconsultas no FROM)
- Criação de tabelas derivadas para pré-processamento
- `JOIN` com tabelas derivadas para enriquecer consultas
- Múltiplos níveis de aninhamento de consultas
- Cálculo de rankings e posições sem `WINDOW FUNCTIONS`
- Pré-cálculo de estatísticas (médias, totais) antes do JOIN principal


---

- Início dos estudos: Fevereiro de 2026
- Autor: Vinícius Henrique Souza
- email: vinicius.h.zlc@gmail.com
- linkedin: https://www.linkedin.com/in/vin%C3%ADcius-henrique-souza-17a077218/
