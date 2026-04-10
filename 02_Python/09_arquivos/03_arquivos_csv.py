"""
Módulo 9: Manipulação de Arquivos
Aula 9.3: Arquivos CSV
Data: 10/04/2026
Objetivo: Aprender a ler e escrever arquivos CSV
"""
from collections import defaultdict
from csv import DictWriter

# ==========================================
# 1. EXPLICAÇÃO: O QUE É CSV?
# ==========================================

print("="*50)
print("1. O QUE É CSV?")
print("="*50)

"""
CSV = Comma-Separated Values (Valores Separados por Vírgula)

É o formato mais comum para troca de dados entre programas.
- Excel, Google Sheets, bancos de dados, etc. usam CSV
- Cada linha é um registro
- Cada coluna é separada por vírgula (ou ponto e vírgula)

Exemplo de arquivo CSV:
nome,idade,cidade
Ana,25,São Paulo
Bruno,30,Rio de Janeiro
Carla,22,Belo Horizonte

Linha 1: cabeçalho (nomes das colunas)
Linhas 2,3,4: dados
"""
# ==========================================
# 2. EXPLICAÇÃO: LENDO CSV COM csv.reader
# ==========================================

print("\n" + "="*50)
print("2. LENDO CSV COM csv.reader")
print("="*50)

# Primeiro, vamos criar um arquivo CSV de exemplo
with open("pessoas.csv", "w") as arquivo:
    arquivo.write("nome,idade,cidade\n")
    arquivo.write("Ana,25,São Paulo\n")
    arquivo.write("Bruno,30,Rio de Janeiro\n")
    arquivo.write("Carla,22,Belo Horizonte\n")

print("Arquivo 'pessoas.csv' criado com sucesso!")

# AGora vamos ler usando o módulo csv
import csv

print('\n--- Lendo CSV com csv.reader ---')
with open('pessoas.csv', 'r') as arquivo:
    leitor = csv.reader(arquivo) # cria um objeto leitor
    for linha in leitor:
        print(linha) # cada linha é uma lista de strings

# Entendendo o que aconteceu:
# - csv.reader transforma cada linha em uma lista
# - Os elementos são separados pela vírgula automaticamente

# ==========================================
# 3. EXPLICAÇÃO: ACESSANDO COLUNAS POR ÍNDICE
# ==========================================

print("\n" + "="*50)
print("3. ACESSANDO COLUNAS POR ÍNDICE")
print("="*50)

with open('pessoas.csv', 'r') as arquivo:
    leitor = csv.reader(arquivo)
    cabecalho = next(leitor) # pula a primeira linha (cabeçalho)
    print(f'Cabeçalho: {cabecalho}')

    for linha in leitor:
        nome = linha[0]      # primeira coluna
        idade = linha[1]     # segunda coluna
        cidade = linha[2]    # terceira coluna

        print(f'{nome} tem {idade} anos e mora em {cidade}')

# ==========================================
# 4. EXPLICAÇÃO: LENDO CSV COM DICTREADER (RECOMENDADO!)
# ==========================================

print("\n" + "="*50)
print("4. LENDO CSV COM csv.DictReader")
print("="*50)

"""
csv.DictReader é MELHOR porque:
- Usa o cabeçalho como chaves do dicionário
- Não precisa lembrar qual é o índice de cada coluna
- O código fica mais legível
"""

print('\n--- Lendo com DictReader ---')
with open('pessoas.csv', 'r') as arquivo:
    leitor = csv.DictReader(arquivo) # usa a primeira linha como chaves

    for linha in leitor:
        # linha é um dicionário!
        print(f'linha["nome"] = {linha["nome"]}')
        print(f'linha["idade"] = {linha["idade"]}')
        print(f'linha["cidade"] = {linha["cidade"]}')
        print('---')

# ==========================================
# 5. EXPLICAÇÃO: ESCREVENDO CSV COM csv.writer
# ==========================================

print("\n" + "="*50)
print("5. ESCREVENDO CSV COM csv.writer")
print("="*50)

# Dados para escrever
dados = [
    ["nome", "idade", "cidade"],  # cabeçalho
    ["Daniel", 28, "Porto Alegre"],
    ["Eduarda", 35, "Curitiba"],
    ["Felipe", 27, "Salvador"]
]

print('\n--- Escrevendo CSV com csv.writer ---')
with open('pessoas2.csv', 'w') as arquivo:
    escritor = csv.writer(arquivo)
    for linha in dados:
        escritor.writerow(linha)

print("Arquivo 'pessoas2.csv' criado!")

# Verificando o resultado
with open("pessoas2.csv", "r") as arquivo:
    print(arquivo.read())

# IMPORTANTE: newline="" evita linhas em branco extras no Windows

# ==========================================
# 6. EXPLICAÇÃO: ESCREVENDO CSV COM DICTWRITER
# ==========================================

print("\n" + "="*50)
print("6. ESCREVENDO CSV COM csv.DictWriter")
print("="*50)

# Dados como lista de dicionários (formato mais comum)
pessoas = [
    {"nome": "Gabriela", "idade": 29, "cidade": "Recife"},
    {"nome": "Henrique", "idade": 32, "cidade": "Fortaleza"},
    {"nome": "Isabela", "idade": 24, "cidade": "Manaus"}
]

print('--- Escrevendo CSV com DictWriter ---')

with open('pessoas3.csv', 'w', newline='') as arquivo:

    # Define os nomes das colunas (chaves dos dicionários)
    campos = ['nome', 'idade', 'cidade']
    escritor = csv.DictWriter(arquivo, fieldnames=campos)

    # Escreve o cabeçalho
    escritor.writeheader()

    # Escreve os dados (cada dicionário é uma linha)
    for pessoa in pessoas:
        escritor.writerow(pessoa)

print("Arquivo 'pessoas3.csv' criado!")

# Verificando
with open("pessoas3.csv", "r") as arquivo:
    print(arquivo.read())

"""
Explicação completa e decente que eu esperava:


1. O que faz newline=''?
python

with open('pessoas3.csv', 'w', newline='') as arquivo:

Resposta: Evita linhas em branco extras no arquivo CSV.
Sem newline='' (problema):
python

with open('teste.csv', 'w') as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(['a', 'b'])
    escritor.writerow(['c', 'd'])

# O arquivo pode ficar com linhas em branco entre os dados:
# a,b
#
# c,d

Com newline='' (correto):
python

with open('teste.csv', 'w', newline='') as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(['a', 'b'])
    escritor.writerow(['c', 'd'])

# O arquivo fica limpo:
# a,b
# c,d

Por que acontece? No Windows, escrever \n pode ser convertido para \r\n, criando linhas extras. newline='' desabilita essa conversão.
2. Por que especificar campos = [] se já são as chaves?
python

campos = ['nome', 'idade', 'cidade']  # parece redundante

Resposta: O DictWriter precisa saber a ordem das colunas. Dicionários não têm ordem garantida!
Exemplo do problema:
python

pessoa = {"nome": "Ana", "idade": 25, "cidade": "SP"}

# Dicionários podem aparecer em qualquer ordem:
print(list(pessoa.keys()))  # Pode ser ['nome', 'idade', 'cidade']
# ou ['cidade', 'nome', 'idade'] (depende da versão do Python)

Com fieldnames você controla a ordem:
python

campos = ['nome', 'idade', 'cidade']  # você decide a ordem!
# O CSV vai ficar: nome,idade,cidade

3. O que faz csv.DictWriter()?
python

escritor = csv.DictWriter(arquivo, fieldnames=campos)

Resposta: Cria um objeto que sabe escrever dicionários como linhas de CSV.
O que acontece internamente:
python

# DictWriter pega um dicionário e:
entrada = {"nome": "Ana", "idade": 25, "cidade": "SP"}
# Usa fieldnames para saber a ordem: ['nome', 'idade', 'cidade']
# Extrai os valores nessa ordem: ['Ana', 25, 'SP']
# Escreve como linha CSV: "Ana,25,SP\n"

4. O que faz writeheader()?
python

escritor.writeheader()

Resposta: Escreve a primeira linha do CSV com os nomes das colunas.
python

# writeheader() usa os fieldnames para escrever:
# "nome,idade,cidade\n"

Equivalente manual:
python

# As duas linhas fazem a MESMA coisa:
escritor.writeheader()  # jeito DictWriter

arquivo.write(','.join(campos) + '\n')  # jeito manual

5. O que faz writerow()?
python

escritor.writerow(pessoa)

Resposta: Escreve UMA linha (um dicionário) no CSV.
O que acontece:
python

pessoa = {"nome": "Gabriela", "idade": 29, "cidade": "Recife"}

# writerow pega os valores na ordem dos fieldnames:
# fieldnames = ['nome', 'idade', 'cidade']
# valores = ['Gabriela', 29, 'Recife']
# escreve: "Gabriela,29,Recife\n"

Visualização completa do processo

pessoas = [
    {"nome": "Gabriela", "idade": 29, "cidade": "Recife"},
    {"nome": "Henrique", "idade": 32, "cidade": "Fortaleza"},
    {"nome": "Isabela", "idade": 24, "cidade": "Manaus"}
]

# Passo a passo:
with open('pessoas3.csv', 'w', newline='') as arquivo:
    # 1. Define a ordem das colunas
    campos = ['nome', 'idade', 'cidade']
    
    # 2. Cria o escritor que entende dicionários
    escritor = csv.DictWriter(arquivo, fieldnames=campos)
    
    # 3. Escreve cabeçalho: "nome,idade,cidade"
    escritor.writeheader()
    
    # 4. Para cada dicionário, escreve uma linha
    for pessoa in pessoas:
        escritor.writerow(pessoa)

# Resultado no arquivo:
# nome,idade,cidade
# Gabriela,29,Recife
# Henrique,32,Fortaleza
# Isabela,24,Manaus

Tive que pegar a sua explicação e jogar em outro chat do deepseek e pedir pra ele me explicar. Complicado, né? "/ ...
"""
# ==========================================
# 7. EXPLICAÇÃO: PARÂMETRO newline=""
# ==========================================

print("\n" + "="*50)
print("7. PARÂMETRO newline=''")
print("="*50)

"""
Por que usar newline="" ao escrever CSV?

Sem newline="", o Python adiciona linhas em branco extras no Windows
entre cada linha do CSV. Isso acontece por causa de diferenças
entre sistemas operacionais.

SOLUÇÃO: SEMPRE use newline="" ao escrever CSV.
"""

# Exemplo do problema (no Windows):
# writer.writerow(linha) + quebra automática = linha em branco extra

# SOLUÇÃO:
# with open("arquivo.csv", "w", newline="") as arquivo:
#     escritor = csv.writer(arquivo)

# ==========================================
# 8. EXEMPLOS PRÁTICOS
# ==========================================

print("\n" + "="*50)
print("8. EXEMPLOS PRÁTICOS")
print("="*50)

# 8.1 Filtrando dados de um CSV
print("\n--- Filtrando pessoas com idade > 25 ---")
with open('pessoas.csv', 'r') as arquivo:
    leitor = csv.DictReader(arquivo)
    print('Pessoas com mais de 25 anos:')
    for pessoa in leitor:
        if int(pessoa['idade']) > 25:
            print(f'   {pessoa["nome"]} - {pessoa["idade"]} anos')

# 8.2. Calculando média de idades
print("\n--- Média de idades ---")

with open('pessoas.csv', 'r') as arquivo:
    leitor = csv.DictReader(arquivo)
    soma = 0
    contador = 0

    for pessoa in leitor:
        soma += int(pessoa['idade'])
        contador += 1

    media = soma/contador
    print(f'Média de idades: {media:.2f} anos')

# 8.3. Criando um CSV a partir de uma lista de dicionários
print("\n--- Criando CSV de produtos ---")
produtos = [
    {"produto": "Notebook", "preco": 3500, "estoque": 10},
    {"produto": "Mouse", "preco": 50, "estoque": 100},
    {"produto": "Teclado", "preco": 200, "estoque": 30}
]

with open('produtos.csv', 'w', newline='') as arquivo:

    campos = ['produto', 'preco', 'estoque']

    escritor = csv.DictWriter(arquivo, fieldnames=campos)

    escritor.writeheader()

    escritor.writerows(produtos) # writerows escreve vários de uma vez!

# ==========================================
# 9. RESUMO
# ==========================================

print("\n" + "="*50)
print("9. RESUMO")
print("="*50)

"""
✅ CSV: formato de dados separados por vírgula
✅ csv.reader: lê CSV como listas
✅ csv.DictReader: lê CSV como dicionários (RECOMENDADO)
✅ csv.writer: escreve CSV a partir de listas
✅ csv.DictWriter: escreve CSV a partir de dicionários (RECOMENDADO)
✅ newline="": SEMPRE use ao escrever CSV (evita linhas em branco extras)
✅ writerows(): escreve vários de uma vez

📌 Regras de ouro:
- Use DictReader/DictWriter - código mais legível
- Sempre use newline="" ao escrever CSV
- Os valores lidos são strings - converta quando necessário (int, float)
"""
##########################################################
# EXERCÍCIOS - AULA 9.3
##########################################################
# NÍVEL 1-3: Aquecimento
##########################################################
"""
1. Lendo CSV com csv.reader

# Crie um arquivo "alunos.csv" com:
# nome,nota
# Ana,8.5
# Bruno,6.0
# Carla,9.0
#
# Use csv.reader para ler e mostrar cada linha como lista
"""
"""
_ = 1

# Vou fazer com pessoas.csv pq o excel é complicadinho pra criar csv limpo

with open('pessoas.csv', 'r') as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        print(linha)
        
"""
##########################################################
"""
2. Lendo CSV com DictReader

# Use o mesmo arquivo "alunos.csv"
# Use csv.DictReader para ler e mostrar o nome e a nota de cada aluno
"""
"""
_ = 1

with open('pessoas.csv', 'r') as arquivo:
    leitor = csv.DictReader(arquivo)
    for aluno in leitor:
        print(f'{aluno["nome"]}: {aluno["idade"]}')
"""
##########################################################
"""
3. Escrevendo CSV com csv.writer

# Crie uma lista de listas com os dados:
# [["nome", "idade"], ["Ana", 25], ["Bruno", 30]]
# Use csv.writer para salvar em "dados.csv"
"""
"""
dados = [
    ["nome", "idade"],
    ["Ana", 25],
    ["Bruno", 30]
]

with open('dados.csv', 'w', newline='') as arquivo:

    escritor = csv.writer(arquivo)

    escritor.writerows(dados)
"""
##########################################################
# NÍVEL 4-6: Aplicação
##########################################################
"""
4. Escrevendo CSV com DictWriter

# Crie uma lista de dicionários com produtos:
# [{"produto": "celular", "preco": 1500}, {"produto": "fone", "preco": 200}]
# Use csv.DictWriter para salvar em "produtos.csv"
"""
"""
produtos = [
    {"produto": "celular", "preco": 1500},
    {"produto": "fone", "preco": 200}
]

with open('produtos.csv', 'r', newline='') as arquivo:

    campos = ['produto', 'preco']
    escritor = csv.DictWriter(arquivo, fieldnames=campos)

    escritor.writeheader()
"""
##########################################################
"""
5. Filtrando dados de um CSV

# Use o arquivo "pessoas.csv" da aula (nome,idade,cidade)
# Leia com DictReader e mostre apenas as pessoas da cidade "São Paulo"
"""
"""
_ = 1

with open('pessoas.csv', 'r') as arquivo:
    leitor = csv.DictReader(arquivo)

    print('Pessoas de São Paulo: ')
    for pessoa in leitor:
        if pessoa['cidade'] == 'São Paulo':
            print(f' - {pessoa["nome"]}')
"""
##########################################################
"""
6. Calculando média de um CSV

# Use o arquivo "alunos.csv" (nome,nota)
# Calcule e mostre:
# - A média das notas
# - O aluno com maior nota
# - O aluno com menor nota
"""
"""
_ = 1

# Vou usar produtos e calcular o preco medio

with open('produtos.csv', 'r') as arquivo:
    leitor = csv.DictReader(arquivo)
    soma_preco = 0
    contador = 0

    for produto in leitor:
        soma_preco += int(produto['preco'])
        contador += 1

    media = soma_preco/contador
    print(f'O preço médio dos produtos é: {media:.2f}')
"""
##########################################################
# NÍVEL 7-8: Manipulação
##########################################################
"""
7. Convertendo CSV para novo formato

# Leia o arquivo "pessoas.csv"
# Crie um novo arquivo "pessoas_maiores.csv" apenas com pessoas com idade >= 18
# Mantenha o mesmo formato (nome,idade,cidade)
"""
"""
_ = 1

with open('pessoas.csv', 'r') as arquivo:

    leitor = csv.DictReader(arquivo)

    dados = []

    for pessoa in leitor:
        if int(pessoa['idade']) >= 18:
            dados.append(pessoa)

print(dados)



with open('pessoas_maiores.csv', 'w', newline='') as arquivo:

    campos = [chave for chave in dados[0]]

    escritor = csv.DictWriter(arquivo, fieldnames=campos)

    escritor.writeheader()

    escritor.writerows(dados)
"""
##########################################################
"""
8. Adicionando coluna a um CSV

# Leia o arquivo "alunos.csv"
# Adicione uma coluna "status" com:
# - "Aprovado" se nota >= 7
# - "Reprovado" se nota < 7
# Salve em um novo arquivo "alunos_status.csv"
"""
"""
alunos = [
    {'nome': 'Ana', 'nota': 8.5},
    {'nome': 'Bruno', 'nota': 6},
    {'nome': 'Carla', 'nota': 9}
]

# Criei o csv "alunos.csv"

with open('alunos.csv', 'w', newline='') as arquivo:
    campos = ['nome', 'nota']
    escritor = csv.DictWriter(arquivo, fieldnames=campos)
    escritor.writeheader()
    escritor.writerows(alunos)

###########################################

with open('alunos.csv', 'r') as arq1:

    dados = []

    leitor = csv.DictReader(arq1)

    for aluno in leitor:
        if float(aluno['nota']) >= 7:
            aluno.update({'status': 'Aprovado'})
            dados.append(aluno)
        else:
            aluno.update({'status': 'Reprovado'})
            dados.append(aluno)

print(dados)

with open('alunos_status.csv', 'w', newline='') as arq2:
    campos = ['nome', 'nota', 'status']
    escritor = csv.DictWriter(arq2, fieldnames=campos)
    escritor.writeheader()
    escritor.writerows(dados)
"""
##########################################################
# NÍVEL 9-10: Desafios
##########################################################
"""
9. Mesclando dois CSVs

# Crie dois arquivos CSV:
# "alunos.csv" com: id,nome
# "notas.csv" com: id,nota
#
# Exemplo:
# alunos.csv:         notas.csv:
# 1,Ana               1,8.5
# 2,Bruno             2,6.0
# 3,Carla             3,9.0
#
# Crie um novo arquivo "relatorio.csv" com:
# id,nome,nota
# 1,Ana,8.5
# 2,Bruno,6.0
# 3,Carla,9.0
#
# Dica: use dicionários para fazer o merge
"""
"""
alunos = [
    {'id': 1, 'nome': 'Ana'},
    {'id': 2, 'nome': 'Bruno'},
    {'id': 3, 'nome': 'Carla'}
]

notas = [
    {'id': 1, 'nota': 8.5},
    {'id': 2, 'nota': 6},
    {'id': 3, 'nota': 9}
]

with open('alunos.csv', 'w', newline='') as arquivo:
    campos = ['id', 'nome']
    escritor = csv.DictWriter(arquivo, fieldnames=campos)
    escritor.writeheader()
    escritor.writerows(alunos)

with open('notas.csv', 'w', newline='') as arquivo:
    campos = ['id', 'nota']
    escritor = csv.DictWriter(arquivo, fieldnames=campos)
    escritor.writeheader()
    escritor.writerows(notas)

######################

with open('alunos.csv', 'r') as arquivo:
    alunos = []
    leitor = csv.DictReader(arquivo)
    for aluno in leitor:
        alunos.append(aluno)

with open('notas.csv', 'r') as arquivo:
    notas = []
    leitor = csv.DictReader(arquivo)
    for nota in leitor:
        notas.append(nota)

alunos_notas = [alunos[i] | notas[i] for i in range(len(alunos))] # que bom que vc indicou o merge. Consegui pesquisar o que era. (esse lc ficou elegante ne?)

with open('relatorio.csv', 'w', newline='') as arquivo:
    campos = [chave for chave in alunos_notas[0]]
    escritor = csv.DictWriter(arquivo, fieldnames=campos)
    escritor.writeheader()
    escritor.writerows(alunos_notas)
"""
##########################################################
"""
10. DESAFIO FINAL: Analisador de vendas CSV

# Crie um arquivo "vendas.csv" com:
# produto,quantidade,preco,vendedor
# celular,10,1500,Ana
# fone,30,200,Bruno
# celular,5,1500,Ana
# notebook,3,3500,Carla
# fone,15,200,Bruno
#
# Leia o arquivo e gere um relatório com:
# - Total de vendas por produto (quantidade * preco)
# - Total de vendas por vendedor
# - Produto mais vendido (em quantidade)
# - Vendedor com maior faturamento
#
# Salve o relatório em um arquivo "relatorio_vendas.csv"
"""
_ = 1

with open('vendas.csv', 'w') as arquivo:
    arquivo.write('produto,quantidade,preco,vendedor\n')
    arquivo.write('celular,10,1500,Ana\n')
    arquivo.write('fone,30,200,Bruno\n')
    arquivo.write('celular,5,1500,Ana\n')
    arquivo.write('notebook,3,3500,Carla\n')
    arquivo.write('fone,15,200,Bruno\n')

vendas = []

with open('vendas.csv', 'r') as arquivo:
    leitor = csv.DictReader(arquivo)
    for venda in leitor:
        vendas.append(venda)

faturamento_produto = defaultdict(float)
quantidade_vendedor = defaultdict(int)
quantidade_produto = defaultdict(int)
faturamento_vendedor = defaultdict(float)

for venda in vendas:
    produto = venda['produto']
    quantidade = int(venda['quantidade'])
    preco = float(venda['preco'])
    vendedor = venda['vendedor']

    faturamento_produto[produto] += preco * quantidade

    quantidade_vendedor[vendedor] += quantidade

    quantidade_produto[produto] += quantidade

    faturamento_vendedor[vendedor] += preco * quantidade

produto_maior_faturamento = max(faturamento_produto.items(), key=lambda x:x[1])
vendedor_maior_quantidade = max(quantidade_vendedor.items(), key=lambda x:x[1])
produto_maior_quantidade = max(quantidade_produto.items(), key=lambda x:x[1])
vendedor_maior_faturamento = max(faturamento_vendedor.items(), key=lambda x:x[1])


with open('relatorio_vendas.csv', 'w') as arquivo:

    arquivo.write('=== Faturamento por produto ===\n')
    arquivo.write(f'produto,faturamento\n')
    for produto, faturamento in faturamento_produto.items():
        arquivo.write(f'{produto},{faturamento}\n')
    arquivo.write(f'=====================================\n')
    arquivo.write(f'Produto com maior faturamento:,{produto_maior_faturamento[0]},{produto_maior_faturamento[1]}\n')
    arquivo.write(f'=====================================\n')

    arquivo.write('=== Quantidade por vendedor ===\n')
    arquivo.write(f'vendedor,quantidade\n')
    for vendedor, quantidade in quantidade_vendedor.items():
        arquivo.write(f'{vendedor},{quantidade}\n')
    arquivo.write(f'=====================================\n')
    arquivo.write(f'Vendedor com mais vendas:,{vendedor_maior_quantidade[0]},{vendedor_maior_quantidade[1]}\n')
    arquivo.write(f'=====================================\n')

    arquivo.write('=== Quantidade por produto ===\n')
    arquivo.write(f'produto,quantidade\n')
    for produto, quantidade in quantidade_produto.items():
        arquivo.write(f'{produto},{quantidade}\n')
    arquivo.write(f'=====================================\n')
    arquivo.write(f'Produto mais vendido:,{produto_maior_quantidade[0]},{produto_maior_quantidade[1]}\n')
    arquivo.write(f'=====================================\n')

    arquivo.write('=== Faturamento por vendedor ===\n')
    arquivo.write(f'vendedor,produto\n')
    for vendedor, faturamento in faturamento_vendedor.items():
        arquivo.write(f'{vendedor},{faturamento}\n')
    arquivo.write(f'=====================================\n')
    arquivo.write(f'Vendedor com maior faturamento:,{vendedor_maior_faturamento[0]},{vendedor_maior_faturamento[1]}\n')
    arquivo.write(f'=====================================\n')


