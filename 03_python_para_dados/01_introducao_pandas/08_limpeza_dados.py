"""
Bloco 3: Python para Dados
Módulo 1: Introdução ao Pandas
Aula 8: Limpeza de Dados
Data: 24/04/2026
Objetivo: Aprender a limpar dados (duplicatas, tipos, rename, strings)
"""

import pandas as pd

# ==========================================
# 1. REMOVENDO DUPLICATAS (.drop_duplicates())
# ==========================================

print("="*50)
print("1. REMOVENDO DUPLICATAS")
print("="*50)

# Criando DataFrame com linhas duplicadas
df = pd.DataFrame({
    'nome': ['Ana', 'Bruno', 'Ana', 'Carla', 'Bruno', 'Ana'],
    'idade': [25, 30, 25, 22, 30, 25],
    'cidade': ['SP', 'RJ', 'SP', 'BH', 'RJ', 'SP']
})

print("DataFrame original:")
print(df)

# Identificar duplicatas
print("\n--- Linhas duplicadas? ---")
print(df.duplicated())  # True onde a linha é duplicada (primeira ocorrência é False)

print("\n--- Contagem de duplicatas ---")
print(f"Total de linhas duplicadas: {df.duplicated().sum()}")

# Remover duplicatas (mantém a primeira ocorrência)
print("\n--- drop_duplicates() (mantém primeira) ---")
df_sem_duplicatas = df.drop_duplicates()
print(df_sem_duplicatas)

# Remover duplicatas mantendo a última ocorrência
print("\n--- drop_duplicates(keep='last') (mantém última) ---")
print(df.drop_duplicates(keep='last'))

# Remover duplicatas baseado em colunas específicas
print("\n--- drop_duplicates(subset=['nome']) (apenas pela coluna nome) ---")
print(df.drop_duplicates(subset=['nome']))

# ==========================================
# 2. CONVERTENDO TIPOS (.astype())
# ==========================================

print("\n" + "="*50)
print("2. CONVERTENDO TIPOS")
print("="*50)

# Criando DataFrame com tipos misturados
df_tipos = pd.DataFrame({
    'idade': ['25', '30', '22', '28'],
    'preco': ['1500,50', '200,00', '3500,00', '50,90'],
    'ativo': ['1', '0', '1', '1']
})

print("DataFrame original:")
print(df_tipos)
print("\nTipos originais:")
print(df_tipos.dtypes)

# Converter string para int
print("\n--- Convertendo 'idade' para int ---")
df_tipos['idade'] = df_tipos['idade'].astype(int)
print(df_tipos['idade'])
print(f"Novo tipo: {df_tipos['idade'].dtypes}")

# Converter string com vírgula para float (precisa tratar antes)
print("\n--- Convertendo 'preco' (vírgula como decimal) ---")
# Primeiro trocar vírgula por ponto, depois converter
df_tipos['preco'] = df_tipos['preco'].str.replace(',', '.').astype(float)
print(df_tipos['preco'])

# Converter string '1'/'0' para booleano
print("\n--- Convertendo 'ativo' para booleano ---")
df_tipos['ativo'] = df_tipos['ativo'].astype(int).astype(bool) # ta errado chefe, esqueceu de converter de string para int primeiro.
print(df_tipos['ativo'])

print("\nDataFrame após conversões:")
print(df_tipos)
print("\nTipos finais:")
print(df_tipos.dtypes)

# ==========================================
# 3. RENOMEANDO COLUNAS (.rename())
# ==========================================

print("\n" + "="*50)
print("3. RENOMEANDO COLUNAS")
print("="*50)

df_rename = pd.DataFrame({
    'nm': ['Ana', 'Bruno', 'Carla'],
    'idade_anos': [25, 30, 22],
    'cidade_uf': ['SP', 'RJ', 'BH']
})

print("DataFrame original:")
print(df_rename)

# Renomear colunas com dicionário
print("\n--- Renomeando colunas ---")
df_rename = df_rename.rename(columns={
    'nm': 'nome',
    'idade_anos': 'idade',
    'cidade_uf': 'cidade'
})
print(df_rename)

# Renomear uma única coluna
df_rename = df_rename.rename(columns={'cidade': 'cidade_nome'})
print("\n--- Renomeando uma coluna ---")
print(df_rename)

# ==========================================
# 4. MANIPULANDO STRINGS (.str)
# ==========================================

print("\n" + "="*50)
print("4. MANIPULANDO STRINGS")
print("="*50)

df_strings = pd.DataFrame({
    'nome': ['ana', 'BRUNO', 'Carla', 'daniel  '],
    'email': [' ana@email.com ', 'BRUNO@EMAIL.COM', 'carla@email.com', 'daniel@email.com'],
    'telefone': ['(11)99999-9999', '(21)88888-8888', '(31)77777-7777', '(51)66666-6666']
})

print("DataFrame original:")
print(df_strings)

# lower() - converter para minúsculas
print("\n--- .str.lower() ---")
df_strings['nome'] = df_strings['nome'].str.lower()
print(df_strings['nome'])

# strip() - remover espaços extras
print("\n--- .str.strip() ---")
df_strings['nome'] = df_strings['nome'].str.strip()
print(df_strings['nome'])

# upper() - converter para maiúsculas
print("\n--- .str.upper() ---")
df_strings['email'] = df_strings['email'].str.upper().str.strip()
print(df_strings['email'])

# contains() - verificar se contém (retorna booleano)
print("\n--- .str.contains() ---")
tem_ana = df_strings['nome'].str.contains('ana')
print(f"Contém 'ana'? \n{tem_ana}")

# replace() - substituir
print("\n--- .str.replace() ---")
df_strings['telefone'] = df_strings['telefone'].str.replace('-', '')
print(df_strings['telefone'])

# ==========================================
# 5. EXEMPLOS PRÁTICOS
# ==========================================

print("\n" + "="*50)
print("5. EXEMPLOS PRÁTICOS")
print("="*50)

# Dados sujos (simulando um arquivo real)
df_sujo = pd.DataFrame({
    'Cliente': ['ana', 'bruno', 'ana', 'carla', 'bruno', 'daniel'],
    'Idade': ['25', '30', '25', '22', '30', '28'],
    'Valor_Compra': ['1.500,00', '200,00', '1.500,00', '50,00', '200,00', '120,00'],
    'Cidade': [' sp ', ' rj ', ' sp ', ' bh ', ' rj ', ' sp ']
})

print("Dados sujos:")
print(df_sujo)

# Passo a passo da limpeza

# 1. Remover duplicatas
df_limpo = df_sujo.drop_duplicates()
print("\n1. Após remover duplicatas:")
print(df_limpo)

# 2. Padronizar nomes (lowercase + strip)
df_limpo['Cliente'] = df_limpo['Cliente'].str.lower().str.strip()
print("\n2. Após padronizar nomes:")
print(df_limpo)

# 3. Converter idade para int
df_limpo['Idade'] = df_limpo['Idade'].astype(int)
print("\n3. Após converter idade para int:")
print(df_limpo)

# 4. Converter valor_compra para float
df_limpo['Valor_Compra'] = df_limpo['Valor_Compra'].str.replace('.', '').str.replace(',', '.').astype(float)
print("\n4. Após converter valor_compra para float:")
print(df_limpo)

# 5. Padronizar cidade (strip)
df_limpo['Cidade'] = df_limpo['Cidade'].str.strip().str.upper()
print("\n5. Após padronizar cidade:")
print(df_limpo)

# 6. Renomear colunas
df_limpo = df_limpo.rename(columns={
    'Cliente': 'cliente',
    'Idade': 'idade',
    'Valor_Compra': 'valor',
    'Cidade': 'cidade'
})
print("\n6. Após renomear colunas:")
print(df_limpo)

# ==========================================
# 6. RESUMO
# ==========================================

print("\n" + "="*50)
print("6. RESUMO")
print("="*50)

"""
✅ Remover duplicatas:
   - df.drop_duplicates() - remove linhas duplicadas
   - df.drop_duplicates(subset=['col']) - baseado em colunas específicas
   - df.duplicated() - identificar duplicatas (True/False)

✅ Converter tipos:
   - df['col'] = df['col'].astype(tipo) - converte para tipo (int, float, str, bool)
   - Cuidado: '1.500,00' → precisa tratar antes (replace)

✅ Renomear colunas:
   - df.rename(columns={'antigo': 'novo'})
   - Pode renomear uma ou várias colunas

✅ Métodos de string (.str):
   - .str.lower() / .str.upper() - maiúsculas/minúsculas
   - .str.strip() - remove espaços nas pontas
   - .str.contains() - verifica se contém substring
   - .str.replace() - substitui texto
   - .str.split() - divide string em lista

📌 Pipeline de limpeza comum:
   1. Remover duplicatas
   2. Padronizar textos (lower/upper/strip)
   3. Converter tipos
   4. Tratar valores nulos (aula anterior)
   5. Renomear colunas
"""
######################################################################
# EXERCÍCIOS - AULA 8
######################################################################

# Dados para os exercícios:

import pandas as pd

df = pd.DataFrame({
    'Nome': [' ana ', 'BRUNO', ' ana', 'carla', 'BRUNO', 'daniel'],
    'Idade': ['25', '30', '25', '22', '30', '28'],
    'Salario': ['3.500,00', '4.200,00', '3.500,00', '5.000,00', '4.200,00', '3.800,00'],
    'Cidade': ['sp', 'rj', 'sp', 'bh', 'rj', 'sp'],
    'Ativo': ['1', '1', '1', '0', '1', '1']
})

######################################################################
# NÍVEL 1-3: Aquecimento
######################################################################
"""
1. Identificando duplicatas

# Mostre o DataFrame
# Mostre quais linhas são duplicadas (.duplicated())
# Mostre quantas duplicatas existem
"""
"""
print(df)
print()
print(df.duplicated())
print(f'\nNúmeros de duplicatas do df: {df.duplicated().sum()}')
"""
######################################################################
"""
2. Removendo duplicatas

# Remova as linhas duplicadas (.drop_duplicates())
# Mostre o resultado
"""
"""
df_limpo = df.drop_duplicates().reset_index(drop=True) # pesquisei como faz pra reorganizar o index que tava me incomodando...
print(df_limpo)
"""
######################################################################
"""
3. Padronizando strings

# A coluna 'Nome' tem espaços extras e maiúsculas/minúsculas
# Use .str.strip() e .str.lower() para padronizar
# Mostre o resultado
"""
"""
df_limpo = df.copy()
df_limpo['Nome'] = df_limpo['Nome'].str.strip().str.lower()

print(df_limpo['Nome'])
"""
######################################################################
# NÍVEL 4-6: Aplicação
######################################################################
"""
4. Convertendo tipos

# Converta a coluna 'Idade' para int
# Converta a coluna 'Ativo' para bool (1=True, 0=False)
# Mostre os tipos após a conversão
"""
"""
df_limpo = df.copy()
df_limpo['Idade'] = df_limpo['Idade'].astype(int)
df_limpo['Ativo'] = df_limpo['Ativo'].astype(int).astype(bool)

print(df_limpo)
"""
######################################################################
"""
5. Convertendo salário (string com ponto e vírgula)

# A coluna 'Salario' está no formato '3.500,00'
# Faça: .str.replace('.', '').str.replace(',', '.').astype(float)
# Mostre o resultado
"""
"""
df_limpo = df.copy()
df_limpo['Salario'] = df_limpo['Salario'].str.replace('.', '').str.replace(',', '.').astype(float)

print(df_limpo)
"""
######################################################################
"""
6. Renomeando colunas

# Renomeie as colunas para:
# 'Nome' → 'nome'
# 'Idade' → 'idade'
# 'Salario' → 'salario'
# 'Cidade' → 'cidade'
# 'Ativo' → 'ativo'
"""
"""
df_limpo = df.rename(columns={
    'Nome': 'nome',
    'Idade': 'idade',
    'Salario': 'salario',
    'Cidade': 'cidade',
    'Ativo': 'ativo'
})

print(df_limpo)
"""
######################################################################
# NÍVEL 7-8: Manipulação
######################################################################
"""
7. Filtrando por string

# Mostre apenas as linhas onde a 'cidade' é 'sp'
# Mostre apenas as linhas onde o 'nome' contém 'ana'
"""
"""
df_limpo = df.rename(columns={
    'Nome': 'nome',
    'Idade': 'idade',
    'Salario': 'salario',
    'Cidade': 'cidade',
    'Ativo': 'ativo'
})

df_limpo['cidade'] = df_limpo['cidade'].str.strip().str.lower()
df_limpo['nome'] = df_limpo['nome'].str.strip().str.lower()

print('Linhas onde a cidade é sp: ')
print(df_limpo[df_limpo['cidade']=='sp'])

print('\nLinhas onde o "nome" contém "ana":')
print(df_limpo[df_limpo['nome'].str.contains('ana')])
"""
######################################################################
"""
8. Pipeline de limpeza completo

# Aplique todas as limpezas em sequência:
# 1. Remover duplicatas
# 2. Padronizar 'nome' (strip + lower)
# 3. Padronizar 'cidade' (lower)
# 4. Converter 'idade' para int
# 5. Converter 'salario' para float
# 6. Converter 'ativo' para bool
# 7. Renomear colunas para português sem maiúsculas
# Mostre o DataFrame final
"""
"""
# Vou renomear as colunas primeiro pq facilitar a escrita do script
# inclusive, quando faço isso, não preciso fazer .copy() pq o df_limpo = df.rename(...) ja cria uma copia, correto?

df_limpo = df.rename(columns={
    'Nome': 'nome',
    'Idade': 'idade',
    'Salario': 'salario',
    'Cidade': 'cidade',
    'Ativo': 'ativo'
})

df_limpo = df_limpo.drop_duplicates().reset_index(drop=True)

df_limpo['nome'] = df_limpo['nome'].str.strip().str.lower()
df_limpo['cidade'] = df_limpo['cidade'].str.lower()
df_limpo['idade'] = df_limpo['idade'].astype(int)
df_limpo['salario'] = df_limpo['salario'].str.replace('.','').str.replace(',','.').astype(float)
df_limpo['ativo'] = df_limpo['ativo'].astype(int).astype(bool)

print(df_limpo)
"""
######################################################################
# NÍVEL 9-10: Desafios
######################################################################
"""
9. Análise após limpeza

# Use o DataFrame limpo do exercício 8
# Calcule e mostre:
# - Média salarial
# - Salário máximo e mínimo
# - Quantidade de clientes ativos
# - Salário médio por cidade
"""
"""
df_limpo = df.rename(columns={
    'Nome': 'nome',
    'Idade': 'idade',
    'Salario': 'salario',
    'Cidade': 'cidade',
    'Ativo': 'ativo'
})

df_limpo = df_limpo.drop_duplicates().reset_index(drop=True)

df_limpo['nome'] = df_limpo['nome'].str.strip().str.lower()
df_limpo['cidade'] = df_limpo['cidade'].str.lower()
df_limpo['idade'] = df_limpo['idade'].astype(int)
df_limpo['salario'] = df_limpo['salario'].str.replace('.','').str.replace(',','.').astype(float)
df_limpo['ativo'] = df_limpo['ativo'].astype(int).astype(bool)

print(f'Média Salarial: R${df_limpo['salario'].mean():.2f}')

print(f'Maior salário: R${df_limpo['salario'].max():.2f}')

print(f'Menor salário: R${df_limpo['salario'].min():.2f}')

print(f'Quantidade de clientes ativos: {df_limpo['ativo'].count()}')

print('Salário médio por cidade: ')
salario_cidade = df_limpo.groupby('cidade')['salario'].mean().reset_index()
print(salario_cidade)
"""
######################################################################
"""
10. DESAFIO FINAL: Limpeza de dados reais (simulado)

# Dados com problemas reais
df_sujo = pd.DataFrame({
    'Cliente': ['Ana Silva', ' bruno santos ', 'Ana Silva', 'CARLA M. ', ' bruno santos ', 'Daniel'],
    'Idade': ['25', '30', '25', '22', '30', '28'],
    'Email': ['ana@email.com', 'BRUNO@EMAIL.COM', 'ana@email.com', 'carla@email.com', 'bruno@email.com', 'daniel@email.com'],
    'Telefone': ['119999-9999', '(21)88888-8888', '119999-9999', '(31)77777-7777', '(21)88888-8888', '519999-9999'],
    'Valor_Compra': ['R$ 1.500,00', 'R$ 200,00', 'R$ 1.500,00', 'R$ 50,00', 'R$ 200,00', 'R$ 120,00'],
    'Status': ['A', 'I', 'A', 'I', 'A', 'A']
})

# Tarefas:
# 1. Remover duplicatas
# 2. Padronizar nomes (strip, lower, remover espaços extras)
# 3. Extrair apenas números dos telefones (remover parênteses, hífen, espaços)
# 4. Converter Valor_Compra para float (remover 'R$ ', ponto, substituir vírgula)
# 5. Converter Status para booleano (A=True, I=False)
# 6. Criar uma coluna 'dominio_email' extraindo o domínio (@email.com)
# 7. Mostrar o DataFrame limpo
"""
df_sujo = pd.DataFrame({
    'Cliente': ['Ana Silva', ' bruno santos ', 'Ana Silva', 'CARLA M. ', ' bruno santos ', 'Daniel'],
    'Idade': ['25', '30', '25', '22', '30', '28'],
    'Email': ['ana@email.com', 'BRUNO@EMAIL.COM', 'ana@email.com', 'carla@email.com', 'bruno@email.com', 'daniel@email.com'],
    'Telefone': ['119999-9999', '(21)88888-8888', '119999-9999', '(31)77777-7777', '(21)88888-8888', '519999-9999'],
    'Valor_Compra': ['R$ 1.500,00', 'R$ 200,00', 'R$ 1.500,00', 'R$ 50,00', 'R$ 200,00', 'R$ 120,00'],
    'Status': ['A', 'I', 'A', 'I', 'A', 'A']
})

df = df_sujo.rename(columns={
    'Cliente': 'nome',
    'Idade': 'idade',
    'Email': 'email',
    'Telefone': 'telefone',
    'Valor_Compra': 'valor',
    'Status': 'ativo'
})

df['nome'] = df['nome'].str.strip().str.lower()
df['telefone'] = df['telefone'].str.replace('(','').str.replace(')', '').str.replace('-', '').str.replace('(', '').astype(int)
df['valor'] = df['valor'].str.replace('R$ ', '').str.replace('.', '').str.replace(',', '.').astype(float)
df['ativo'] = df['ativo'].str.replace('A', '1').str.replace('I', '0').astype(int).astype(bool)
df['email'] = df['email'].str.strip().str.lower()
df['dominio_email'] = ['@'+dominio for nome, dominio in df['email'].str.split('@')]

df = df.drop_duplicates(subset=['nome', 'idade', 'email', 'telefone']) # fui pesquisar e descobri isso. Antes tava com uma duplicata do Bruno que diferia só na coluna status.

print(df.to_string())



