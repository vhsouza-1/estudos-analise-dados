"""
Bloco 3: Python para Dados
Módulo 1: Introdução ao Pandas
Aula 4: Leitura de Dados
Data: 21/04/2026
Objetivo: Aprender a ler arquivos com Pandas
"""
# Antes de começar, crie um arquivo vendas.csv na mesma pasta:

with open('vendas.csv', 'w', newline='') as f:
    f.write('produto,quantidade,preco,vendedor\n')
    f.write('celular,10,1500,Ana\n')
    f.write('fone,30,200,Bruno\n')
    f.write('notebook,5,3500,Carla\n')
    f.write('mouse,100,50,Ana\n')
    f.write('teclado,50,120,Bruno\n')

import pandas as pd

# ==========================================
# 1. POR QUE USAR PANDAS PARA LER ARQUIVOS?
# ==========================================

print("="*50)
print("1. POR QUE USAR PANDAS?")
print("="*50)

"""
SEM PANDAS (módulo csv):
    import csv
    with open('vendas.csv', 'r') as f:
        leitor = csv.DictReader(f)
        dados = list(leitor)
    # Depois precisa converter tipos manualmente

COM PANDAS:
    df = pd.read_csv('vendas.csv')
    # Já é um DataFrame! Tipos já estão corretos!

Vantagens do Pandas:
- Uma linha de código
- Já reconhece cabeçalho
- Infere tipos automaticamente
- Muito mais rápido para arquivos grandes
"""

# ==========================================
# 2. LENDO CSV COM pd.read_csv()
# ==========================================

print("\n" + "="*50)
print("2. LENDO CSV COM pd.read_csv()")
print("="*50)

# O básico: passar o nome do arquivo
df = pd.read_csv('vendas.csv')
print('DataFrame lido do CSV:')
print(df)

# Verificando os tipos inferidos automaticamente
print('\nTipos inferidos: ')
print(df.dtypes)

# .info() mostra as informações completas
print('\n.info(): ')
df.info()

# ==========================================
# 3. PARÂMETROS ÚTEIS DO read_csv()
# ==========================================

print("\n" + "="*50)
print("3. PARÂMETROS ÚTEIS")
print("="*50)

# 3.1 sep - separador (se não for vírgula)
print('sep= (separador)')
# Se o arquivo usasse ponto e vírgula: pd.read_csv('arquivo.csv', sep=';')

# 3.2. encoding - codificação (para arquivos com acentos)
print("--- encoding ---")
# pd.read_csv('arquivo.csv', encoding='utf-8')
# pd.read_csv('arquivo.csv', encoding='latin1')

# 3.3. header - qual linha é o cabeçalho (padrão é 0 = primeira linha)
print("--- header ---")
# Se o arquivo NÃO tem cabeçalho: pd.read_csv('arquivo.csv', header=None)
# Se o cabeçalho está na linha 2: pd.read_csv('arquivo.csv', header=1)

# 3.4. usecols - selecionar apenas algumas colunas
print('usecols (selecionar colunas): ')
df_colunas = pd.read_csv('vendas.csv', usecols=['produto', 'preco'])
print('Apenas colunas "produto" e "preco": ')
print(df_colunas)

# 3.5. nroes - ler apenas as primeiras N linhas
print('nrows (limitar linhas)')
df_3linhas = pd.read_csv('vendas.csv', nrows=3) # é a mesma coisa que fazer .head(3)?
print(f'Apenas as 3 primeiras linhas: ')
print(df_3linhas)

# ==========================================
# 4. LENDO CSV SEM CABEÇALHO
# ==========================================

print("\n" + "="*50)
print("4. LENDO CSV SEM CABEÇALHO")
print("="*50)

# Criando um arquivo sem cabeçalho para exemplo
with open('vendas_sem_cabecalho.csv', 'w') as f:
    f.write("celular,10,1500,Ana\n")
    f.write("fone,30,200,Bruno\n")
    f.write("notebook,5,3500,Carla\n")

# Lendo sem cabeçalho
df_sem_cabecalho = pd.read_csv('vendas_sem_cabecalho.csv', header=None)
print('Arquivo sem cabeçalho: ')
print(df_sem_cabecalho)

# Dando nomes as colunas
nomes_colunas = ['produto', 'quantidade', 'preco', 'vendedor']
df_com_nomes = pd.read_csv('vendas_sem_cabecalho.csv', header=None, names=nomes_colunas)
print('\nCom nomes de colunas: ')
print(df_com_nomes)

# ==========================================
# 5. LENDO EXCEL COM pd.read_excel()
# ==========================================

print("\n" + "="*50)
print("5. LENDO EXCEL COM pd.read_excel()")
print("="*50)

# Para ler Excel, precisa instalar: pip install openpyxl
# Vamos criar um arquivo Excel de exemplo (simulação - na prática você teria o arquivo)

print("Para ler Excel:")
print("df = pd.read_excel('arquivo.xlsx')")
print("df = pd.read_excel('arquivo.xlsx', sheet_name='Planilha1')")
print("df = pd.read_excel('arquivo.xlsx', sheet_name=0)  # primeira planilha")

# instalei!

df_excel = pd.read_excel('vendas_excel.xlsx')
print()
print(df_excel)

# ==========================================
# 6. COMPARANDO COM O MÓDULO CSV (REVISÃO)
# ==========================================

print("\n" + "="*50)
print("6. COMPARANDO COM O MÓDULO CSV")
print("="*50)

print("--- Módulo csv (sem Pandas) ---")
print("""
import csv
with open('vendas.csv', 'r') as f:
    leitor = csv.DictReader(f)
    dados = []
    for linha in leitor:
        linha['quantidade'] = int(linha['quantidade'])
        linha['preco'] = float(linha['preco'])
        dados.append(linha)
# 6 linhas de código, conversão manual
""")

print("\n--- Pandas ---")
print("""
df = pd.read_csv('vendas.csv')
# 1 linha, tipos já corretos!
""")

# ==========================================
# 7. EXEMPLOS PRÁTICOS
# ==========================================

print("\n" + "="*50)
print("7. EXEMPLOS PRÁTICOS")
print("="*50)

# 7.1 Lendo e analisando dados de vendas
print('Análise de vendas: ')
df_vendas = pd.read_csv('vendas.csv')

# Verificando os dados
print('Primeiras linhas: ')
print(df_vendas.head())

print('\nInformações: ')
df_vendas.info()

print('\nEstatísticas: ')
print(df_vendas.describe())

# 7.2 Calculando total de vendas
df_vendas['total'] = df_vendas['quantidade'] * df_vendas['preco']
print(f'\nFaturamento total: R${df_vendas['total'].sum():,.2f}')

# 7.3 Filtrando dados (já aprendemos)
print('\nVendas acima de R$1000: ')
vendas_acima = df_vendas[df_vendas['total']>1000]
print(vendas_acima)

# ==========================================
# 8. ONDE O ARQUIVO PRECISA ESTAR?
# ==========================================

print("\n" + "="*50)
print("8. ONDE O ARQUIVO PRECISA ESTAR?")
print("="*50)

"""
Caminhos possíveis:

1. Mesma pasta do script:
   df = pd.read_csv('vendas.csv')

2. Subpasta:
   df = pd.read_csv('dados/vendas.csv')

3. Caminho absoluto (não recomendado):
   df = pd.read_csv('C:/Users/usuario/documentos/vendas.csv')

4. Usando pathlib (recomendado para projetos):
   from pathlib import Path
   caminho = Path('dados') / 'vendas.csv'
   df = pd.read_csv(caminho)
"""
# ==========================================
# 9. TRATANDO ERROS (ARQUIVO NÃO ENCONTRADO)
# ==========================================

print("\n" + "="*50)
print("9. TRATANDO ERROS")
print("="*50)

try:
    df_erro = pd.read_csv('arquivo_que_n_existe.csv')
    print(df_erro)
except FileNotFoundError:
    print('Erro: Arquivo não encontrado')
except Exception as e:
    print(f'Erro inesperado: {e}')

# ==========================================
# 10. RESUMO
# ==========================================

print("\n" + "="*50)
print("10. RESUMO")
print("="*50)

"""
✅ pd.read_csv('arquivo.csv'): lê CSV para DataFrame
✅ pd.read_excel('arquivo.xlsx'): lê Excel para DataFrame

Parâmetros úteis do read_csv:
- sep=';' : separador (padrão é vírgula)
- encoding='utf-8' : codificação para acentos
- header=None : arquivo sem cabeçalho
- names=['col1','col2'] : nomes das colunas (com header=None)
- usecols=['col1','col2'] : selecionar apenas algumas colunas
- nrows=10 : ler apenas as primeiras 10 linhas

Vantagens do Pandas sobre csv módulo:
- Uma linha de código
- Tipos inferidos automaticamente
- Já é um DataFrame (pronto para análise)
- Muito mais rápido
"""
######################################################################
# EXERCÍCIOS - AULA 4
######################################################################
# NÍVEL 1-3: Aquecimento
######################################################################
"""
1. Lendo CSV básico

# Leia o arquivo "vendas.csv" usando pd.read_csv()
# Mostre o DataFrame
"""
"""
df_vendas = pd.read_csv('vendas.csv')
print(df_vendas)
"""
######################################################################
"""
2. Verificando os dados

# Use o DataFrame do exercício 1
# Mostre:
# - As primeiras 3 linhas (.head(3))
# - As informações (.info())
"""
"""
df_vendas = pd.read_csv('vendas.csv')

print(df_vendas.head(3))
print()
df_vendas.info()
"""
######################################################################
"""
3. Selecionando colunas na leitura

# Leia o arquivo "vendas.csv" usando apenas as colunas "produto" e "preco"
# Use o parâmetro usecols
"""
"""
df_vendas = pd.read_csv('vendas.csv', usecols=['produto', 'preco'])
print(df_vendas)
"""
######################################################################
# NÍVEL 4-6: Aplicação
######################################################################
"""
4. Limitando linhas

# Leia apenas as 3 primeiras linhas do arquivo "vendas.csv"
# Use o parâmetro nrows
"""
"""
df_vendas = pd.read_csv('vendas.csv', nrows=3)
print(df_vendas)
"""
######################################################################
"""
5. Lendo CSV sem cabeçalho

# Crie um arquivo "dados_sem_cabecalho.csv" com:
# 10,20,30
# 40,50,60
# 70,80,90
#
# Leia o arquivo sem cabeçalho (header=None)
# Dê nomes às colunas: "A", "B", "C" (use names)
"""
"""
_=1

with open('dados_sem_cabecalho.csv', 'w', newline='') as f:
    f.write('10,20,30\n')
    f.write('40,50,60\n')
    f.write('70,80,90\n')

df_dados_sem = pd.read_csv('dados_sem_cabecalho.csv', header=None)
print(df_dados_sem)
print('------')
nome_colunas = ['A', 'B', 'C']
df_dados_com = pd.read_csv('dados_sem_cabecalho.csv', header=None, names=nome_colunas)
print(df_dados_com)
"""
######################################################################
"""
6. Calculando a partir dos dados lidos

# Leia o arquivo "vendas.csv"
# Adicione uma coluna "total" (quantidade * preco)
# Mostre o faturamento total (soma da coluna total)
"""
"""
df_vendas = pd.read_csv('vendas.csv')

df_vendas['total'] = df_vendas['quantidade'] * df_vendas['preco']

print(f'Faturamento total: R${df_vendas['total'].sum():,.2f}')
"""
######################################################################
# NÍVEL 7-8: Manipulação
######################################################################
"""
7. Filtrando após leitura

# Leia o arquivo "vendas.csv"
# Mostre apenas as vendas do vendedor "Ana"
# Mostre apenas as vendas com quantidade > 20
"""
"""
df_vendas = pd.read_csv('vendas.csv')

df_vendas_ana = df_vendas[df_vendas['vendedor']=='Ana']

print(df_vendas_ana)

"""
######################################################################
"""
8. Criando um resumo

# Leia o arquivo "vendas.csv"
# Calcule e mostre:
# - Preço médio dos produtos
# - Quantidade total vendida
# - Faturamento total
# - Quantas vendas cada vendedor fez (conte as linhas por vendedor)
"""
"""
df_vendas = pd.read_csv('vendas.csv')

df_vendas['total'] = df_vendas['quantidade'] * df_vendas['preco']

preco_medio = df_vendas['total'].sum()/df_vendas['quantidade'].sum()

print(f'Preço médio dos produtos: R${preco_medio:,.2f}')
print(f'Quantidade total vendida: {df_vendas['quantidade'].sum()}')
print(f'Faturamento total: R${df_vendas['total'].sum():,.2f}')

df_vendas_vendedor = df_vendas[['quantidade', 'vendedor']]

print(df_vendas_vendedor) # ainda n aprendemos agrupamento no pandas, então vou deixar assim.
"""
######################################################################
# NÍVEL 9-10: Desafios
######################################################################
"""
9. Analisando dados reais (simulado)

# Crie um arquivo "funcionarios.csv" com:
# nome,idade,salario,departamento
# Ana,25,4500,Vendas
# Bruno,30,6200,TI
# Carla,22,4800,Vendas
# Daniel,41,3800,RH
# Eduarda,29,5800,TI
# Felipe,33,4700,Vendas
#
# Leia o arquivo e mostre:
# - Média salarial por departamento
# - Funcionário mais velho de cada departamento
# - Salário total por departamento
# - Quantos funcionários em cada departamento
"""
_=1

with open('funcionarios.csv', 'w', newline='') as f:
    f.write('nome,idade,salario,departamento\n')
    f.write('Ana,25,4500,Vendas\n')
    f.write('Bruno,30,6200,TI\n')
    f.write('Carla,22,4800,Vendas\n')
    f.write('Daniel,41,3800,RH\n')
    f.write('Eduarda,29,5800,TI\n')
    f.write('Felipe,33,4700,Vendas\n')

df_funcionarios = pd.read_csv('funcionarios.csv')

# mais um exercício que precisa de groupby para fazer. Acho que seu cerebrozinho ta começando a dar defeito ne? A memoria do chat ta acabando? Pode falar...

print(f'Média salarial total: {df_funcionarios['salario'].mean()}')
print(f'Funcionário mais velho: {df_funcionarios.loc[df_funcionarios['idade'].idxmax(), 'nome']}')
print(f'Salário total: {df_funcionarios['salario'].sum()}')
print(f'Quantos funcionários total: {len(df_funcionarios)}')
