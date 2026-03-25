"""
Módulo 6: Listas
Aula 6.3: Zip - Combinando Listas
Data: 25/03/2026
Objetivo: Aprender a combinar listas de forma elegante com zip()
"""

# ==========================================
# 1. O PROBLEMA QUE ZIP RESOLVE
# ==========================================

print("="*50)
print("1. O PROBLEMA (sem zip)")
print("="*50)

nomes = ["Ana", "Bruno", "Carla"]
idades = [25, 30, 22]

# Como juntar essas duas listas em pares?
# Jeito tradicional (com índices):
print("--- Jeito tradicional ---")
for i in range(len(nomes)):
    print(f'{nomes[i]} tem {idades[i]}')

# Funciona, mas é verboso e usa índices.

# ==========================================
# 2. ZIP - A SOLUÇÃO ELEGANTE
# ==========================================

print("\n" + "="*50)
print("2. ZIP - A SOLUÇÃO ELEGANTE")
print("="*50)

nomes = ["Ana", "Bruno", "Carla"]
idades = [25, 30, 22]

# zip() junta as listas elemento a elemento
print('--- Usando zip() ---')
for nome, idade in zip(nomes, idades):
    print(f'{nome} tem {idade} anos')

# Muito mais limpo! Sem índices, sem range(len())

# ==========================================
# 3. O QUE ZIP RETORNA?
# ==========================================

print("\n" + "="*50)
print("3. O QUE ZIP RETORNA?")
print("="*50)

nomes = ["Ana", "Bruno", "Carla"]
idades = [25, 30, 22]

# zip() retorna um objeto zip (não é uma lista)
resultado = zip(nomes, idades)
print(f'Tipo: {type(resultado)}')
print(f'Objeto zip: {resultado}')

# Para ver o conteúdo, precisamos converter
print(f'Como lista: {list(resultado)}')

# CUIDADO! uma vez convertido, o zip se esgota!
# print(list(resultado)) # dá vazio!

# Por isso, é comum usar zip() diretamente no loop

# ==========================================
# 4. ZIP COM TRÊS OU MAIS LISTAS
# ==========================================

print("\n" + "="*50)
print("4. ZIP COM TRÊS OU MAIS LISTAS")
print("="*50)

nomes = ["Ana", "Bruno", "Carla"]
idades = [25, 30, 22]
cidades = ["São Paulo", "Rio de Janeiro", "Belo Horizonte"]

print('--- Três listas ---')
for nome, idade, cidade in zip(nomes, idades, cidades):
    print(f'{nome} tem {idade} anos e mora em {cidade}')

# ==========================================
# 5. ZIP COM LISTAS DE TAMANHOS DIFERENTES
# ==========================================

print("\n" + "="*50)
print("5. ZIP COM LISTAS DE TAMANHOS DIFERENTES")
print("="*50)

nomes = ["Ana", "Bruno", "Carla", "Daniel"]
idades = [25, 30, 22]  # só 3 idades

print("Listas:")
print(f"Nomes: {nomes}")
print(f"Idades: {idades}")

print("\n--- zip() para no menor tamanho ---")
for nome, idade in zip(nomes, idades):
    print(f'{nome} tem {idade} anos') # Daniel não aparece porque não tem idade correspondente

# Se quiser que preencha com valor padrão, existe zip_longest

print("\n--- zip_longest (preenche com None) ---")
from itertools import zip_longest
for nome, idade in zip_longest(nomes, idades):
    print(f'{nome} tem {idade} anos')

# ==========================================
# 6. CRIANDO LISTAS A PARTIR DO ZIP
# ==========================================

print("\n" + "="*50)
print("6. CRIANDO LISTAS A PARTIR DO ZIP")
print("="*50)

nomes = ["Ana", "Bruno", "Carla"]
idades = [25, 30, 22]

# Criando lista de tuplas
pares = list(zip(nomes, idades))
print(f'Lista de tuplas: {pares}') # O que é um tupla? Tem alguma coisa a ver com aquele tal de dicionário que eu tbm n sei o que é?

# Criando lista de strings combinadas
combinadas = [f"{nome} ({idade} anos)" for nome, idade in zip(nomes, idades)]  # list comprehension (vamos ver depois)

# Por enquanto vamos fazer com loop
combinadas_loop = []
for nome, idade in zip(nomes, idades):
    combinadas_loop.append(f'{nome} ({idade} anos)')
print(f'Lista combinada: {combinadas_loop}')

# ==========================================
# 7. CRIANDO DICIONÁRIO COM ZIP
# ==========================================

print("\n" + "="*50)
print("7. CRIANDO DICIONÁRIO COM ZIP")
print("="*50)

nomes = ["Ana", "Bruno", "Carla"]
idades = [25, 30, 22]

# Transformar em dicionário (nomes como chave, idades como valor)

dicionario = dict(zip(nomes, idades))
print(f'Dicionário: {dicionario}')
print(f'Idade da ana: {dicionario['Ana']}')

# ==========================================
# 8. DESZIPANDO - SEPARANDO LISTAS
# ==========================================

print("\n" + "="*50)
print("8. DESZIPANDO - SEPARANDO LISTAS")
print("="*50)

# Se temos uma lista de pares, como separar em duas listas?
pares = [('Ana', 25),('Bruno', 30), ('Carla', 22)]
print(f'Lista de pares: {pares}')

# Jeito 1: com loop
nomes_sep = []
idades_sep = []

for nome, idade in pares:
    nomes_sep.append(nome)
    idades_sep.append(idade)

print(f"Nomes: {nomes_sep}")
print(f"Idades: {idades_sep}")

# Jeito 2: com zip (o "deszip")
nomes_sep2, idades_sep2 = zip(*pares)
print(f"Nomes (deszip): {nomes_sep2}")
print(f"Idades (deszip): {idades_sep2}")

# O * desempacota a lista de pares
# É o oposto do zip

# ==========================================
# 9. EXEMPLOS PRÁTICOS
# ==========================================

print("\n" + "="*50)
print("9. EXEMPLOS PRÁTICOS")
print("="*50)

# 9.1 Média por aluno com duas listas
print(f'\n Média por aluno')
nomes = ["Ana", "Bruno", "Carla"]
notas1 = [8.0, 7.5, 9.0]
notas2 = [7.5, 8.0, 9.5]

for nome, n1, n2 in zip(nomes, notas1, notas2):
    media = (n1 + n2) / 2
    print(f'{nome}: média {media}')

# 9.2. Combinando três listas para relatório
print("\n--- Relatório de vendas ---")
produtos = ["Arroz", "Feijão", "Macarrão"]
quantidades = [50, 30, 80]
precos = [23.50, 8.75, 5.99]

print(f"{'Produto':<12} {'Qtd':>5} {'Preço':>8} {'Total':>10}")
print("-" * 40)
for produto, qtd, preco in zip(produtos, quantidades, precos):
    total = qtd * preco
    print(f"{produto:<12} {qtd:>5} {preco:>8.2f} {total:>10.2f}")

# 9.3. Verificando aprovação com múltiplas listas
print("\n--- Verificação de aprovação ---")
nomes = ["Ana", "Bruno", "Carla"]
notas = [8.5, 6.0, 7.5]
frequencias = [90, 75, 80]

for nome, nota, freq in zip(nomes, notas, frequencias):
    if nota >= 7 and freq >= 75:
        status = 'Aprovado'
    elif nota >= 5 and freq >= 75:
        status = 'Recuperação'
    else:
        status = 'Reprovado'
    print(f'{nome}: nota {nota}, freq {freq}% -- {status}')

# ==========================================
# 10. RESUMO
# ==========================================

print("\n" + "="*50)
print("10. RESUMO")
print("="*50)

"""
✅ zip(): junta listas elemento a elemento
✅ Retorna um objeto zip (iterável)
✅ Para no tamanho da menor lista
✅ list(zip(...)) converte para lista de tuplas
✅ dict(zip(...)) converte para dicionário
✅ zip(*lista) desfaz o zip (separar listas)
✅ from itertools import zip_longest para preencher valores

📌 Quando usar zip():
- Quando você tem listas paralelas que precisam ser percorridas juntas
- Muito mais elegante que usar range(len())
"""
################################################
# EXERCÍCIOS - AULA 6.3
################################################
# NÍVEL 1-3: Aquecimento
################################################
"""
1. Zip básico

    Crie duas listas: nomes = ["Ana", "Bruno", "Carla"] e idades = [25, 30, 22]

    Use zip() e um loop for para imprimir: "Ana tem 25 anos"
"""
"""
nomes = ['Ana', 'Bruno', 'Carla']
idades = [25, 30, 22]

for nome, idade in zip(nomes, idades):
    print(f'{nome} tem {idade} anos')
"""
##################################################
"""
2. Zip com três listas

    Crie listas: nomes, idades, cidades

    Use zip() para imprimir: "Ana tem 25 anos e mora em São Paulo"
"""
"""
nomes = ['Ana', 'Bruno', 'Carla']
idades = [25, 30, 22]
cidades = ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte']

for nome, idade, cidade in zip(nomes, idades, cidades):
    print(f'{nome} tem {idade} anos e mora em {cidade}')
"""
###################################################
"""
3. Convertendo zip em lista

    Use zip() nas listas nomes e idades

    Converta o resultado para uma lista de tuplas

    Mostre a lista
"""
"""
nomes = ['Ana', 'Bruno', 'Carla']
idades = [25, 30, 22]

nomes_idades = list(zip(nomes, idades))

print(nomes_idades)
"""
################################################
# NÍVEL 4-6: Aplicação
################################################
"""
4. Criando dicionário com zip

    Crie duas listas: frutas = ["maçã", "banana", "laranja"] e precos = [3.50, 2.00, 4.50]

    Use zip() e dict() para criar um dicionário onde a fruta é a chave e o preço é o valor

    Mostre o preço da banana
"""
"""
frutas = ["maçã", "banana", "laranja"]
precos = [3.50, 2.00, 4.50]

frutas_precos = dict(zip(frutas, precos))

print(f'O preço da banana é: {frutas_precos['banana']}')
"""
###############################################
"""
5. Média por aluno

    Crie listas: nomes, notas1, notas2, notas3 (cada uma com 4 alunos)

    Use zip() para calcular a média de cada aluno

    Mostre: "Ana: média 8.5"
"""
"""
nomes = ['Ana', 'Bruno', 'Carla', 'Daniel']
notas1 = [7.3, 8.6, 5.9, 9.2]
notas2 = [6.8, 7.9, 6.5, 8.9]

for nome, n1, n2 in zip(nomes, notas1, notas2):
    media = (n1+n2)/2
    print(f'{nome}: média {media}')
"""
#################################################
"""
6. Relatório de produtos

    Crie listas: produtos, quantidades, precos_unitarios

    Use zip() para calcular o valor total em estoque de cada produto

    Mostre um relatório tabular (use formatação com f-strings e alinhamento)
"""
"""
produtos = ['Intruder', 'CG', 'Factor']
precos = [8000, 8500, 9200]
quantidades = [2, 5, 3]


a=10 # parametros para facilitar a formatação tabular
b=5
c=8
d=8
print(f"{'Produto':<{a}} {'Qtd':>{b}} {'Preço':>{c}} {'Total':>{d}}")
for prod, preco, qnt in zip(produtos, precos, quantidades):
    total = preco * qnt
    print(f"{prod:<{a}} {qnt:>{b}} {preco:>{c}} {total:>{d}}")
"""
################################################
# NÍVEL 7-8: Manipulação
################################################
"""
7. Filtrando com zip

    Crie listas: nomes, notas

    Use zip() e um if dentro do loop para mostrar apenas os alunos com nota >= 7

    Mostre: "Ana: 8.5 - Aprovado"
"""
"""
nomes = ['Ana', 'Bruno', 'Carla', 'Daniel']
notas = [7.3, 8.6, 5.9, 9.2]

for nome, nota in zip(nomes, notas):
    if nota >= 7:
        print(f'{nome}: {nota} - Aprovado')
    else:
        print(f'{nome}: {nota} - Reprovado')
"""
###############################################
"""
8. Lista de compras combinada

    Crie listas: itens, quantidades, precos_unitarios

    Use zip() para criar uma lista de strings: "Arroz (3 x R$ 5.00) = R$ 15.00"

    Mostre o total geral da compra
"""
"""
itens = ['Arroz', 'Feijão', 'Carne', 'Ovos']
quantidades = [1, 2, 4, 3]
preco_unit = [22.0, 7.5, 32.0, 16.0]

total = 0
for item, qnt, preco in zip(itens, quantidades, preco_unit):
    tot = qnt * preco
    print(f'{item} ({qnt} x R$ {preco}) = {tot}')
    total += tot
print(f'Total da compra foi de: {total}')
"""
################################################
# NÍVEL 9-10: Desafios
################################################
"""
9. Deszip (separar listas)

    Crie uma lista de tuplas: pares = [("Ana", 25), ("Bruno", 30), ("Carla", 22)]

    Use zip(*pares) para separar em duas listas: nomes e idades

    Mostre as duas listas
"""
"""
pares = [("Ana", 25), ("Bruno", 30), ("Carla", 22)]
nomes, idades = zip(*pares)
print(nomes)
print(idades)
"""
"""
10. DESAFIO FINAL: Relatório de vendas com zip

    Crie um programa que:

        Peça ao usuário para digitar produtos, quantidades e preços (um por vez)

        O usuário digita "fim" para parar de adicionar produtos

    Armazene os dados em três listas

    Depois que o usuário terminar, use zip() para:

        Mostrar um relatório com produto, quantidade, preço unitário e valor total

        Calcular e mostrar o valor total do estoque

        Mostrar o produto mais caro (preço unitário)

        Mostrar o produto com maior quantidade em estoque
"""
produtos = []
quantidades = []
precos = []

while True:
    produto = input('Informe o produto: ')
    produtos.append(produto)

    quantidade = input('Informe a quantidade: ')
    quantidades.append(int(quantidade))

    preco = input('Informe o preco: ')
    precos.append(int(preco))

    index = input('Mais produtos? (s/n): ').strip().lower()
    if index in ['n', 'nao', 'não']:
        break


index_caro = float('-inf')
for prod, prec in zip(produtos, precos):
    if prec > index_caro:
        prod_caro = prod
        index_caro = prec

index_qnt = float('-inf')
for prod, qnt in zip(produtos, quantidades):
    if qnt > index_qnt:
        prod_freq = prod
        index_qnt = qnt

estoque = 0
for prod, qnt, prec in zip(produtos, quantidades, precos):
    tot = qnt * prec
    print(f'nome: {prod}, quantidade: {qnt}, preço: R$ {prec} e total: R$ {tot}' )
    estoque += tot

print(f'O valor total em estoque: R$ {estoque}')
print(f'O produto mais caro é: {prod_caro}')
print(f'O produto mais frequente é: {prod_freq}')









