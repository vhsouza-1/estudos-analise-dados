"""
Bloco 3: Python para Dados
Módulo 1: Introdução ao Pandas
Aula 7: Tratamento de Valores Nulos
Data: 23/04/2026
Objetivo: Aprender a identificar e tratar valores nulos
"""

import pandas as pd
import numpy as np

# ==========================================
# 1. O QUE SÃO VALORES NULOS?
# ==========================================

print("="*50)
print("1. O QUE SÃO VALORES NULOS?")
print("="*50)

"""
Valores nulos representam dados faltantes/ausentes.

Em Python puro: None
Em Pandas: NaN (Not a Number) - importado do numpy

Quando aparecem?
- Dados não preenchidos em planilhas
- Erros na coleta de dados
- LEFT/RIGHT/OUTER merges sem correspondência
"""

# Criando um DataFrame com valores nulos
df = pd.DataFrame({
    'nome': ['Ana', 'Bruno', None, 'Daniel'],
    'idade': [25, None, 30, 22],
    'cidade': ['SP', 'RJ', None, 'BH']
})

print("DataFrame com valores nulos:")
print(df)

# ==========================================
# 2. IDENTIFICANDO VALORES NULOS
# ==========================================

print("\n" + "="*50)
print("2. IDENTIFICANDO VALORES NULOS")
print("="*50)

# .isnull() - retorna True onde o valor é nulo
print('.isnull(): ')
print(df.isnull())

# .isna() - é equivalente a .isnull()
print('.isna(): ')
print(df.isna())

# isnull().sum() - conta quantos nulos por coluna
print('\nContagem de nulos por coluna: ')
print(df.isnull().sum())

# is.null().sum().sum() - conta quanto nulos no DataFrame
print('\nTotal de nulos no DataFrame: ')
print(df.isnull().sum().sum())

# ==========================================
# 3. REMOVENDO VALORES NULOS (.dropna())
# ==========================================

print("\n" + "="*50)
print("3. REMOVENDO VALORES NULOS (.dropna())")
print("="*50)

print("Original:")
print(df)

# .dropna() - remove linhas com QUALQUER valor nulo
print('\n .dropna() (remove qualquer linha com nulo)')
df_sem_nulos = df.dropna()
print(df_sem_nulos)

# dropna(how='all') - remove apenas linhas com TODOS os valores nulos
print('\n .dropna(how="all") (remove só linhas totalmente nulas)')
df_todos_nulos = pd.DataFrame({
    'a': [1, None, None],
    'b': [2, None, None],
    'c': [3, None, None]
})
print("Original:")
print(df_todos_nulos)
print("\nApós dropna(how='all'):")
print(df_todos_nulos.dropna(how='all'))

# dropna(thresh=n) - remove linhas com menos de n valores não-nulos
print("\n--- dropna(thresh=2) (mantém linhas com pelo menos 2 não-nulos) ---")
print(df)
print("\nApós dropna(thresh=2):")
print(df.dropna(thresh=2))

# ==========================================
# 4. PREENCHENDO VALORES NULOS (.fillna())
# ==========================================

print("\n" + "="*50)
print("4. PREENCHENDO VALORES NULOS (.fillna())")
print("="*50)

print("Original:")
print(df)

# fillna(valor) - preenche todos os nulos com um valor
print('\nfillna("Desconhecido")')
print(df.fillna('Desconhecido'))

# Preenchendo colunas difrentes com valores diferentes
print('\nPreenchendo por coluna: ')
df_preenchido = df.copy()
df_preenchido['nome'] = df_preenchido['nome'].fillna('Desconhecido')
df_preenchido['idade'] = df_preenchido['idade'].fillna(0)
df_preenchido['cidade'] = df_preenchido['cidade'].fillna('Não informado')
print(df_preenchido)

# ==========================================
# 5. PREENCHENDO COM MÉDIA/MEDIANA/MODA
# ==========================================

print("\n" + "="*50)
print("5. PREENCHENDO COM MÉDIA/MEDIANA/MODA")
print("="*50)

df_idades = pd.DataFrame({
    'nome': ['Ana', 'Bruno', 'Carla', 'Daniel', 'Eduarda'],
    'idade': [25, None, 30, None, 28]
})

print("Original:")
print(df_idades)

# Preencher com a média
media_idade = round(df_idades['idade'].mean(), 1)
print(f'\nMédia das idades: {media_idade:.1f}')

df_media = df_idades.copy()
df_media['idade'] = df_media['idade'].fillna(media_idade)
print('\nPreenchido com a média:')
print(df_media)

# Preencher com a mediana (mais robusto para outliers)
mediana_idade = df_idades['idade'].median()
print(f'\nMediana das idades: {mediana_idade:.1f}')

df_mediana = df_idades.copy()
df_mediana['idade'] = df_mediana['idade'].fillna(mediana_idade)
print('\nPreenchido com a mediana:')
print(df_mediana)

# ==========================================
# 6. PREENCHENDO COM VALOR ANTERIOR/POSTERIOR
# ==========================================

print("\n" + "="*50)
print("6. PREENCHENDO COM VALOR ANTERIOR/POSTERIOR")
print("="*50)

df_series = pd.DataFrame({
    'dia': ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab', 'Dom'],
    'vendas': [100, None, None, 200, None, 300, None]
})

print("Original:")
print(df_series)

# method='ffill' (forward fill) - preenche com o valor anterior
print("\n--- ffill (valor anterior) ---")
# print(df_series.fillna(method='ffill'))

# method='bfill' (backward fill) - preenche com o próximo valor
print("\n--- bfill (próximo valor) ---")
# print(df_series.fillna(method='bfill'))

# ta errado mestre, é .ffill() e bfill() agora...

# ==========================================
# 7. EXEMPLOS PRÁTICOS
# ==========================================

print("\n" + "="*50)
print("7. EXEMPLOS PRÁTICOS")
print("="*50)

# Criando um DataFrame de exemplo com nulos
vendas = pd.DataFrame({
    'produto': ['celular', 'fone', 'notebook', 'mouse', 'teclado'],
    'quantidade': [10, None, 5, 100, 50],
    'preco': [1500, 200, None, 50, 120],
    'vendedor': ['Ana', 'Bruno', None, 'Ana', 'Bruno']
})

print("Dados de vendas com nulos:")
print(vendas)

# 1. Verificar quantos nulos existem
print(f"\nTotal de valores nulos: {vendas.isnull().sum().sum()}")

# 2. Remover linhas com nulos (se forem poucas)
vendas_limpo = vendas.dropna()
print("\n--- Removendo linhas com nulos ---")
print(vendas_limpo)

# 3. Preencher preços nulos com a média
media_preco = vendas['preco'].mean()
vendas['preco'] = vendas['preco'].fillna(media_preco)
print(f"\nPreços nulos preenchidos com média: {media_preco:.2f}")
print(vendas)

# 4. Preencher quantidades nulas com 0
vendas['quantidade'] = vendas['quantidade'].fillna(0)
print("\nQuantidades nulas preenchidas com 0:")
print(vendas)

# ==========================================
# 8. RESUMO
# ==========================================

print("\n" + "="*50)
print("8. RESUMO")
print("="*50)

"""
✅ Valores nulos: NaN (Pandas) / None (Python)

✅ Identificar nulos:
   - df.isnull() / df.isna() - True onde é nulo
   - df.isnull().sum() - contagem por coluna
   - df.isnull().sum().sum() - total de nulos

✅ Remover nulos:
   - df.dropna() - remove linhas com qualquer nulo
   - df.dropna(how='all') - remove só linhas totalmente nulas
   - df.dropna(thresh=n) - mantém linhas com pelo menos n não-nulos

✅ Preencher nulos:
   - df.fillna(valor) - preenche com valor fixo
   - df.fillna(method='ffill') - preenche com valor anterior
   - df.fillna(method='bfill') - preenche com próximo valor
   - df['col'] = df['col'].fillna(df['col'].mean()) - preenche com média

📌 Regras de ouro:
- Use dropna() quando poucos dados são nulos
- Use fillna() quando muitos dados são nulos
- Prefira mediana em vez de média para dados com outliers
"""
############################################################
# EXERCÍCIOS - AULA 7
############################################################
# Dados para os exercícios:

import pandas as pd
import numpy as np

df = pd.DataFrame({
    'nome': ['Ana', 'Bruno', 'Carla', 'Daniel', 'Eduarda', None],
    'idade': [25, None, 30, None, 28, 35],
    'salario': [5000, 4500, None, 6000, 5200, None],
    'cidade': ['SP', 'RJ', 'BH', None, 'SP', 'RJ']
})

############################################################
# NÍVEL 1-3: Aquecimento
############################################################
"""
1. Identificando nulos

# Mostre o DataFrame
# Mostre quantos valores nulos existem em cada coluna (use .isnull().sum())
"""
"""
print(df)
print(df.isnull().sum())
"""
############################################################
"""
2. Removendo nulos

# Remova todas as linhas que contêm QUALQUER valor nulo (.dropna())
# Mostre o resultado
"""
"""
print(df.dropna())
"""
############################################################
"""
3. Preenchendo nulos com valor fixo

# Preencha todos os valores nulos com a string "Desconhecido"
# Mostre o resultado
"""
"""
print(df.fillna('Desconhecido'))
"""
############################################################
# NÍVEL 4-6: Aplicação
############################################################
"""
4. Preenchendo colunas diferentes

# Preencha:
# - coluna 'nome' com "Anônimo"
# - coluna 'idade' com 0
# - coluna 'salario' com 0
# - coluna 'cidade' com "Não informado"
"""
"""
df_p = df.copy()
df_p['nome'] = df_p['nome'].fillna('Anônimo')
df_p['idade'] = df_p['idade'].fillna(0)
df_p['salario'] = df_p['salario'].fillna(0)
df_p['cidade'] = df_p['cidade'].fillna('Não informado')

print(df_p)
"""
############################################################
"""
5. Preenchendo com média

# Calcule a média da coluna 'idade'
# Preencha os valores nulos da coluna 'idade' com a média
"""
"""
media_idade1 = round(df['idade'].mean(), 1)

df_mi = df.copy()
df_mi['idade'] = df_mi['idade'].fillna(media_idade1)

print(f'Idade média: {media_idade1}')
print(df_mi)
"""
############################################################
"""
6. Removendo linhas com muitos nulos

# Remova apenas as linhas que têm mais de 2 valores nulos
# Dica: use .dropna(thresh=...)
"""
"""
print(df.dropna(thresh=2))
"""
############################################################
# NÍVEL 7-8: Manipulação
############################################################
"""
7. Preenchendo com mediana

# Calcule a mediana da coluna 'salario'
# Preencha os valores nulos da coluna 'salario' com a mediana
# Compare com o resultado usando média (qual é melhor para salários?)
"""
"""
mediana_salario = df['salario'].median()
media_salario = df['salario'].mean()

print(f'Mediana salário: {mediana_salario}')
print(f'Média salário: {media_salario}')
# nesse caso não muda muita coisa...

df_ms = df.copy()
df_ms['salario'] = df_ms['salario'].fillna(mediana_salario)

print(df_ms)
"""
############################################################
"""
8. Forward fill (preencher com valor anterior)

# Ordene o DataFrame por 'idade'
# Use method='ffill' para preencher os valores nulos com o valor anterior
# Mostre o resultado
"""
"""
df_ord = df.sort_values('idade')

print(df_ord.ffill())
"""
############################################################
# NÍVEL 9-10: Desafios
############################################################
"""
9. Limpeza completa de dados

# Faça uma limpeza completa do DataFrame:
# 1. Remova linhas onde 'nome' é nulo
# 2. Preencha 'idade' com a mediana das idades
# 3. Preencha 'salario' com a média dos salários
# 4. Preencha 'cidade' com a moda (valor mais frequente)
# Mostre o DataFrame limpo
"""
"""
df_limpo = df.copy()
df_limpo = df_limpo.dropna(subset='nome') # pesquisei pra descobrir como fazer, vc não passou...

df_limpo['idade'] = df_limpo['idade'].fillna(df_limpo['idade'].median())
df_limpo['salario'] = df_limpo['salario'].fillna(df_limpo['salario'].mean())
df_limpo['cidade'] = df_limpo['cidade'].fillna(df_limpo['cidade'].mode()[0]) # tive que pesquisar o .mode() tbm... descobri que tem que usar o [0] pq mode retorna uma serie.

print(df_limpo)
"""
############################################################
"""
10. DESAFIO FINAL: Análise de dados com nulos

# Dados de vendas (simulando um arquivo real)
vendas = pd.DataFrame({
    'produto': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
    'quantidade': [10, None, 30, None, 50, 20, None, 40],
    'preco': [100, 200, None, 400, 500, None, 700, 800],
    'categoria': ['X', 'Y', 'X', None, 'Y', 'X', None, 'Y']
})

# Responda:
# 1. Quantos valores nulos existem no total?
# 2. Qual coluna tem mais valores nulos?
# 3. Remova as linhas onde 'preco' é nulo
# 4. Preencha os nulos de 'quantidade' com a mediana
# 5. Preencha os nulos de 'categoria' com 'Não categorizado'
# 6. Mostre o DataFrame limpo
# 7. Calcule o faturamento total (quantidade * preco) após a limpeza
"""
vendas = pd.DataFrame({
    'produto': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
    'quantidade': [10, None, 30, None, 50, 20, None, 40],
    'preco': [100, 200, None, 400, 500, None, 700, 800],
    'categoria': ['X', 'Y', 'X', None, 'Y', 'X', None, 'Y']
})

print(f'Valor nulos ao total: {vendas.isnull().sum().sum()}')

print(f'Coluna com maior valores nulos: "{vendas.isnull().sum().idxmax()}"')

vendas_limpo = vendas.copy()
vendas_limpo = vendas_limpo.dropna(subset='preco')

vendas_limpo['quantidade'] = vendas_limpo['quantidade'].fillna(vendas_limpo['quantidade'].median())
vendas_limpo['categoria'] = vendas_limpo['categoria'].fillna('Não categorizado')

print('DataFrame limpo:')
print(vendas_limpo)

vendas_limpo['faturamento'] = vendas_limpo['quantidade'] * vendas_limpo['preco']

print('\nFaturamento por produto: ')
print(vendas_limpo[['produto', 'faturamento']])

print(f'\nFaturamento total: R${vendas_limpo['faturamento'].sum():,.2f}')