"""
Bloco 3: Python para Dados
Módulo 3: Limpeza de Dados Avançada
Aula 1: Tratamento de Valores Nulos (Avançado)
Data: 04/05/2026
Objetivo: Aprender estratégias avançadas para lidar com valores nulos em DataFrames
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# ==========================================
# 1. REVISÃO RÁPIDA (O QUE VOCÊ JÁ SABE)
# ==========================================

print("="*50)
print("1. REVISÃO RÁPIDA - VALORES NULOS BÁSICOS")
print("="*50)

# Criando um DataFrame com valores nulos
np.random.seed(42)
df_exemplo = pd.DataFrame({
    'nome': ['Ana', 'Bruno', 'Carlos', None, 'Eduarda'],
    'idade': [25, None, 30, 22, 35],
    'salario': [3000, 3500, None, 2800, 4000],
    'cidade': ['SP', 'RJ', 'BH', None, 'SP']
})

print("DataFrame exemplo:")
print(df_exemplo)

print("\n--- Revisão básica ---")
print(f"isnull():\n{df_exemplo.isnull()}")
print(f"\nisnull().sum():\n{df_exemplo.isnull().sum()}")
print(f"\nTotal de nulos: {df_exemplo.isnull().sum().sum()}")

# ==========================================
# 2. dropna() AVANÇADO
# ==========================================

print("\n" + "="*50)
print("2. dropna() AVANÇADO")
print("="*50)

"""
O que já sabemos:
- df.dropna() - remove qualquer linha com nulo
- df.dropna(axis=1) - remove qualquer coluna com nulo

O que vamos aprender:
- subset: remove apenas se nulos estiverem em colunas específicas
- thresh: mantém linha se tiver pelo menos N valores não-nulos
- how='all': remove apenas se TODOS os valores forem nulos
"""

# Dados para demonstração
df_demo = pd.DataFrame({
    'A': [1, 2, None, 4, None, 6],
    'B': [None, 2, 3, None, 5, 6],
    'C': [1, None, 3, 4, 5, None],
    'D': [None, None, None, 4, 5, None]
})

print("\nDataFrame demo:")
print(df_demo)

# 2.1 subset - considera apenas colunas específicas
print("\n--- subset (considera apenas colunas específicas) ---")
print("df_demo.dropna(subset=['A', 'B']):")
print(df_demo.dropna(subset=['A', 'B']))
print("Só remove se A OU B forem nulos")

# 2.2 thresh - número mínimo de não-nulos
print("\n--- thresh (número mínimo de valores não-nulos) ---")
print("df_demo.dropna(thresh=3):")  # precisa de pelo menos 3 não-nulos
print(df_demo.dropna(thresh=3))
print("\ndf_demo.dropna(thresh=4):")  # precisa de pelo menos 4 não-nulos
print(df_demo.dropna(thresh=4))

# 2.3 how='all' - remove só se todos forem nulos
print("\n--- how='all' (remove só se TODOS forem nulos) ---")
df_todos_nulos = pd.DataFrame({
    'X': [1, None, None],
    'Y': [2, None, None],
    'Z': [3, None, None]
})
print("DataFrame com linha totalmente nula:")
print(df_todos_nulos)
print("\ndf_todos_nulos.dropna(how='all'):")
print(df_todos_nulos.dropna(how='all'))

# ==========================================
# 3. fillna() AVANÇADO
# ==========================================

print("\n" + "="*50)
print("3. fillna() AVANÇADO")
print("="*50)

"""
O que já sabemos:
- df.fillna(valor) - preenche com um valor fixo

O que vamos aprender:
- Preencher com estatísticas (média, mediana, moda)
- method='ffill' (forward fill)
- method='bfill' (backward fill)
- Preencher colunas diferentes com valores diferentes
- limit - limitar quantidade de preenchimentos
"""

df_preencher = pd.DataFrame({
    'data': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05'],
    'vendas': [100, None, None, 150, 200],
    'estoque': [50, None, 60, None, 80]
})

print("DataFrame para preenchimento:")
print(df_preencher)

# 3.1 Preencher com estatísticas
print("\n--- Preencher com estatísticas ---")
print(f"Média das vendas: {df_preencher['vendas'].mean():.1f}")
df_preencher_media = df_preencher.copy()
df_preencher_media['vendas'] = df_preencher_media['vendas'].fillna(df_preencher_media['vendas'].mean())
print("Preenchido com média:")
print(df_preencher_media)

print("\n--- Preencher com mediana (mais robusta para outliers) ---")
print(f"Mediana das vendas: {df_preencher['vendas'].median()}")
df_preencher_mediana = df_preencher.copy()
df_preencher_mediana['vendas'] = df_preencher_mediana['vendas'].fillna(df_preencher_mediana['vendas'].median()) # vamos evitar de usar inplace=True e usar atribuição direta pq o inplace ta bugando meu PyCharm haha
print("Preenchido com mediana:")
print(df_preencher_mediana)

# 3.2 Preencher com método forward fill (propaga o último valor válido)
print("\n--- method='ffill' (forward fill) ---")
df_ffill = df_preencher.copy()
# df_ffill['vendas'].fillna(method='ffill', inplace=True) na minha versão do Python o method='ffill' não existe mais, agora se usa:
df_ffill['vendas'] = df_ffill['vendas'].ffill()
print("ffill aplicado:")
print(df_ffill)

# 3.3 Preencher com método backward fill (propaga o próximo valor válido)
print("\n--- method='bfill' (backward fill) ---")
df_bfill = df_preencher.copy()
df_bfill['vendas'] = df_bfill['vendas'].bfill()
print("bfill aplicado:")
print(df_bfill)

# 3.4 Preencher colunas diferentes com valores diferentes
print("\n--- Preencher colunas diferentes com valores diferentes ---")
df_diferente = df_preencher.copy()
valores_preenchimento = {'vendas': 0, 'estoque': df_preencher['estoque'].median()} # interessante essa forma de fazer o tratamento.
# df_diferente.fillna(valores_preenchimento, inplace=True)
df_diferente = df_diferente.fillna(valores_preenchimento)
print("Preenchimento por coluna:")
print(df_diferente)

# 3.5 limit - limitar quantidade de preenchimentos
print("\n--- limit (limitar quantidade) ---")
df_limit = df_preencher.copy()
df_limit['vendas'] = df_limit['vendas'].ffill(limit=1)
print("ffill com limit=1 (só preenche o primeiro nulo):")
print(df_limit)

# ==========================================
# 4. INTERPOLAÇÃO (MÉTODO MAIS SOFISTICADO)
# ==========================================

print("\n" + "="*50)
print("4. INTERPOLAÇÃO (interpolate)")
print("="*50)

"""
INTERPOLAÇÃO: estima valores intermediários com base em tendências.

Quando usar:
- Séries temporais (dados com ordem lógica)
- Dados que seguem uma tendência (linear, polinomial, etc.)
- Evitar: dados categóricos ou sem ordem natural

Métodos comuns:
- 'linear' (padrão) - reta entre pontos conhecidos
- 'polynomial' - curva polinomial (requer order)
- 'quadratic' - parábola
- 'pad' - repetir valores
"""

# Dados de temperatura ao longo do tempo
df_temp = pd.DataFrame({
    'dia': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'temperatura': [22, None, 24, None, 26, None, 28, None, 30, 31]
})

print("Dados de temperatura (com nulos):")
print(df_temp)

# 4.1 Interpolação linear
print("\n--- Interpolação linear (padrão) ---")
df_temp_linear = df_temp.copy()
df_temp_linear['temperatura'] = df_temp_linear['temperatura'].interpolate()
print(df_temp_linear)

# 4.2 Interpolação polinomial (quadrática)
print("\n--- Interpolação quadrática ---")
df_temp_quadratic = df_temp.copy()
df_temp_quadratic['temperatura'] = df_temp_quadratic['temperatura'].interpolate(method='quadratic')
print(df_temp_quadratic)

# 4.3 Interpolação limitada
print("\n--- Interpolação com limit=2 ---")
df_temp_limit = df_temp.copy()
df_temp_limit['temperatura'] = df_temp_limit['temperatura'].interpolate(limit=2)
print(df_temp_limit)

# Visualização (opcional - comentado)
# plt.figure(figsize=(10, 6))
# plt.plot(df_temp['dia'], df_temp['temperatura'], 'o-', label='Original (com nulos)')
# plt.plot(df_temp_linear['dia'], df_temp_linear['temperatura'], 's--', label='Linear')
# plt.plot(df_temp_quadratic['dia'], df_temp_quadratic['temperatura'], '^--', label='Quadrática')
# plt.legend()
# plt.title('Comparação de Métodos de Interpolação')
# plt.xlabel('Dia')
# plt.ylabel('Temperatura')
# plt.show()

# Descomentei, visualizei e comentei dnv. Nesse caso os 3 graficos são iguais.

# ==========================================
# 5. replace() PARA PADRONIZAR NULOS
# ==========================================

print("\n" + "="*50)
print("5. replace() - Padronizando valores que representam nulos")
print("="*50)

"""
Muitas vezes, valores como -999, 0, 'NA', 'N/A', 'desconhecido' representam nulos.
O replace() permite converter esses valores para np.nan.
"""

df_sujo = pd.DataFrame({
    'produto': ['A', 'B', 'C', 'D', 'E'],
    'preco': [100, -999, 150, 0, 200],
    'quantidade': [10, 20, 'NA', 30, -1],
    'categoria': ['eletro', 'moveis', 'N/A', 'eletro', 'desconhecido']
})

print("DataFrame com valores representando nulos:")
print(df_sujo)

df_limpo = df_sujo.copy()
df_limpo['preco'] = df_limpo['preco'].replace([-999, 0, -1], np.nan)
df_limpo['quantidade'] = pd.to_numeric(df_limpo['quantidade'].replace(['NA', -1], np.nan)) # pq vc passou esse to_numeric nessa coluna? N deveria ter passado em preco tbm?
df_limpo['categoria'] = df_limpo['categoria'].replace(['N/A', 'desconhecido'], np.nan)

print("\nDataFrame após padronização (valores inválidos viraram np.nan):")
print(df_limpo)

# ==========================================
# 6. ESTRATÉGIAS DE DECISÃO (QUAL MÉTODO USAR?)
# ==========================================

print("\n" + "="*50)
print("6. ESTRATÉGIAS DE DECISÃO - QUANDO USAR CADA MÉTODO")
print("="*50)

"""

QUADRO DE DECISÃO PARA VALORES NULOS:

| Situação                        | Estratégia             | Exemplo |
|---------------------------------|------------------------|---------|
| Poucos nulos (<5%)              | dropna()               | 2 linhas nulas em 1000 |
| Muitos nulos na linha           | dropna(thresh=...)     | Manter linhas com 80% preenchido |
| Série temporal com tendência    | interpolate()          | Temperatura, preço de ações |
| Coluna numérica (sem tendência) | fillna(mediana)        | Idade, salário |
| Coluna categórica               | fillna(moda)           | Cidade, categoria |
| Dados com sazonalidade          | .ffill()               | Vendas de mês anterior |
| Linha inteira nula              | dropna(how='all')      | Remove completamente vazia |
| Valores -999, 0, 'NA'           | replace() + fillna()   | Padronizar primeiro |

REGRAS DE OURO:
1. SEMPRE documente por que escolheu cada estratégia
2. NUNCA preencha com média se dados têm outliers fortes
3. SEMPRE verifique a distribuição ANTES de decidir
"""
# ==========================================
# 7. EXEMPLO PRÁTICO: ANÁLISE DE NULOS REAL
# ==========================================

print("\n" + "="*50)
print("7. EXEMPLO PRÁTICO - Dataset Titanic")
print("="*50)

# Carregar dados do Titanic (dataset real)
titanic = sns.load_dataset('titanic')

print("Dataset Titanic (informações básicas):")
titanic.info() # n precisa de print no .info()

print("\nQuantidade de nulos por coluna:")
print(titanic.isnull().sum())

print("\nPorcentagem de nulos:")
print((titanic.isnull().sum() / len(titanic)) * 100)

# Estratégia para cada coluna
print("\n--- Estratégia de limpeza para Titanic ---")
print("age (20% nulos): preencher com mediana por classe/sexo")
print("embarked (0.2% nulos): preencher com moda (porto mais comum)")
print("deck (77% nulos): dropar a coluna (muitos nulos)")
print("embark_town (0.2% nulos): preencher com moda")

# Implementação
# Implementação (comentada)
# titanic['age'] = titanic.groupby(['sex', 'class'])['age'].transform(lambda x: x.fillna(x.median())) # não entendi, n foi explicado...
# titanic['embarked'].fillna(titanic['embarked'].mode()[0], inplace=True)
# titanic.drop('deck', axis=1, inplace=True)

print("\nApós limpeza (simulada):")
print("- age: nulos preenchidos com mediana por grupo")
print("- deck: coluna removida")
print("- embarked: preenchido com 'S' (moda)")

print("\nApós limpeza (simulada):")
print("- age: nulos preenchidos com mediana por grupo")
print("- deck: coluna removida")
print("- embarked: preenchido com 'S' (moda)")

# ==========================================
# 8. RESUMO DA AULA
# ==========================================

print("\n" + "="*50)
print("8. RESUMO DA AULA")
print("="*50)

"""
✅ dropna() AVANÇADO:
   - subset=['col1', 'col2']  # só considera essas colunas
   - thresh=3                 # precisa de 3 não-nulos
   - how='all'                # remove só se TODOS forem nulos

✅ fillna() AVANÇADO:
   - fillna(df['col'].mean())    # média
   - fillna(df['col'].median())  # mediana (robusta a outliers)
   - fillna(df['col'].mode()[0]) # moda (categóricas)
   - fillna(method='ffill')      # forward fill
   - fillna(method='bfill')      # backward fill
   - fillna({'col1': valor1, 'col2': valor2})  # por coluna
   - fillna(limit=2)             # limita quantidade

✅ interpolate():
   - interpolate()               # linear (padrão)
   - interpolate(method='quadratic')  # quadrático
   - interpolate(limit=2)        # limita quantidade

✅ replace():
   - replace(-999, np.nan)       # valor único
   - replace([-999, -1, 0], np.nan)  # múltiplos valores

📌 REGRA DE OURO: SEMPRE documente suas decisões!
"""
# ==========================================
# EXERCÍCIOS - AULA 1
# ==========================================

print("\n" + "="*50)
print("EXERCÍCIOS - TRATAMENTO DE NULOS AVANÇADO")
print("="*50)

# Dados para todos os exercícios
np.random.seed(42)

df_exercicios = pd.DataFrame({
    'produto': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
    'preco': [100, 200, None, 150, None, 300, 250, None, 180, 220],
    'quantidade': [10, None, 30, 20, 25, None, 35, 40, None, 15],
    'categoria': ['eletro', 'moveis', 'eletro', None, 'moveis', 'eletro', None, 'moveis', 'eletro', 'moveis'],
    'data': pd.date_range('2024-01-01', periods=10)
})

# Adicionar alguns valores problemáticos
df_exercicios.loc[2, 'preco'] = -999
df_exercicios.loc[5, 'quantidade'] = -1
df_exercicios.loc[8, 'categoria'] = 'N/A'

########################################################################
# NÍVEL 1-3: Aquecimento
########################################################################

"""
1. Identificando nulos

# Calcule e mostre:
# - Total de valores nulos no DataFrame
# - Porcentagem de nulos por coluna
# - Quais colunas têm mais de 20% de nulos
"""
"""
print(f'Total de valores nulos no df: {df_exercicios.isnull().sum().sum()}')

print(f'\nPorcentagem de valores nulos no df:')
print(df_exercicios.isnull().sum() / len(df_exercicios) * 100)

print(f'\nColunas com pelo menos 20% de nulos: ') # coloquei "pelo menos" para testar melhor.
for column in df_exercicios.columns:
    pct_nulos = df_exercicios[column].isnull().sum()/len(df_exercicios)
    if pct_nulos >= 0.2:
        print(f' - {column}')
"""
########################################################################
"""
2. dropna com subset

# Remova as linhas que têm NULO especificamente nas colunas 'preco' e 'quantidade'
# Mostre o DataFrame resultante
"""
"""
df = df_exercicios.copy()
df = df.dropna(subset=['preco', 'quantidade'])
print(df)
"""
########################################################################
"""
3. dropna com thresh

# Mantenha apenas as linhas que têm pelo menos 3 valores NÃO-NULOS
# Mostre quantas linhas foram removidas
"""
"""
df = df_exercicios.copy()

df = df.dropna(thresh=5) # como o nome do produto e a data sempre está preenchida, fiz +2 nos seus requisitos

print(f'Quantidade de linhas removidas: {len(df_exercicios) - len(df)}')
"""
########################################################################
# NÍVEL 4-6: Aplicação
########################################################################
"""
4. Preenchimento com estatísticas

# Preencha os nulos da coluna 'preco' com a MEDIANA
# Preencha os nulos da coluna 'quantidade' com a MÉDIA
# Preencha os nulos da coluna 'categoria' com a MODA (valor mais frequente)
# Mostre o DataFrame preenchido
"""
"""
df = df_exercicios.copy()

df['preco'] = df['preco'].fillna(df['preco'].median())
df['quantidade'] = df['quantidade'].fillna(df['quantidade'].mean())
df['categoria'] = df['categoria'].fillna(df['categoria'].mode()[0])

print(df)
"""
########################################################################
"""
5. Forward fill e Backward fill

# Crie uma cópia do DataFrame original
# Preencha os nulos de 'preco' com ffill (forward fill)
# Preencha os nulos de 'quantidade' com bfill (backward fill)
# Compare com o resultado do exercício 4
"""
"""
df = df_exercicios.copy()

df['preco'] = df['preco'].ffill()
df['quantidade'] = df['quantidade'].bfill()

print(df)
"""
########################################################################
"""
6. Padronizando valores problemáticos

# No DataFrame original:
# - Substitua -999 da coluna 'preco' por np.nan
# - Substitua -1 da coluna 'quantidade' por np.nan
# - Substitua 'N/A' da coluna 'categoria' por np.nan
# Depois, preencha todos os nulos com estratégia apropriada
"""
"""
df = df_exercicios.copy()

df['preco'] = df['preco'].replace(-999, np.nan)
df['quantidade'] = df['quantidade'].replace(-1, np.nan)
df['categoria'] = df['categoria'].replace('N/A', np.nan)

df['preco'] = df['preco'].fillna(df['preco'].median())
df['quantidade'] = df['quantidade'].fillna(df['quantidade'].mean())
df['categoria'] = df['categoria'].fillna(df['categoria'].mode()[0])

# Usei os mesmos do ex. 4

print(df)
"""
########################################################################
# NÍVEL 7-8: Manipulação
########################################################################

"""
7. Preenchimento por grupo (avançado)

# Calcule a mediana do preço por categoria
# Preencha os nulos de 'preco' usando a mediana da CATEGORIA correspondente
# Dica: use groupby + transform
"""
"""
df = df_exercicios.copy()

mediana = df.groupby('categoria')['preco'].transform('median') # n conhecia, dei uma pesquisada como funciona. Acredito ter entendido o básico

df['preco'] = df['preco'].fillna(mediana)

print(df)
"""
########################################################################
"""
8. Interpolação em série temporal

# Use o DataFrame original (com nulos)
# A coluna 'data' é uma série temporal
# Aplique interpolação linear nos valores de 'preco' e 'quantidade'
# Compare visualmente (opcional: plote o antes e depois)
"""
"""
df = df_exercicios.copy()

df['preco'] = df['preco'].replace(-999, np.nan)
df['quantidade'] = df['quantidade'].replace(-1, np.nan)

plt.figure(figsize=(16, 10))
plt.subplot(2, 2, 1)
plt.plot(df['data'], df['preco'], 'r--')
plt.title('Preço com NaN')

plt.subplot(2, 2, 2)
df['preco'] = df['preco'].interpolate()
plt.plot(df['data'], df['preco'], 'b--')
plt.title('Preço com .interpolate()')

plt.subplot(2, 2, 3)
plt.plot(df['data'], df['quantidade'], 'r--')
plt.title('Quantidade com NaN')

plt.subplot(2, 2, 4)
df['quantidade'] = df['quantidade'].interpolate()
plt.plot(df['data'], df['quantidade'], 'b--')
plt.title('Quantidade com .interpolate()')

plt.tight_layout()
plt.show()
"""
########################################################################
# NÍVEL 9-10: Desafios
########################################################################

"""
9. Análise completa de nulos (estratégia mista)

# Para o DataFrame abaixo (dados de vendas por região), crie uma estratégia PARA CADA COLUNA:
#
# regras_sugeridas = {
#     'vendas': 'interpolate',  # série temporal
#     'marketing': 'ffill',     # investimento se mantém
#     'funcionarios': 'mediana_por_regiao',
#     'regiao': 'moda',
#     'meta': 'media'
# }
#
# Implemente sua estratégia e justifique cada decisão com print()
"""
"""
df_desafio = pd.DataFrame({
    'mes': pd.date_range('2024-01-01', periods=12, freq='ME'),
    'regiao': ['Norte', 'Sul', 'Norte', 'Sul', 'Norte', 'Sul', 'Norte', 'Sul', 'Norte', 'Sul', 'Norte', 'Sul'],
    'vendas': [100, 120, None, 140, 160, None, 180, 200, None, 220, 240, 260],
    'marketing': [50, 55, None, None, 65, 70, None, 80, 85, None, 95, 100],
    'funcionarios': [5, 6, None, 8, 9, None, 11, 12, None, 14, 15, None],
    'meta': [110, 130, 150, 170, None, 190, 210, 230, 250, 270, 290, 310]
})

df = df_desafio.copy()

nulos_simples = {
    'regiao': df['regiao'].mode()[0],
    'meta': df['meta'].mean()
}

df = df.fillna(nulos_simples)

df['vendas'] = df['vendas'].interpolate()
df['marketing'] = df['marketing'].ffill()
df['funcionarios'] = df.groupby('regiao')['funcionarios'].transform(lambda x: x.fillna(x.median()))

print(df)

# Usei as recomendações, achei que ficaram muito boas! Decidi mesclar o dicionario com o coluna-coluna para testar.
"""
########################################################################

"""
10. DESAFIO FINAL: Pipeline de limpeza profissional

# Crie uma FUNÇÃO que recebe um DataFrame e retorna um DataFrame limpo
# A função deve:
# 1. Identificar colunas com >50% de nulos e dropar
# 2. Para colunas numéricas com poucos nulos: preencher com mediana
# 3. Para colunas categóricas: preencher com moda
# 4. Para colunas temporais: usar interpolate
# 5. Remover linhas que ficaram com algum nulo após as etapas
# 6. Retornar o DataFrame limpo E um dicionário com o relatório de transformações
#
# Teste no DataFrame abaixo
"""

df_sujo_completo = pd.DataFrame({
    'id': range(1, 101),
    'nome': [f'Cliente_{i}' for i in range(1, 101)],
    'idade': np.random.choice([np.nan, 25, 30, 35, 40], 100, p=[0.1, 0.3, 0.3, 0.2, 0.1]),
    'renda': np.random.choice([np.nan, 3000, 4000, 5000, 6000], 100, p=[0.15, 0.3, 0.3, 0.2, 0.05]),
    'cidade': np.random.choice(['SP', 'RJ', 'BH', 'POA', np.nan], 100, p=[0.3, 0.2, 0.2, 0.15, 0.15]),
    'data_cadastro': pd.date_range('2024-01-01', periods=100),
    'score': np.random.choice([np.nan, 1, 2, 3, 4, 5], 100, p=[0.1, 0.2, 0.2, 0.2, 0.15, 0.15]),
    'coluna_lixo': np.random.choice([np.nan, 'x', 'y', 'z'], 100, p=[0.8, 0.1, 0.05, 0.05])  # 80% nulo
})

def pipeline_limpeza(df):
    df_limpo = df.copy()
    relatorio = {}

    for coluna in df.columns:

        if df_limpo[coluna].dtype == 'str':
            df_limpo[coluna] = df_limpo[coluna].replace('nan', np.nan) # tive que fazer isso pq os NaN tava aparecendo como 'nan' n sei pq...

        pct_nulos = df_limpo[coluna].isnull().sum() / len(df_limpo)

        if pct_nulos > 0.5:
            df_limpo = df_limpo.drop(columns=[coluna])
            relatorio[coluna] = 'Dropada (>50% nulos)'
            continue

        if df_limpo[coluna].dtype in ['int64', 'float64']:
            if df_limpo[coluna].isnull().sum() != 0:
                df_limpo[coluna] = df_limpo[coluna].fillna(df_limpo[coluna].median())
                relatorio[coluna] = 'Valores nulos preenchidos com mediana'

        elif df_limpo[coluna].dtype == 'str':
            if df_limpo[coluna].isnull().sum() != 0:
                df_limpo[coluna] = df_limpo[coluna].fillna(df_limpo[coluna].mode()[0])
                relatorio[coluna] = 'Valores nulos preenchidos com moda'

        elif df_limpo[coluna].dtype == 'datetime64[us]':
            if df_limpo[coluna].isnull().sum() > 0:
                df_limpo[coluna] = df_limpo[coluna].interpolate()
                relatorio[coluna] = 'Aplicado interpolação linear'

        if df_limpo[coluna].isnull().sum() != 0:
            df_limpo = df_limpo.drop(coluna, axis=1)
            relatorio[coluna] = 'Dropada (sobrou nulos depois do tratamento)'

    return df_limpo, relatorio

df_limpo, relatorio = pipeline_limpeza(df_sujo_completo)

print(relatorio)

df_limpo.info()

# esse foi realmente desafiador, mas foi divertido de fazer! Tinha tempo que não trabalhava com funções.