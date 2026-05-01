"""
Bloco 3: Python para Dados
Módulo 2: Visualização de Dados
Aula 4: Histograma e Boxplot com Seaborn
Data: 01/05/2026
Objetivo: Aprender a criar histogramas e boxplots com Seaborn
"""

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# ==========================================
# 1. O QUE É SEABORN?
# ==========================================

print("="*50)
print("1. O QUE É SEABORN?")
print("="*50)

"""
Seaborn é uma biblioteca baseada no Matplotlib, feita especificamente para 
criar gráficos estatísticos de forma mais simples e com visual mais bonito.

Vantagens:
- Gráficos mais bonitos com menos código
- Funciona muito bem com DataFrames do Pandas
- Tem gráficos específicos para análise estatística

Desvantagens:
- Menos flexível que Matplotlib para personalizações muito específicas
- Para gráficos muito simples, pode ser "excessivo"

IMPORTANTE: Seaborn NÃO substitui o Matplotlib. Eles se complementam.
- Seaborn: gráficos estatísticos prontos
- Matplotlib: ajustes finos e personalizações
"""

# ==========================================
# 2. IMPORTANDO O SEABORN
# ==========================================

print("\n" + "="*50)
print("2. IMPORTANDO O SEABORN")
print("="*50)

# A convenção padrão da comunidade é:
import seaborn as sns
import matplotlib.pyplot as plt

# Seaborn geralmente é usado com Pandas
import pandas as pd
import numpy as np

print("Seaborn importado com sucesso!")

# ==========================================
# 3. O QUE É UM HISTOGRAMA?
# ==========================================

print("\n" + "="*50)
print("3. O QUE É UM HISTOGRAMA?")
print("="*50)

"""
HISTOGRAMA: mostra como os dados estão distribuídos.

Para que serve?
- Ver a forma da distribuição (simétrica, assimétrica)
- Identificar valores mais frequentes
- Identificar outliers (valores muito diferentes)
- Ver a dispersão dos dados

Como funciona?
- Divide os dados em "bins" (intervalos)
- Conta quantos valores caem em cada intervalo
- Desenha barras com a altura igual à contagem

Exemplo: idades de 100 pessoas
- Eixo X: idade (dividida em intervalos: 20-25, 25-30, etc.)
- Eixo Y: quantas pessoas têm idade naquele intervalo
"""

# ==========================================
# 4. CRIANDO UM HISTOGRAMA (sns.histplot)
# ==========================================

print("\n" + "="*50)
print("4. CRIANDO UM HISTOGRAMA (sns.histplot)")
print("="*50)

# Dados: 100 idades aleatórias (média 30, desvio padrão 5)
np.random.seed(42)  # para resultados reproduzíveis
idades = np.random.normal(30, 5, 100)
print(f"Primeiras 10 idades: {idades[:10]}")
print(f"Média: {idades.mean():.1f}")
print(f"Mínimo: {idades.min():.1f}")
print(f"Máximo: {idades.max():.1f}")

# Criando histograma (versão mais simples)
# plt.figure(figsize=(10, 6))
# sns.histplot(idades)
# plt.title('Histograma de Idades')
# plt.xlabel('Idade')
# plt.ylabel('Frequência')
# plt.show()

# ==========================================
# 5. PARÂMETROS DO HISTOGRAMA
# ==========================================

print("\n" + "="*50)
print("5. PARÂMETROS DO HISTOGRAMA")
print("="*50)

# 5.1. bins - número de intervalos
print("--- bins (número de intervalos) ---")
# plt.figure(figsize=(12, 4))
#
# plt.subplot(1, 3, 1)
# sns.histplot(idades, bins=5)
# plt.title('bins=5 (poucos intervalos)')
#
# plt.subplot(1, 3, 2)
# sns.histplot(idades, bins=20)
# plt.title('bins=20 (médio)')
#
# plt.subplot(1, 3, 3)
# sns.histplot(idades, bins=50)
# plt.title('bins=50 (muitos intervalos)')
#
# plt.tight_layout()
# plt.show()

print("bins pequeno (5): perde detalhes")
print("bins médio (20): bom equilíbrio")
print("bins grande (50): muito ruído, difícil interpretar")

# 5.2 color - cor do histograma
print('\n color (cor)')
# plt.figure(figsize=(10, 6))
# sns.histplot(idades, bins=20, color='green')
# plt.title('Histograma na cor verde')
# plt.show()

# 5.3 alpha - transparência
print('\nalpha (transparência)')
# plt.figure(figsize=(10, 6))
# sns.histplot(idades, bins=20, color='blue', alpha=0.5)
# plt.title('Histograma azul com alpha=0.5')
# plt.show()

# ==========================================
# 6. HISTOGRAMA A PARTIR DE UM DATAFRAME
# ==========================================

print("\n" + "="*50)
print("6. HISTOGRAMA COM DATAFRAME")
print("="*50)

# Criando DataFrame de exemplo
df = pd.DataFrame({
    'vendas': np.random.normal(1000, 200, 200),
    'custos': np.random.normal(600, 150, 200),
    'lucro': np.random.normal(400, 100, 200)
})

print('\nDataFrame de vendas: ')
print(df.head())

# Histograma de uma coluna
# plt.figure(figsize=(10, 6))
# sns.histplot(df['vendas'], bins=30, color='blue')
# plt.title('Distribuição das Vendas')
# plt.xlabel('Valor (R$)')
# plt.ylabel('Frequência')
# plt.show()

# Múltiplos histogramas na mesma figura
# plt.figure(figsize=(10, 6))
# sns.histplot(df['vendas'], bins=30, color='blue', alpha=0.5, label='Vendas')
# sns.histplot(df['custos'], bins=30, color='red', alpha=0.5, label='Custos')
# sns.histplot(df['lucro'], bins=30, color='green', alpha=0.5, label='Lucros')
# plt.title('Distibuição de Vendas, Custos e Lucro')
# plt.xlabel('Valor (R$)')
# plt.ylabel('Frequência')
# plt.legend()
# plt.show()

# ==========================================
# 7. O QUE É UM BOXPLOT?
# ==========================================

print("\n" + "="*50)
print("7. O QUE É UM BOXPLOT?")
print("="*50)

"""
BOXPLOT (gráfico de caixa): mostra a distribuição dos dados através de quartis.

Para que serve?
- Comparar distribuições entre diferentes categorias
- Identificar outliers (valores atípicos)
- Ver a mediana e a dispersão dos dados

Como interpretar um boxplot?

    Outlier (ponto fora)
         |
         v
    -----|----- 
    |    |    |  
    |    |    |  
    |    |    |  
    |    |    |  
    -----|----- 
         |
    -----|-----  (Q3 = 75% dos dados estão abaixo)
    |    |    |
    |    |    |  (Mediana = 50% dos dados estão abaixo)
    |    |    |
    |    |    |
    -----|-----  (Q1 = 25% dos dados estão abaixo)
         |
         |
    (Whisker - limite inferior)

- Q1 (primeiro quartil): 25% dos dados estão abaixo
- Mediana (Q2): 50% dos dados estão abaixo
- Q3 (terceiro quartil): 75% dos dados estão abaixo
- Distância entre Q3 e Q1 = IQR (intervalo interquartil)
- Limites: Q1 - 1.5*IQR e Q3 + 1.5*IQR
- Pontos fora dos limites = outliers
"""

# ==========================================
# 8. CRIANDO UM BOXPLOT (sns.boxplot)
# ==========================================

print("\n" + "="*50)
print("8. CRIANDO UM BOXPLOT (sns.boxplot)")
print("="*50)

# Dados: vendas por categoria
# np.random.seed(42)
vendas_categoria = pd.DataFrame({
    'categoria': ['A']*50 + ['B']*50 + ['C']*50,
    'vendas': np.concatenate([
        np.random.normal(100, 15, 50),
        np.random.normal(120, 20, 50),
        np.random.normal(80, 10, 50)
    ])
})

print('Boxplot de vendas por categoria: ')
# plt.figure(figsize=(10, 6))
# sns.boxplot(data=vendas_categoria, x='categoria', y='vendas')
# plt.title('Distribuição de Vendas por Categoria')
# plt.xlabel('Categoria')
# plt.ylabel('Vendas (R$)')
# plt.show()

# ==========================================
# 9. PARÂMETROS DO BOXPLOT
# ==========================================

print("\n" + "="*50)
print("9. PARÂMETROS DO BOXPLOT")
print("="*50)

# 9.1 orientação horizontal
print('Boxplot Horizontal: ')
# plt.figure(figsize=(10, 6))
# sns.boxplot(data=vendas_categoria, x='vendas', y='categoria')
# plt.title('Boxplot Horizontal')
# plt.xlabel('Vendas (R$)')
# plt.ylabel('Categoria')
# plt.show()

# 9.2. color - cor
print("\n--- Boxplot com cor personalizada ---")
# plt.figure(figsize=(10, 6))
# sns.boxplot(data=vendas_categoria, x='categoria', y='vendas', color='purple')
# plt.title('Boxplot na cor roxa')
# plt.show()

# 9.3. palette - cores diferentes por categoria
print("\n--- Boxplot com paleta de cores ---")
# plt.figure(figsize=(10, 6))
# sns.boxplot(data=vendas_categoria, x='categoria', y='vendas', palette='Set2')
# plt.title('Boxplot com cores diferentes por categoria')
# plt.show()

# O console me voltou o seguinte aviso:
# C:\Users\code\Desktop\estudos-analise-dados\03_python_para_dados\02_visualizacao\04_histograma_boxplot.py:291: FutureWarning:
#
# Passing `palette` without assigning `hue` is deprecated and will be removed in v0.14.0. Assign the `x` variable to `hue` and set `legend=False` for the same effect.
#
#   sns.boxplot(data=vendas_categoria, x='categoria', y='vendas', palette='Set2')
#
# Process finished with exit code 0

# ==========================================
# 10. EXEMPLOS PRÁTICOS
# ==========================================

print("\n" + "="*50)
print("10. EXEMPLOS PRÁTICOS")
print("="*50)

# Dados: funcionários por departamento
np.random.seed(42)
funcionarios = pd.DataFrame({
    'departamento': ['Vendas']*30 + ['TI']*30 + ['RH']*30,
    'salario': np.concatenate([
        np.random.normal(5000, 1000, 30),
        np.random.normal(7000, 1500, 30),
        np.random.normal(4500, 800, 30)
    ])
})

print("Distribuição de Salários por Departamento")
# plt.figure(figsize=(12, 5))
#
# # Boxplot
# plt.subplot(1, 2, 1)
# sns.boxplot(data=funcionarios, x='departamento', y='salario', hue='departamento', palette='Set1', legend=False, width=0.5)
# plt.title('Boxplot - Salários por Departamento')
# plt.ylabel('Salário (R$)')
#
# # Histograma
# plt.subplot(1, 2, 2)
# sns.histplot(funcionarios['salario'], bins=30, color='blue')
# plt.title('Histograma - Distribuição Geral de Salários')
# plt.xlabel('Salário (R$)')
# plt.ylabel('Frequência')
#
# plt.tight_layout()
# plt.show()

# ==========================================
# 11. RESUMO
# ==========================================

print("\n" + "="*50)
print("11. RESUMO")
print("="*50)

"""
✅ HISTOGRAMA (sns.histplot):
   - Mostra como os dados estão distribuídos
   - sns.histplot(dados)
   - sns.histplot(dados, bins=20) - controla número de intervalos
   - sns.histplot(dados, color='blue') - cor
   - sns.histplot(dados, alpha=0.5) - transparência

✅ BOXPLOT (sns.boxplot):
   - Compara distribuições entre categorias
   - sns.boxplot(data=df, x='categoria', y='valor')
   - sns.boxplot(data=df, x='valor', y='categoria') - horizontal
   - sns.boxplot(data=df, x='categoria', y='valor', palette='Set2')

📌 Quando usar cada um:
- Histograma: para entender a forma da distribuição de UMA variável
- Boxplot: para comparar distribuições entre CATEGORIAS

📌 O que falta nas próximas aulas:
- sns.heatmap() - mapa de calor (correlações)
- sns.pairplot() - matriz de dispersão
- Estilos e paletas de cores
"""
#####################################################################
# EXERCÍCIOS - AULA 2.4
#####################################################################
# Dados para todos os exercícios:

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Dados de uma loja (200 produtos)
np.random.seed(42)
df = pd.DataFrame({
    'produto': np.random.choice(['A', 'B', 'C', 'D'], 200),
    'preco': np.random.choice([50, 100, 150, 200], 200),
    'quantidade': np.random.randint(1, 100, 200),
    'categoria': np.random.choice(['Eletrônicos', 'Vestuário', 'Alimentos', 'Móveis'], 200)
})
df['total'] = df['quantidade'] * df['preco']

#####################################################################
# NÍVEL 1-3: Aquecimento
#####################################################################
"""
1. Primeiro histograma

# Crie um histograma da coluna 'total' do DataFrame
# Use sns.histplot()
# Título: "Distribuição do Valor Total das Vendas"
"""
"""
plt.figure(figsize=(10, 6))

sns.histplot(df['total'], bins=30, color='blue')
plt.title('Distribuição do Valor Total das Vendas')

plt.show()
"""
#####################################################################
"""
2. Primeiro boxplot

# Crie um boxplot comparando 'total' entre os diferentes 'produto'
# Use sns.boxplot()
# Título: "Valor Total por Produto"
"""
"""
plt.figure(figsize=(10, 6))

sns.boxplot(data=df, x='produto', y='total', hue='produto', palette='Set1', width=0.5)
plt.title('Valor Total por Produto')

plt.show()
"""
#####################################################################
"""
3. Ajustando bins

# Use os dados do exercício 1
# Crie um histograma com 50 bins
# Crie outro com 10 bins
# Mostre os dois lado a lado
"""
"""
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
sns.histplot(df['total'], bins=50)
plt.title('Distribuição do Valor Total das Vendas (bin=50)')

plt.subplot(1, 2, 2)
sns.histplot(df['total'], bins=10)
plt.title('Distribuição do Valor Total das Vendas (bin=10)')

plt.tight_layout()
plt.show()
"""
#####################################################################
# NÍVEL 4-6: Aplicação
#####################################################################
"""
4. Múltiplos histogramas

# Crie um único gráfico com os histogramas de 'preco' e 'quantidade'
# Use transparência (alpha=0.5) para que um não esconda o outro
# Adicione legendas ("Preço", "Quantidade")
"""
"""
plt.figure(figsize=(10, 6))

sns.histplot(df['preco'], bins=10, label='Preço', color='blue', alpha=0.5)
sns.histplot(df['quantidade'], bins='auto', label='Quantidade', color='green', alpha=0.5)
plt.legend()

plt.show()
"""
#####################################################################
"""
5. Boxplot por categoria

# Crie um boxplot comparando 'total' entre as diferentes 'categoria'
# Use palette='Set2' para cores diferentes
"""
"""
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='categoria', y='total', hue='categoria', palette='Set2', width=0.5)
plt.title('Valor total x Categoria')
plt.ylabel('Valor (R$)')

plt.show()
"""
#####################################################################
"""
6. Boxplot horizontal

# Crie o mesmo boxplot do exercício 5, mas na horizontal
# (total no eixo X, categoria no eixo Y)
"""
"""
plt.figure(figsize=(6, 10))
sns.boxplot(data=df, x='total', y='categoria', hue='categoria', palette='Set2', width=0.5)
plt.title('Valor total x Categoria')
plt.ylabel('Valor (R$)')

plt.tight_layout()
plt.show()
"""
#####################################################################
# NÍVEL 7-8: Manipulação
#####################################################################
"""
7. Boxplot + Histograma juntos

# Crie uma figura com 2 subplots (1 linha, 2 colunas)
# Gráfico 1: histograma do 'total'
# Gráfico 2: boxplot do 'total' por 'produto'
# Dê o título apropriado para cada
"""
"""
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
sns.histplot(df['total'], bins='auto', color='blue')
plt.title('Distribuição do Valor Total')

plt.subplot(1, 2, 2)
sns.boxplot(data=df, x='produto', y='total', hue='produto', palette='Set2', width=0.5)
plt.title('Valor total x Produto')
plt.ylabel('Valor (R$)')

plt.tight_layout()
plt.show()
"""
#####################################################################
"""
8. Comparação entre produtos

# Filtre o DataFrame para apenas os produtos 'A' e 'B'
# Crie um boxplot comparando o 'total' desses dois produtos
# Use cores diferentes (dica: palette)
"""
"""
df_ab = df[(df['produto']=='A') | (df['produto']=='B')].reset_index(drop=True)

plt.figure(figsize=(10, 6))
sns.boxplot(data=df_ab, x='produto', y='total', hue='produto', palette='Set2', width=0.5)
plt.title('Produto A x Produto B (valor total)')
plt.show()
"""
#####################################################################
# NÍVEL 9-10: Desafios
#####################################################################
"""
9. Dashboard de análise

# Crie um dashboard (2 linhas, 2 colunas) com:
# (0,0): histograma do 'total'
# (0,1): histograma do 'preco'
# (1,0): boxplot do 'total' por 'produto'
# (1,1): boxplot do 'total' por 'categoria'
#
# Use títulos, rótulos e grades apropriados
"""
"""
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

sns.histplot(df['total'], bins='auto', color='blue', ax=axes[0, 0])
axes[0, 0].set_title('Distribuição do Valor Total')

sns.histplot(df['preco'], bins='auto', color='green', ax=axes[0, 1])
axes[0, 1].set_title('Distribuição do Preço')

sns.boxplot(data=df, x='produto', y='total', hue='produto', palette='Set1', width=0.5, ax=axes[1,0])
axes[1, 0].set_title('Valor total x Produto')
axes[1, 0].set_ylabel('Valor (R$)')

sns.boxplot(data=df, x='categoria', y='total', hue='categoria', palette='Set2', width=0.5, ax=axes[1,1])
axes[1, 1].set_title('Valor total x Categoria')
axes[1, 1].set_ylabel('Valor (R$)')

plt.tight_layout()
plt.show()
"""
#####################################################################
"""
10. DESAFIO FINAL: Análise de desempenho

# Calcule para o DataFrame:
# - Total de vendas (soma do 'total')
# - Média do 'total' por produto
# - Média do 'total' por categoria
# - O produto com maior média de 'total'
# - A categoria com maior média de 'total'
#
# Depois, crie:
# - Um boxplot do 'total' por 'produto' (em ordem decrescente de média)
# - Um histograma do 'total' apenas para o produto com maior média
# - Um histograma do 'total' apenas para a categoria com maior média
#
# Mostre os resultados no console
"""
# Dados para análise simulada

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Dados de uma loja (200 produtos)
np.random.seed(42)
df = pd.DataFrame({
    'produto': np.random.choice(['A', 'B', 'C', 'D'], 200),
    'preco': np.random.choice([50, 100, 150, 200], 200),
    'quantidade': np.random.randint(1, 100, 200),
    'categoria': np.random.choice(['Eletrônicos', 'Vestuário', 'Alimentos', 'Móveis'], 200)
})

df['total'] = df['quantidade'] * df['preco']

total_vendas = df['total'].sum()
print(f'\nTotal de vendas: R$ {total_vendas:,.2f}')

media_total_produto = df.groupby('produto').agg(
    med_tot_prod=('total', 'mean')
).round(2).reset_index()

print(f'\nMédia do "total" por produto:\n{media_total_produto}')

media_total_categoria = df.groupby('categoria').agg(
    med_tot_cat=('total', 'mean')
).round(2).reset_index()

print(f'\nMédia do "total" por categoria:\n{media_total_categoria}')

produto_maior_media_total = media_total_produto.loc[media_total_produto['med_tot_prod'].idxmax(), 'produto']
print(f'\nProduto com maior média de "total": Produto {produto_maior_media_total}')

categoria_maior_media_total = media_total_categoria.loc[media_total_categoria['med_tot_cat'].idxmax(), 'categoria']
print(f'\nCategoria com maior média de "total": {categoria_maior_media_total}')

df_completo = pd.merge(df, media_total_produto, on='produto', how='inner')
df_completo = pd.merge(df_completo, media_total_categoria, on='categoria', how='inner')
df_completo_ord = df_completo.sort_values('med_tot_prod', ascending=False)

# Gráficos:

fig, axes = plt.subplots(1, 3, figsize=(18, 6))

sns.boxplot(data=df_completo_ord, x='produto', y='total', hue='produto', palette='Set1', width=0.5, ax=axes[0])
axes[0].set_title('Valor total x Produto (ord. Produto maior média)')
axes[0].set_ylabel('Valor (R$)')

df_produto_maior_media = df[df['produto']==produto_maior_media_total]
sns.histplot(df_produto_maior_media['total'], bins='auto', color='blue', ax=axes[1])
axes[1].set_title(f'Dist. do Valor Total do Produto {produto_maior_media_total} (maior média)')

df_categoria_maior_media = df[df['categoria']==categoria_maior_media_total]
sns.histplot(df_categoria_maior_media['total'], bins='auto', color='green', ax=axes[2])
axes[2].set_title(f'Dist. do Valor Total da Categoria {categoria_maior_media_total} (maior média)')

plt.tight_layout()
plt.savefig('dashboard_básico_análise.png')