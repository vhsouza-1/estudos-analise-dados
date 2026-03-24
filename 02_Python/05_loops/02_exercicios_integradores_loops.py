"""
Módulo 5: Loops
Exercícios Integradores
Data: 23/03/2026
Objetivo: Resolver problemas que misturam tudo que vimos
"""
"""
1. Exercício 1: Analisador de Números com Menu

Tema: Combinação de while, for e validação

Crie um programa que:

    Mostre um menu com opções:

        1 - Analisar números pares/ímpares

        2 - Verificar números primos

        3 - Calcular potência

        4 - Sair

    Para a opção 1:

        Peça ao usuário um número N

        Mostre, de 1 até N, quantos são pares e quantos são ímpares

    Para a opção 2:

        Peça ao usuário um número

        Informe se é primo ou não

        Extra: Mostre todos os primos menores que esse número

    Para a opção 3:

        Peça base e expoente

        Calcule a potência usando apenas multiplicação (não usar **)

        Mostre o resultado

    O menu deve continuar até o usuário escolher sair
"""
"""
opcao = 0


print(--- MENU ---
\n1 - Analisar números pares/ímpares
\n2 - Verificar números primos
\n3 - Calcular potência
\n4 - Sair)

while opcao != 4:
    opcao = int(input('Informe um número do menu: '))
    if opcao == 1:
        N = int(input('Informe um número inteiro: '))
        qnt_par = 0
        qnt_impar = 0
        for i in range(1, N+1):
            if i % 2 == 0:
                qnt_par += 1
            elif i % 2 != 0:
                qnt_impar += 1
        print(f'De 1 à {N} temos {qnt_par} pares e {qnt_impar} impares!')

    if opcao == 2:
        N = int(input('Informe um número inteiro: '))
        indice_primo = 0
        primos_menores = []

        for i in range(2, N):
            if N % i == 0:
                indice_primo += 1
        if indice_primo == 0:
            print(f'{N} é primo!')
        elif indice_primo != 0:
            print(f'{N} não é primo!')

        for i in range (N-1, 1, -1):
            indice_primo = 0
            for j in range (2, i):
                if i % j == 0:
                    indice_primo += 1
            if indice_primo == 0:
                primos_menores.append(i)

        print(f'Primos menores que {N}: {primos_menores}')

    if opcao == 3:
        base = int(input('Informe a base (inteiro): '))
        exp = int(input('Informe o expoente (inteiro): '))
        potencia = base
        if base == 0 and exp < 0:
            print('Entrada inválida, divisão por zero!')
        else:
            for i in range(1, exp):
                potencia *= base
            print(f'O resultado da potenciação é: {potencia}')

    if opcao != [1, 2, 3, 4]: # testei para ver se funcionava e deu certo hehe
        print('Entrada inválida!')
        
print('Programa encerrado!')
"""
##############################################################
"""
2. Exercício 2: Validador de Números com Múltiplas Tentativas

Tema: Validação robusta com while e flags

Crie um programa que:

    Peça ao usuário para digitar números (pode ser inteiro ou decimal)

    Valide cada entrada:

        Números negativos: "Valor inválido! Digite um número positivo."

        Letras ou símbolos: "Entrada inválida! Digite um número válido."

        Decimais: deve aceitar (use .replace('.', '').isdigit() ou trate com try/except - se quiser, posso explicar try/except brevemente)

    O programa deve pedir números até que o usuário digite "sair"

    No final, mostre:

        Quantos números válidos foram digitados

        Maior valor

        Menor valor

        Média

        Quantos são maiores que a média

Desafio extra: Se o usuário digitar "sair" sem nenhum número válido, mostre "Nenhum número foi digitado"
"""
"""
numeros = []
opcao = 'abc'

while True:
    opcao = input('Informe um número: ')
    if opcao == 'sair':
        break
    elif opcao[0] == '-':
        print('Valor inválido! Digite um número positivo!')
    elif opcao.isalpha():
        if opcao.strip().lower() == 'sair':
            break
        else:
            print('Entrada inválida! Digite um número válido!')
    elif opcao.replace('.', '').isdigit():
        opcao = float(opcao)
        numeros.append(opcao)
    elif opcao.isdigit():
        opcao = float(opcao)
        numeros.append(opcao)

qnt_maior_media = 0
for i in numeros:
    if i > (sum(numeros)/len(numeros)):
        qnt_maior_media += 1

if len(numeros) == 0:
    print('Nenhum número foi digitado!')
else:
    print(f'Foram digitados {len(numeros)} números válidos!')
    print(f'O maior valor foi: {max(numeros)}, o menor valor foi: {min(numeros)}')
    print(f'A média é: {sum(numeros)/len(numeros):.2f}')
    print(f'A quantidade de números maiores que a média é: {qnt_maior_media}')
"""
###################################################
"""
3. Exercício 3: Gerador de Sequências Numéricas

Tema: Múltiplos padrões com for

Crie um programa que:

    Peça ao usuário um número N

    Gere e mostre as seguintes sequências:

        Sequência 1: 1, 3, 5, 7, ... até N (ímpares)

        Sequência 2: 1, 4, 9, 16, ... até N (quadrados perfeitos)

        Sequência 3: 1, 2, 4, 8, 16, ... até N (potências de 2)

        Sequência 4: 1, 1, 2, 3, 5, 8, ... até N (Fibonacci - mas sem usar a solução do exercício anterior, crie do zero)

        Sequência 5: N, N-1, N-2, ..., 1 (contagem regressiva)

Importante: Cada sequência deve ser gerada em um loop separado (não misturar). Mostre cada sequência em uma linha.
"""
"""
N = int(input('Informe um número inteiro: '))

for i in range(1, N+1, 2):
    print(i, end=' ')
print(f' -- Ímpares até {N}!')

for i in range(1, N+1):
    if i/(i**(1/2)) == i//(i**(1/2)): # eu sei que isso é meio que uma gambiarra, mas foi o jeito que eu encontrei de mostrar que o num é inteiro... haha
        print(i, end=' ')
print(f' -- Quadrados perfeitos até {N}!')

for i in range(1, N):
    if 2**i <= N:
        print(2**i, end=' ')
print(f' -- Potências de 2 até {N}!')

f1=0
f2=1
print(f'{f1} {f2}', end=' ')
for i in range(1, N):
    f=f1+f2
    print(f'{f} ', end='')
    f1=f2
    f2=f
    if f >= N:
        break
print(f' -- Fibonacci até {N}!')

for i in range(N, -1, -1):
    print(i, end=' ')
print(f' -- Contagem regressiva começando em {N}!')
"""
#####################################################
"""
4. Exercício 4: Caça-Números com Dicas

Tema: Jogo com lógica e validação

Crie um jogo onde:

    O programa gera um número secreto entre 1 e 100

    O usuário tem tentativas ilimitadas, mas:

        A cada 3 tentativas erradas, o programa dá uma dica:

            "O número é par" ou "O número é ímpar"

            "O número está entre X e Y" (reduzindo o intervalo)

    O programa conta e mostra:

        Número de tentativas

        Se o usuário acertou ou desistiu

    Após acertar, o programa pergunta se o usuário quer jogar novamente

Regras de validação:

    Só aceita números inteiros entre 1 e 100

    Se o usuário digitar "desistir", encerra o jogo atual
"""
"""
import random

novamente = 'sim'

while novamente in ['sim', 's']: # descobri que tenho que colocar in no lugar de == aqui
    entrada = 101
    numero = random.randint(1, 100)

    tentativas = 0
    lim_inf = 1
    lim_sup = 100

    while int(entrada) != numero:
        entrada = input(f'Informe um número inteiro entre {lim_inf} e {lim_sup}({numero}): ')
        if entrada.strip().lower() == 'desistir':
            print('Você desistiu :(')
            print(f'Número de tentativas: {tentativas}')
            break
        elif not entrada.isdigit():
            print('Entrada inválida!')
        elif lim_inf < int(entrada) > lim_sup:
            print(f'Entrada inválida! Apenas números entre {lim_inf} e {lim_sup}')
        elif int(entrada) == numero:
                print('Você acertou!')
                tentativas += 1
                print(f'Número de tentativas: {tentativas}')
        elif int(entrada) != numero:
                print('Você errou!')
                tentativas += 1
                if tentativas % 3 == 0:
                    print('Dicas:')
                    if numero % 2 == 0:
                        print('O número é par!')
                    else:
                        print('O número é ímpar!')
                    if numero < lim_sup - 10:
                        lim_sup -= 10
                    elif numero > lim_inf + 10:
                        lim_inf += 10

    novamente = input('Deseja jogar novamente?(sim/não): ').strip().lower()
    if novamente in ['n', 'nao', 'não']:
        print('Obrigado por jogar!')
        break

# Eu acho que esse código ficou muito bom hehe
"""
#####################################################
"""
5. Exercício 5: Analisador de Sequência com Padrões

Tema: Descoberta de padrões em sequências

Crie um programa que:

    Peça ao usuário para digitar uma sequência de números (um por vez)

    O programa deve parar quando o usuário digitar "fim"

    Depois que a sequência for inserida, o programa deve analisar e mostrar:

    a) Tendência:

        "Crescente" se cada número for maior que o anterior

        "Decrescente" se cada número for menor que o anterior

        "Alternada" se oscila (ex: 2,5,3,6,4)

        "Constante" se todos iguais

        "Sem padrão claro" se não se encaixa nos padrões acima

    b) Diferenças entre números consecutivos:

        Mostre a lista de diferenças

        A maior diferença (em valor absoluto)

        A menor diferença

    c) Pontos de inflexão:

        Quantas vezes a sequência mudou de direção (crescente→decrescente ou decrescente→crescente)
"""
print('Informe uma sequência de números inteiros, positivos, não-nulos (um por vez)')
numeros = []
entrada = ''

while entrada != 'fim':
    entrada = input('Informe um valor: ')
    if entrada == 'fim':
        break
    elif not entrada.isdigit():
        print('Entrada inválida!')
    elif entrada.isdigit():
        if int(entrada) <= 0:
            print('Entrada inválida!')
        else:
            entrada = int(entrada)
            numeros.append(entrada)
            print(numeros)

cres_index = 0
for i in range(0, len(numeros)):
    for j in range(i+1, len(numeros)):
        if numeros[i] >= numeros[j]:
            cres_index += 1

decres_index = 0
for i in range(0, len(numeros)):
    for j in range(i+1, len(numeros)):
        if numeros[i] <= numeros[j]:
            decres_index += 1

cons_index = 0
for i in numeros:
    if numeros[0] != i:
        cons_index += 1

if cres_index == 0:
    print('\nCrescente!')
elif decres_index == 0:
    print('\nDecrescente!')
elif cons_index == 0:
    print('\nConstante!')
else:
    print('\nSem padrão claro!')

print('Sequência: ', end='')
for i in range(0, len(numeros)-1):
    print(numeros[i], end=', ')
print(numeros[len(numeros)-1])

diferencas = []
for i in range(0, len(numeros)-1):
    dif = numeros[i+1] - numeros[i]
    diferencas.append(dif)
# print(diferencas)

print('Diferenças: ', end='')
for i in range(0, len(diferencas)-1):
    print(diferencas[i], end=', ')
print(diferencas[len(diferencas)-1])

print(f'Maior diferença: {max(diferencas)}')
print(f'Menor diferença: {min(diferencas)}')



































