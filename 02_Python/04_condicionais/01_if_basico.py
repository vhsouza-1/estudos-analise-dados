"""
Módulo 4: Condicionais
Aula 4.1: If básico e If-else
Data: 19/03/2026
Objetivo: Aprender a tomar decisões no código
"""
from http.client import CannotSendHeader

# ==========================================
# 1. POR QUE PRECISAMOS DE IF?
# ==========================================

print("="*50)
print("1. O PROBLEMA (sem if)")
print("="*50)

# Até agora os nossos programas eram LINEares:
print("Passo 1")
print("Passo 2")
print("Passo 3")
# Sempre executam TUDO, sempre na MESMA ordem

# Mas e se quisermos que algo SÓ aconteça em certas condições?
# Exemplo: "Só mostra média se nota for maior que 7"

# ==========================================
# 2. COMPARADORES (as ferramentas da decisão)
# ==========================================

print("\n" + "="*50)
print("2. COMPARADORES")
print("="*50)

x = 10
y = 5

print(f'x = {x}, y = {y}')
print(f'x == y? {x == y}') # igualdade
print(f'x != y? {x != y}') # diferente
print(f'x > y? {x > y}')   # maior que
print(f'x < y? {x < y}')   # menor que
print(f'x >= y? {x >= y}') # maior ou igual
print(f'x <= y? {x <= y}') # menor ou igual

# DICA IMPORTANTE:
# = é atribuição (x = 10)
# == é comparação (x == 10)

# ==========================================
# 3. IF SIMPLES (a decisão)
# ==========================================

print("\n" + "="*50)
print("3. IF SIMPLES")
print("="*50)

idade = 18
print(f'Idade: {idade}')

if idade >= 18:
    print('Você é maior de idade')
    print('Pode entrar!')

print(f'Esta linha executa SEMPRE (está fora do if)')

# ESTRUTURA:
# if condição:
#     código identado (4 espaços)
#     esse bloco inteiro executa SE a condição for True
# código sem indentação executa sempre

# Testando com idade diferente
print(f'\n--- Teste com idade 16 ---')
idade = 16
print(f'Idade: {idade}')

if idade >= 18:
    print('Você é maior de idade') # Não executa
    print('Pode entrar!')          # Não executa

print(f'Fim do programa')

# ==========================================
# 4. IF-ELSE (os dois caminhos)
# ==========================================

print("\n" + "="*50)
print("4. IF-ELSE")
print("="*50)

idade = 16

if idade >= 18:
    print(f'Maior de idade')
    print(f'Pode dirigir!')
else:
    print('Menor de idade')
    print('Não pode dirigir ainda')

print('Continuação do programa...')

# ESTRUTURA:

# if condição:
#     bloco SE for True
# else:
#     bloco SE for False

# ==========================================
# 5. EXEMPLO PRÁTICO COM INPUT
# ==========================================

print("\n" + "="*50)
print("5. EXEMPLO PRÁTICO - VALIDAÇÃO DE NOTA")
print("="*50)

# (Vamos deixar descomentado só quando for executar)
"""
nota = float(input('Digite sua nota: '))

if nota >= 7:
    print(f'Aprovado!')
    print('Parabéns')
else:
    print('Reprovado.')
    print('Estude mais na próxima!')

print(f'Sua nota foi {nota:.1f}')
"""

# ==========================================
# 6. ARMADILHAS COMUNS (muito importante!)
# ==========================================

print("\n" + "="*50)
print("6. ARMADILHAS COMUNS")
print("="*50)

# 6.1 Dois pontos esquecidos
# if idade >= 18  # Isso dá erro! Faltou ":"

# 6.2. Indentação errada
"""
if idade >= 18:
print("Maior de idade")  # Erro! Precisa indentar
"""

# 6.3. = em vez de ==
x = 10
# if x = 5:   # Isso NÃO funciona! = é atribuição
#     print("x é 5")

# 6.4. Comparação com string vs número
print("\n--- Comparação string vs número ---")
print('"10" == 10?', "10" == 10)  # False (tipos diferentes)
print('int("10") == 10?', int("10") == 10)  # True

# 6.5. Indentação inconsistente (espaços vs tabs)
# Use SEMPRE 4 espaços (o PyCharm faz isso automático)

# ==========================================
# 7. EXEMPLO COM MÚLTIPLAS CONDIÇÕES (introdução)
# ==========================================

print("\n" + "="*50)
print("7. PREPARAÇÃO PARA PRÓXIMA AULA")
print("="*50)

nota = 8.5

if nota >= 9:
    conceito = 'A'
else:
    if nota >= 7:
        conceito = 'B'
    else:
        if nota >= 5:
            conceito = 'C'
        else:
            conceito = 'D'

print(f'Nota {nota} - Conceito {conceito}')

# Esse formato funciona, mas é feio.
# Na próxima aula veremos if-elif-else para isso!

# ======================================================================================================================
#                                                      EXERCÍCIOS
# ======================================================================================================================
print('-' * 45, 'EXERCÍCIOS', '-' * 45, '\n')

#####################################################
# NÍVEL 1-3: Aquecimento
####################################################
"""
1.Par ou ímpar

    Peça um número inteiro

    Use % 2 para verificar se é par (resto 0) ou ímpar (resto 1)

    Imprima "Par" ou "Ímpar"
"""
"""
num_int = int(input('Informe um número inteiro: '))

if num_int % 2 == 0:
    print(f'Seu número é par!')
else:
    print('Seu número é ímpar!')
"""
#####################################################
"""
2.Positivo ou negativo

    Peça um número

    Verifique se é positivo (>0), negativo (<0) ou zero (=0)

    Use if-else (mas como fazer para 3 casos? Pense!)
"""

"""
num_float = float(input('Informe um número: '))

if num_float > 0:
    print('Seu número é positivo!')
else:
    if num_float < 0:
        print('Seu número é negativo!')
    else:
        print('Seu número é Zero!')
"""
#####################################################
"""
3. Maioridade

    Peça a idade

    Se for 18 ou mais: "Maior de idade"

    Senão: "Menor de idade"
"""

"""
idade = int(input('Informe uma idade: '))

if idade >= 18:
    print('Maior de idade')
else:
    print('Menor de idade')
"""
#####################################################
# NÍVEL 4-6: Aplicação
#####################################################
"""
4.Aprovação escolar

    Peça duas notas

    Calcule a média

    Se média >= 7: "Aprovado"

    Senão: "Reprovado"
"""
"""
nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))

media_notas = (nota1 + nota2)/2

if media_notas >= 7:
    print('Aprovado')
else:
    print('Reprovado')
"""
#####################################################
"""
5. Desconto progressivo (introdução)

    Peça o valor da compra

    Se valor > 100: dê 10% de desconto

    Senão: sem desconto

    Mostre valor final
"""
"""
valor_compra = float(input('Informe o valor da compra: '))

if valor_compra > 100:
    valor_compra_final = 0.9 * valor_compra
else:
    valor_compra_final = valor_compra
print(f'O valor a ser pago é: R$ {valor_compra_final}')
"""
#####################################################
"""
6.Calculadora de IMC com classificação (simplificada)

    Peça peso e altura

    Calcule IMC

    Se IMC < 18.5: "Abaixo do peso"

    Senão: "Peso normal" (vamos simplificar por enquanto)
"""
"""
peso = float(input('Informe o peso (em Kg): '))
altura = float(input('Informe a altura (em m): '))

IMC = peso / altura ** 2

if IMC < 18.5:
    print('Abaixo do peso')
else: 
    print('Peso normal')
"""
#####################################################
# NÍVEL 4-6: Aplicação
#####################################################
"""
7.Validação de entrada (finalmente!)

    Peça um número

    Use .isdigit() para verificar se é número

    Se for, converta e mostre o dobro

    Senão, mostre "Entrada inválida"
"""
"""
numero_validacao = input('Informe um número: ')

if numero_validacao.isdigit(): # não preciso fazer numero_validacao.isdigit() == True então?
    numero_validacao = float(numero_validacao)
    print(f'O dobro do seu número é: {2 * numero_validacao:.2f}')
else:
    print('Entrada inválida')
"""
#####################################################
"""
8. Maior entre dois números

    Peça dois números

    Descubra e mostre o maior

    Se forem iguais, mostre "Números iguais"
"""
"""
num1 = float(input('Informe um número: '))
num2 = float(input('Informe outro número: '))

if num1 > num2:
    print(f'O primeiro número, {num1}, é maior!')
else:
    if num2 > num1:
        print(f'O segundo número, {num2}, é maior!')
    else:
        print('Número iguais')
"""
#####################################################
# NÍVEL 9-10: Desafios
#####################################################
"""
9. Calculadora de troco com validação

    Peça valor da compra e valor pago

    Se valor pago < valor compra: "Dinheiro insuficiente"

    Senão: calcule e mostre o troco
"""
"""
valor_compra = float(input('Informe o valor da compra: '))
valor_pago = float(input('Informe o valor pago: '))

if valor_pago < valor_compra:
    print('Dinheiro insuficiente!')
    print(f'Falta(m): R$ {valor_compra - valor_pago}')
else:
    if valor_pago > valor_compra:
        print('Dinheiro a mais!')
        print(f'O troco é: R$ {valor_pago - valor_compra}')
    else:
        print('Dinheiro exato!')
"""
#####################################################
"""
10. DESAFIO FINAL: Classificação de triângulos

    Peça 3 lados (números)

    Verifique se formam um triângulo (cada lado < soma dos outros dois)

    Se formam: "É um triângulo"

    Senão: "Não é um triângulo"

    (Na próxima aula classificaremos em equilátero, isósceles, escaleno)
"""
"""
print('Informe os o valor dos três lados para a validação de triângulo!')
lado1 = float(input('Informe o primeiro lado: '))
lado2 = float(input('Informe o segundo lado: '))
lado3 = float(input('Informe o terceiro lado: '))

if lado1 < (lado2 + lado3) and lado2 < (lado1 + lado3) and lado3 < (lado1 + lado2):
    print('Os três lados formam um triângulo!')
else:
    print('Os três lados não forma um triângulo :(')

# Ou ainda

if lado1 < (lado2 + lado3):
    if lado2 < (lado1 + lado3):
        if lado3 < (lado1 + lado2):
            print('Os três lados formam um triângulo!')
        else:
            print('Os três lados não forma um triângulo :(')
    else:
        print('Os três lados não forma um triângulo :(')
else:
    print('Os três lados não forma um triângulo :(')
"""







