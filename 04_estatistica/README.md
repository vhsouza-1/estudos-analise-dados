# Bloco 4: Estatística para Dados

![Status](https://img.shields.io/badge/Status-Concluído-brightgreen.svg)
![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Pandas](https://img.shields.io/badge/Pandas-2.0+-green.svg)
![NumPy](https://img.shields.io/badge/NumPy-1.24+-orange.svg)
![SciPy](https://img.shields.io/badge/SciPy-1.10+-red.svg)

## Sobre o Bloco

Este bloco cobre os fundamentos de Estatística para Análise de Dados, com foco em aplicação prática usando Python. Todo o conteúdo foi desenvolvido com ênfase no que um Analista de Dados Jr precisa saber no dia a dia.

**Carga horária estimada:** 8 aulas | ~25 horas

## Estrutura do Bloco

- 00_numpy_essencial.py - NumPy para iniciantes
- 01_estatistica_descritiva.py - Média, mediana, desvio, quartis
- 02_distribuicoes_probabilidade.py - Normal, Binomial, Poisson, TCL
- 03_correlacao_causalidade.py - Pearson, Spearman, heatmap
- 04_teste_ab_conceitos.py - H0, H1, p-valor, erros
- 05_teste_ab_pratica.py - Proporções, médias, IC
- 06_regressao_linear_conceitos.py - Reta, inclinação, R²
- 07_regressao_linear_pratica.py - stats.linregress(), previsões

## Conteúdo das Aulas

### Aula 00: NumPy Essencial
**Arquivo:** `00_numpy_essencial.py`

| Conceito | Função |
|----------|--------|
| Arrays vs listas | np.array(), np.arange(), np.linspace() |
| Dados aleatórios | np.random.normal(), np.random.uniform(), np.random.choice() |
| Indexação | arr[0], arr[2:5], matriz[0,1] |
| Operações vetorizadas | arr * 2, arr1 + arr2 |
| axis=0 vs axis=1 | np.sum(arr, axis=0), np.mean(arr, axis=1) |
| Condicional | np.where(cond, true, false) |

### Aula 01: Estatística Descritiva
**Arquivo:** `01_estatistica_descritiva.py`

| Conceito | Função | Interpretação |
|----------|--------|---------------|
| Média | np.mean() | Valor típico (dados simétricos) |
| Mediana | np.median() | Valor típico (dados assimétricos) |
| Moda | stats.mode() | Valor mais frequente |
| Desvio Padrão | np.std() | Dispersão dos dados |
| IQR | Q3 - Q1 | Dispersão robusta a outliers |
| Assimetria | stats.skew() | >0 direita, <0 esquerda |
| Curtose | stats.kurtosis() | Caudas pesadas/leves |

### Aula 02: Distribuições de Probabilidade
**Arquivo:** `02_distribuicoes_probabilidade.py`

| Distribuição | Quando usar | Função |
|--------------|-------------|--------|
| Normal (Gaussiana) | Dados contínuos e simétricos | stats.norm.pdf(), stats.norm.cdf() |
| Binomial | Sucessos em n tentativas | stats.binom.pmf(), stats.binom.cdf() |
| Poisson | Eventos por tempo/espaço | stats.poisson.pmf(), stats.poisson.cdf() |
| Uniforme | Valores igualmente prováveis | np.random.uniform() |

**Teorema Central do Limite:** A média amostral tende à normal quando n ≥ 30.

### Aula 03: Correlação e Causalidade
**Arquivo:** `03_correlacao_causalidade.py`

| Conceito | Função | Interpretação |
|----------|--------|---------------|
| Pearson (r) | stats.pearsonr(x, y) | Correlação LINEAR |
| Spearman (ρ) | stats.spearmanr(x, y) | Correlação de ordem (robusta) |
| Matriz de correlação | df.corr() | Todas as correlações de uma vez |
| Heatmap | sns.heatmap(corr, annot=True) | Visualização da matriz |

** LIÇÃO MAIS IMPORTANTE:** Correlação não implica causalidade!

### Aula 04: Teste A/B - Conceitos
**Arquivo:** `04_teste_ab_conceitos.py`

| Conceito | Significado |
|----------|-------------|
| H0 (Hipótese Nula) | "Não há diferença" |
| H1 (Hipótese Alternativa) | "Há diferença" |
| P-valor | P(ver os dados | H0 verdadeira) |
| α (nível de significância) | Limiar para rejeitar H0 (tradicionalmente 0.05) |
| Erro Tipo I | Falso positivo (α) |
| Erro Tipo II | Falso negativo (β) |
| Poder estatístico | 1 - β (detectar efeito real) |

### Aula 05: Teste A/B - Aplicação Prática
**Arquivo:** `05_teste_ab_pratica.py`

| Situação | Teste | Função |
|----------|-------|--------|
| Comparar proporções (conversão) | Z-test | proportions_ztest(count, nobs) |
| Comparar médias (tempo, valor) | T-test | stats.ttest_ind(grupoA, grupoB) |
| Tamanho da amostra | Power analysis | NormalIndPower().solve_power() |

**Regra de decisão (α = 0.05):**
- p-valor < 0.05 → Rejeitamos H0 (diferença significativa)
- p-valor ≥ 0.05 → Não rejeitamos H0

### Aula 06: Regressão Linear - Conceitos
**Arquivo:** `06_regressao_linear_conceitos.py`

| Conceito | Equação | Significado |
|----------|---------|-------------|
| Inclinação (a) | y = a*x + b | Impacto de x em y |
| Intercepto (b) | y = a*x + b | Valor de y quando x=0 |
| R² | r ** 2 | % da variação explicada pelo modelo |

**Interpretação do R²:**
- R² > 0.7: Forte (modelo confiável)
- 0.4 - 0.7: Moderado (útil com cautela)
- R² < 0.4: Fraco (outras variáveis são mais importantes)

### Aula 07: Regressão Linear - Aplicação Prática
**Arquivo:** `07_regressao_linear_pratica.py`

| O que fazer | Como fazer |
|-------------|------------|
| Executar regressão | slope, intercept, r, p, stderr = stats.linregress(x, y) |
| Fazer previsão | y_pred = slope * x_novo + intercept |
| Calcular R² | r_squared = r ** 2 |

## Exemplos Práticos (com Python)

### Correlação

from scipy import stats
r, p_valor = stats.pearsonr(df['horas_estudo'], df['nota'])

### Teste A/B (conversão)

from statsmodels.stats.proportion import proportions_ztest
z_stat, p_valor = proportions_ztest([conversoes_A, conversoes_B], [n_A, n_B])

### Regressão Linear

slope, intercept, r, p, stderr = stats.linregress(df['marketing'], df['vendas'])
print(f"vendas = {slope:.2f} * marketing + {intercept:.2f}")
print(f"R² = {r**2:.4f}")

## 📌 Principais Aprendizados

| Conceito | O que você deve saber |
|----------|----------------------|
| Média vs Mediana | Média para dados simétricos, mediana para dados com outliers |
| Correlação | Mede RELAÇÃO, não CAUSA |
| P-valor | Probabilidade de ver os dados SE H0 for verdadeira |
| Teste A/B | Padrão ouro para causalidade em negócios |
| Regressão | Prever y a partir de x (mas cuidado com extrapolação) |

## 🛠️ Bibliotecas Utilizadas

| Biblioteca | Versão | Finalidade |
|------------|--------|------------|
| numpy | 1.24+ | Operações numéricas e arrays |
| pandas | 2.0+ | Manipulação de dados |
| scipy.stats | 1.10+ | Testes estatísticos e distribuições |
| statsmodels | 0.14+ | Teste de proporções e poder estatístico |
| matplotlib | 3.7+ | Visualizações base |
| seaborn | 0.12+ | Gráficos estatísticos |

## ▶️ Como Utilizar

# Clone o repositório
git clone https://github.com/seu-usuario/estudo-analise-dados.git

# Navegue até a pasta do bloco
cd estudo-analise-dados/04_estatistica

# Execute qualquer aula (exemplo)
python 05_teste_ab_pratica.py

## Projetos Relacionados

- [Análise Estatística do ENEM 2019](../projetos/03_analise_dados_enem_2019) - Projeto integrador aplicando todos os conceitos

## Contato

- Nome: Vinícius Henrique Souza
- Físico | Mestre em Educação em Ciências | Estudante de Análise de Dados
- email: vinicius.h.zlc@gmail.com
- linkedin: [https://www.linkedin.com/in/vin%C3%ADcius-henrique-souza-17a077218/](https://www.linkedin.com/in/vin%C3%ADcius-henrique-souza-17a077218/)


## Agradecimentos

- DeepSeek (assistente de estudos)
- INEP pelos microdados do ENEM
- Comunidade de dados (documentação aberta)
