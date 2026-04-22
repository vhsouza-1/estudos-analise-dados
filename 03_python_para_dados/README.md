# Python para Dados - Estudos

Esta pasta documenta minha jornada de aprendizado em Python para análise de dados, estruturada em módulos progressivos que vão desde a introdução ao Pandas até visualização de dados.

- Ambiente: Anaconda, PyCharm
- Período: Abril 2026 - Em andamento
- Status: Em desenvolvimento

## Estrutura dos Estudos

| Módulo | Tema |
|--------|------|
| [01_introducao_pandas](./01_introducao_pandas) | Series, DataFrame, leitura de dados, groupby |

## Detalhamento dos Módulos

### MÓDULO 1 - Introdução ao Pandas
**Objetivo:** Aprender a biblioteca mais importante para análise de dados em Python

#### Aula 01 - O que é Pandas?
- O que é Pandas e por que usar
- Instalação e importação (`import pandas as pd`)
- Estruturas principais: Series e DataFrame
- Primeiro contato com a documentação

#### Aula 02 - Series (Uma coluna de dados)
- Criar Series a partir de listas e dicionários
- Índices personalizados
- Acessar elementos por posição (`.iloc[]`) e por rótulo (`[]`)
- Operações matemáticas elemento a elemento
- Métodos úteis: `.sum()`, `.mean()`, `.max()`, `.min()`, `.count()`, `.describe()`
- Filtrar Series com condições

#### Aula 03 - DataFrame (Tabela completa)
- Criar DataFrame a partir de dicionários e listas de listas
- Visualizar dados: `.head()`, `.tail()`
- Informações básicas: `.info()`, `.shape`, `.columns`
- Resumo estatístico: `.describe()`
- Selecionar colunas (`df["coluna"]`, `df[["col1", "col2"]]`)
- Adicionar novas colunas (fixas, calculadas, condicionais com `.apply()`)

#### Aula 04 - Leitura de Dados
- `pd.read_csv()` - ler arquivos CSV
- `pd.read_excel()` - ler arquivos Excel
- Parâmetros úteis: `sep`, `encoding`, `header`, `names`, `usecols`, `nrows`
- Comparação com o módulo `csv` (Pandas é muito mais simples)

#### Aula 05 - Agrupamentos (groupby)
- `df.groupby()` - agrupar dados por uma ou mais colunas
- Operações: `.sum()`, `.mean()`, `.count()`
- `.agg()` para múltiplas operações de uma vez
- `.idxmax()` para encontrar índices de valores máximos
- `.reset_index()` para transformar índice em coluna

#### Aula 06 - Merge e Concatenação (JOIN do Pandas) - *Em andamento*
- `pd.concat()` - empilhar DataFrames (UNION)
- `pd.merge()` - juntar DataFrames por colunas (INNER JOIN, LEFT JOIN, etc.)

#### Aula 07 - Tratamento de valores nulos - *Planejado*
- Identificar valores nulos (`.isnull()`, `.isna()`)
- Remover valores nulos (`.dropna()`)
- Preencher valores nulos (`.fillna()`)

#### Aula 08 - Limpeza de dados - *Planejado*
- Remover duplicatas (`.drop_duplicates()`)
- Converter tipos de dados (`.astype()`)
- Renomear colunas (`.rename()`)

#### Aula 09 - Projeto guiado - *Planejado*
- Aplicar todos os conceitos em um projeto completo
- Análise exploratória de dados
- Geração de relatórios

## Contato

- **Autor:** Vinícius Henrique Souza
- **Email:** vinicius.h.zlc@gmail.com
- **LinkedIn:** [linkedin.com/in/vinícius-henrique-souza](https://www.linkedin.com/in/vin%C3%ADcius-henrique-souza-17a077218/)
