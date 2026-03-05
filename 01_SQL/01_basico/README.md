# SQL Básico - Estudos

Aqui está uma síntese de meus primeiros passos em SQL, desenvolvidos durante estudos autodidatas. Nessa parte encontram-se conceitos fundamentais do SQL, desde consultas simples até subconsultas escalares e correlacionadas.

- Obs1: aqui encontram-se apenas alguns dos exercícios feitos, buscando uma síntese dos estudos.
- Obs2: o ambiente utilizado foi o MySQL.

## Estrutura

- ['tabela_estoque.sql'](01_tabela_estoque.sql) - Criação e inserção dos dados da tabela `estoque`, utilizadas em todos os exercícios. 
- ['02_fundamentos_sql.sql'](02_fundamentos_sql.sql) - Consultas básicas, funções agregadas, `GROUP BY`, `HAVING`, `LIMIT` e `OFFSET`.
- ['03_subconsultas.sql'](03_subconsultas.sql) - Subconsultas escalares, subconsultas correlacionadas e alguns desafios intermediários.

## Tabela 'estoque'

A tabela contém 15 produtos (carros e motos) com as seguintes colunas:

- 'id' - identificador único
- 'name' - nome do produto
- 'price' - preço
- 'tipo' - categoria ('carro' ou 'moto')
- 'color' - cor
- 'fabrication' - ano de fabricação


## Conceitos praticados

### Parte 1 - Fundamentos

- `SELECT`, `WHERE`, `ORDER BY`
- Operadores lógicos (`AND`, `OR`, `<>`)
- Funções agregadas: `COUNT`, `AVG`, `SUM`, `MIN`, `MAX`
- `GROUP BY` e `HAVING`
- `LIMIT` e `OFFSET`

### Parte 2 - Subconsultas

- Subconsultas escalares no `WHERE`
- Subconsultas escalares no `SELECT`
- Subconsultas no `HAVING`
- Subconsultas correlacionadas (com aliases `e1`, `e2`)
- Problemas combinando agregação, filtros e subconsultas

---

- Início dos estudos: Fevereiro de 2026
- Autor: Vinícius Henrique Souza
- email: vinicius.h.zlc@gmail.com
- linkedin: https://www.linkedin.com/in/vin%C3%ADcius-henrique-souza-17a077218/
