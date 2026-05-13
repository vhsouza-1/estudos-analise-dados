"""
Bloco 4: Estatística para Dados
Módulo 1: Estatística Descritiva
Aula 1: Fundamentos de Estatística Descritiva com Python
Data: 13/05/2026
Objetivo: Aprender a calcular e interpretar medidas estatísticas descritivas

CONTEÚDO:
1. O que é Estatística Descritiva?
2. Medidas de Tendência Central (média, mediana, moda)
3. Medidas de Dispersão (variância, desvio padrão, amplitude, IQR)
4. Medidas de Posição (quartis, percentis)
5. Assimetria e Curtose
6. Visualizações para Estatística Descritiva
7. Aplicação em Dataset Real
8. Resumo e Exercícios
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# ==========================================
# 1. O QUE É ESTATÍSTICA DESCRITIVA?
# ==========================================

print("="*50)
print("1. O QUE É ESTATÍSTICA DESCRITIVA?")
print("="*50)

"""
ESTATÍSTICA DESCRITIVA = resumir e descrever as principais características de um conjunto de dados.

Perguntas que ela responde:
- Qual o valor típico? (média, mediana)
- Os dados são muito dispersos? (desvio padrão)
- Existem valores extremos? (outliers)
- Como os dados se distribuem? (assimetria)

EXEMPLO: Você tem as idades de 100 clientes.
- A idade típica é 35 anos (média)
- A maioria está entre 25 e 45 anos (dispersão)
- Há alguns clientes com mais de 80 anos? (outliers)

DIFERENÇA IMPORTANTE:
- Estatística DESCRITIVA: descreve os dados que você TEM
- Estatística INFERENCIAL: tira conclusões sobre uma POPULAÇÃO maior
"""

# ==========================================
# 2. MEDIDAS DE TENDÊNCIA CENTRAL
# ==========================================

print("\n" + "="*50)
print("2. MEDIDAS DE TENDÊNCIA CENTRAL")
print("="*50)

"""
MEDIDAS DE TENDÊNCIA CENTRAL = "valor típico" ou "centro" dos dados

| Medida  | O que é                       | Quando usar                        | Fórmula                    |
|---------|-------------------------------|------------------------------------|----------------------------|
| Média   | Soma dividido pelo total      | Dados simétricos, sem outliers     | (x1+x2+...+xn)/n           |
| Mediana | Valor do meio (50º percentil) | Dados assimétricos ou com outliers | Valor central após ordenar |
| Moda    | Valor que mais aparece        | Dados categóricos ou discretos     | Frequência máxima          |
"""

# Criando dados de exemplo
np.random.seed(42)

# Dados simétricos (distribuição normal)
dados_simetricos = np.random.normal(50, 10, 100)  # média 50, desvio 10

# Dados assimétricos (com outliers)
dados_assimetricos = np.array([15, 18, 20, 22, 25, 28, 30, 32, 35, 200])

print("--- Dados Simétricos (Normal) ---")
print(f"Primeiros 10 valores: {dados_simetricos[:10].round(2)}")
print(f"Média: {np.mean(dados_simetricos):.2f}")
print(f"Mediana: {np.median(dados_simetricos):.2f}")
print(f"Moda: {stats.mode(dados_simetricos.round(0))[0]} (arredondado)")
print("✅ Média ≈ Mediana → distribuição simétrica")

print("\n--- Dados Assimétricos (com outlier) ---")
print(f"Dados: {dados_assimetricos}")
print(f"Média: {np.mean(dados_assimetricos):.2f}")
print(f"Mediana: {np.median(dados_assimetricos):.2f}")
print(f"Moda: {stats.mode(dados_assimetricos)[0] if len(stats.mode(dados_assimetricos)) > 0 else 'sem moda única'}")
print("⚠️ Média (40.5) > Mediana (26.5) → assimetria à direita (outlier puxa média)")

# ==========================================
# 3. MEDIDAS DE DISPERSÃO
# ==========================================

print("\n" + "="*50)
print("3. MEDIDAS DE DISPERSÃO")
print("="*50)

"""
MEDIDAS DE DISPERSÃO = mostram como os dados se espalham

| Medida        | O que é                       | Interpretação                  |
|---------------|-------------------------------|--------------------------------|
| Amplitude     | Max - Min                     | Sensível a outliers            |
| Variância     | Média dos desvios quadráticos | Difícil interpretar (unidade²) |
| Desvio Padrão | Raiz da variância             | Mesma unidade dos dados        |
| IQR           | Q3 - Q1                       | Robusto a outliers             |
"""

# Comparando dois conjuntos com mesma média, mas dispersões diferentes
dados_baixa_dispersao = np.array([48, 49, 50, 51, 52])
dados_alta_dispersao = np.array([10, 30, 50, 70, 90])

print("--- Comparação de Dispersão ---")
print(f"Conjunto 1 (baixa dispersão): {dados_baixa_dispersao}")
print(f"Média: {np.mean(dados_baixa_dispersao)}")
print(f"Desvio Padrão: {np.std(dados_baixa_dispersao):.2f}")
print(f"Amplitude: {np.ptp(dados_baixa_dispersao)}")  # ptp = peak to peak

print(f"\nConjunto 2 (alta dispersão): {dados_alta_dispersao}")
print(f"Média: {np.mean(dados_alta_dispersao)}")
print(f"Desvio Padrão: {np.std(dados_alta_dispersao):.2f}")
print(f"Amplitude: {np.ptp(dados_alta_dispersao)}")

print("\n📌 Conclusão: Desvio padrão maior = dados mais espalhados")

# ==========================================
# 4. MEDIDAS DE POSIÇÃO (QUARTIS E PERCENTIS)
# ==========================================

print("\n" + "="*50)
print("4. MEDIDAS DE POSIÇÃO - QUARTIS E PERCENTIS")
print("="*50)

"""
QUARTIS dividem os dados em 4 partes iguais:
- Q1 (25%): 25% dos dados estão abaixo
- Q2 (50%): mediana
- Q3 (75%): 75% dos dados estão abaixo

PERCENTIS: dividem em 100 partes
- Percentil 90: 90% dos dados estão abaixo

IQR (Intervalo Interquartil) = Q3 - Q1
- Contém 50% dos dados centrais
- Usado para identificar outliers
"""

dados = np.array([10, 15, 20, 25, 30, 35, 40, 45, 50, 100])

print(f"Dados: {dados}")
print(f"Q1 (25%): {np.percentile(dados, 25)}")
print(f"Q2 (50% / Mediana): {np.percentile(dados, 50)}")
print(f"Q3 (75%): {np.percentile(dados, 75)}")
print(f"IQR (Q3 - Q1): {np.percentile(dados, 75) - np.percentile(dados, 25)}")

print("\n--- Regra do IQR para identificar outliers ---")
Q1 = np.percentile(dados, 25)
Q3 = np.percentile(dados, 75)
IQR = Q3 - Q1
limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

print(f"Limite inferior: {limite_inferior}")
print(f"Limite superior: {limite_superior}")
outliers = dados[(dados < limite_inferior) | (dados > limite_superior)]
print(f"Outliers identificados: {outliers}")

# ==========================================
# 5. ASSIMETRIA E CURTOSE
# ==========================================

print("\n" + "="*50)
print("5. ASSIMETRIA (SKEWNESS) E CURTOSE")
print("="*50)

"""
ASSIMETRIA (Skewness): mede o quanto a distribuição se desvia da simetria

| Valor | Tipo                  | Interpretação                                |
|-------|-----------------------|----------------------------------------------|
| 0     | Simétrica             | Média = Mediana                              |
| > 0   | Positiva (à direita)  | Cauda mais longa à direita, Média > Mediana  |
| < 0   | Negativa (à esquerda) | Cauda mais longa à esquerda, Média < Mediana |

CURTOSE: mede o quanto a distribuição tem caudas "pesadas"

| Valor | Tipo         | Interpretação                         |
|-------|--------------|---------------------------------------|
| 0     | Mesocúrtica  | Como distribuição normal              |
| > 0   | Leptocúrtica | Caudas mais pesadas, pico mais alto   |
| < 0   | Platicúrtica | Caudas mais leves, pico mais achatado |
"""

# Gerar diferentes tipos de distribuição
normal = np.random.normal(0, 1, 1000)
positiva = np.random.gamma(2, 1, 1000)  # assimetria positiva
negativa = -np.random.gamma(2, 1, 1000)  # assimetria negativa

print("--- Comparação de Assimetria ---")
print(f"Distribuição Normal - Skewness: {stats.skew(normal):.2f} (simétrica)")
print(f"Distribuição Gamma - Skewness: {stats.skew(positiva):.2f} (assimetria positiva)")
print(f"Distribuição Negativa - Skewness: {stats.skew(negativa):.2f} (assimetria negativa)")

print("\n--- Comparação de Curtose ---")
print(f"Distribuição Normal - Curtose: {stats.kurtosis(normal):.2f} (mesocúrtica)")
print(f"Distribuição Gamma - Curtose: {stats.kurtosis(positiva):.2f} (leptocúrtica - caudas mais pesadas)")

# ==========================================
# 6. VISUALIZAÇÕES PARA ESTATÍSTICA DESCRITIVA
# ==========================================

print("\n" + "="*50)
print("6. VISUALIZAÇÕES PARA ESTATÍSTICA DESCRITIVA")
print("="*50)

"""
PRINCIPAIS GRÁFICOS PARA ANÁLISE DESCRITIVA:

1. HISTOGRAMA: mostra a distribuição dos dados
   - Permite ver forma (simétrica, assimétrica)
   - Identifica moda (pico mais alto)

2. BOXPLOT: mostra estatísticas em um gráfico
   - Mostra mediana, Q1, Q3, outliers
   - Bom para comparar grupos

3. VIOLIN PLOT: combina boxplot com densidade
   - Mostra a forma da distribuição completa
"""
"""
# Criar dados para visualização
np.random.seed(42)
dados_viz = np.random.normal(50, 10, 500)
categorias = np.random.choice(['Grupo A', 'Grupo B'], 500)
dados_grupoA = dados_viz[categorias == 'Grupo A']
dados_grupoB = dados_viz[categorias == 'Grupo B'] + 5  # deslocar grupo B

# Criar figura com múltiplos subplots
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# Histograma
axes[0].hist(dados_viz, bins=30, edgecolor='black', alpha=0.7)
axes[0].axvline(np.mean(dados_viz), color='red', linestyle='--', label=f'Média: {np.mean(dados_viz):.1f}')
axes[0].axvline(np.median(dados_viz), color='green', linestyle='--', label=f'Mediana: {np.median(dados_viz):.1f}')
axes[0].set_title('Histograma com Média e Mediana')
axes[0].set_xlabel('Valor')
axes[0].set_ylabel('Frequência')
axes[0].legend()

# Boxplot
axes[1].boxplot([dados_grupoA, dados_grupoB], tick_labels=['Grupo A', 'Grupo B'])
axes[1].set_title('Boxplot - Comparação entre Grupos')
axes[1].set_ylabel('Valor')

# Violin plot
parts = axes[2].violinplot([dados_grupoA, dados_grupoB], positions=[1, 2], showmeans=True)
axes[2].set_xticks([1, 2])
axes[2].set_xticklabels(['Grupo A', 'Grupo B'])
axes[2].set_title('Violin Plot - Distribuição Completa')
axes[2].set_ylabel('Valor')

plt.tight_layout()
plt.savefig('visualizacoes_estatistica.png')
plt.show()

print("📊 Gráficos salvos como 'visualizacoes_estatistica.png'")
"""

# ==========================================
# 7. APLICAÇÃO EM DATASET REAL
# ==========================================

print("\n" + "="*50)
print("7. APLICAÇÃO PRÁTICA - ANÁLISE DE VENDAS")
print("="*50)

# Dataset realista de vendas
np.random.seed(42)

df_vendas = pd.DataFrame({
    'produto': np.random.choice(['A', 'B', 'C', 'D'], 500),
    'vendas': np.random.normal(1000, 250, 500),
    'preco': np.random.uniform(50, 200, 500),
    'clientes': np.random.poisson(50, 500)
})

# Adicionar alguns outliers
df_vendas.loc[0, 'vendas'] = 5000  # outlier alto
df_vendas.loc[1, 'vendas'] = -100  # outlier baixo

print("Análise Descritiva do Dataset de Vendas")
print(f"Shape: {df_vendas.shape}")
print(f"\n--- Estatísticas Descritivas (describe) ---")
print(df_vendas.describe())

print("\n--- Análise Detalhada da coluna 'vendas' ---")
vendas = df_vendas['vendas']
print(f"Média: R$ {vendas.mean():.2f}")
print(f"Mediana: R$ {vendas.median():.2f}")
print(f"Desvio Padrão: R$ {vendas.std():.2f}")
print(f"Mínimo: R$ {vendas.min():.2f}")
print(f"Máximo: R$ {vendas.max():.2f}")
print(f"Assimetria (Skewness): {vendas.skew():.2f}")
print(f"Curtose: {vendas.kurtosis():.2f}")

# Identificando outliers com IQR
Q1 = vendas.quantile(0.25)
Q3 = vendas.quantile(0.75)
IQR = Q3 - Q1
limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

outliers_vendas = vendas[(vendas < limite_inferior) | (vendas > limite_superior)]
print(f"\n--- Outliers em Vendas ---")
print(f"Limites: [{limite_inferior:.2f}, {limite_superior:.2f}]")
print(f"Número de outliers: {len(outliers_vendas)}")
print(f"Outliers: {outliers_vendas.values[:5]}...")

# Análise por produto
print("\n--- Vendas por Produto ---")
print(df_vendas.groupby('produto')['vendas'].agg(['mean', 'median', 'std', 'count']))

# ==========================================
# 8. QUANDO USAR MÉDIA VS MEDIANA (CASO PRÁTICO)
# ==========================================

print("\n" + "="*50)
print("8. CASO PRÁTICO - MÉDIA VS MEDIANA EM SALÁRIOS")
print("="*50)

# Simulando salários de uma empresa
salarios = np.array([2500, 2800, 3000, 3200, 3500, 4000, 4500, 5000, 5500, 100000])

print(f"Salários (R$): {salarios}")
print(f"Média: R$ {np.mean(salarios):,.2f}")
print(f"Mediana: R$ {np.median(salarios):,.2f}")

"""
📌 INTERPRETAÇÃO:

- A MÉDIA (R$ 14.000) é puxada pelo outlier (salário de R$ 100.000)
- A MEDIANA (R$ 3.750) representa melhor o salário 'típico'

✅ USE MEDIANA QUANDO:
   - Dados têm outliers
   - Distribuição é assimétrica
   - Você quer o valor "típico" (ex: salário, preço de imóveis)

✅ USE MÉDIA QUANDO:
   - Dados são simétricos
   - Não há outliers significativos
   - Você precisa de propriedades matemáticas (ex: soma total)
"""

# ==========================================
# 9. RESUMO DA AULA
# ==========================================

print("\n" + "="*50)
print("9. RESUMO - ESTATÍSTICA DESCRITIVA")
print("="*50)

"""
✅ MEDIDAS DE TENDÊNCIA CENTRAL:
   - Média: np.mean() - soma / n
   - Mediana: np.median() - valor central
   - Moda: stats.mode() - valor mais frequente

✅ MEDIDAS DE DISPERSÃO:
   - Amplitude: np.ptp() ou max() - min()
   - Variância: np.var()
   - Desvio Padrão: np.std() (raiz da variância)
   - IQR: np.percentile(q75) - np.percentile(q25)

✅ MEDIDAS DE POSIÇÃO:
   - Quartis: np.percentile(dados, [25, 50, 75])
   - Percentis: np.percentile(dados, p)

✅ ASSIMETRIA E CURTOSE:
   - Skewness: stats.skew() (>0 assimetria direita)
   - Curtose: stats.kurtosis() (>0 caudas pesadas)

✅ VISUALIZAÇÕES:
   - Histograma: distribuição e forma
   - Boxplot: mediana, quartis, outliers
   - Violin plot: distribuição completa

📌 REGRA DE OURO:
   - Dados simétricos + sem outliers → MÉDIA
   - Dados assimétricos ou com outliers → MEDIANA
   - Dados categóricos → MODA
"""

# ==========================================
# EXERCÍCIOS - AULA 1 (ESTATÍSTICA DESCRITIVA)
# ==========================================

print("\n" + "="*50)
print("EXERCÍCIOS - ESTATÍSTICA DESCRITIVA")
print("="*50)

# Dados para todos os exercícios
np.random.seed(42)

df_funcionarios = pd.DataFrame({
    'funcionario': range(1, 101),
    'salario': np.random.normal(5000, 1000, 100).round(2), # arredondei o salario
    'idade': np.random.normal(35, 8, 100).astype(int), # arredondei a idade
    'anos_empresa': np.random.exponential(5, 100).astype(int),
    'avaliacao': np.random.choice([1, 2, 3, 4, 5], 100, p=[0.05, 0.1, 0.2, 0.4, 0.25])
})

# Adicionar alguns outliers
df_funcionarios.loc[0, 'salario'] = 25000
df_funcionarios.loc[1, 'idade'] = 65
df_funcionarios.loc[2, 'anos_empresa'] = 30

########################################################################
# NÍVEL 1-3: Aquecimento
########################################################################

"""
1. Calculando medidas centrais

# Para a coluna 'salario', calcule e mostre:
# - Média
# - Mediana
# - Moda (use scipy.stats.mode)
# - Compare os valores e comente a diferença
"""

"""
df = df_funcionarios.copy()

media = df['salario'].mean()
mediana = df['salario'].median()
moda = df['salario'].mode()[0]

print('Coluna salário: ')
print(f' - Média: R${media:,.2f}')
print(f' - Mediana: R${mediana:,.2f}')
print(f' - Moda: R${moda:,.2f}')

print(f'\nDiferença entre Média e Mediana: {media - mediana:.2f} (diferença positiva, indício de outlier grande)')
"""

########################################################################

"""
2. Medidas de dispersão

# Para a coluna 'idade', calcule:
# - Desvio padrão
# - Variância
# - Amplitude (max - min)
# - IQR (Intervalo Interquartil)
"""

"""
df = df_funcionarios.copy()
idade = df['idade']

desvio = idade.std()
variancia = idade.var()
amplitude = idade.max() - idade.min()
IQR = idade.quantile(0.75) - idade.quantile(0.25)

print(f'Coluna "idade":')
print(f' - Desvio padrão: {desvio:.2f}')
print(f' - Variância: {variancia:.2f}')
print(f' - Amplitude: {amplitude}')
print(f' - IQR: {IQR}')
"""

########################################################################

"""
3. Quartis e percentis

# Para a coluna 'anos_empresa', encontre:
# - Q1, Q2 (mediana), Q3
# - Percentil 90
# - Qual o valor abaixo do qual estão 95% dos funcionários?
"""

"""
df = df_funcionarios.copy()
anos_empresa = df['anos_empresa']

Q1 = anos_empresa.quantile(0.25).astype(int)
Q2 = anos_empresa.quantile(0.5).astype(int)
Q3 = anos_empresa.quantile(0.75).astype(int)
P90 = anos_empresa.quantile(0.9).astype(int)
P95 = anos_empresa.quantile(0.95).astype(int)

print('Coluna "anos_empresa":')
print(f' - Q1, Q2 (mediana), Q3: {Q1}, {Q2}, {Q3}')
print(f' - Percentil 90: {P90}')
print(f' - Qual o valor abaixo do qual estão 95% dos funcionários?: {P95}')
"""

########################################################################
# NÍVEL 4-6: Aplicação
########################################################################

"""
4. Identificando outliers com IQR

# Use a regra do IQR (1.5 * IQR) para identificar outliers na coluna 'salario'
# Mostre:
# - Quantos outliers foram encontrados
# - Quais são os valores dos outliers
# - Qual o percentual de outliers
"""

"""
df = df_funcionarios.copy()
salario = df['salario']

Q1 = salario.quantile(0.25)
Q3 = salario.quantile(0.75)
IQR = Q3 - Q1

lim_inf = Q1 - 1.5 * IQR
lim_sup = Q3 + 1.5 * IQR

outliers_mask = (salario > lim_sup) | (salario < lim_inf)
outliers = salario[outliers_mask]

print('Coluna "salario": ')
print(f' - Quantos outliers foram encontrados: {outliers.count()}')
print(f' - Quais são os valores dos outliers: {outliers.tolist()}')
print(f' - Qual o percentual de outliers: {outliers.count()/salario.count()*100:.2f}%')
"""

########################################################################

"""
5. Análise de assimetria

# Calcule a assimetria (skewness) das colunas:
# - 'salario'
# - 'idade'
# - 'anos_empresa'
#
# Para cada uma, diga se a distribuição é:
# - Simétrica
# - Assimétrica à direita (positiva)
# - Assimétrica à esquerda (negativa)
"""

"""
df = df_funcionarios.copy()

# Assimetrias:
colunas = ['salario', 'idade', 'anos_empresa']
assimetrias = [(coluna, df[coluna].skew()) for coluna in colunas]

# Função para classificar skewness:

def classificar_skew(skew):
    if -1 < skew < 1:
        return 'Simétrica'
    elif skew >= 1:
        return 'Assimétrica à direita (positiva)'
    elif skew <= -1:
        return 'Assimétrica à esquerda (negativa)'
    else:
        return None

for coluna, assimetria in assimetrias:
    print(f'Coluna: "{coluna}"')
    print(f' - Skewness: {assimetria:.2f}')
    print(f' - Classificação: {classificar_skew(assimetria)}')
    print()

# Não sei se é uma boa prática, mas gosto de ficar generalizando esse tipo de estrutura hehe
"""

########################################################################

"""
6. Comparando grupos com boxplot

# Use a biblioteca matplotlib ou seaborn para criar:
# - Um boxplot de 'salario' para cada nível de 'avaliacao' (1 a 5)
# - Qual grupo tem maior mediana? E maior dispersão?
#
# (Os gráficos podem ser exibidos ou salvos como imagem)
"""

"""
df = df_funcionarios.copy()

# Plotar boxplot
plt.figure(figsize=(10,12))
sns.boxplot(data=df, x='avaliacao', y='salario', hue='avaliacao', palette='Set1', width=0.3)
plt.title('Boxplot Salário x Avaliação')
plt.ylabel('Salário (R$)')
plt.xlabel('Avaliação')

# Plotar linhas horizontais das medianas:

cores = ['red', 'blue', 'green', 'purple', 'orange']
for i, cor in enumerate(cores, 1):
    mediana_av = df.loc[df['avaliacao']==i, 'salario'].mean()
    plt.axhline(mediana_av, linestyle='--', color=cor, label=f'mediana_av{i}')

plt.legend()
plt.show()

# Tinha feito esse sem o loop, depois que percebi que dava pra fazer o loop, modifiquei a estrutura.
"""

########################################################################
# NÍVEL 7-8: Manipulação
########################################################################

"""
7. Resumo estatístico por categoria

# Agrupe os dados por 'avaliacao' (1 a 5) e calcule:
# - Média do salário
# - Mediana do salário
# - Desvio padrão do salário
# - Contagem de funcionários
#
# Qual avaliação tem a maior média salarial?
"""

"""
df = df_funcionarios.copy()

df = df.groupby('avaliacao').agg(
    media_salario=('salario', 'mean'),
    mediana_salario=('salario', 'median'),
    desvio_salario=('salario', 'std'),
    cont_funcionarios=('funcionario', 'count')
).reset_index()

av_maior_media_salarial = df.loc[df['media_salario'].idxmax(), 'avaliacao']
print(f'Qual avaliação tem a maior média salarial?: {av_maior_media_salarial}')
"""

########################################################################

"""
8. Criando um relatório descritivo completo

# Crie uma função relatorio_descritivo(df, coluna) que retorna um dicionário com:
# - media
# - mediana
# - moda
# - desvio_padrao
# - variancia
# - min
# - max
# - q1, q2, q3
# - iqr
# - skewness
# - kurtosis
# - num_outliers_iqr
#
# Aplique para a coluna 'salario' e mostre o resultado
"""

"""
def relatorio_descritivo(df, coluna):
    relatorio = {}

    relatorio['media'] = df[coluna].mean()
    relatorio['mediana'] = df[coluna].median()
    relatorio['moda'] = df[coluna].mode()[0]
    relatorio['desvio_padrao'] = df[coluna].std()
    relatorio['variancia'] = df[coluna].var()
    relatorio['min'] = df[coluna].min()
    relatorio['max'] = df[coluna].max()

    Q1 = df[coluna].quantile(0.25)
    Q2 = df[coluna].quantile(0.5)
    Q3 = df[coluna].quantile(0.75)
    IQR = Q3 - Q1

    relatorio['Q1'] = Q1
    relatorio['Q2'] = Q2
    relatorio['Q3'] = Q3
    relatorio['IQR'] = IQR

    lim_sup = Q3 + 1.5 * IQR
    lim_inf = Q1 - 1.5 * IQR

    mask_outlier = (df[coluna] > lim_sup) | (df[coluna] < lim_inf)
    relatorio['num_outliers_iqr'] = mask_outlier.sum()

    relatorio['skewness'] = df[coluna].skew()
    relatorio['kurtosis'] = df[coluna].kurt()

    return relatorio

relatorio = relatorio_descritivo(df_funcionarios, 'salario')

for chave, valor in relatorio.items():
    print(f'{chave}: {valor:.2f}')

"""

########################################################################
# NÍVEL 9-10: Desafios
########################################################################

"""
9. Dashboard de análise descritiva

# Crie um dashboard com 3 subplots (1 linha, 3 colunas) mostrando:
# (0) Histograma do 'salario' com linha vertical para média e mediana
# (1) Boxplot do 'salario' por 'avaliacao'
# (2) Gráfico de barras da frequência das avaliações
#
# Salve a figura como 'dashboard_descritivo.png'
"""

"""
df = df_funcionarios.copy()

plt.figure(figsize=(16, 6))

plt.subplot(1, 3, 1)
sns.histplot(data=df, x='salario', bins=50)
plt.axvline(df['salario'].mean(), linestyle='--', color='red', label=f'Média: R${df['salario'].mean():.2f}')
plt.axvline(df['salario'].median(), linestyle='--', color='green', label=f'Mediana: R${df['salario'].median():.2f}')
plt.title('Distribuição dos salários')
plt.ylabel('Frequência')
plt.xlabel('Salário (R$)')
plt.legend()

plt.subplot(1, 3, 2)
sns.boxplot(data=df, x='avaliacao', y='salario', hue='avaliacao', palette='Set1', width=0.3)
plt.title('Boxplot Salário x Avaliação')
plt.ylabel('Salário (R$)')
plt.xlabel('Avaliação')

# Plotar linhas horizontais das medianas:
cores = ['red', 'blue', 'green', 'purple', 'orange']
for i, cor in enumerate(cores, 1):
    mediana_av = df.loc[df['avaliacao']==i, 'salario'].mean()
    plt.axhline(mediana_av, linestyle='--', color=cor, label=f'mediana_av{i}')

plt.legend()

plt.subplot(1, 3, 3)
sns.countplot(data=df, x='avaliacao', hue='avaliacao', palette='Set1')
plt.title('Frequência das avaliações')
plt.ylabel('Frequência')
plt.xlabel('Avaliações')
plt.legend()

plt.tight_layout()
plt.show()
"""

########################################################################

"""
10. DESAFIO FINAL: Relatório executivo

# Crie um relatório em formato de texto que responda:
# 1. Qual é o perfil típico do funcionário? (idade, salário, tempo de casa)
# 2. O salário tem outliers? Se sim, quantos e quais?
# 3. A avaliação está relacionada com salário? (Compare médias por avaliação)
# 4. Existe assimetria nos dados? O que isso significa?
# 5. Qual seria um salário "justo" para um novo funcionário (use mediana ou média? por quê?)
#
# O relatório deve ser escrito em português, com valores e justificativas
"""
df = df_funcionarios.copy()

# 1. Qual é o perfil típico do funcionário? (idade, salário, tempo de casa)
idade_tipica = df['idade'].median()
salario_tipico = df['salario'].median()
tempo_tipico = df['anos_empresa'].median()

print(f'O perfil típico do funcionário é: idade: {idade_tipica.astype(int)} anos, salario: R${salario_tipico:,.2f} e tempo de casa: {tempo_tipico.astype(int)} anos')

# 2. O salário tem outliers? Se sim, quantos e quais?
Q1 = df['salario'].quantile(0.25)
Q3 = df['salario'].quantile(0.75)
IQR = Q3 - Q1
lim_sup = Q3 + 1.5 * IQR
lim_inf = Q1 - 1.5 * IQR
outliers_mask = (df['salario'] > lim_sup) | (df['salario'] < lim_inf)
num_outliers = outliers_mask.sum()
outliers = df.loc[outliers_mask, 'salario']

print(f'O salário tem outliers? Se sim, quantos e quais?')

if num_outliers > 1:
    print(f'Sim, a coluna "salário" tem {num_outliers} outliers, sendo eles:')
    print(f' - {outliers.tolist()}')
else:
    print(f'Não, a coluna salário não possui outliers!')

# 3. A avaliação está relacionada com salário? (Compare médias por avaliação)

media_salario_av = df.groupby('avaliacao')['salario'].mean().reset_index()

print(f'A avaliação está relacionada com salário? (Compare médias por avaliação)')
print(f'Não necessariamente, como podemos ver na comparação: ')
print(media_salario_av)
print(f'É possivel perceber que a média salarial da avaliação 2 é maior que a média salarial da avaliação 4')

# 4. Existe assimetria nos dados? O que isso significa?

# Assimetrias:
colunas = ['salario', 'idade', 'anos_empresa', 'avaliacao']
assimetrias = [(coluna, df[coluna].skew()) for coluna in colunas]

# Função para classificar skewness:
def classificar_skew(skew):
    if -1 < skew < 1:
        return 'Simétrica, dados bem distribuídos em torno da média'
    elif skew >= 1:
        return 'Assimétrica à direita, dados pendem para valores maiores que a media'
    elif skew <= -1:
        return 'Assimétrica à esquerda dados pendem para valores menos que a media'
    else:
        return None

print(f'\nExiste assimetria nos dados? O que isso significa?')
print(f'Medida de assimetria de todas as colunas:')
for coluna, assimetria in assimetrias:
    print(f'Coluna: "{coluna}"')
    print(f' - Skewness: {assimetria:.2f}')
    print(f' - Classificação: {classificar_skew(assimetria)}')
    print()

# 5. Qual seria um salário "justo" para um novo funcionário (use mediana ou média? por quê?)
print(f'Qual seria um salário "justo" para um novo funcionário?')
print(f'Como os dados de salário possuem outliers, o salário justo para um novo funcionário seria a mediana do salário')
print(f'Ou seja, R${salario_tipico:,.2f}')

# Não sei se era bem isso que você queria...