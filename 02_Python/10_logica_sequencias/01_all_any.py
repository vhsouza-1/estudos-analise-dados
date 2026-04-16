"""
Aula Extra: Funções de Lógica para Sequências
Data: 16/04/2026
Objetivo: Aprender all(), any() e operações relacionadas
"""
import csv
from collections import defaultdict

# ==========================================
# 1. ALL() - TODOS os itens devem ser True
# ==========================================

print("="*50)
print("1. ALL() - TODOS OS ITENS")
print("="*50)

# all() retorna True se TODOS os itens da sequência forem True
# Se algum for False, retorna False

lista1 = [True, True, True]
lista2 = [True, False, True]
lista3 = []

print(f'all([True, True, True]) = {all(lista1)}')
print(f'all([True, False, True]) = {all(lista2)}')
print(f"all([]) = {all(lista3)}") # vazio = True

# Exemplo prático: verificar se todos os números são positivos:
numeros = [10, 20, 30, 40]
todos_positivos = all(n > 0 for n in numeros)
print(f'\nTodos os números são positivos? {todos_positivos}')

numeros2 = [10, -5, 20, 30]
todos_positivos2 = all(n > 0 for n in numeros2)
print(f"Todos os números são positivos? {todos_positivos2}")

# Exemplo prático: verificar se todos os itens de uma lista são None:
lista_none = [None, None, None]
todos_none = all(item is None for item in lista_none)
print(f"\nTodos os itens são None? {todos_none}")

lista_mista = [None, 1, None]
todos_none2 = all(item is None for item in lista_mista)
print(f"Todos os itens são None? {todos_none2}")

# ==========================================
# 2. ANY() - ALGUM item deve ser True
# ==========================================

print("\n" + "="*50)
print("2. ANY() - ALGUM ITEM")
print("="*50)

# any() retorna True se PELO MENOS UM item for True
# Se todos forem False, retorna False

lista1 = [False, False, True]
lista2 = [False, False, False]
lista3 = []

print(f"any([False, False, True]) = {any(lista1)}")   # True
print(f"any([False, False, False]) = {any(lista2)}")  # False
print(f"any([]) = {any(lista3)}")                    # False (vazio = False)

# Exemplo prático: verificar se existe algum número negativo:
numeros = [10, 20, 30, -5]
algum_negativo = any(n < 0 for n in numeros)
print(f'Algum negativo? {algum_negativo}')

numeros2 = [10, 20, 30, 40]
tem_negativo2 = any(n < 0 for n in numeros2)
print(f"Existe número negativo? {tem_negativo2}")

# Exemplo prático: verificar se algum item é None (seu problema!)
lista = [1, 2, None, 3]
tem_none = any(item is None for item in lista)
print(f"\nExiste algum None? {tem_none}")

# ==========================================
# 3. CONTANDO QUANTOS ATENDEM (com sum())
# ==========================================

print("\n" + "="*50)
print("3. CONTANDO COM SUM()")
print("="*50)

# Em Python, True vale 1, False vale 0
# Então sum() de booleanos conta quantos são True

numeros = [10, -5, 20, -3, 30, 40, -1]

quantos_negativos = sum(n < 0 for n in numeros)
print(f'Quantos negativos? {quantos_negativos}')

quantos_positivos = sum(n > 0 for n in numeros)
print(f'Quantos positivos? {quantos_positivos}')

# Exemplo prático: contar quantos None em uma lista:
lista = [1, None, 2, None, 3, None]
quantos_none = sum(n is None for n in lista)
print(f'Quantos None? {quantos_none}')

# ==========================================
# 4. COMPARAÇÃO: all() vs any() vs sum()
# ==========================================

print("\n" + "="*50)
print("4. COMPARAÇÃO")
print("="*50)

dados = [10, 20, 30, 40]

# all(): todos são > 5?
print(f'Todos são > 5? {all(n > 5 for n in dados)}')

# any(): algum é > 35?
print(f'Algum é > 35? {any(n > 35 for n in dados)}')

# sum(): quantos são > 25?
print(f'Quantos são > 25? {sum(n > 25 for n in dados)}')

# ==========================================
# 5. EXEMPLOS PRÁTICOS (relacionados ao seu problema)
# ==========================================

print("\n" + "="*50)
print("5. EXEMPLOS PRÁTICOS")
print("="*50)

# 5.1. Validar se um CSV tem cabeçalho (todos os campos têm nome)
print("\n--- Validando cabeçalho do CSV ---")
# Simulando o que o DictReader faz quando uma linha não tem cabeçalho
linha_com_cabecalho = {"nome": "Ana", "idade": "25"}
linha_sem_cabecalho = {None: "Ana", None: "25"}  # DictReader usa None quando não há cabeçalho

# Verificar se tem cabeçalho (nenhuma chave é None)
tem_cabecalho = all(chave is not None for chave in linha_com_cabecalho.keys())
print(f"Linha com cabeçalho: {tem_cabecalho}")

tem_cabecalho2 = all(chave is not None for chave in linha_sem_cabecalho.keys())
print(f"Linha sem cabeçalho: {tem_cabecalho2}")

# 5.2. Verificar se algum campo está vazio
print("\n--- Verificando campos vazios ---")
registro = {"nome": "Ana", "idade": "", "cidade": "SP"}
algum_vazio = any(valor == "" for valor in registro.values())
print(f"Algum campo vazio? {algum_vazio}")

# 5.3. Verificar se todos os campos estão preenchidos
todos_preenchidos = all(valor != "" for valor in registro.values())
print(f"Todos preenchidos? {todos_preenchidos}")

# 5.4. Contar quantos campos estão vazios
quantos_vazios = sum(valor == "" for valor in registro.values())
print(f"Quantos campos vazios? {quantos_vazios}")

# ==========================================
# 6. RESUMO
# ==========================================

print("\n" + "="*50)
print("6. RESUMO")
print("="*50)

"""
✅ all(iterável): True se TODOS os itens forem True
   Ex: all(x > 0 for x in lista)

✅ any(iterável): True se ALGUM item for True
   Ex: any(x < 0 for x in lista)

✅ sum(iterável): conta quantos são True (True = 1, False = 0)
   Ex: sum(x < 0 for x in lista)  # conta negativos

📌 Padrões comuns:
- all(item is None for item in lista)  # todos são None?
- any(item is None for item in lista)  # algum é None?
- sum(item is None for item in lista)  # quantos são None?
- all(chave is not None for chave in dict.keys())  # dicionário tem cabeçalho?
"""
##############################################################
# EXERCÍCIOS - AULA EXTRA
##############################################################
# NÍVEL 1-3: Aquecimento
##############################################################
"""
. Verificando se todos são pares

# Dada a lista: numeros = [2, 4, 6, 8, 10]
# Use all() para verificar se todos são pares
"""
"""
numeros = [2, 4, 6, 8, 10]
todos_pares = all(n % 2 == 0 for n in numeros)

print(f'Todos pares? {todos_pares}')
"""
##############################################################
"""
2. Verificando se algum é negativo

# Dada a lista: numeros = [10, -5, 20, 30]
# Use any() para verificar se existe algum número negativo
"""
"""
numeros = [10, -5, 20, 30]
algum_negativo = any(n < 0 for n in numeros)
print(f'Algum negativo? {algum_negativo}')
"""
##############################################################
"""
3. Contando os positivos

# Dada a lista: numeros = [10, -5, 20, -3, 30]
# Use sum() para contar quantos números são positivos
"""
"""
numeros = [10, -5, 20, -3, 30]
quantos_positivos = sum(n > 0 for n in numeros)
print(f'Quantos positivos? {quantos_positivos}')
"""
##############################################################
# NÍVEL 4-6: Aplicação
##############################################################
"""
4. Validação de lista de números
python

# Dada a lista: notas = [8.5, 7.0, 9.0, 5.5, 6.0]
# Verifique:
# - Todas as notas são válidas (entre 0 e 10)?
# - Alguma nota é menor que 6?
# - Quantas notas são >= 7?
"""
"""
notas = [8.5, 7.0, 9.0, 5.5, 6.0]

todos_validas = all(0 <= n <= 10 for n in notas)
alguma_menor6 = any(n < 6 for n in notas)
quantas_maiori7 = sum(n >= 7 for n in notas)

print(f'Todas as notas são válidas (entre 0 e 10)?: {todos_validas}')
print(f'Alguma nota é menor que 6? {alguma_menor6}')
print(f'Quantas notas são >= 7? {quantas_maiori7}')
"""
##############################################################
"""
6. Validação de lista de dicionários

# Dada a lista de alunos:
alunos = [
    {"nome": "Ana", "nota": 8.5},
    {"nome": "Bruno", "nota": 6.0},
    {"nome": "", "nota": 9.0},  # nome vazio
    {"nome": "Daniel", "nota": 5.5}
]
# Verifique:
# - Todos os alunos têm nome não vazio?
# - Algum aluno tem nota >= 9?
# - Quantos alunos têm nota < 7?
"""
"""
alunos = [
    {"nome": "Ana", "nota": 8.5},
    {"nome": "Bruno", "nota": 6.0},
    {"nome": "", "nota": 9.0},  # nome vazio
    {"nome": "Daniel", "nota": 5.5}
]

todos_nome_n_vazio = all(aluno['nome'] != '' for aluno in alunos)
algum_nota_maior9 = any(aluno['nota'] >= 9 for aluno in alunos)
quantas_nota_menor7 = sum(aluno['nota'] < 7 for aluno in alunos)

print(f'Todos os alunos têm nome não vazio? {todos_nome_n_vazio}')
print(f'Algum aluno tem nota >= 9? {algum_nota_maior9}')
print(f'Quantos alunos têm nota < 7? {quantas_nota_menor7}')
"""
##############################################################
# NÍVEL 7-8: Manipulação
##############################################################
"""
7. Validação de CSV (simulado)
python

# Simulando a leitura de um CSV com DictReader
linhas = [
    {"nome": "Ana", "idade": "25"},
    {"nome": "Bruno", "idade": "30"},
    {None: "Carla", None: "22"}  # linha sem cabeçalho
]
# Para cada linha, verifique:
# - Se a linha tem cabeçalho válido (nenhuma chave é None)
# - Se a linha tem valores válidos (nenhum valor é string vazia)
"""
"""
linhas = [
    {"nome": "Ana", "idade": "25"},
    {"nome": "Bruno", "idade": "30"},
    {None: "Carla", None: "22"}  # linha sem cabeçalho
]

for i, linha in enumerate(linhas):
    cabecalho_valido = all(chave is not None for chave in linha.keys())
    valores_validos = all(valor != '' for valor in linha.values())

    print(f'Linha {i+1}:')
    print(f'  Tem cabeçalho válido: {cabecalho_valido}')
    print(f'  Tem valores válidos: {valores_validos}')
    print()
"""
##############################################################
"""
8. Validação de arquivo de configuração

# Dado o dicionário de configuração:
config = {
    "host": "localhost",
    "port": "",
    "user": "admin",
    "password": ""
}
# Verifique:
# - Todas as configurações obrigatórias estão preenchidas? (campos: host, port, user, password)
# - Quais campos estão vazios?
# - A configuração é válida? (host não vazio, port é número? - use .isdigit())
"""
"""
config = {
    "host": "localhost",
    "port": "",
    "user": "admin",
    "password": ""
}

print(f'Todas as configurações obrigatórias estão preenchidas? {all(campo != '' for campo in list(config.values()))}')

campos_vazios = []

for chave, valor in config.items():
    if not valor:
        campos_vazios.append(chave)

print(f'Campos vazios: {campos_vazios}')

config_valida = True if config['host'] != '' and config['port'].isdigit() else False

print(f'A configuração é válida? {config_valida}')
"""
##############################################################
# NÍVEL 9-10: Desafios
##############################################################
"""
9. Validador de dados complexo

# Dada a lista de produtos:
produtos = [
    {"nome": "celular", "preco": 1500, "quantidade": 10},
    {"nome": "fone", "preco": 200, "quantidade": 0},
    {"nome": "", "preco": -50, "quantidade": 5},  # nome vazio, preco negativo
    {"nome": "notebook", "preco": 3500, "quantidade": -3}  # quantidade negativa
]
# Crie uma função que valida cada produto e retorna:
# - produtos_validos: lista com produtos que passam em todas as validações
# - erros: dicionário com os erros encontrados (nome vazio, preco <= 0, quantidade < 0)
# Use all(), any(), sum() onde fizer sentido
"""
"""
produtos1 = [
    {"nome": "celular", "preco": 1500, "quantidade": 10},
    {"nome": "fone", "preco": 200, "quantidade": 0},
    {"nome": "", "preco": -50, "quantidade": 5},  # nome vazio, preco negativo
    {"nome": "notebook", "preco": 3500, "quantidade": -3}  # quantidade negativa
]

def validador(produtos):

    produtos_validados = []
    erros = defaultdict(list)

    for produto in produtos:
        nome = produto['nome']
        preco = produto['preco']
        quantidade = produto['quantidade']

        if not nome:
            erros[nome].append('nome vazio')

        if preco <= 0:
            erros[nome].append('preco negativo')

        if quantidade < 0:
            erros[nome].append('quantidade negativa')

        if nome not in erros.keys():
            produtos_validados.append(nome)

    return {'produtos_validados': produtos_validados, 'erros': dict(erros)}

print(validador(produtos1))
"""
##############################################################
"""
10. DESAFIO FINAL: Validador de CSV com relatório

# Simule a leitura de um arquivo CSV (use uma lista de dicionários)
dados = [
    {"nome": "Ana", "idade": "25", "cidade": "SP"},
    {"nome": "Bruno", "idade": "-5", "cidade": "RJ"},  # idade negativa
    {"nome": "Carla", "idade": "", "cidade": "BH"},    # idade vazia
    {"nome": "", "idade": "30", "cidade": "POA"},      # nome vazio
    {"nome": "Daniel", "idade": "abc", "cidade": "SP"} # idade não numérica
]
# Crie um relatório de validação que mostre:
# - Quantas linhas têm todos os campos válidos
# - Quantas linhas têm erro de nome (vazio)
# - Quantas linhas têm erro de idade (vazia, negativa ou não numérica)
# - Quantas linhas têm erro de cidade (vazia)
# - Lista dos índices das linhas com erro
# Use all(), any(), sum() para as contagens
"""
dados = [
    {"nome": "Ana", "idade": "25", "cidade": "SP"},
    {"nome": "Bruno", "idade": "-5", "cidade": "RJ"},  # idade negativa
    {"nome": "Carla", "idade": "", "cidade": "BH"},    # idade vazia
    {"nome": "", "idade": "30", "cidade": "POA"},      # nome vazio
    {"nome": "Daniel", "idade": "abc", "cidade": "SP"} # idade não numérica
]

print(f'Quantas linhas têm erro de nome: {sum(pessoa['nome'] == '' for pessoa in dados)}')
print(f'Quantas linhas têm erro de idade: {sum(pessoa['idade'] == '' or not pessoa['idade'].isdigit() or int(pessoa['idade']) < 0 for pessoa in dados)}')
print(f'Quantas linhas têm erro de cidade: {sum(pessoa['cidade'] == '' for pessoa in dados)}')

indice_erros = defaultdict(list)
indice_valido = []

for i, pessoa in enumerate(dados):
    nome = pessoa['nome']
    idade = pessoa['idade']
    cidade = pessoa['cidade']

    if not nome:
        indice_erros[f'Linha {i+1}'].append('nome vazio')

    if not idade:
        indice_erros[f'Linha {i+1}'].append('idade vazia')
    elif not idade[1:].isdigit():
        indice_erros[f'Linha {i+1}'].append('idade não numérica')
    elif int(idade) < 0:
        indice_erros[f'Linha {i+1}'].append('idade negativa')

    if not cidade:
        indice_erros[f'Linha {i+1}'].append('cidade vazia')

for i,_ in enumerate(dados):
    print(i+1)
    if i+1 not in [int(indice[-1:]) for indice in indice_erros.keys()]:
        indice_valido.append(i+1)


print(f'Quantas linhas têm todos os campos válidos: {len(indice_valido)}')
print(f'Quantas linhas têm erro de nome: {sum(pessoa['nome'] == '' for pessoa in dados)}')
print(f'Quantas linhas têm erro de idade: {sum(pessoa['idade'] == '' or not pessoa['idade'].isdigit() or int(pessoa['idade']) < 0 for pessoa in dados)}')
print(f'Quantas linhas têm erro de cidade: {sum(pessoa['cidade'] == '' for pessoa in dados)}')

print(f'Lista dos índices das linhas com erro: ')
for linha, erros in indice_erros.items():
    print(f' - {linha}: {erros}')