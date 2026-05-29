# Bloco 5: Excel para Análise de Dados

![Status](https://img.shields.io/badge/Status-Concluído-brightgreen.svg)
![Excel](https://img.shields.io/badge/Excel-2019%2B-blue.svg)
![Nível](https://img.shields.io/badge/Nível-Intermediário-orange.svg)

## 📋 Sobre o Bloco

Este bloco cobre os fundamentos do Excel para Análise de Dados, com foco no que um Analista de Dados Jr precisa saber no dia a dia. Todo o conteúdo foi desenvolvido para quem já tem familiaridade com Python/pandas, estabelecendo paralelos entre as ferramentas.

**Carga horária estimada:** 5 aulas | ~15 horas

## Estrutura do Bloco

- 01_funcoes_logicas/ - Arquivo .py para gerar dataset, .xlsx com exercícios resolvidos e .txt com descrição dos exercícios
- 02_procv_xlookup/ - Arquivo .py para gerar dataset, .xlsx com exercícios resolvidos e .txt com descrição dos exercícios
- 03_tabela_dinamica/ - Arquivo .py para gerar dataset, .xlsx com exercícios resolvidos e .txt com descrição dos exercícios
- 04_formatacao_condicional/ - Arquivo .py para gerar dataset, .xlsx com exercícios resolvidos e .txt com descrição dos exercícios
- 05_graficos/ - Arquivo .py para gerar dataset, .xlsx com exercícios resolvidos e .txt com descrição dos exercícios

## Conteúdo das Aulas

### Aula 01: Funções Lógicas
**Arquivo:** `01_funcoes_logicas/`

| Função | O que faz | Equivalente Python |
|--------|-----------|-------------------|
| =SE(cond; verdadeiro; falso) | Testa uma condição | np.where(cond, true, false) |
| =E(cond1; cond2; ...) | Verdadeiro se TODAS forem verdadeiras | & (and) |
| =OU(cond1; cond2; ...) | Verdadeiro se ALGUMA for verdadeira | | (or) |
| =SEERRO(fórmula; fallback) | Se der erro, retorna fallback | try/except ou pd.to_numeric(..., errors='coerce') |

### Aula 02: PROCV e XLOOKUP
**Arquivo:** `02_procv_xlookup/`

| Função | O que faz | Equivalente Python |
|--------|-----------|-------------------|
| =PROCV(valor; tabela; coluna_retorno; 0) | Busca à direita (esquerda não) | df.merge(on='col') |
| =PROCX(valor; vetor_proc; vetor_ret; "não achou") | Busca em qualquer direção | df['col'].map(dict(zip(...))) |
| =ÍNDICE(vetor; posição) + =CORRESP(valor; vetor; 0) | Alternativa clássica | vetor[posicao] |

### Aula 03: Tabela Dinâmica
**Arquivo:** `03_tabela_dinamica/`

| Área da Tabela Dinâmica | O que faz | Equivalente Python |
|------------------------|-----------|-------------------|
| LINHAS | Agrupa por esta coluna (vertical) | groupby(...) |
| COLUNAS | Agrupa por esta coluna (horizontal) | pivot_table(columns=...) |
| VALORES | O que você quer calcular | .sum(), .mean() |
| FILTROS | Filtra antes de agrupar | df[df['col'] == valor] |

### Aula 04: Formatação Condicional
**Arquivo:** `04_formatacao_condicional/`

| Tipo de Formatação | O que faz | Quando usar |
|-------------------|-----------|-------------|
| Barras de Dados | Barra proporcional ao valor | Comparar magnitude |
| Escala de Cores | Gradiente (verde → vermelho) | Destacar padrões |
| Conjunto de Ícones | ✔️, ⚠️, ❌ | Status binário/ternário |
| Regras personalizadas | Fórmula para definir condição | Casos complexos |

### Aula 05: Gráficos
**Arquivo:** `05_graficos/`

| Tipo de Gráfico | Para que serve | Equivalente Python |
|-----------------|----------------|-------------------|
| Colunas/Barras | Comparar categorias | sns.barplot() |
| Linhas | Mostrar tendência ao longo do tempo | sns.lineplot() |
| Pizza/Anel | Mostrar proporções (poucas categorias) | plt.pie() |
| Dispersão (XY) | Relação entre duas variáveis | sns.scatterplot() |
| Barras empilhadas | Composição por categoria | df.plot(kind='bar', stacked=True) |

## Paralelo Excel ↔ Python

| Conceito | Excel | Python (pandas) |
|----------|-------|-----------------|
| Condicional | =SE(cond; true; false) | np.where(cond, true, false) |
| Busca | =PROCX(valor; vetor_proc; vetor_ret) | df.merge() ou .map(dict) |
| Agrupamento | Tabela Dinâmica | df.groupby().agg() |
| Formatação condicional | Formatação Condicional | df.style |
| Gráfico de barras | Inserir → Gráfico → Colunas | sns.barplot() |
| Gráfico de linhas | Inserir → Gráfico → Linhas | sns.lineplot() |
| Dispersão | Inserir → Gráfico → Dispersão | sns.scatterplot() |

## 👨‍💻 Autor

Vinicius H. Souza

- Físico | Mestre em Educação em Ciências
- Estudante de Análise de Dados

![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-100000?style=flat&logo=github&logoColor=white)

## 📄 Licença

Este projeto está sob a licença MIT.

## 🙏 Agradecimentos

- DeepSeek (assistente de estudos)
- Microsoft (Excel)
