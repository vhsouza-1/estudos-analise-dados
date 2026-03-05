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


## Tabela 'estoque'

A tabela contém 15 produtos (carros e motos) com as seguintes colunas:

- 'id' - identificador único
- 'name' - nome do produto
- 'price' - preço
- 'categoria_id' - id da categoria (referência a tabela categoria)
- 'cor_id' - id da cor (referência a tabela cores)
- 'fabrication' - ano de fabricação

## Tabela 'cores'

A tabela contém 6 cores, usadas para referenciar as cores do 'estoque'

- 'id' - identificar único
- 'nome_cor' - nome da cor

## Tabela 'categorias'

A tabela contém 2 categorias (Carro/Moto), usadas para referenciar as categorias do 'estoque'

- 'id' - identificar único
- 'nome_categoria' - nome da categoria

---

- Início dos estudos: Fevereiro de 2026
- Autor: Vinícius Henrique Souza
- email: vinicius.h.zlc@gmail.com
- linkedin: https://www.linkedin.com/in/vin%C3%ADcius-henrique-souza-17a077218/
