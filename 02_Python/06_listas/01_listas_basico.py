"""
Módulo 6: Listas
Aula 6.1: Introdução às listas
Data: 24/03/2026
Objetivo: Aprender a criar e manipular listas
"""

# ==========================================
# 1. O QUE SÃO LISTAS?
# ==========================================

print("="*50)
print("1. O QUE SÃO LISTAS?")
print("="*50)

# Listas são estruturas que guardam MÚLTIPLOS valores em uma única variável
# Pense como uma "caixa com compartimentos"

# Variável simples (guarda um valor)
nome = "Vinícius"

# Lista (guarda vários valores)
nomes = ['Vinícius', 'Ana', 'Carlos', 'Mariana']
print(f'Lista de nomes: {nomes}')

# Listas podem guardar diferentes tipos de dados
misturada = [10, 'texto', 3.14, True]
print(f'Lista mista: {misturada}')

# Lista vazia (começa sem nada)
vazia = []
print(f'Lista vazia: {vazia}')

# ==========================================
# 2. CRIANDO LISTAS
# ==========================================

print("\n" + "="*50)
print("2. CRIANDO LISTAS")
print("="*50)

# Jeito 1: colchetes
frutas = ['maçã', 'banana', 'laranja']
print(f'Frutas: {frutas}')

# Jeito 2: usando list()
numeros = list([1, 2, 3, 4, 5])
print(f'Números: {numeros}')

# Jeito 3: convertendo de string (cada caractere vira elemento)
palavra = list('Python')
print(f'String "Python" virada em lista: {palavra}')

# Jeito 4: range() transformando em lista
rangos = list(range(1, 10, 2))
print(f'range(1, 10, 2) como lista: {rangos}')

# ==========================================
# 3. INDEXAÇÃO (acessando elementos)
# ==========================================

print("\n" + "="*50)
print("3. INDEXAÇÃO")
print("="*50)

# Lembra quando você descobriu que listas começam do 0?
# Vamos formalizar!

frutas = ["maçã", "banana", "laranja", "uva", "manga"]

print(f"Lista: {frutas}")
print(f"Índice 0: {frutas[0]}")   # primeiro elemento
print(f"Índice 1: {frutas[1]}")   # segundo
print(f"Índice 2: {frutas[2]}")   # terceiro
print(f"Índice 3: {frutas[3]}")   # quarto
print(f"Índice 4: {frutas[4]}")   # quinto

# Índices negativos (contam do final)
print(f"\nÍndice -1: {frutas[-1]}")  # último elemento
print(f"Índice -2: {frutas[-2]}")  # penúltimo
print(f"Índice -3: {frutas[-3]}")  # antepenúltimo

# ==========================================
# 4. FATIAMENTO (slicing) - pegando pedaços
# ==========================================

print("\n" + "="*50)
print("4. FATIAMENTO")
print("="*50)

frutas = ["maçã", "banana", "laranja", "uva", "manga", "abacaxi", "kiwi"]

print(f"Lista completa: {frutas}")

# lista[inicio:fim] - fim NÃO INCLUI
print(f'frutas[0:3]: {frutas[0:3]}')
print(f'frutas[2:5]: {frutas[2:5]}')

# Omite início = começa do 0
print(f'frutas[:4]: {frutas[:4]}') # primeiros 4 elementos

# Omite fim = vai até o final
print(f'frutas[3:]: {frutas[3:]}') # do índice 3 até o fim

# Com passo
print(f'frutas[::2]: {frutas[::2]}') # pula de 2 em 2
print(f'frutas[1::2]: {frutas[1::2]}') # Começa do 1, pula de 2 em 2

# Invertendo a lista
print(f'frutas[::-1]: `{frutas[::-1]}') # lista invertida

# ==========================================
# 5. OPERAÇÕES BÁSICAS
# ==========================================

print("\n" + "="*50)
print("5. OPERAÇÕES BÁSICAS")
print("="*50)

# 5.1 Tamanho da lista (len)
frutas = ['maçã', 'banana', 'laranja']
print(f'Tamanho: {len(frutas)}')

# 5.2 Verificar se elemento existe (in)
print(f'"banana" está na lista? {'banana' in frutas}')
print(f'"uva" está na lista? {'uva' in frutas}')

# 5.3 Concatenação (+)
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
concatenada = lista1 + lista2
print(f'{lista1} + {lista2} = {concatenada}')

# 5.4 Repetição (*)
repetida = [1, 2] * 3
print(f'[1, 2] * 3 = {repetida}')

# ==========================================
# 6. MÉTODOS ESSENCIAIS (modificam a lista)
# ==========================================

print("\n" + "="*50)
print("6. MÉTODOS ESSENCIAIS")
print("="*50)

# 6.1 append() - adicional no FINAL
print('\n--- append() ---')
numeros = [1, 2, 3]
print(f'Original: {numeros}')
numeros.append(4)
print(f'Após append(4): {numeros}')

# 6.2 insert() - insere em posição específica
print('\n--- insert() ---')
numeros = [1, 2, 3, 5]
print(f'Original: {numeros}')
numeros.insert(3, 4)
print(f'Após insert(3, 4): {numeros}')

# 6.3 remove() - remove pela PRIMEIRA OCORRÊNCIA do valor
print('\n--- remove() ---')
frutas = ["maçã", "banana", "laranja", "banana"]
print(f'Original: {frutas}')
frutas.remove('banana') # remove a primeira banana
print(f'Após remove("banana"): {frutas}')

# 6.4 pop() - remove pelo ÍNDICE e RETORNA o valor
print("\n--- pop() ---")
frutas = ["maçã", "banana", "laranja"]
print(f"Original: {frutas}")
removida = frutas.pop(1) # remove o índice 1 (banana)
print(f'Após pop(1): {frutas}')
print(f'Elemento removido: {removida}')

# pop() sem índice remove o último
ultimo = frutas.pop()
print(f'Após pop(): {frutas}')
print(f'Último removido: {ultimo}')

# ==========================================
# 7. EXEMPLOS PRÁTICOS
# ==========================================

print("\n" + "="*50)
print("7. EXEMPLOS PRÁTICOS")
print("="*50)

# 7.1. Média de notas
print("\n--- Média de notas ---")
notas = [7.5, 8.0, 6.5, 9.0, 7.0]
media = sum(notas) / len(notas)
print(f"Notas: {notas}")
print(f"Média: {media:.2f}")

# 7.2 Filtrando números pares
print('\n--- Números pares ---')
numeros = list(range(1, 21))
pares = []
for num in numeros:
    if num % 2 == 0:
        pares.append(num)
print(f'Pares de 1 a 20: {pares}')

# 7.3. Juntando listas
print('\n--- Junção de listas ---')
alunos = ['Ana', 'Bruno', 'Carla']
notas = [8.5, 7.0, 9.5]
# Queremos criar: ["Ana: 8.5", "Bruno: 7.0", "Carla: 9.5"]
resultado = []
for i in range(len(alunos)):
    resultado.append(f'{alunos[i]}: {notas[i]}')
print(resultado)

# ==========================================
# 8. ARMADILHAS COMUNS
# ==========================================

print("\n" + "="*50)
print("8. ARMADILHAS COMUNS")
print("="*50)

# 1. Índice inexistente
# frutas = ["maçã", "banana"]
# print(frutas[2])  # IndexError!

# 2. remove() em elemento que não existe
# frutas = ["maçã", "banana"]
# frutas.remove("laranja")  # ValueError!

# 3. Fatiamento não modifica a original
print("\n--- Fatiamento não altera original ---")
frutas = ["maçã", "banana", "laranja"]
fatiado = frutas[0:2]
print(f"Original: {frutas}")
print(f"Fatiado: {fatiado}")
print(f"Original continua igual: {frutas}")

# 4. append() vs extend()
print("\n--- append() vs extend() ---")
lista = [1, 2]
lista.append([3, 4])  # adiciona uma lista como elemento
print(f"append([3,4]): {lista}")

lista2 = [1, 2]
lista2.extend([3, 4])  # adiciona os elementos individualmente
print(f"extend([3,4]): {lista2}")

# ==========================================
# 9. RESUMO
# ==========================================

print("\n" + "="*50)
print("9. RESUMO")
print("="*50)

"""
✅ Listas: estruturas que guardam múltiplos valores
✅ Índices: começam em 0 (positivos) e vão até -1 (negativos)
✅ Fatiamento: lista[inicio:fim:passo] - fim NÃO inclui
✅ len(): tamanho da lista
✅ in: verifica se elemento existe
✅ append(): adiciona no final
✅ insert(pos, valor): insere em posição específica
✅ remove(valor): remove pela primeira ocorrência do valor
✅ pop(indice): remove pelo índice e retorna o valor
"""
# EXERCÍCIOS - AULA 6.1

########################################
# NÍVEL 1-3: Aquecimento
########################################
"""
1. Criando listas

    Crie uma lista com os nomes de 5 amigos

    Mostre o primeiro e o último nome usando índices
"""
"""
amigos = ['Marcos', 'Mateus', 'Ana', 'Edu', 'Gui']

print(amigos[0])
print(amigos[4])
"""
########################################
"""
2. Fatiamento

    Crie uma lista com os números de 1 a 10

    Mostre:

        Os 3 primeiros

        Os 3 últimos

        Do índice 2 ao 7

        Os números pares (use fatiamento com passo)
"""
"""
numeros = list(range(1, 11))

print(numeros[:3])
print(numeros[7:]) # tem algum jeito de pegar os 3 últimos sem eu saber o tamanho da lista?
print(numeros[len(numeros)-3:]) # assim talvez?
print(numeros[2:7])
print(numeros[1:len(numeros):2])
"""
##########################################
"""
3. Verificando existência

    Peça ao usuário um nome

    Verifique se esse nome está na sua lista de amigos

    Mostre "Está na lista" ou "Não está"
"""
"""
amigos = ['Marcos', 'Mateus', 'Ana', 'Edu', 'Gui']
nome = input('Informe um nome: ').strip().capitalize()
if nome in amigos:
    print('Está na lista')
else:
    print('Não está na lista')
"""
########################################
# NÍVEL 4-6: Aplicação
########################################
"""
4. Cadastro de notas

    Crie uma lista vazia para notas

    Peça 5 notas ao usuário (valide se são números)

    Adicione cada nota à lista

    No final, mostre:

        Todas as notas

        A maior e a menor nota

        A média
"""
"""
notas = []

while len(notas) != 5:
    nota = input('Informe uma nota: ')
    if nota[0] == '-':
        print('Entrada inválida! Apenas números positivos')
    elif nota.isalpha():
        print('Entrada inválida! Valor deve ser numérico')
    elif nota.isdigit():
        notas.append(float(nota))
print(notas)
print(f'maior: {max(notas)}, menor: {min(notas)}')
print(f'média: {sum(notas)/len(notas)}')
"""
#####################################################
"""
5. Gerenciador de tarefas (simples)

    Crie uma lista vazia para tarefas

    Mostre um menu:

        Adicionar tarefa

        Remover tarefa

        Ver tarefas

        Sair

    Use append() para adicionar

    Use remove() para remover (peça o nome da tarefa)
"""
"""
tarefas = []
entrada = ''
print('MENU\n1. Adicionar tarefa\n2. Remover tarefa\n3. Ver tarefas\n4. Sair')

while entrada != 'sair':
    entrada = input('Informe a entrada: ')
    if not entrada.isdigit():
        print('Entrada inválida! Apenas números')
    elif int(entrada) not in [1, 2, 3, 4]:
        print('Entrada inválida! Apenas números entre 1 e 4')
    elif int(entrada) == 1:
        print('Adicionar tarefa')
        tarefa_add = input('Informe a tarefa a ser adicionada: ')
        tarefas.append(tarefa_add)
    elif int(entrada) == 2:
        print('Remover tarefa')
        tarefa_rem = input('Informe a tarefa a ser removida: ')
        if tarefa_rem in tarefas:
            tarefas.remove(tarefa_rem)
        else:
            print('A tarefa não consta na lista!')
    elif int(entrada) == 3:
        print(tarefas)
    elif int(entrada) == 4:
        print('Saindo...')
        break
    elif entrada.isalpha:
        print('Entrada inválida! Apenas números')
"""
###############################################################
"""
6. Filtrando e transformando

    Crie uma lista de números: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    Crie uma nova lista com o quadrado de cada número

    Crie outra lista apenas com os números pares

    Mostre todas as listas
"""
"""
numeros = list(range(1, 11))
quadrados = []
pares = []

for num in numeros:
    quadrados.append(num**2)
    if num % 2 == 0:
        pares.append(num)

print(numeros)
print(quadrados)
print(pares)

"""
########################################
# NÍVEL 7-8: Manipulação
########################################
"""
7. Analisador de texto

    Peça uma frase ao usuário

    Transforme a frase em uma lista de palavras (use .split())

    Mostre:

        Quantas palavras tem

        A primeira e a última palavra

        A palavra mais longa (dica: compare len() de cada palavra)

    (Se quiser um desafio extra: a palavra mais curta)
"""
"""
frase = input('Informe uma frase: ')
palavras = frase.split()

maior_index = float('-inf')
for palavra in palavras:
    if len(palavra) > maior_index:
        maior_index = len(palavra)
        maior_palavra = palavra

menor_index = float('inf')
for palavra in palavras:
    if len(palavra) < menor_index:
        menor_index = len(palavra)
        menor_palavra = palavra

print(f'A frase tem: {len(palavras)} palavras!')
print(f'A primeira palavras é "{palavras[0]}"')
print(f'A última palavra é "{palavras[len(palavras)-1]}"')
print(f'A maior palavra é "{maior_palavra}"')
print(f'A menor palavra é "{menor_palavra}"')

"""
############################################
"""
8. Mesclando listas

    Crie duas listas: alunos = ["Ana", "Bruno", "Carla"] e notas = [8.5, 7.0, 9.5]

    Crie uma terceira lista onde cada elemento é uma string "Aluno: nota"

    Faça isso usando um loop for com range(len())
"""
"""
alunos = ["Ana", "Bruno", "Carla"]
notas = [8.5, 7.0, 9.5]
aluno_nota = []

for i in range(len(alunos)):
    aluno_nota.append(f'{alunos[i]}: {notas[i]}')

print(aluno_nota)
"""
########################################
# NÍVEL 9-10: Desafios
########################################
"""
9. Removendo duplicatas (versão manual)

    Crie uma lista com elementos repetidos: [1, 2, 2, 3, 4, 4, 4, 5]

    Crie uma nova lista que contenha apenas os elementos únicos

    Não use set() ou list(dict.fromkeys()) - faça manualmente com um loop e if
"""
"""
nums_rep = [1, 2, 2, 3, 4, 4, 4, 5]
nums = []

for i in range(0, len(nums_rep)):
    if nums_rep[i] in nums:
        continue
    nums.append(nums_rep[i])
print(nums)
"""
##########################################
"""
10. DESAFIO FINAL: Simulador de fila

    Simule uma fila de atendimento:

        Use uma lista como fila (append no final, pop no início)

        Menu:

            Chegar (adicionar nome ao final)

            Atender (remover do início e mostrar quem foi atendido)

            Mostrar fila

            Sair

    Valide: se tentar atender com fila vazia, mostre "Fila vazia"
"""

fila = []
entrada = ''
numero = 0

print('--- MENU ---\n1. Chegar\n2. Atender\n3. Mostrar fila\n4. Sair')

while True:
    entrada = input('Informe um número do menu: ')
    if not entrada.isdigit():
        print('Entrada inválida! Apenas números!')
    elif int(entrada) == 1:
        numero += 1
        fila.append(numero)
        print(f'Chegando! Seu número é {numero}')
    elif int(entrada) == 2:
        if len(fila) == 0:
            print('Fila vazia!')
        else:
            print(f'Atender! Vez do {fila[0]}')
            fila.pop(0)
    elif int(entrada) == 3:
        print(fila)
    elif int(entrada) == 4:
        print('Você saiu, adeus!')
        break
    elif not int(entrada) in [1, 2, 3, 4]:
        print('Entrada inválida! Apenas números do menu!')

