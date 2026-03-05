# SQL Intermediário - Estudos


Aqui está uma síntese dos meus passos intermediários em SQL, desenvolvidos durante estudos autodidatas. Nessa parte encontram-se estudos sobre Funções de String e de data, lógica condicional (CASE WHEN) e UNION/UNION ALL.

- Obs1: aqui encontram-se apenas alguns dos exercícios feitos, buscando uma síntese dos estudos.
- Obs2: o ambiente utilizado foi o MySQL.
- Obs3: aqui foi onde me apaixonei por SQL.

## Estrutura

- ['tabelas_utilizadas.sql'](01_tabelas_utilizadas.sql) - Criação e inserção dos dados da tabela 'estoque', 'cores', 'categorias' e 'vendas' utilizadas em todos os exercícios.
- ['string_funcions.sql'](02_string_functions.sql) - Exercícios focados em manipulação de textos.
- ['date_functions.sql'](03_date_functions.sql) - Análises temporais e séries históricas.
- ['case_when.sql'](04_case_when.sql) - Lógica condicional e classificação.
- ['union_and_union_all'](05_union_and_union_all.sql) - Combinação de resultados.


## Tabela 'estoque'

A tabela contém 15 produtos (carros e motos) com as seguintes colunas:

- 'id' - identificador único
- 'nome' - nome do produto
- 'preco' - preço
- 'categoria_id' - id da categoria (referência à tabela categoria)
- 'cor_id' - id da cor (referência à tabela cores)
- 'fabrication' - ano de fabricação
- NOVO 'data_entrada' - data de entrada no estoque

## Tabela 'cores'

A tabela contém 6 cores, usadas para referenciar as cores do 'estoque'

- 'id' - identificar único
- 'nome_cor' - nome da cor

## Tabela 'categorias'

A tabela contém 2 categorias (Carro/Moto), usadas para referenciar as categorias do 'estoque'

- 'id' - identificar único
- 'nome_categoria' - nome da categoria

## NOVO Tabela 'vendas'

Contém 6 vendas, com as seguintes colunas:

- id_venda - identificador único
- id_produto - id do produto (referência à tabela estoque)
- data_venda - data da venda
- preco_venda - preço da venda
- cliente_nome - nome do cliente

---

- Início dos estudos: Fevereiro de 2026
- Autor: Vinícius Henrique Souza
- email: vinicius.h.zlc@gmail.com
- linkedin: https://www.linkedin.com/in/vin%C3%ADcius-henrique-souza-17a077218/
