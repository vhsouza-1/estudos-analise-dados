"""
Módulo 6: Listas
Aula 6.5: Listas Aninhadas e Cópia
Data: 26/03/2026
Objetivo: Aprender a trabalhar com listas dentro de listas e entender cópias
"""

# ==========================================
# 1. O QUE SÃO LISTAS ANINHADAS?
# ==========================================

print("="*50)
print("1. LISTAS ANINHADAS")
print("="*50)

# Listas podem conter qualquer tipo de dado, inclusive outras listas
aninhada = [1, 2, [3, 4], 5, [6, 7, 8]]
print(f"Lista aninhada: {aninhada}")

# Aplicação mais comum: matrizes (tabelas)
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("\nMatriz 3x3:")
for linha in matriz:
    print(linha)

# ==========================================
# 2. ACESSANDO ELEMENTOS EM LISTAS ANINHADAS
# ==========================================

print("\n" + "="*50)
print("2. ACESSANDO ELEMENTOS")
print("="*50)

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Acessando: matriz[linha][coluna]
print(f"matriz[0][0]: {matriz[0][0]}")  # 1
print(f"matriz[1][2]: {matriz[1][2]}")  # 6
print(f"matriz[2][1]: {matriz[2][1]}")  # 8

# Modificando elementos
matriz[0][0] = 100
matriz[1][1] = 200
matriz[2][2] = 300

print("\nMatriz modificada:")
for linha in matriz:
    print(linha)

# ==========================================
# 3. PERCORRENDO LISTAS ANINHADAS
# ==========================================

print("\n" + "="*50)
print("3. PERCORRENDO LISTAS ANINHADAS")
print("="*50)

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Jeito 1: com índices
print('--- Com índices ---')
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(f'matriz[{i}][{j}] = {matriz[i][j]}')

# Jeito 2: com for direto
print('\n--- Com for direto ---')
for linha in matriz:
    for elemento in linha:
        print(elemento, end=' ')
    print() # quebra de linha

# ==========================================
# 4. CRIANDO MATRIZES COM LIST COMPREHENSION
# ==========================================

print("\n" + "="*50)
print("4. CRIANDO MATRIZES COM LIST COMPREHENSION")
print("="*50)

# Matriz 3x3 com zeros
zeros = [[0 for j in range(3)] for i in range(3)]
print('Matriz de zeros:')
for linha in zeros:
    print(linha)

# Matriz identidade 4x4
identidade = [[1 if i==j else 0 for i in range(4)] for j in range(4)]
print('\nMatriz identidade 4x4:')
for linha in identidade:
    print(linha)

# Tabuada 5x5
tabuada = [[(i+1) * (j+1) for j in range(5)] for i in range(5)]
print("\nTabuada 5x5:")
for linha in tabuada:
    for elemento in linha:
        print(f"{elemento:>3}", end=" ")
    print()

# ==========================================
# 5. O PROBLEMA DA CÓPIA EM PYTHON
# ==========================================

print("\n" + "="*50)
print("5. O PROBLEMA DA CÓPIA")
print("="*50)

# 5.1 Atribuição não é cópia!
print('\n--- Atribuição não copia ---')
original = [1, 2, [3, 4]]
copia = original # isso NÂO é uma cópia!

print(f'Original: {original}')
print(f'Cópia: {copia}')

copia[0] = 100
print('\nApós modificar cópia[0] = 100')
print(f'Original: {original}')
print(f'Cópia: {copia}')

# 5.2 Cópia rasa (shallow copy)
print('\n--- Cópia rasa (shallow copy) ---')
import copy

original = [1, 2, [3, 4]]
copia_rasa = original.copy()

print(f"Original: {original}")
print(f"Cópia rasa: {copia_rasa}")

copia_rasa[2][0] = 999
print("\nApós modificar copia_rasa[2][0] = 999:")
print(f"Original: {original}")  # também mudou! (lista interna é compartilhada)
print(f"Cópia rasa: {copia_rasa}")

# Modificando elemento da lista externa
copia_rasa[0] = 100
print("\nApós modificar copia_rasa[0] = 100:")
print(f"Original: {original}")  # não mudou!
print(f"Cópia rasa: {copia_rasa}")

# 5.3. Cópia profunda (deep copy)
print("\n--- Cópia profunda (deep copy) ---")
original = [1, 2, [3, 4]]
copia_profunda = copy.deepcopy(original)

print(f"Original: {original}")
print(f"Cópia profunda: {copia_profunda}")

copia_profunda[2][0] = 999
print("\nApós modificar copia_profunda[2][0] = 999:")
print(f"Original: {original}")  # não mudou!
print(f"Cópia profunda: {copia_profunda}")

# ==========================================
# 6. RESUMO DOS TIPOS DE CÓPIA
# ==========================================

print("\n" + "="*50)
print("6. RESUMO DOS TIPOS DE CÓPIA")
print("="*50)

"""
📌 TRÊS TIPOS:

1. ATRIBUIÇÃO (=): 
   - Não copia! Apenas cria uma nova referência ao mesmo objeto
   - Modificações afetam o original

2. CÓPIA RASA (shallow copy):
   - copy() ou [:]
   - Cria um novo objeto externo
   - Elementos internos (listas aninhadas) são compartilhados
   - Útil quando não há estruturas aninhadas

3. CÓPIA PROFUNDA (deep copy):
   - copy.deepcopy()
   - Cria um novo objeto externo E novos objetos internos
   - Independente completo
   - Útil quando há estruturas aninhadas
"""

# ==========================================
# 7. EXEMPLOS PRÁTICOS
# ==========================================

print("\n" + "="*50)
print("7. EXEMPLOS PRÁTICOS")
print("="*50)


# 7.1. Média por aluno (matriz de notas)

print("\n--- Média por aluno ---")
notas = [
    [8.0, 7.5, 9.0],  # Ana
    [7.0, 8.0, 6.5],  # Bruno
    [9.0, 9.5, 8.5]   # Carla
]
nomes = ["Ana", "Bruno", "Carla"]

for i, nome in enumerate(nomes):
    media = sum(notas[i]) / len(notas[i])
    print(f'{nome}: {media:.2f}')


# 7.2 Média por bimestre
print('\n--- Média por bimestre ---')
for j in range(len(notas[0])):
    soma_bimestre = 0
    for i in range(len(notas)):
        soma_bimestre += notas[i][j]
    media_bimestre = soma_bimestre / len(notas)
    print(f'Bimestre {j+1}: {media_bimestre:.2f}')

# 7.3. Cópia rasa vs profunda na prática
print("\n--- Cópia rasa vs profunda na prática ---")
configuracao_padrao = [
    ["admin", "senha123"],
    ["usuário", "senha456"]
]

# Cópia rasa: compartilha as senhas!
config_rasa = configuracao_padrao.copy()
config_rasa[0][1] = 'nova_senha'

print(f"Original: {configuracao_padrao}")  # mudou!
print(f"Cópia rasa: {config_rasa}")

# Cópia profunda: independente
config_padrao = [
    ["admin", "senha123"],
    ["usuário", "senha456"]
]
config_profunda = copy.deepcopy(config_padrao)
config_profunda[0][1] = "nova_senha"

print(f"\nOriginal: {config_padrao}")  # não mudou
print(f"Cópia profunda: {config_profunda}")

# ==========================================
# 8. RESUMO FINAL
# ==========================================

print("\n" + "="*50)
print("8. RESUMO FINAL")
print("="*50)

"""
✅ Listas aninhadas: listas dentro de listas
✅ Acesso: lista[linha][coluna]
✅ Percorrer: for linha in matriz: for elemento in linha
✅ Atribuição (=): só cria referência
✅ Cópia rasa ([:] ou .copy()): nova lista externa, mas elementos internos compartilhados
✅ Cópia profunda (copy.deepcopy()): totalmente independente

📌 Quando usar cada tipo:
- Atribuição: quando você quer a mesma lista com nome diferente
- Cópia rasa: para listas simples (sem aninhamento)
- Cópia profunda: para listas aninhadas ou estruturas complexas
"""
################################################
# EXERCÍCIOS - AULA 6.5
################################################
# NÍVEL 1-3: Aquecimento
################################################
"""
1. Criando e acessando matriz

# Crie uma matriz 3x3 com os números de 1 a 9
# Mostre:
# - O elemento da linha 1, coluna 2
# - O elemento da linha 2, coluna 0
# - A segunda linha inteira
"""
"""
matriz = [[j for j in range(3*i+1, 3*i+4)] for i in range(3)] # deu certo hahaha quebrei a cabeça aqui, mas consegui!

print(f'O elemento da linha 1, coluna 2: {matriz[1][2]}')
print(f'O elemento da linha 2, coluna 0: {matriz[2][0]}')
print(f'A segunda linha inteira: {matriz[2]}')
"""
###############################################
"""
2. Somando matrizes

# Dadas duas matrizes 2x2:
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

# Crie uma matriz C onde cada elemento é a soma dos elementos correspondentes
# Resultado esperado: [[6, 8], [10, 12]]
"""
"""
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

C = [[A[i][j]+B[i][j] for j in range(2)] for i in range(2)]

print(C)
"""
"""
3. 3. Diagonal principal

# Dada uma matriz 4x4 com números aleatórios (use list comprehension)
# Extraia e mostre os elementos da diagonal principal (onde linha == coluna)
"""
"""
matriz = [[j for j in range(4*i+1, 4*i+5)] for i in range(4)] # peguei emprestado do ex1 pra fazer a matriz 4x4

for linha in matriz:
    print(linha) # para ver a matriz na forma de matriz

for i in range(len(matriz[0])):
    for j in range(len(matriz)):
        if i == j:
            print(matriz[i][j]) # precisei fazer o for antes pra visualizar o list comprehension. Esse é um dos casos que o list comprehension não é aconselhado né? haha

diagonal = [matriz[i][j] for i in range(len(matriz[0])) for j in range(len(matriz)) if i == j]

print(diagonal)
"""
################################################
# NÍVEL 4-6: Aplicação
################################################
"""
4. Matriz transposta (revisão com list comprehension)

# Dada uma matriz 3x4:
matriz = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

# Crie a matriz transposta usando list comprehension aninhada
# Mostre ambas as matrizes
"""
"""
matriz = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

for linha in matriz:
    print(linha)

transposta = [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]

print()
for linha in transposta:
    print(linha)
"""
###############################################
"""
5. Produto de matrizes

# Dada uma matriz 2x3 e um vetor (lista) de tamanho 3:
matriz = [
    [1, 2, 3],
    [4, 5, 6]
]
vetor = [7, 8, 9]

# Calcule o produto matriz * vetor (resultado é um vetor de tamanho 2)
# Cada elemento do resultado é a soma dos produtos linha * vetor
# Exemplo: resultado[0] = 1*7 + 2*8 + 3*9 = 7 + 16 + 27 = 50
"""
"""
matriz = [
    [1, 2, 3],
    [4, 5, 6]
]
vetor = [7, 8, 9]

resultado = [0, 0]

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        resultado[i] += matriz[i][j]*vetor[j]

print(resultado)

# Tem como fazer com list comprehension?
"""
###################################################
"""
6. Notas dos alunos (matriz)

# Crie uma matriz 5x4 com notas aleatórias (5 alunos, 4 bimestres)
# Use list comprehension com random.uniform(0,10)
# Calcule e mostre:
# - A média de cada aluno
# - A média de cada bimestre
# - A média geral da turma
"""
"""
import random

notas = [[round(random.uniform(0,10), 2) for j in range(4)] for i in range(5)] # arredondei pq tinham muitas casas decimais

for i in range(5):
    print(f'Aluno: {i+1} - média: {sum(notas[i])/len(notas[i]):.2f}')

for i in range(4):
    soma_bimestre = 0
    for j in range(5):
        soma_bimestre += notas[j][i]
    print(f'Bimestre: {i+1} - média: {soma_bimestre/4:.2f}')
"""
################################################
# NÍVEL 7-8: Manipulação
################################################
"""
7. Cópia rasa vs profunda - descobrindo o problema
python

# Crie uma lista aninhada: dados = [[1, 2], [3, 4], [5, 6]]
# Faça:
# - Uma atribuição (dados2 = dados)
# - Uma cópia rasa (dados3 = dados.copy())
# - Uma cópia profunda (dados4 = copy.deepcopy(dados))
#
# Modifique o primeiro elemento da primeira lista interna em cada uma
# Mostre todas as listas e explique o que aconteceu
"""
"""
dados = [[1, 2], [3, 4], [5, 6]]
dados2 = dados
dados3 = dados.copy()
dados4 = copy.deepcopy(dados)

print(dados)
dados[0][0] = 123
print(dados)
print(dados2)
print(dados3)
print(dados4)

# dados2 e dados1 é o mesmo objeto com "etiquetas" diferentes.
# dados3 é uma cópia rasa, copia a estrutura, mas não os elementos internos, modificação nos elementos internos de dados1 afetam ele
# dados4 é uma true copia, modificações no dados1 não afeta ele.
"""
#######################################################
"""
8. Soma de matrizes com list comprehension

# Dadas duas matrizes 3x3:
A = [[i + j for j in range(3)] for i in range(3)]
B = [[(i * 2) + j for j in range(3)] for i in range(3)]

# Use list comprehension aninhada para criar C = A + B
# Mostre todas as matrizes formatadas
"""
"""
A = [[i + j for j in range(3)] for i in range(3)]
B = [[(i * 2) + j for j in range(3)] for i in range(3)]

# C = [[3*i + 2*j for j in range(3)] for i in range(3)] # forma mais simples, menos geral

# C = [[A[i][j]+B[i][j] for j in range(3)] for i in range(3)] # meio do caminho

C = [[A[i][j]+B[i][j] for j in range(len(A))] for i in range(len(A[0]))] # forma menos simples, mais geral
"""
################################################
# NÍVEL 9-10: Desafios
################################################
"""
9. Matriz em espiral

# Crie uma função (usando loops e list comprehension) que gere uma matriz N x N em espiral
# Exemplo para N=4:
# [
#   [ 1,  2,  3, 4],
#   [12, 13, 14, 5],
#   [11, 16, 15, 6],
#   [10,  9,  8, 7]
# ]
# (Pesquise o padrão se necessário)
"""
"""
N = 4

top = 0
bot = N-1
left = 0
right = N-1

numero = 1

matriz = [[0 for j in range(N)] for i in range(N)]

while top <= bot and left <= right:
    for coluna in range(left, right+1):
        matriz[top][coluna] = numero
        numero += 1
    top += 1

    for linha in range(top, bot+1):
        matriz[linha][right] = numero
        numero += 1
    right -= 1

    if top <= bot:
        for coluna in range(right, left-1, -1):
            matriz[bot][coluna] = numero
            numero += 1
        bot -= 1

    if left <= right:
        for linha in range(bot+1, top-1, -1):
            matriz[linha][left] = numero
            numero += 1
        left += 1

for linha in matriz:
    print(linha)

#Eu usei muito a ajuda de outro chat do DS pra resolver isso aqui e mesmo assim ele fez praticamente tudo e eu não entendi o código 100%
# Eu acho que não preciso dominar isso aqui pra mexer com dados né? Entretanto foi divertido e consegui entender melhor itrerações de modo geral
"""
#######################################################
"""
# Você tem um estoque representado por uma matriz onde:
# - Cada linha é um produto
# - Cada coluna é um mês (4 meses)
# - Cada elemento é a quantidade vendida

estoque = [
    [10, 15, 20, 25],  # Produto A
    [5, 10, 15, 20],   # Produto B
    [30, 25, 20, 15]   # Produto C
]

# Crie um programa que:
# a) Mostre a matriz formatada
# b) Calcule o total vendido por produto (soma das linhas)
# c) Calcule o total vendido por mês (soma das colunas)
# d) Encontre o produto mais vendido no total
# e) Encontre o mês com maior venda total
# f) Crie uma cópia profunda do estoque
# g) Na cópia, aplique um aumento de 10% nas vendas do produto mais vendido
# h) Mostre a cópia modificada e o original (que não deve ter mudado)
"""
estoque = [
    [10, 15, 20, 25],  # Produto A
    [5, 10, 15, 20],   # Produto B
    [30, 25, 20, 15]   # Produto C
]
print('------ VENDAS POR MÊS ------\n')


print(f'{'Jan':>12}{'Fev':>5}{'Mar':>5}{'Abr':>5}')

for i in range(len(estoque)):
    print(f'Prod {i+1}: ', end='')
    for j in range(len(estoque[0])):
        print(f'{estoque[i][j]: >4}', end= ' ')
    print()

print()
for i in range(len(estoque)):
    soma_produto = 0
    for j in range(len(estoque[0])):
        soma_produto += estoque[i][j]
    print(f'Total vendido do Prod. {i+1}: {soma_produto}')

print()
for i in range(len(estoque[0])):
    soma_mes = 0
    for j in range(len(estoque)):
        soma_mes += estoque[j][i]
    print(f'Total vendido no mês {i+1}: {soma_mes}')

print()
index_mais_vendido = float('-inf')
for i in range(len(estoque)):
    soma_produto = 0
    for j in range(len(estoque[0])):
        soma_produto += estoque[i][j]
        if soma_produto > index_mais_vendido:
            index_prod_mais_vendido = i
            prod_mais_vendido = f'Prod. {i+1}'
            index_mais_vendido = soma_produto
print(f'O produto mais vendido foi: {prod_mais_vendido}')

print()
index_mes_maior = float('-inf')
for i in range(len(estoque[0])):
    soma_mes = 0
    for j in range(len(estoque)):
        soma_mes += estoque[j][i]
        if soma_mes > index_mes_maior:
            mes_mais_vendas = f'Mês {i+1}'
            index_mes_maior = soma_mes
print(f'O mês com mais vendas foi: {mes_mais_vendas}')

import copy

estoque_copia = copy.deepcopy(estoque)

for j in range(len(estoque_copia[index_prod_mais_vendido])):
    estoque_copia[index_prod_mais_vendido][j] = int(1.1*estoque_copia[index_prod_mais_vendido][j])

print(estoque_copia)
print(estoque)

