"""
Módulo 5: Loops
Data: 23/03/2026
Objetivo: Aprender a repetir ações com while e for
"""

# ==========================================
# 1. O PROBLEMA QUE LOOPS RESOLVEM
# ==========================================

print("="*50)
print("1. O PROBLEMA (sem loops)")
print("="*50)

# Se eu quiser imprimir números de 1 a 5, sem loop:

print(1)
print(2)
print(3)
print(4)
print(5)

# E se eu quiser de 1 a 100? Inviável escrever um por um!
# É aí que entram os loops.

# ==========================================
# 2. WHILE - repete enquanto condição for verdadeira
# ==========================================

print("\n" + "="*50)
print("2. WHILE - O LOOP CONDICIONAL")
print("="*50)

# Exemplo: contar de 1 a 5

contador = 1
while contador <=5:
    print(contador)
    contador = contador + 1

# ESTRUTURA:
# while condicao:
#     bloco que repete enquanto condicao for True

# CUIDADO! Se a condição nunca ficar False, o loop é INFINITO
# contador = 1
# while contador <= 5:
#     print(contador)  # SEMPRE 1, loop infinito!

# ==========================================
# 3. FOR - o loop mais usado em Python
# ==========================================

print("\n" + "="*50)
print("3. FOR - O LOOP DE SEQUÊNCIA")
print("="*50)

# O for percorre cada item de uma sequência

# Exemplo: percorrer uma lista (ainda não vimos listas formalmente, mas vamos usar)

print('--- Percorrendo uma lista ---')
frutas = ['maçã', 'banana', 'laranja']
for fruta in frutas:
    print(f'Eu gosto de {fruta}')

# Exemplo: percorrer cada caractere de uma string

print('--- Percorrendo uma string ---')
palavra = 'Python'
for letra in palavra:
    print(f'Letra: {letra}')

# ESTRUTURA:
# for item in sequencia:
#     bloco executado para cada item

# ==========================================
# 4. RANGE() - o gerador de números
# ==========================================

print("\n" + "="*50)
print("4. RANGE() - SEQUÊNCIAS NUMÉRICAS")
print("="*50)

# range(stop) - de 0 até stop-1
print('range(5): ', list(range(5)))

# range(start, stop) - de start até stop-1
print('range(2, 7)', list(range(2, 7)))

# range(start, stop, step) - com passo
print('range(1, 10, 2):', list(range(1, 10, 2)))
print('range(10, 0, -1): ', list(range(10, 0, -1)))

# Usando range com for

print('\n--- For com Range ---')
for i in range(5):
    print(f'Volta {i}')

print('\n --- Tabuada do 5 ---')
for i in range(1, 11):
    print(f'5 x {i} = {5*i}')

# ==========================================
# 5. BREAK e CONTINUE - controlando o loop
# ==========================================

print("\n" + "="*50)
print("5. BREAK e CONTINUE")
print("="*50)

# BREAK: interrompe o loop imediatamente

print('--- BREAK (para no 3) ---')
for i in range (1, 10):
    if i == 3:
        break
    print(i)

# CONTINUE: pula para a próxima iteração
print('\n--- CONTINUE (pula o 3) ---')
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# ==========================================
# 6. WHILE vs FOR - quando usar cada um
# ==========================================

print("\n" + "="*50)
print("6. QUANDO USAR WHILE e QUANDO USAR FOR")
print("="*50)

# FOR: quando sabemos quantas repetições teremos
print('--- FOR (sabemos o número de iterações) ---')
for i in range(5):
    print(f'repetição {i}')

# WHILE quando não sabemos quantas repetições
# print('\n--- WHILE (não sabemos quando vai parar) ---')
# numero = 0
# while numero != 7:
#     # Simulando uma entrada do usuário
#     numero = int(input('Adivinhe o número (1-10): '))
#     if numero != 7:
#         print('Errou! Tente novamente.')
# print('Acertou!')

# ==========================================
# 7. EXEMPLOS PRÁTICOS
# ==========================================

print("\n" + "="*50)
print("7. EXEMPLOS PRÁTICOS")
print("="*50)

# 7.1 Somando números

print('\n--- Somando de 1 a 100 ---')
soma = 0
for i in range(1, 101):
    soma += i # soma = soma + i # eu conhecia só essa segunda versão, qual é mais utilizada?
print(f'Soma de 1 a 100: {soma}')

# 7.2 Encontrando o primeiro múltiplo

print('\n--- Primeiro múltiplo de 7 entre 1 e 100 ---')
for i in range(1, 101):
    # print(i)
    if i % 7 == 0:
        print(f'Encontrando: {i}')
        break # para no primeiro

# 7.3 Validação de entrada com while

# print('\n--- Validação de idade ---')
# idade = -1
# while idade < 0 or idade > 120:
#     idade = int(input('Digite uma idade válida (0-120): '))
#     if idade < 0 or idade > 120:
        print('Idade inválida! Tente novamente.')
# print(f'Idade registrada: {idade}')

# ==========================================
# 8. ARMADILHAS COMUNS
# ==========================================

print("\n" + "="*50)
print("8. ARMADILHAS COMUNS")
print("="*50)

# 1. Loop infinito (esquecer de atualizar a condição)
# x = 0
# while x < 10:
#     print(x)  # x nunca muda!

# 2. Esquecer os dois pontos e indentação
# for i in range(5)
# print(i)  # Erro!

# 3. Modificar a lista enquanto itera (avançado, mas importante)
# for fruta in frutas:
#     frutas.append("uva")  # Pode causar loop infinito!

# 4. Break só sai do loop mais interno
print("\n--- Break no loop interno ---")
for i in range(3):
    for j in range(3):
        if j == 1:
            break  # só sai do loop do j
        print(f"i={i}, j={j}")

# ==========================================
# 9. RESUMO
# ==========================================

print("\n" + "="*50)
print("9. RESUMO")
print("="*50)

"""
✅ FOR: percorre sequências (range, listas, strings)
✅ WHILE: repete enquanto condição for True
✅ RANGE: gera sequências numéricas
✅ BREAK: interrompe o loop
✅ CONTINUE: pula para a próxima iteração
✅ FOR: quando sabemos quantas vezes repetir
✅ WHILE: quando a parada depende de uma condição
"""

# ======================================================================================================================
#                                                      EXERCÍCIOS
# ======================================================================================================================
print('-' * 45, 'EXERCÍCIOS', '-' * 45, '\n')

#########################################
# NÍVEL 1-3: Aquecimento
#########################################
"""
1.Contagem regressiva

    Peça um número ao usuário

    Use for com range para contar de 0 até esse número

    Depois use while para fazer a mesma contagem
"""
"""
num = int(input('Informe um número inteiro: '))

print('\nContagem com for e range:')
for i in range(num + 1): # +1 para não parar no número anterior ao informado.
    print(i)

print('\nContagem com while:')
j=0
while j != num + 1:
    print(j)
    j += 1
"""
################################################
"""
2. Soma dos pares

    Peça um número N

    Some todos os números pares de 1 até N

    Mostre o resultado
"""
"""
N = int(input('Informe um valor inteiro para N: '))

soma = 0
for i in range(N+1):
    if i % 2 == 0:
        soma += i
print(f'O resultado da soma dos pares até {N} é: {soma}')

soma = 0
while j != N+1:
    if j % 2 == 0:
        soma += j
    j += 1
print(f'O resultado da soma dos pares até {N} é: {soma}')

# Fiz das duas formas para tirar uma dúvida. Nessa situação o mais adequado seria o for com range, não só pq eu conheço
# O limite (que é o N informado), mas também pq nessas situações eu preciso atualizar o valor de j com um contador
# a questão é que o for ja faz isso de forma embutida em sua própria syntax...
# Claro, existem situações em que eu preciso do contador, mas o for com range n da conta, pq a lista não é definida a priori...
"""
##################################################
"""
3.Tabuada completa

    Peça um número ao usuário

    Use for para mostrar a tabuada de 1 a 10 desse número
"""
"""
num = int(input('Informe um número inteiro: '))

for i in range(1, 11):
    print(f'{num} x {i} = {num * i}')
"""
##################################################
# NÍVEL 4-6: Aplicação
##################################################
"""
4. Adivinhação com while

    Gere um número aleatório (use import random; numero = random.randint(1, 100))

    Enquanto o usuário não acertar, peça um palpite e dê dicas ("maior" ou "menor")

    Quando acertar, mostre quantas tentativas foram necessárias
"""
"""
import random
numero = random.randint(1, 100)
palpite = int(input('Tente acertar um número entre 1 e 100!: '))

while palpite != numero:
    print('Errou!')
    if palpite > numero:
        print('Menor!')
        palpite = int(input('Tente novamente: '))
    elif palpite < numero:
        print('Maior!')
        palpite = int(input('Tente novamente: '))
print('Acertou!')
# tem como contar o número de iterações para mostrar a quantidade de tentativas?
"""
######################################################
"""
5. Validação de múltiplos inputs

    Peça ao usuário para digitar 5 números

    Valide cada um: se não for número, peça novamente (use .isdigit())

    No final, mostre a soma e a média
"""
"""
print('Informe 5 números')

n1 = input('Primeiro número: ')
while not n1.isdigit():
    print('Entrada inválida! Faça novamente!')
    n1 = input('Primeiro número: ')
n1 = int(n1)

n2 = input('Segundo número: ')
while not n2.isdigit():
    print('Entrada inválida! Faça novamente!')
    n2 = input('Segundo número: ')
n2 = int(n2)

n3 = input('Terceiro número: ')
while not n3.isdigit():
    print('Entrada inválida! Faça novamente!')
    n3 = input('Terceiro número: ')
n3 = int(n3)

n4 = input('Quarto número: ')
while not n4.isdigit():
    print('Entrada inválida! Faça novamente!')
    n4 = input('Quarto número: ')
n4 = int(n4)

n5 = input('Quinto número: ')
while not n5.isdigit():
    print('Entrada inválida! Faça novamente!')
    n5 = input('Quinto número: ')
n5 = int(n5)

soma = n1 + n2 + n3 + n4 + n5
media = soma/5
print(f'A soma dos números informados é: {soma} e a média é: {media}')
"""
"""
SOLUÇÃO ALTERNATIVA PARA O EXERCÍCIO 5:

n1, n2, n3, n4, n5 = 0, 0, 0, 0, 0
soma = 0

print('Informe um total de 5 números!')

for n in [n1, n2, n3, n4, n5]:
    n = input('Informe um número: ')
    while not n.isdigit():
        print('Entrada inválida, apenas números!')
        n = input('Informe um número: ')
    n = int(n)
    soma += n

media = soma/5
print(f'A soma dos números informados é: {soma} e a média é: {media}')
"""
#####################################################
"""
6. Fatorial de um número

    Peça um número N

    Calcule N! (fatorial = N * (N-1) * ... * 1)

    Use for com range para calcular
"""
"""
fatorial = 1
N = int(input('Informe um número inteiro: '))

for i in range(N, 0, -1): # Aqui quando chega no zero, o programa não roda? Ele só roda no 1? Achei que daria erro assim, mas deu certo.
    fatorial = fatorial * i

print(f'O fatorial do seu número é: {fatorial}')
"""
##################################################
# NÍVEL 7-8: Manipulação
##################################################
"""
7. Números primos

    Peça um número N

    Verifique se ele é primo (divisível apenas por 1 e por ele mesmo)

    Dica: use for para testar divisão por todos os números de 2 até N-1
"""
"""
N = int(input('Informe um número inteiro: '))
cont = 0

for i in range(2, N):
    if N % i == 0:
        cont += 1

if cont == 0:
    print(f'Seu número {N} é primo!')
else:
    print(f'Seu número {N} não é primo!')
"""
###################################################
"""
8. Série de Fibonacci

    Peça um número N

    Mostre os primeiros N termos da sequência de Fibonacci (0, 1, 1, 2, 3, 5, 8, ...)

    Dica: use variáveis para guardar os dois últimos termos
"""
"""
N = int(input(f'Informe um número inteiro: '))

f1 = 0
f2 = 1

print(f'{f1}\n{f2}')

for i in range(1, N-1): # esse range esta correto?
    f = f1 + f2
    print(f)
    f1 = f2
    f2 = f
"""
##################################################
# NÍVEL 9-10: Desafios
##################################################
"""
9. Menu interativo (sem funções ainda)

    Crie um programa com um menu que oferece opções:

        Calcular fatorial

        Verificar se é primo

        Mostrar Fibonacci

        Sair

    Use while para manter o menu ativo até o usuário escolher sair

    Para cada opção, peça os dados necessários e mostre o resultado
"""
"""
funcao = 'abc'

while not funcao == 'sair':
    funcao = input('Informe a função desejada (fatorial/primo/fibonacci/sair): ').strip().lower()
    if funcao == 'fatorial':
        fatorial = 1
        N = int(input('Informe um número inteiro: '))

        for i in range(N, 0, -1):
            fatorial = fatorial * i

        print(f'O fatorial do seu número é: {fatorial}')

    elif funcao == 'primo':
        N = int(input('Informe um número inteiro: '))
        cont = 0

        for i in range(2, N):
            if N % i == 0:
                cont += 1

        if cont == 0:
            print(f'Seu número {N} é primo!')
        else:
            print(f'Seu número {N} não é primo!')

    elif funcao == 'fibonacci':
        N = int(input(f'Informe um número inteiro: '))

        f1 = 0
        f2 = 1

        print(f'{f1}\n{f2}')

        for i in range(1, N-1):
            f = f1 + f2
            print(f)
            f1 = f2
            f2 = f

print('Aplicativo encerrado!')
#ADOREI ESSE!!! muito legal mesmo
"""
##################################################
"""
10. DESAFIO FINAL: Analisador de sequência

    Peça ao usuário para digitar números (até digitar "sair")

    Armazene os números em uma lista (ainda não vimos listas formalmente, mas podemos usar)

    Depois que o usuário digitar "sair", analise:

        Quantos números foram digitados

        Maior e menor valor

        Soma e média

        Quantos números pares e ímpares

    Mostre todos os resultados formatados
"""
"""
entrada = 'a'
numeros = []
qnt_par = 0
qnt_impar = 0


while True:
    entrada = input('Informe a entrada: ')
    if entrada.strip().lower() == 'sair':
        break
    elif not entrada.isdigit():
        print('Entrada inválida!')
    elif entrada.isdigit():
        entrada = int(entrada)
        numeros.append(entrada)

for i in numeros:
    if i % 2 == 0:
        qnt_par +=1
    elif i %2 != 0:
        qnt_impar +=1

print(f'Foram digitados {len(numeros)} números!')
print(f'O maior valor é {max(numeros)} e o menor valor é: {min(numeros)} ')
print(f'A soma é: {sum(numeros)} e a média é {sum(numeros)/len(numeros)}')
print(f'a quantidade de pares é: {qnt_par} e a quantidade de ímpares é: {qnt_impar}')

# Gostei de trabalhar com listas, mas cuidado com conteúdos que vc não me ensinou...
# Por sorte esses eram simples...
"""










