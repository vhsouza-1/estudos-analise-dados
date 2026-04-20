"""
Bloco 3: Python para Dados
Módulo 1: Introdução ao Pandas
Aula 1: O que é Pandas?
Data: 20/04/2026
Objetivo: Entender o que é Pandas e como começar a usar
"""

# ==========================================
# 1. O QUE É PANDAS?
# ==========================================

print("="*50)
print("1. O QUE É PANDAS?")
print("="*50)

"""
Pandas é uma biblioteca do Python para análise de dados.

Ela fornece estruturas de dados fáceis de usar e ferramentas para:
- Ler dados de arquivos (CSV, Excel, JSON, etc.)
- Limpar e transformar dados
- Filtrar, agrupar, agregar, ordenar
- Analisar e visualizar

Pandas é a biblioteca MAIS IMPORTANTE para análise de dados em Python.
"""
# ==========================================
# 2. POR QUE USAR PANDAS?
# ==========================================

print("\n" + "="*50)
print("2. POR QUE USAR PANDAS?")
print("="*50)

"""
SEM PANDAS (usando listas e dicionários):
- Código longo e repetitivo
- Loops manuais para tudo
- Difícil fazer agrupamentos e agregações

COM PANDAS:
- Código curto e legível
- Operações em uma linha
- Ferramentas prontas para análise

Exemplo de diferença:

SEM PANDAS (cálculo da média de idades):
    idades = [25, 30, 22, 28, 35]
    soma = 0
    for idade in idades:
        soma += idade
    media = soma / len(idades)

COM PANDAS:
    import pandas as pd
    idades = pd.Series([25, 30, 22, 28, 35])
    media = idades.mean()
"""
# ==========================================
# 3. INSTALANDO O PANDAS
# ==========================================

print("\n" + "="*50)
print("3. INSTALANDO O PANDAS")
print("="*50)

"""
No terminal:

pip install pandas

OU (se usar Anaconda):

conda install pandas

Verificando instalação:
"""
try:
    import pandas as pd
    print(f'Pandas instalado! Versão: {pd.__version__}')
except ImportError:
    print('Pandas NÃO está instalado. Execute: pip install pandas')


# ==========================================
# 4. IMPORTANDO O PANDAS (CONVENÇÃO)
# ==========================================

print("\n" + "="*50)
print("4. IMPORTANDO O PANDAS")
print("="*50)

"""
A convenção padrão da comunidade é importar pandas como 'pd'
Isso encurta o nome e é usado em TODOS os projetos

import pandas as pd

Agora podemos usar pd.algo() em vez de pandas.algo()
"""

import pandas as pd

print(f'Pandas importado como "pd"')
print(f'Tipo do módulo: {type(pd)}')

# ==========================================
# 5. AS DUAS ESTRUTURAS PRINCIPAIS
# ==========================================

print("\n" + "="*50)
print("5. AS DUAS ESTRUTURAS PRINCIPAIS")
print("="*50)

"""
Pandas tem duas estruturas principais:

1. Series: 
   - Uma coluna de dados (como uma lista com índice)
   - Equivalente a uma coluna no Excel

2. DataFrame:
   - Uma tabela completa (múltiplas colunas)
   - Equivalente a uma planilha no Excel

Vamos ver exemplos simples (sem detalhes ainda):
"""

# Series (uma coluna)
print('\n--- Exemplo de Series ---')
nomes = pd.Series(['Ana', 'Bruno', 'Carla'])
print(nomes)
print(f'Tipo: {type(nomes)}')

# DataFrame (tabela completa)
print('\n--- Exemplo de DataFrame ---')
dados = pd.DataFrame({
    "nome": ["Ana", "Bruno", "Carla"],
    "idade": [25, 30, 22],
    "cidade": ["SP", "RJ", "BH"]
})
print(dados) # isso aqui é incrivel *0*
print(f'Tipo: {type(dados)}')

# ==========================================
# 6. PRIMEIRO CONTATO COM A DOCUMENTAÇÃO
# ==========================================

print("\n" + "="*50)
print("6. PRIMEIRO CONTATO COM A DOCUMENTAÇÃO")
print("="*50)

"""
Documentação oficial: https://pandas.pydata.org/docs/

Principais seções:
- Getting started: tutoriais para iniciantes
- API reference: todas as funções disponíveis # O que é API nesse contexto? Vejo muito isso em vários lugares, principalmente em alguns requisitos de vagas.
- Cookbook: exemplos de problemas comuns

No dia a dia, você vai usar muito:
- help(pd.algo) no Python
- Google + "pandas como fazer X"
- Stack Overflow # O que é isso? Também é um termo que vejo muito.
"""

# Como ver a documentação de uma função no Python
print("\n--- Ver documentação de uma função ---")
print("No Python, use help()")
print("Exemplo: help(pd.Series)")
print("(Descomente a linha abaixo para testar)")

# help(pd.Series)  # Descomente para ver

# ==========================================
# 7. EXEMPLO PRÁTICO (O QUE VEM POR AÍ)
# ==========================================

print("\n" + "="*50)
print("7. EXEMPLO PRÁTICO")
print("="*50)

"""
Vamos ver um exemplo do que você vai conseguir fazer com Pandas:

Ler um arquivo CSV:
    df = pd.read_csv('vendas.csv') # O que é esse df?

Ver as primeiras linhas:
    df.head()

Filtrar vendas acima de R$1000:
    df[df['preco'] > 1000]

Calcular total por produto:
    df.groupby('produto')['quantidade'].sum()

Isso em poucas linhas, sem loops manuais!
"""
# Exemplo com dados em memória (simulando um CSV)
print("\n--- Dados de vendas ---")
vendas = pd.DataFrame({
    "produto": ["celular", "fone", "celular", "notebook"],
    "quantidade": [10, 30, 5, 3],
    "preco": [1500, 200, 1500, 3500]
})
print(vendas)

print("\n--- Vendas acima de R$1000 (quantidade * preco) ---")
vendas_acima = vendas[vendas['quantidade'] * vendas['preco'] > 1000] # interessante, mas ainda meio confuso haha
print(vendas_acima)

print("\n--- Total por produto ---")
total_por_produto = vendas.groupby('produto')['quantidade'].sum()
print(total_por_produto)

# ==========================================
# 8. RESUMO
# ==========================================

print("\n" + "="*50)
print("8. RESUMO")
print("="*50)

"""
✅ Pandas: biblioteca para análise de dados em Python
✅ Instalação: pip install pandas (ou conda install pandas)
✅ Importação: import pandas as pd (convenção padrão)
✅ Series: uma coluna de dados
✅ DataFrame: tabela completa (múltiplas colunas)

📌 O que vem nas próximas aulas:
- Aula 2: Series em detalhes (criar, acessar, operar)
- Aula 3: DataFrame em detalhes (criar, visualizar, explorar)
"""
#############################################################
# EXERCÍCIOS - AULA 1
#############################################################
# NÍVEL 1-3: Aquecimento
#############################################################
"""
1. Verificando instalação

# Importe pandas como pd
# Mostre a versão instalada
"""
"""
import pandas as pd
print(pd.__version__)
"""
#############################################################
"""
2. Criando sua primeira Series
python

# Crie uma Series com os números de 1 a 5
# Mostre a Series
"""
"""
numeros = [n for n in range(1, 6)] # qual é mais comum:
numeros_serie = pd.Series(numeros) # esse jeito?
print(numeros_serie)

numeros_serie2 = pd.Series([6, 7, 8, 9, 10]) # ou esse jeito?
print(numeros_serie2)

print(pd.Series([11, 12, 13, 14, 15]))
"""
#############################################################
"""
3. Criando seu primeiro DataFrame
python

# Crie um DataFrame com duas colunas: "nome" e "idade"
# Adicione 3 linhas de dados
# Mostre o DataFrame
"""
"""
dados = pd.DataFrame({
    'nome': ['Ana', 'Bruno', 'Carla'],
    'idade': [25, 28, 23]
})

print(dados)

# Interessante que o DataFrame tem uma sintaxe diferente da Lista de Dicionários né, na verdade ele é um dicionário só, com as listas atreladas as chaves. Interessante, é mais legivel tbm

"""
#############################################################
# NÍVEL 4-6: Aplicação
#############################################################
"""
4. Entendendo a diferença

# Sem Pandas: calcule a média da lista [10, 20, 30, 40, 50]
# Com Pandas: crie uma Series e use .mean()
# Compare os resultados
"""
"""
numeros = [n*10 for n in range(1,6)]

print(f'Media sem pandas: {sum(numeros)/len(numeros)}')

print(f'Média com pandas: {pd.Series(numeros).mean()}')
"""
#############################################################
"""
5. Explorando a documentação

# Use help() para ver a documentação de pd.Series
# Anote (em comentário) 3 coisas que você aprendeu

# Dei uma lida la na documentação, ela é enorme hahaha deixa isso pra depois.
"""
#############################################################
"""
6. Criando dados para análise

# Crie um DataFrame com dados de 3 produtos:
# - produto, preco, quantidade
# Calcule o valor total (preco * quantidade) para cada produto
# Mostre o resultado
"""
dados = pd.DataFrame({
    'produto': ['fone', 'celular', 'notebook'],
    'preco': [100, 1000, 3000],
    'quantidade': [50, 10, 5]
})

print(dados)





























