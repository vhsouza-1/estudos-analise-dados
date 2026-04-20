"""
Bloco 3: Python para Dados (É BLOCO 3 PARA DE ESCREVER BLOCO 2 POR FAVOR)
Módulo 1: Introdução ao Pandas
Aula 3: DataFrame - Tabela completa
Data: 20/04/2026
Objetivo: Aprender a criar e manipular DataFrames
"""
import pandas as pd

# ==========================================
# 1. O QUE É UM DATAFRAME?
# ==========================================

print("="*50)
print("1. O QUE É UM DATAFRAME?")
print("="*50)

"""
Um DataFrame é uma tabela completa (como uma planilha do Excel):
- Tem linhas e colunas
- Cada coluna é uma Series
- Cada linha é um registro

Comparação:
- Series: uma coluna
- DataFrame: várias colunas (tabela completa)

Exemplo visual:

     nome    idade  cidade
0    Ana       25      SP
1  Bruno       30      RJ
2  Carla       22      BH

- Linhas: 0, 1, 2 (índices)
- Colunas: "nome", "idade", "cidade"
"""

# ==========================================
# 2. CRIANDO DATAFRAME A PARTIR DE DICIONÁRIO
# ==========================================

print("\n" + "="*50)
print("2. CRIANDO DATAFRAME A PARTIR DE DICIONÁRIO")
print("="*50)

# Jeito mais comum: dicionário onde chave = nome da coluna, valor = lista de valores

print(f'DataFrame a partir de dicionário: ')
dados = {
    "nome": ["Ana", "Bruno", "Carla", "Daniel"],
    "idade": [25, 30, 22, 28],
    "cidade": ["SP", "RJ", "BH", "POA"]
}
df = pd.DataFrame(dados)
print(df)

# Cada coluna é uma Series
print(f'\nTipo da coluna "nome": {type(df['nome'])}')
print(f"Coluna 'nome' é uma Series:\n{df['nome']}")

# ==========================================
# 3. CRIANDO DATAFRAME A PARTIR DE LISTA DE LISTAS
# ==========================================

print("\n" + "="*50)
print("3. CRIANDO DATAFRAME A PARTIR DE LISTA DE LISTAS")
print("="*50)

print('DataFrame a partir de lista de listas:')
dados_linhas = [
    ["Ana", 25, "SP"],
    ["Bruno", 30, "RJ"],
    ["Carla", 22, "BH"],
    ["Daniel", 28, "POA"]
]
colunas = ['nome', 'idade', 'cidade']
df2 = pd.DataFrame(dados_linhas, columns=colunas)
print(df2)

# ==========================================
# 4. VISUALIZANDO DADOS
# ==========================================

print("\n" + "="*50)
print("4. VISUALIZANDO DADOS")
print("="*50)

# Criando um DataFrame maior para os exemplos
dados_vendas = {
    "produto": ["celular", "fone", "notebook", "mouse", "teclado", "celular", "fone"],
    "quantidade": [10, 30, 5, 100, 50, 8, 20],
    "preco": [1500, 200, 3500, 50, 120, 1500, 200],
    "vendedor": ["Ana", "Bruno", "Carla", "Ana", "Bruno", "Carla", "Ana"]
}
df_vendas = pd.DataFrame(dados_vendas)

print('DataFrame de vendas:')
print(df_vendas)

# .head() - primeiras 5 linhas (padrão)
print('\n.head() (primeiras 5 linhas)')
print(df_vendas.head())

# .head(3) - primeiras 3 linhas
print('\n.head(3) (primeiras 3 linhas)')
print(df_vendas.head(3))

# .tail() - últimas 5 linhas (padrão)
print('\n.tail() (últimas 5 linhas)')
print(df_vendas.tail())

# .tail(2) - últimas 2 linhas
print('\n.tail(2) (últimas 2 linhas)')
print(df_vendas.tail(2))

# ==========================================
# 5. INFORMAÇÕES BÁSICAS DO DATAFRAME
# ==========================================

print("\n" + "="*50)
print("5. INFORMAÇÕES BÁSICAS")
print("="*50)

# .info() - informações sobgre o DataFrase (tipos, valores não-nulos, etc.)

print('.info()')
print(df_vendas.info())

#  <class 'pandas.DataFrame'>
# RangeIndex: 7 entries, 0 to 6
# Data columns (total 4 columns):
#  #   Column      Non-Null Count  Dtype
# ---  ------      --------------  -----
#  0   produto     7 non-null      str
#  1   quantidade  7 non-null      int64
#  2   preco       7 non-null      int64
#  3   vendedor    7 non-null      str
# dtypes: int64(2), str(2)
# memory usage: 356.0 bytes
# None # o que é esse None?

# apareceu desse jeito, parece que o Non-Null com o Count ta trocado, né?

# .shape - dimensões (linhas x colunas)
print('.shape:')
print(f'Linhas: {df_vendas.shape[0]}')
print(f'Colunas: {df_vendas.shape[1]}')
print(f'Formato: {df_vendas.shape}')

# .columns - nome das colunas
print('\n.columns')
print(df_vendas.columns)

# .index - índices das linhas
print('\n .index: ')
print(df_vendas.index)

# ==========================================
# 6. RESUMO ESTATÍSTICO
# ==========================================

print("\n" + "="*50)
print("6. RESUMO ESTATÍSTICO")
print("="*50)

# .describe() - estatísticas das colunas numéricas
print('.describe(): ')
print(df_vendas.describe())

# .describe(include='all') - inclui colunas não numéricas
print('\n.describe(include=all)')
try:
    print(df_vendas.describe(include=all))
except Exception as e:
    print(e)

# ==========================================
# 7. SELECIONANDO COLUNAS
# ==========================================

print("\n" + "="*50)
print("7. SELECIONANDO COLUNAS")
print("="*50)

# Selecionar uma coluna (retorna Series)
print('Uma coluna (Series)')
produtos = df_vendas['produto'] # como o df é um "tipo" de dicionário, quando eu uso essa estrutura de dict ele me volta aquela lista que esta associada à chave. E como as Series são de certa forma uma lista, então ela já é interpretada nesse formato.
print(produtos)
print(f'Tipo: {type(produtos)}')

# Selectionar múltiplas colunas (retorna DataFrame)
print(f'Múltiplas colunas (DataFrame)')
subset = df_vendas[['produto', 'preco']]
print(subset)
print(f'Tipo: {type(subset)}')

# ==========================================
# 8. ADICIONANDO NOVAS COLUNAS
# ==========================================

print("\n" + "="*50)
print("8. ADICIONANDO NOVAS COLUNAS")
print("="*50)

# Adicionar uma coluna com valores fixos
df_vendas['desconto'] = 0.10
print('Adicionando coluna "desconto"')
print(df_vendas.head())

# Adicionar coluna calculada a partir de outras colunas
df_vendas['total'] = df_vendas['quantidade'] * df_vendas['preco']
print('Adicionando coluna "total" (quantidade * preco)')
print(df_vendas.head())

# Adicionar coluna condicional
df_vendas['venda_grande'] = df_vendas['quantidade'] > 50 # Tem como eu transformar isso aqui em "Sim" ou "Não"?
print(f'Adicionando coluna venda_grande (quantidade > 50)')
print(df_vendas.head())

# ==========================================
# 9. EXEMPLOS PRÁTICOS
# ==========================================

print("\n" + "="*50)
print("9. EXEMPLOS PRÁTICOS")
print("="*50)

# 9.1. Analisando dados de alunos
print("\n--- Análise de alunos ---")
alunos = pd.DataFrame({
    "nome": ["Ana", "Bruno", "Carla", "Daniel", "Eduarda"],
    "nota1": [8.5, 7.0, 9.0, 5.5, 8.0],
    "nota2": [7.0, 6.5, 8.5, 6.0, 7.5],
    "nota3": [9.0, 7.0, 9.5, 5.0, 8.5]
})

alunos['media'] = (alunos['nota1'] + alunos['nota2'] + alunos['nota3'])/3
print(f'Médias:\n{alunos[['nome', 'media']]}')

# Adicionar coluna de status
alunos['status'] = alunos['media'].apply(lambda x: 'Aprovado' if x >= 7 else 'Reprovado') # O que é esse apply??
print(f"\nStatus:\n{alunos[['nome', 'media', 'status']]}")

# 9.2 Filtrando linhas (introdução)
print('Aprovados: ')
aprovados = alunos[ alunos['status'] == 'Aprovado' ]
print(aprovados)

# 9.3 Ordenando dados
print('--- Alunos ordenados por média (decrescente): ')
alunos_ordenados = alunos.sort_values('media', ascending=False) # O que é esse sort_values??? Me lembrou o Order by...
print(alunos_ordenados)

# ==========================================
# 10. RESUMO
# ==========================================

print("\n" + "="*50)
print("10. RESUMO")
print("="*50)

"""
✅ DataFrame: tabela completa (várias colunas)
✅ Criar: pd.DataFrame(dicionario) ou pd.DataFrame(lista, columns=...)
✅ .head(n): primeiras n linhas
✅ .tail(n): últimas n linhas
✅ .info(): informações sobre tipos e valores nulos
✅ .shape: (linhas, colunas)
✅ .columns: nomes das colunas
✅ .describe(): estatísticas das colunas numéricas
✅ df["coluna"]: seleciona uma coluna (retorna Series)
✅ df[["col1", "col2"]]: seleciona múltiplas colunas (retorna DataFrame)
✅ df["nova"] = valores: adiciona nova coluna
✅ df["nova"] = df["col1"] * df["col2"]: coluna calculada
"""
##################################################################
# EXERCÍCIOS - AULA 3
##################################################################
# NÍVEL 1-3: Aquecimento
##################################################################
"""
1. Criando DataFrame a partir de dicionário

# Crie um DataFrame com os dados:
# nome: Ana, Bruno, Carla
# idade: 25, 30, 22
# cidade: SP, RJ, BH
# Mostre o DataFrame
"""
"""
dados = pd.DataFrame({
    'nome': ['Ana', 'Bruno', 'Carla'],
    'idade': [25, 30, 22],
    'cidade': ['SP', 'RJ', 'BH']
})
print(dados)
"""
##################################################################
"""
2. Visualizando dados

# Use o DataFrame do exercício 1
# Mostre:
# - As primeiras 2 linhas (.head(2))
# - As últimas 2 linhas (.tail(2))
"""
"""
dados = pd.DataFrame({
    'nome': ['Ana', 'Bruno', 'Carla'],
    'idade': [25, 30, 22],
    'cidade': ['SP', 'RJ', 'BH']
})

print(dados.head(2))
print()
print(dados.tail(2))
"""
##################################################################
"""
3. Informações básicas

# Use o DataFrame do exercício 1
# Mostre:
# - O formato (.shape)
# - Os nomes das colunas (.columns)
"""
"""
dados = pd.DataFrame({
    'nome': ['Ana', 'Bruno', 'Carla'],
    'idade': [25, 30, 22],
    'cidade': ['SP', 'RJ', 'BH']
})

print(dados.shape)
print()
print(dados.columns)
"""
##################################################################
# NÍVEL 4-6: Aplicação
##################################################################
"""
4. Selecionando colunas

# Use o DataFrame do exercício 1
# Selecione e mostre:
# - Apenas a coluna "nome" (como Series)
# - As colunas "nome" e "idade" (como DataFrame)
"""
"""
dados = pd.DataFrame({
    'nome': ['Ana', 'Bruno', 'Carla'],
    'idade': [25, 30, 22],
    'cidade': ['SP', 'RJ', 'BH']
})

print(dados['nome'])
print(dados[['nome', 'idade']])
"""
##################################################################
"""
5. Resumo estatístico

# Crie um DataFrame com dados de produtos:
# produto: celular, fone, notebook, mouse, teclado
# preco: 1500, 200, 3500, 50, 120
# quantidade: 10, 30, 5, 100, 50
#
# Use .describe() para ver as estatísticas das colunas numéricas
"""
"""
estoque = pd.DataFrame({
    'produto': ['celular', 'fone', 'notebook', 'mouse', 'teclado'],
    'preco': [1500, 200, 3500, 50, 120],
    'quantidade': [10, 30, 5, 100, 50]
})
print(estoque.describe())
"""
##################################################################
"""
6. Adicionando colunas

# Use o DataFrame do exercício 5
# Adicione as colunas:
# - "total" (preco * quantidade)
# - "desconto_10" (preco * 0.9)
# Mostre o DataFrame resultante
"""
"""
estoque = pd.DataFrame({
    'produto': ['celular', 'fone', 'notebook', 'mouse', 'teclado'],
    'preco': [1500, 200, 3500, 50, 120],
    'quantidade': [10, 30, 5, 100, 50]
})

estoque['total'] = estoque['quantidade'] * estoque['preco']
estoque['desconto_10'] = estoque['preco'] * 0.9

print(estoque)
"""
##################################################################
# NÍVEL 7-8: Manipulação
##################################################################
"""
7. Coluna condicional

# Use o DataFrame do exercício 5
# Adicione uma coluna "categoria" com:
# - "Caros" se preco > 1000
# - "Médios" se 100 <= preco <= 1000
# - "Baratos" se preco < 100
# Mostre o DataFrame com a nova coluna
"""
"""
estoque = pd.DataFrame({
    'produto': ['celular', 'fone', 'notebook', 'mouse', 'teclado'],
    'preco': [1500, 200, 3500, 50, 120],
    'quantidade': [10, 30, 5, 100, 50]
})

estoque['categoria'] = estoque['preco'].apply(lambda x: 'Caros' if x > 1000 else 'Medios' if 100 <= x <= 1000 else 'Baratos') # Me lembro o CASE WHEN do MySQL
print(estoque)
"""
##################################################################
"""
8. Filtrando linhas (introdução)

# Use o DataFrame do exercício 5
# Mostre:
# - Produtos com preco > 500
# - Produtos com quantidade > 20
# - Produtos com total > 1000
"""
"""
estoque = pd.DataFrame({
    'produto': ['celular', 'fone', 'notebook', 'mouse', 'teclado'],
    'preco': [1500, 200, 3500, 50, 120],
    'quantidade': [10, 30, 5, 100, 50]
})

estoque['total'] = estoque['quantidade'] * estoque['preco']

estoque1 = estoque[estoque['preco'] > 500]
estoque2 = estoque[estoque['quantidade'] > 20]
estoque3 = estoque[estoque['total'] > 1000]

print(estoque1)
print()
print(estoque2)
print()
print(estoque3)
"""
##################################################################
# NÍVEL 9-10: Desafios
##################################################################
"""
# Crie um DataFrame com dados de vendas (8 linhas):
# - vendedor: Ana, Bruno, Carla, Ana, Bruno, Carla, Ana, Bruno
# - produto: celular, fone, notebook, mouse, teclado, celular, fone, mouse
# - quantidade: 10, 30, 5, 100, 50, 8, 20, 30
# - preco: 1500, 200, 3500, 50, 120, 1500, 200, 50
#
# Calcule e mostre:
# - Total de vendas por vendedor (soma dos totais)
# - Produto mais vendido (em quantidade)
# - Produto com maior faturamento
"""
"""
df_vendas = pd.DataFrame({
    'vendedor': ['Ana', 'Bruno', 'Carla', 'Ana', 'Bruno', 'Carla', 'Ana', 'Bruno'],
    'produto': ['celular', 'fone', 'notebook', 'mouse', 'teclado', 'celular', 'fone', 'mouse'],
    'quantidade': [10, 30, 5, 100, 50, 8, 20, 30],
    'preco': [1500, 200, 3500, 50, 120, 1500, 200, 50]
})

df_vendas['total'] = df_vendas['quantidade'] * df_vendas['preco']

print(f'Total de vendas por vendedor: ')
print(df_vendas[['vendedor', 'total']])

print(f'\nQuantidade de vendas por produto: ')
print(df_vendas[['produto', 'quantidade']])

print(f'\nFaturamento por produto: ')
print(df_vendas[['produto', 'total']])

# Não da pra fazer todo o seu execicio pq eu preciso de algo pra fazer GROUP BY (agrupamento) e ainda não aprendemos.
"""
##################################################################
"""
10. DESAFIO FINAL: Relatório de alunos

# Crie um DataFrame com dados de 10 alunos:
# - nome (você escolhe)
# - nota1, nota2, nota3, nota4 (notas aleatórias entre 0 e 10)
#
# Calcule e mostre:
# - Média de cada aluno
# - Status (Aprovado se média >= 7, Recuperação se 5 <= média < 7, Reprovado se média < 5)
# - Média da turma
# - Quantos alunos foram aprovados
# - Quantos foram para recuperação
# - Quantos foram reprovados
# - O aluno com maior média
# - O aluno com menor média
#
# Extra: Mostre o relatório ordenado por média (do maior para o menor)
"""
df_alunos = pd.DataFrame({
    "nome": ["Ana", "Bruno", "Carla", "Daniel", "Eduarda", "Fernando", "Gabriela", "Henrique", "Isabela", "João"],
    "nota1": [8.5, 7.0, 9.0, 5.5, 8.0, 6.5, 9.5, 7.5, 6.0, 8.0],
    "nota2": [7.0, 6.5, 8.5, 6.0, 7.5, 7.0, 9.0, 8.0, 6.5, 7.5],
    "nota3": [9.0, 7.0, 9.5, 5.0, 8.5, 6.0, 9.5, 7.0, 7.0, 8.5],
    "nota4": [8.0, 8.0, 9.0, 6.5, 8.0, 7.5, 9.0, 8.5, 7.0, 7.0]
})

df_alunos['media'] = (df_alunos['nota1'] + df_alunos['nota2'] + df_alunos['nota3'] + df_alunos['nota4'])/4
df_alunos['status'] = df_alunos['media'].apply(lambda x: 'Aprovado' if x >= 7 else 'Recuperação' if 5 <= x < 7 else 'Reprovado')

print(f'Média da turma: {df_alunos['media'].mean():.2f}')

alunos_aprovados = df_alunos[df_alunos['status'] == 'Aprovado']
alunos_recuperacao = df_alunos[df_alunos['status'] == 'Recuperação']
alunos_reprovados = df_alunos[df_alunos['status'] == 'Reprovado']

print(f'Quantos alunos foram aprovados: {alunos_aprovados['nome'].count()}')
print(f'Quantos alunos foram para recuperação: {alunos_recuperacao['nome'].count()}')
print(f'Quantos alunos foram reprovados: {alunos_reprovados['nome'].count()}')

aluno_media = pd.Series(list(df_alunos['media']), index=list(df_alunos['nome'])) # gostou da criatividade? hahaha

print(f'Aluno com maior média: {aluno_media.idxmax()}')
print(f'Aluno com menor média: {aluno_media.idxmin()}')

df_alunos_ordenados = df_alunos.sort_values('media', ascending=False)
print(df_alunos_ordenados)