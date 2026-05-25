# Análise Estatística do ENEM 2019

## Sobre o Projeto

Este projeto consiste em uma análise estatística básica dos microdados do ENEM 2019, utilizando técnicas de estatística descritiva, testes de hipóteses, correlação e regressão linear.

**Objetivo:** Identificar padrões de participação e desempenho, além de investigar diferenças significativas entre grupos (gênero, cor/raça) e relações entre variáveis numéricas.

**Fonte dos dados:** 
- [INEP - Microdados do ENEM 2019](https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enem)
- [Enem 2019(filtred)](https://www.kaggle.com/datasets/joseedmario/enem-2019filtred)

## Estrutura do Projeto

- 01_scripts/setup.py - Criação da estrutura de pastas
- 01_scripts/01_limpeza_padronizacao_adaptacao.py - Pré-processamento dos dados
- 01_scripts/02_analise_participacao.py - Análise do perfil dos participantes
- 01_scripts/03_analise_resultado.py - Estatísticas das notas e acertos
- 01_scripts/04_analises_cruzadas.py - Correlações, regressões e testes
- 02_data/01_raw/enem2019_final_filter.csv - Dataset original (não está presente no github pelo tamanho. Pode ser acessado através de: [Enem 2019(filtred)](https://www.kaggle.com/datasets/joseedmario/enem-2019filtred))
- 02_data/02_processed/enem2019_basico.csv - Dataset limpo e preparado
- 03_output/01_analise_participacao.png - Gráficos de participação
- 03_output/02_analise_resultado/ - Histogramas e boxplots das notas
- 03_output/03_analises_cruzadas/ - Heatmap, regressões e boxplots cruzados
- 03_output/relatorio_analise_participacao.txt - Relatório técnico
- 03_output/relatorio_analise_resultado.txt - Relatório técnico
- 03_output/relatorio_analises_cruzadas.txt - Relatório técnico

## Tecnologias Utilizadas

| Biblioteca | Versão | Finalidade |
|------------|--------|------------|
| pandas | 2.0+ | Manipulação e análise de dados |
| numpy | 1.24+ | Operações numéricas |
| matplotlib | 3.7+ | Visualizações base |
| seaborn | 0.12+ | Gráficos estatísticos |
| scipy.stats | 1.10+ | Testes estatísticos |

## Principais Análises Realizadas

### 1. Análise de Participação (02_analise_participacao.py)

| O que foi analisado | Principais descobertas |
|---------------------|------------------------|
| Distribuição por gênero | Aproximadamente 2/3 F (64.89%) e 1/3 M (35.11%) |
| Distribuição por cor/raça | Maioria se declarou Parda, seguida por Branca e Preta. |
| Distribuição por UF | Maior concentração em SP, MG, BA |
| Distribuição etária | Média de idade 22 anos, participantes majoritariamente entre 17-28 |

**Visualizações:** Gráficos de barras com porcentagens, histograma da idade

### 2. Análise de Resultados (03_analise_resultado.py)

| Métrica | Total de Acertos | Nota da Redação | Nota Média |
|---------|-----------------|-----------------|------------|
| Média | 62 acertos | 608 pontos | 532 pontos |
| Mediana | 58 acertos | 600 pontos | 524 pontos |
| Desvio | 21 acertos | 178 pontos | 82 pontos |
| Outliers | ~2.5% (superiores) | ~2% (inferiores) | 0.5% (superiores) |

**Visualizações:** Histogramas e boxplots para cada métrica

### 3. Análises Cruzadas (04_analises_cruzadas.py)

#### Comparação por Gênero (Teste t)
- Homens tiveram desempenho estatisticamente superior às mulheres
- Diferença pequena mas significativa (p < 0.05)

#### Comparação por Cor/Raça (ANOVA + Testes t post-hoc)
- Diferenças significativas entre grupos (p < 0.05)
- Maiores disparidades: Brancos com melhor desempenho médio

#### Correlação entre Variáveis (Pearson)

| Par de variáveis | Correlação | Interpretação |
|------------------|------------|---------------|
| Total Acertos ↔ Nota Média | 0.91 | Muito forte (positiva) |
| Nota Redação ↔ Nota Média | 0.84 | Forte (positiva) |
| Total Acertos ↔ Nota Redação | 0.59 | Moderada (positiva) |

#### Regressões Lineares

**Modelo 1:** Nota Média = 0.39 × Nota Redação + 294.63
- R² = 0.71 → 71% da variação na nota média é explicada pela redação

**Modelo 2:** Nota Média = 3.57 × Total Acertos + 311.47
- R² = 0.83 → 83% da variação é explicada pelos acertos

## Resultados e Conclusões

1. **Perfil do participante típico:** Mulher 22 anos, residente do Sudeste, autodeclarada Parda.

2. **Disparidades por grupo:** Há diferenças estatisticamente significativas no desempenho entre gêneros e grupos raciais.

3. **Fatores determinantes:** O número de acertos é o fator que mais influencia a nota média (R² = 0.82), seguido pela redação (R² = 0.70).

4. **Distribuição das notas:** Apresenta leve assimetria à direita (maioria dos participantes com desempenho abaixo da média).

## Como Executar

### Pré-requisitos

pip install pandas numpy matplotlib seaborn scipy

### Execução (ordem recomendada)

#### 1. Preparar estrutura de pastas
python 01_scripts/setup.py

#### 2. Limpar e preparar dados
python 01_scripts/01_limpeza_padronizacao_adaptacao.py

#### 3. Analisar participação
python 01_scripts/02_analise_participacao.py

#### 4. Analisar resultados
python 01_scripts/03_analise_resultado.py

#### 5. Análises cruzadas
python 01_scripts/04_analises_cruzadas.py

### Observação

O dataset original é grande (~3-4M linhas). O script utiliza uma amostra de 100k linhas para performance.

## Saídas Geradas

- 03_output/ - Gráficos de participação e análise de resultados
- 03_output/03_analises_cruzadas/ - Heatmap, regressões, boxplots cruzados
- 03_output/*.txt - Relatórios técnicos de cada etapa


## Contato
- Nome: Vinícius Henrique Souza
- Físico | Mestre em Educação em Ciências | Estudante de Análise de Dados
- email: vinicius.h.zlc@gmail.com
- linkedin: [https://www.linkedin.com/in/vin%C3%ADcius-henrique-souza-17a077218/](https://www.linkedin.com/in/vin%C3%ADcius-henrique-souza-17a077218/)
