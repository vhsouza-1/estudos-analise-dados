"""
Módulo 6: Listas
Aula 6.2: Ordenação e Contagem
Data: 25/03/2026
Objetivo: Aprender a ordenar listas e contar elementos
"""

# ==========================================
# 1. SORT() - ORDENANDO A LISTA ORIGINAL
# ==========================================

print("="*50)
print("1. SORT() - ORDENA A LISTA ORIGINAL")
print("="*50)

# sort() modifica a lista original
numeros = [3, 1, 4, 1, 5, 9, 2]
print(f'Lista original: {numeros}')
numeros.sort()
print(f'Após sort(): {numeros}')

# Ordem decrescente
numeros.sort(reverse=True)
print(f'Após sort(reverse=True): {numeros}')

# ==========================================
# 2. SORTED() - CRIANDO UMA NOVA LISTA ORDENADA
# ==========================================

print("\n" + "="*50)
print("2. SORTED() - CRIA NOVA LISTA ORDENADA")
print("="*50)

# sorted() não modifica a original
numeros = [3, 1, 4, 1, 5, 9, 2]
print(f'Lista original: {numeros}')

ordenada_crescente = sorted(numeros)
print(f'Ordenada crescente: {ordenada_crescente}')

ordenada_decrescente = sorted(numeros, reverse=True)
print(f'Ordenada decrescente: {ordenada_decrescente}')

print(f"Original continua: {numeros}")

# Quando usar cada um?
# - sort(): quando você quer ordenar a lista que já tem
# - sorted(): quando você quer preservar a original

# ==========================================
# 3. REVERSE() - INVERTENDO A ORDEM
# ==========================================

print("\n" + "="*50)
print("3. REVERSE() - INVERTE A ORDEM")
print("="*50)

# reverse() modifica a lista original (inverte, não ordena)
frutas = ["maçã", "banana", "laranja", "uva"]
print(f"Original: {frutas}")

frutas.reverse()
print(f'Após reverse(): {frutas}')

# Se quiser inverter sem modificar a original:
frutas = ["maçã", "banana", "laranja", "uva"]
invertida = frutas[::-1]  # fatiamento
print(f"\nOriginal: {frutas}")
print(f"Invertida (fatiamento): {invertida}")
print(f"Original continua: {frutas}")

# ==========================================
# 4. COUNT() - CONTANDO OCORRÊNCIAS
# ==========================================

print("\n" + "="*50)
print("4. COUNT() - CONTA OCORRÊNCIAS")
print("="*50)

numeros = [1, 2, 2, 3, 2, 4, 2, 5]
print(f"Lista: {numeros}")
print(f"Quantos 2? {numeros.count(2)}")
print(f"Quantos 1? {numeros.count(1)}")
print(f"Quantos 10? {numeros.count(10)}")

# Útil para verificar frequência em listas
frutas = ["maçã", "banana", "maçã", "laranja", "banana", "maçã"]
print(f"\nLista de frutas: {frutas}")
print(f"maçã aparece: {frutas.count('maçã')} vezes")
print(f"banana aparece: {frutas.count('banana')} vezes")
print(f"laranja aparece: {frutas.count('laranja')} vezes")

# ==========================================
# 5. INDEX() - ENCONTRANDO A POSIÇÃO
# ==========================================

print("\n" + "="*50)
print("5. INDEX() - ENCONTRA O ÍNDICE")
print("="*50)

frutas = ["maçã", "banana", "laranja", "banana", "uva"]
print(f"Lista: {frutas}")

# Retorna o índice da PRIMEIRA ocorrência
print(f"Posição de 'banana': {frutas.index('banana')}")  # 1
print(f"Posição de 'uva': {frutas.index('uva')}")        # 4

# Buscar a partir de uma posição específica
print(f"Posição de 'banana' após índice 2: {frutas.index('banana', 2)}")  # 3

# Buscar em um intervalo
# frutas.index('banana', 2, 5)  # entre índices 2 e 5

# CUIDADO: se não encontrar, dá erro (ValueError)
# print(frutas.index("abacaxi"))  # ValueError!

# ==========================================
# 6. EXEMPLOS PRÁTICOS
# ==========================================

print("\n" + "="*50)
print("6. EXEMPLOS PRÁTICOS")
print("="*50)

# 6.1. Ordenando notas e mantendo a original
print("\n--- Notas dos alunos ---")
notas = [7.5, 8.0, 6.5, 9.0, 7.0]
print(f"Notas originais: {notas}")

notas_ordenadas = sorted(notas)
print(f"Notas ordenadas: {notas_ordenadas}")
print(f"Menor nota: {notas_ordenadas[0]}")
print(f"Maior nota: {notas_ordenadas[-1]}")
print(f"Notas originais preservadas: {notas}")

# 6.2. Contando notas por conceito
print("\n--- Distribuição de conceitos ---")
notas = [8.5, 6.0, 7.5, 5.0, 9.0, 6.5, 7.0, 4.5]

aprovados = [n for n in notas if n >= 7]  # list comprehension (vamos ver depois)
reprovados = [n for n in notas if n < 5]
recuperacao = [n for n in notas if 5 <= n < 7]

print(f"Total de alunos: {len(notas)}")
print(f"Aprovados: {len(aprovados)}")
print(f"Recuperação: {len(recuperacao)}")
print(f"Reprovados: {len(reprovados)}")

# 6.3. Encontrando posição de um valor específico
print("\n--- Encontrando posição do maior valor ---")
notas = [7.5, 8.0, 6.5, 9.0, 7.0]
maior = max(notas)
posicao = notas.index(maior)
print(f"Notas: {notas}")
print(f"Maior nota: {maior}")
print(f"Posição do aluno: {posicao} (índice {posicao})")

# ==========================================
# 7. RESUMO
# ==========================================

print("\n" + "="*50)
print("7. RESUMO")
print("="*50)

"""
✅ sort(): ordena a lista ORIGINAL (modifica)
✅ sorted(): retorna uma NOVA lista ordenada (preserva original)
✅ reverse(): inverte a ordem da lista ORIGINAL
✅ count(): conta quantas vezes um elemento aparece
✅ index(): encontra a posição da PRIMEIRA ocorrência

📌 Dicas:
- Use sort() quando não precisa da original
- Use sorted() quando precisa preservar a original
- count() é ótimo para verificar frequência
- index() retorna erro se o elemento não existir
"""

##############################################
# EXERCÍCIOS - AULA 6.2
##############################################
# NÍVEL 1-3: Aquecimento
##############################################
"""
1. Ordenação básica

    Crie uma lista numeros = [5, 2, 8, 1, 9, 3]

    Mostre a lista ordenada crescente (use sorted())

    Mostre a lista ordenada decrescente (use sorted() com reverse=True)

    Mostre que a lista original não foi modificada
"""
"""
numeros = [5, 2, 8, 1, 9, 3]
ord_cres = sorted(numeros)
ord_decres = sorted(numeros, reverse=True)

print(ord_cres)
print(ord_decres)
print(numeros)
"""
#########################################
"""
2. Contando elementos

    Crie uma lista cores = ["azul", "vermelho", "azul", "verde", "azul", "amarelo"]

    Use count() para mostrar quantas vezes cada cor aparece

    Mostre o total de elementos com len()
"""
"""
cores = ["azul", "vermelho", "azul", "verde", "azul", "amarelo"]
print(f'Azul aparece: {cores.count("azul")} vez(es)!')
print(f'Vermelho aparece: {cores.count("vermelho")} vez(es)!')
print(f'Verde aparece: {cores.count("verde")} vez(es)!')
print(f'Amarelo aparece: {cores.count("amarelo")} vez(es)!')
"""
###########################################
"""
3. Encontrando posição

    Crie uma lista frutas = ["maçã", "banana", "laranja", "uva", "banana"]

    Use index() para encontrar a posição de "laranja"

    Encontre a posição da primeira "banana"

    Encontre a posição da segunda "banana" (dica: use o parâmetro start)
"""
"""
frutas = ["maçã", "banana", "laranja", "uva", "banana"]

print(f'A posição de "laranja" é: {frutas.index('laranja')}')
print(f'A posição da primeira "banana" é: {frutas.index('banana')}')
print(f'A posição da segunda "banana" é: {frutas.index('banana', 2)}')
"""
###########################################
# NÍVEL 4-6: Aplicação
###########################################
"""
4. Ordenando e analisando notas

    Crie uma lista de notas: [8.5, 6.0, 9.0, 7.5, 5.0, 8.0, 6.5, 7.0]

    Use sorted() para ordenar

    Mostre:

        A menor nota

        A maior nota

        A mediana (a nota do meio - para lista par, pegue as duas do meio e faça média)

        Quantas notas são maiores ou iguais a 7
"""
"""
notas = [8.5, 6.0, 9.0, 7.5, 5.0, 8.0, 6.5, 7.0] #
notas_ord = sorted(notas)

maior_7 = []

if len(notas_ord) % 2 != 0:
    mediana = notas_ord[(len(notas_ord)//2)]
elif len(notas_ord) % 2 == 0:
    a = int(len(notas_ord) / 2)
    mediana = (notas_ord[a] + notas_ord[a - 1]) / 2

for nota in notas_ord:
    if nota >= 7:
        maior_7.append(nota)


print(f'Notas ordenadas: {notas_ord}')
print(f'A menor nota é: {min(notas)}')
print(f'A maior nota é: {max(notas)}')
print(f'A mediana é: {mediana}')
print(f'A quantidade de notas maiores ou iguais a 7 são: {len(maior_7)}')
"""
################################################
"""
5. Lista de compras ordenada

    Crie uma lista vazia

    Peça ao usuário 5 itens de compra

    Adicione cada um à lista

    Mostre a lista em ordem alfabética

    Mostre a lista em ordem inversa (do último para o primeiro)

    Mostre quantas vezes "leite" aparece (use count())
"""
"""
compras = []

while len(compras) != 5:
    item = input(f'Informe um item para compra: ').strip().lower()
    compras.append(item)

compras_ord = sorted(compras)
# compras_rev = compras.reverse()
compras.reverse()

print(f'Lista em ordem alfabética: {compras_ord}')
print(f'Lista em ordem inversa: {compras}')
print(f'Leite apareceu {compras.count('leite')} vez(es)')
"""
#########################################################
"""
6. Encontrando o maior valor e sua posição

    Crie uma lista valores = [15, 23, 8, 42, 17, 31, 5]

    Encontre o maior valor (use max())

    Encontre a posição desse valor (use index())

    Encontre o menor valor e sua posição

    Mostre todos os resultados
"""
"""
valores = [15, 23, 8, 42, 17, 31, 5]
maior_valor = max(valores)
menor_valor = min(valores)

print(f'O maior valor é: {maior_valor} e sua posição é: {valores.index(maior_valor)}')
print(f'O maior valor é: {menor_valor} e sua posição é: {valores.index(menor_valor)}')
"""
####################################
# NÍVEL 7-8: Manipulação
####################################
"""
7. Ordenação com critérios

    Crie uma lista de strings: palavras = ["casa", "carro", "abacaxi", "sol", "computador", "gato"]

    Mostre a lista ordenada alfabeticamente

    Mostre a lista ordenada por tamanho (da menor para a maior palavra)

    Dica: sorted(palavras, key=len) - key diz qual critério usar
"""
"""
palavras = ["casa", "carro", "abacaxi", "sol", "computador", "gato"]

palavras_alf = sorted(palavras)
palavras_tam = sorted(palavras, key=len)

print(f'Lista original: {palavras}')
print(f'Lista ordenada alfabeticamente: {palavras_alf}')
print(f'Lista ordenada por tamanho: {palavras_tam} ')
"""
#################################
"""
8. Contando e filtrando

    Crie uma lista com números aleatórios (use import random; numeros = [random.randint(1, 20) for _ in range(20)])

    Use count() para encontrar o número que mais aparece (pode fazer manualmente)

    Use sort() para ordenar a lista

    Mostre os 5 maiores números (últimos 5 da lista ordenada)

    Mostre os 5 menores números (primeiros 5)
"""
"""
import random; numeros = [random.randint(1, 20) for _ in range(20)]

print(numeros)
numeros_ord = sorted(numeros)
print(numeros_ord)

indice_freq = float('-inf')
for i in range(0, len(numeros_ord)):
    print(i, numeros_ord[i], numeros_ord.count(numeros_ord[i]))
    if numeros_ord.count(numeros_ord[i]) > indice_freq:
        indice_freq = numeros_ord.count(numeros_ord[i])
        num_mais_freq = numeros_ord[i]

print(f'Lista original: {numeros}')
print(f'Lista ordenada: {numeros_ord}')
print(f'O número que mais aparece é: {num_mais_freq}')
print(f'Os 5 maiores números: {numeros_ord[-5:]}')
print(f'Os 5 menores números: {numeros_ord[:5]}')
"""
############################################
# NÍVEL 9-10: Desafios
############################################
"""
9. Ordenando lista de dicionários (preparação)

    Crie uma lista de dicionários com alunos e notas:
    python

    alunos = [
        {"nome": "Ana", "nota": 8.5},
        {"nome": "Bruno", "nota": 7.0},
        {"nome": "Carla", "nota": 9.5},
        {"nome": "Daniel", "nota": 6.0}
    ]

    Use sorted() com key=lambda x: x["nota"] para ordenar por nota

    Mostre o ranking (do maior para o menor)

    Mostre o nome do aluno com a maior nota usando max() com key
"""
"""
alunos = [
    {"nome": "Ana", "nota": 8.5},
    {"nome": "Bruno", "nota": 7.0},
    {"nome": "Carla", "nota": 9.5},
    {"nome": "Daniel", "nota": 6.0}
]
alunos_ord = sorted(alunos, key = lambda x: x['nota'])
alunos_rank = sorted(alunos, key = lambda x: x['nota'], reverse=True)

print(f'Ordenados por nota: {alunos_ord}')
print(f'Ordenados por ranking: {alunos_rank}')
print(f'Aluno(a) com maior nota: {max(alunos, key= lambda x: x['nota'])}') # como faz para pegar só o nome? Não sei fazer...
"""
##################################################
"""
10. DESAFIO FINAL: Estatísticas de uma sequência

    Peça ao usuário para digitar números (um por vez) até digitar "sair"

    Armazene os números em uma lista

    Depois que o usuário digitar "sair", mostre:

        A lista original

        A lista ordenada

        A lista em ordem inversa

        Quantos números únicos (dica: crie uma cópia e remova duplicatas)

        Quantas vezes o número mais frequente aparece

        O maior e o menor valor

        A posição do maior valor (índice na lista original)
"""
numeros = []

while True:
    entrada = input(f'Informe números (um por vez): ')
    if entrada == 'sair':
        print('Saindo...')
        break
    elif not entrada.isdigit():
        print('Entrada inválida! Apenas números')
    else:
        numeros.append(int(entrada))

numeros_ord = sorted(numeros)
numeros_inv = sorted(numeros, reverse=True)

numeros_unicos = []

for i in range(0, len(numeros)):
    if numeros[i] not in numeros_unicos:
        numeros_unicos.append(numeros[i])
    else:
        continue

print(f'unicos: {numeros_unicos}')

indice_freq = float('-inf')
for i in range(0, len(numeros_ord)):
    print(i, numeros_ord[i], numeros_ord.count(numeros_ord[i]))
    if numeros_ord.count(numeros_ord[i]) > indice_freq:
        indice_freq = numeros_ord.count(numeros_ord[i])
        num_mais_freq = numeros_ord[i]
print(num_mais_freq)

print(f'Lista original: {numeros}')
print(f'Lista ordenada: {numeros_ord}')
print(f'Lista inversa: {numeros_inv}')
print(f'Números únicos: {numeros_unicos}')
print(f'O número mais frequente é: {num_mais_freq} e ele aparece: {numeros_ord.count(num_mais_freq)} vez(es)!')
print(f'Maior valor: {max(numeros)}, Menor valor: {min(numeros)}')
print(f'A posição do maior valor (na lista original): {numeros.index(max(numeros))}')
