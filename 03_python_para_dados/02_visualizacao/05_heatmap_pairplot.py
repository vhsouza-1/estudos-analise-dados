"""
Bloco 3: Python para Dados
Módulo 2: Visualização de Dados
Aula 5: Heatmap e Pairplot
Data: 02/05/2026
Objetivo: Aprender a criar heatmaps e pairplots com Seaborn
"""
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# ==========================================
# 1. O QUE É UM HEATMAP?
# ==========================================

print("="*50)
print("1. O QUE É UM HEATMAP?")
print("="*50)

"""
HEATMAP (mapa de calor): mostra a intensidade de valores em uma matriz usando cores.

Para que serve?
- Visualizar correlações entre variáveis
- Identificar padrões em dados tabulares
- Comparar valores em uma matriz

Como funciona?
- Cores mais escuras/fortes = valores maiores (ou correlação mais forte)
- Cores mais claras = valores menores (ou correlação mais fraca)
- Geralmente usado com matriz de correlação
"""
# ==========================================
# 2. MATRIZ DE CORRELAÇÃO
# ==========================================

print("\n" + "="*50)
print("2. MATRIZ DE CORRELAÇÃO")
print("="*50)

"""
CORRELAÇÃO: mede a relação entre duas variáveis numéricas.

Valores:
- 1: correlação positiva perfeita (uma aumenta, a outra aumenta)
- 0: sem correlação
- -1: correlação negativa perfeita (uma aumenta, a outra diminui)

Exemplos:
- Idade e altura em crianças: correlação positiva (quanto mais idade, mais altura)
- Preço e quantidade vendida: correlação negativa (quanto mais caro, menos vende)
"""

# Dados de exemplo
np.random.seed(42)
df = pd.DataFrame({
    'vendas': np.random.normal(1000, 200, 100),
    'marketing': np.random.normal(500, 100, 100),
    'preco': np.random.normal(100, 20, 100),
    'clientes': np.random.normal(50, 10, 100)
})

# Adicionar algumas correlações artificiais
df['vendas'] = df['vendas'] + df['marketing'] * 0.5
df['clientes'] = df['clientes'] + df['marketing'] * 0.3

print("Primeiras linhas dos dados:")
print(df.head())

# Calculando a matriz de correlação
correlacao = df.corr()
print("\nMatriz de correlação:")
print(correlacao.round(2))

# ==========================================
# 3. CRIANDO UM HEATMAP (sns.heatmap)
# ==========================================

print("\n" + "="*50)
print("3. CRIANDO UM HEATMAP")
print("="*50)

# Heatmap básico
# plt.figure(figsize=(8, 6))
# sns.heatmap(correlacao)
# plt.title('Heatmap de Correlação - Básico')
# plt.show()

# ==========================================
# 4. PARÂMETROS DO HEATMAP
# ==========================================

print("\n" + "="*50)
print("4. PARÂMETROS DO HEATMAP")
print("="*50)

# 4.1. annot - mostrar os valores
print("--- annot=True (mostrar valores) ---")
# plt.figure(figsize=(8, 6))
# sns.heatmap(correlacao, annot=True)
# plt.title('Heatmap com valores')
# plt.show()

# 4.2. cmap - mapa de cores
print("\n--- cmap (mapa de cores) ---")
print("Cores disponíveis: 'coolwarm', 'viridis', 'Blues', 'Reds', 'RdYlBu'")

# plt.figure(figsize=(12, 4))
#
# plt.subplot(1, 3, 1)
# sns.heatmap(correlacao, annot=True, cmap='coolwarm')
# plt.title('coolwarm')
#
# plt.subplot(1, 3, 2)
# sns.heatmap(correlacao, annot=True, cmap='viridis')
# plt.title('viridis')
#
# plt.subplot(1, 3, 3)
# sns.heatmap(correlacao, annot=True, cmap='Blues')
# plt.title('Blues')
#
# plt.tight_layout()
# plt.show()

# 4.3. fmt - formato dos números
print("\n--- fmt (formato dos números) ---")
# plt.figure(figsize=(8, 6))
# sns.heatmap(correlacao, annot=True, fmt='.2f', cmap='coolwarm')
# plt.title('Heatmap com 2 casas decimais')
# plt.show()

# 4.4. vmin, vmax - limites da escala de cores
print("\n--- vmin e vmax (limites da escala) ---")
# plt.figure(figsize=(8, 6))
# sns.heatmap(correlacao, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
# plt.title('Heatmap com limites -1 a 1')
# plt.show()

# ==========================================
# 5. HEATMAP COM DATASET REAL (IRIS)
# ==========================================

print("\n" + "="*50)
print("5. HEATMAP COM DATASET IRIS")
print("="*50)

# Carregar dataset Iris (flores)
iris = sns.load_dataset('iris')
print("Dataset Iris (5 primeiras linhas):")
print(iris.head())

# Selecionar apenas colunas numéricas
iris_num = iris.select_dtypes(include=[np.number])
correlacao_iris = iris_num.corr()

# plt.figure(figsize=(8, 6))
# sns.heatmap(correlacao_iris, annot=True, cmap='coolwarm', fmt='.2f', vmax=1, vmin=-1)
# plt.title('Correlação entre características das flores Iris')
# plt.show()

# ==========================================
# 6. INTERPRETANDO O HEATMAP
# ==========================================

print("\n" + "="*50)
print("6. INTERPRETANDO O HEATMAP")
print("="*50)

"""
Como ler um heatmap de correlação:

- Quanto mais VERMELHO (positivo), mais forte a correlação positiva
- Quanto mais AZUL (negativo), mais forte a correlação negativa
- Quanto mais BRANCO, mais fraca a correlação
- Diagonal principal sempre é 1 (correlação de uma variável com ela mesma)

Exemplo de interpretação:
- se petal_length e petal_width têm correlação ~0.96 → estão fortemente relacionados
- se sepal_length e petal_length têm correlação ~0.87 → também são relacionados
- Isso faz sentido botanicamente!
"""

# ==========================================
# 7. O QUE É UM PAIRPLOT?
# ==========================================

print("\n" + "="*50)
print("7. O QUE É UM PAIRPLOT?")
print("="*50)

"""
PAIRPLOT: mostra todos os gráficos de dispersão entre pares de variáveis.

Para que serve?
- Explorar relações entre todas as variáveis numéricas de uma vez
- Identificar padrões, tendências e outliers
- Visualizar distribuições na diagonal

O que mostra?
- Diagonal: histograma da variável (distribuição)
- Fora da diagonal: gráfico de dispersão entre duas variáveis
- Cores: podem diferenciar categorias (parâmetro hue)
"""

# ==========================================
# 8. CRIANDO UM PAIRPLOT (sns.pairplot)
# ==========================================

print("\n" + "="*50)
print("8. CRIANDO UM PAIRPLOT")
print("="*50)

# Pairplot básico
# sns.pairplot(iris)
# plt.tight_layout()
# plt.show()

print("Pairplot Iris - cada gráfico mostra a relação entre duas variáveis")

# ==========================================
# 9. PARÂMETROS DO PAIRPLOT
# ==========================================

print("\n" + "="*50)
print("9. PARÂMETROS DO PAIRPLOT")
print("="*50)

# 9.1. hue - colorir por categoria
print("--- hue (colorir por categoria) ---")
# sns.pairplot(iris, hue='species')
# plt.show()

print("Pairplot colorido por espécie - mostra diferenças entre grupos")

# 9.2. diag_kind - tipo de gráfico na diagonal
print("\n--- diag_kind (tipo na diagonal) ---")
print("Opções: 'hist' (histograma), 'kde' (densidade)")
# sns.pairplot(iris, hue='species', diag_kind='kde')
# plt.show()

# 9.3. markers - marcadores diferentes por categoria
print("\n--- markers (marcadores diferentes) ---")
# sns.pairplot(iris, hue='species', markers=['o', 's', 'D'])
# plt.show()

# 9.4. plot_kws - personalizar gráficos de dispersão
print("\n--- plot_kws (personalizar) ---")
# sns.pairplot(iris, hue='species', plot_kws={'alpha': 0.5})
# plt.show()

# ==========================================
# 10. EXEMPLO PRÁTICO: ANÁLISE DE VENDAS
# ==========================================

print("\n" + "="*50)
print("10. EXEMPLO PRÁTICO")
print("="*50)

# Dados de vendas simulados
np.random.seed(42)
vendas_df = pd.DataFrame({
    'preco': np.random.normal(100, 30, 200),
    'marketing': np.random.normal(1000, 200, 200),
    'funcionarios': np.random.randint(5, 20, 200),
    'vendas': np.random.normal(5000, 1000, 200)
})

# Adicionar correlações
vendas_df['vendas'] = vendas_df['vendas'] - vendas_df['preco'] * 10 + vendas_df['marketing'] * 2 + vendas_df['funcionarios'] * 50

print("Primeiras linhas dos dados de vendas:")
print(vendas_df.head())

# 1. Heatmap de correção
correlacao_vendas = vendas_df.corr()
# plt.figure(figsize=(8, 6))
# sns.heatmap(correlacao, annot=True, cmap='coolwarm', fmt='.2f', vmax=1, vmin=-1)
# plt.title('Correlação entre variáveis de vendas')
# plt.show()

print("\nInterpretação:")
print(f'Preço vs Vendas: {correlacao_vendas.loc['preco', 'vendas']:.2f} (negativo - quanto maior preço, menor venda)')
print(f'Marketing vs Vendas: {correlacao_vendas.loc['marketing', 'vendas']:.2f} (positivo - mais marketing, mais vendas)')
print(f'Funcionários vs Vendas: {correlacao_vendas.loc['funcionarios', 'vendas']:.2f} (positivo - mais funcionários, mais vendas)')

# 2. Pairplot
# sns.pairplot(vendas_df)
# plt.show()

# ==========================================
# 11. RESUMO
# ==========================================

print("\n" + "="*50)
print("11. RESUMO")
print("="*50)

"""
✅ HEATMAP (sns.heatmap):
   - sns.heatmap(matriz) - básico
   - sns.heatmap(matriz, annot=True) - mostrar valores
   - sns.heatmap(matriz, cmap='coolwarm') - mapa de cores
   - sns.heatmap(matriz, fmt='.2f') - formato dos números
   - sns.heatmap(matriz, vmin=-1, vmax=1) - limites da escala

✅ MATRIZ DE CORRELAÇÃO:
   - df.corr() - calcula correlações entre colunas numéricas
   - Valores entre -1 e 1

✅ PAIRPLOT (sns.pairplot):
   - sns.pairplot(df) - básico
   - sns.pairplot(df, hue='categoria') - colorir por categoria
   - sns.pairplot(df, diag_kind='kde') - densidade na diagonal
   - sns.pairplot(df, markers=['o', 's', 'D']) - marcadores diferentes

📌 Quando usar cada um:
- Heatmap: para ver correlações entre várias variáveis de uma vez
- Pairplot: para explorar relações entre pares de variáveis
"""
########################################################################
# EXERCÍCIOS - AULA 2.5
########################################################################
# Dados para os exercícios

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(42)

# Preços fixos por produto
precos = {'Smartphone': 1500, 'Notebook': 3500, 'Tablet': 800, 'Fone': 200}
custos = {'Smartphone': 800, 'Notebook': 2000, 'Tablet': 400, 'Fone': 100}

# Gerar dados
produtos = np.random.choice(['Smartphone', 'Notebook', 'Tablet', 'Fone'], 200)
regioes = np.random.choice(['Norte', 'Sul', 'Leste', 'Oeste'], 200)
quantidades = np.random.randint(1, 50, 200)

df = pd.DataFrame({
    'produto': produtos,
    'regiao': regioes,
    'quantidade': quantidades,
    'preco': [precos[p] for p in produtos],
    'custo': [custos[p] for p in produtos]
})

df['receita'] = df['quantidade'] * df['preco']
df['lucro'] = df['quantidade'] * (df['preco'] - df['custo'])

########################################################################
# NÍVEL 1-3: Aquecimento
########################################################################
"""
1. Matriz de correlação

# Calcule a matriz de correlação das colunas numéricas
# (quantidade, preco, custo, receita, lucro)
# Mostre a matriz no console
"""
"""
df_num = df.select_dtypes(include=[np.number])
df_correlacao = df_num.corr()
print(df_correlacao)
"""
########################################################################
"""
2. Heatmap básico

# Crie um heatmap da matriz de correlação
# Título: "Correlação entre Métricas"
"""
"""
df_num = df.select_dtypes(include=[np.number])
df_correlacao = df_num.corr()

plt.figure(figsize=(10, 6))
sns.heatmap(df_correlacao, annot=True, cmap='coolwarm', fmt='.2f', vmin=-1, vmax=1)
plt.title('Correlação entre Métricas')
plt.show()
"""
########################################################################
"""
3. Heatmap com valores

# Crie um heatmap com annot=True, fmt='.2f', cmap='coolwarm'
"""
"""
df_num = df.select_dtypes(include=[np.number])
df_correlacao = df_num.corr()

plt.figure(figsize=(10, 6))
sns.heatmap(df_correlacao, annot=True, cmap='coolwarm', fmt='.2f', vmin=-1, vmax=1)
plt.title('Correlação entre Métricas')
plt.show()
"""
########################################################################
# NÍVEL 4-6: Aplicação
########################################################################
"""
4. Interpretando correlações

# Com base no heatmap:
# - Qual variável tem maior correlação com 'lucro'?
# - Qual variável tem menor correlação com 'lucro'?
# O que isso significa na prática?
"""
"""
df_num = df.select_dtypes(include=[np.number])
df_correlacao = df_num.corr()

plt.figure(figsize=(10, 6))
sns.heatmap(df_correlacao, annot=True, cmap='coolwarm', fmt='.2f', vmin=-1, vmax=1)
plt.title('Correlação entre Métricas')
plt.show()

# Receita tem a maior correlação. Todas as variáveis são positivamente relacionadas com lucro, mas a receita é maior, pois elas tem uma relação linear direta.
# Quantidade tem a menor correlação. Elas ainda são positivamente relacionadas (0.59) mas as outras variaveis tem mais relação. 
"""
########################################################################
"""
5. Pairplot básico

# Crie um pairplot das colunas numéricas
# (quantidade, preco, custo, receita, lucro)
"""
"""
sns.pairplot(df)
plt.show()
"""
########################################################################
"""
6. Pairplot colorido por produto

# Crie um pairplot colorido por 'produto' (hue='produto')
"""
"""
sns.pairplot(df, hue='produto')
plt.show()
"""
########################################################################
# NÍVEL 7-8: Manipulação
########################################################################
"""
7. Pairplot colorido por região

# Crie um pairplot colorido por 'regiao' (hue='regiao')
"""
"""
sns.pairplot(df, hue='regiao')
plt.show()
"""
########################################################################
"""
8. Análise por produto

# Agrupe os dados por 'produto' e calcule:
# - Receita total
# - Lucro total
# - Quantidade total vendida
# Mostre os resultados
"""
"""
analise_produto = df.groupby('produto').agg(
    receita_total=('receita', 'sum'),
    lucro_total=('lucro', 'sum'),
    qtd_total=('quantidade', 'sum')
).reset_index()

print(analise_produto)

analise_produto_num = analise_produto.select_dtypes(include=[np.number])

plt.figure(figsize=(10,8))
sns.heatmap(analise_produto_num.corr(), annot=True, fmt='.2f', cmap='coolwarm', vmin=-1, vmax=1)

plt.tight_layout()
plt.show()
"""
########################################################################
# NÍVEL 9-10: Desafios
########################################################################
"""
9. Dashboard de correlações

# Crie um dashboard com:
# (0,0): heatmap da correlação
# (0,1): boxplot de lucro por produto
# (1,0): boxplot de lucro por região
"""
"""
plt.figure(figsize=(18, 6))
plt.subplot(1, 3, 1)
df_num = df.select_dtypes(include=[np.number])
sns.heatmap(df_num.corr(), annot=True, cmap='coolwarm', fmt='.2f', vmin=-1, vmax=1)
plt.title('Heatmap da correção')

plt.subplot(1, 3, 2)
sns.boxplot(data=df, x='produto', y='lucro', hue='produto', palette='Set1', width=0.5)
plt.title('Lucro x Produto')

plt.subplot(1, 3, 3)
sns.boxplot(data=df, x='regiao', y='lucro', hue='produto', palette='Set1', width=0.5)
plt.title('Lucro x Região')

plt.tight_layout()
plt.show()
"""
########################################################################
"""
10. DESAFIO FINAL: Relatório simples

# Com base nos dados, responda:
# 1. Qual produto dá mais lucro? (total)
# 2. Qual região vende mais? (quantidade total)
# 3. Existe correlação entre preço e quantidade? (positiva/negativa?)
# 4. Existe correlação entre quantidade e lucro?
#
# Mostre as respostas com print() e um gráfico de barras do lucro por produto
"""
"""
analise_produto = df.groupby('produto').agg(
    receita_total=('receita', 'sum'),
    lucro_total=('lucro', 'sum'),
    qtd_total=('quantidade', 'sum')
).reset_index()

analise_regiao = df.groupby('regiao').agg(
    receita_total=('receita', 'sum'),
    lucro_total=('lucro', 'sum'),
    qtd_total=('quantidade', 'sum')
).reset_index()


print(f'Qual produto da mais lucro: {analise_produto.loc[analise_produto['lucro_total'].idxmax(), 'produto']}')
print(f'Qual região vende mais: {analise_regiao.loc[analise_produto['qtd_total'].idxmax(), 'regiao']}')

df_num = df.select_dtypes(include=[np.number])
df_num_corr = df_num.corr()

print(f'Preço x Quantidade: {df_num_corr.loc['preco', 'quantidade']:.2f} (Correção positiva muito baixa)')
print(f'Quantidade x Lucro {df_num_corr.loc['quantidade', 'lucro']:.2f} (Correção positiva considerável)')

sns.barplot(data=df, x='produto', y='lucro', hue='produto')
plt.show()
"""
