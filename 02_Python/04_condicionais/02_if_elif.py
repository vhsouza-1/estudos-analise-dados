"""
Módulo 4: Condicionais
Aula 4.2: If-elif-else e operadores lógicos
Data: 19/03/2026
Objetivo: Aprender a lidar com múltiplas condições
"""
from http.client import CannotSendHeader

# ==========================================
# 1. O PROBLEMA QUE ELIF RESOLVE
# ==========================================

print("="*50)
print("1. O PROBLEMA (sem elif)")
print("="*50)

nota = 6.5

# Jeito feio (que vimos na aula passada)
if nota >= 9:
    conceito = "A"
else:
    if nota >= 7:
        conceito = "B"
    else:
        if nota >= 5:
            conceito = "C"
        else:
            conceito = "D"

print(f"Nota {nota} → Conceito {conceito}")
print("Esse código funciona, mas fica cada vez mais indentado...")

# ==========================================
# 2. IF-ELIF-ELSE (a solução elegante)
# ==========================================

print("\n" + "="*50)
print("2. IF-ELIF-ELSE")
print("="*50)

nota = 6.5

if nota >= 9.5:
    conceito = 'A'
elif nota >= 7:
    conceito = 'B'
elif nota >= 5:
    conceito = 'C'
else:
    conceito = 'D'

print(f"Nota {nota} → Conceito {conceito}")
print("Muito mais limpo!")

# Me lembra a estrutura condicional do SQL! CASE WHEN, vários WHEN e ELSE no final

# ESTRUTURA:
# if condicao1:
#     bloco1
# elif condicao2:
#     bloco2
# elif condicao3:
#     bloco3
# else:
#     bloco_final

# IMPORTANTE: Só EXECUTA O PRIMEIRO que for True
# Se nota = 9.5, entra no primeiro e ignora os outros

# Testando com vários valores
print("\n--- Testando diferentes notas ---")
for nota_teste in [9.5, 7.5, 5.5, 3.0]:
    if nota_teste >= 9:
        conceito = "A"
    elif nota_teste >= 7:
        conceito = "B"
    elif nota_teste >= 5:
        conceito = "C"
    else:
        conceito = "D"
    print(f"Nota {nota_teste} → {conceito}")

# Eu achei que o código ia dar errado, pois achei que faria tudo de uma vez, mas, na verdade, ele faz nota_teste assumir
# um valor por vez, ai a ele é atribuido um conceito e printado, ai depois começa novamente.

# ==========================================
# 3. OPERADORES LÓGICOS
# ==========================================

print("\n" + "="*50)
print("3. OPERADORES LÓGICOS")
print("="*50)

# 3.1 AND (E) - TUDO precisa ser True
print("\n--- AND (E) ---")
idade = 25
tem_carteira = True

if idade >= 18 and tem_carteira:
    print("Pode dirigir")
else:
    print("Não pode dirigir")

# Tabela verdade do AND:
print(f"True and True = {True and True}")
print(f"True and False = {True and False}")
print(f"False and True = {False and True}")
print(f"False and False = {False and False}")

# 3.2 OR (OU) - PELO MENOS UM precisa ser True
print("\n--- OR (OU) ---")
tem_cartao = True
tem_dinheiro = False

if tem_cartao or tem_dinheiro:
    print("Pode comprar")
else:
    print("Não pode comprar")

# Tabela verdade do OR:
print(f"True or True = {True or True}")
print(f"True or False = {True or False}")
print(f"False or True = {False or True}")
print(f"False or False = {False or False}")

# 3.3 NOT (NÃO) - inverte o valor
print("\n--- NOT (NÃO) ---")
esta_chovendo = False

if not esta_chovendo:
    print("Vamos sair!")
else:
    print("Ficamos em casa")

print(f"not True = {not True}")
print(f"not False = {not False}")

# ==========================================
# 4. COMBINANDO OPERADORES
# ==========================================

print("\n" + "="*50)
print("4. COMBINAÇÕES")
print("="*50)

idade = 17
autorizacao_pais = True # como eu faço para transformar isso em um input()?

# AND tem precedência sobre OR (como multiplicação sobre adição)
# Mas use parênteses para deixar claro!

if (idade >= 18) or (idade < 18 and autorizacao_pais):
    print("Pode entrar no evento")
else:
    print("Não pode entrar")

# Outro exemplo: validação de senha
usuario = "joao"
senha = "123456"
confirmado = True

if usuario != "" and senha != "" and confirmado:
    print("Login válido")
else:
    print("Dados incompletos")

# ==========================================
# 5. EXEMPLO PRÁTICO: IMC COMPLETO
# ==========================================

print("\n" + "="*50)
print("5. EXEMPLO PRÁTICO - IMC COMPLETO")
print("="*50)

# (Deixaremos comentado para não travar)
"""
peso = float(input("Seu peso (kg): "))
altura = float(input("Sua altura (m): "))

imc = peso / (altura ** 2)

print(f"\nSeu IMC: {imc:.2f}")

if imc < 18.5:
    print("Abaixo do peso")
elif imc < 25:
    print("Peso normal")
elif imc < 30:
    print("Sobrepeso")
elif imc < 35:
    print("Obesidade Grau I")
elif imc < 40:
    print("Obesidade Grau II")
else:
    print("Obesidade Grau III")
"""

# ==========================================
# 6. EXEMPLO: APROVAÇÃO COM MÚLTIPLOS CRITÉRIOS
# ==========================================

print("\n" + "="*50)
print("6. EXEMPLO - APROVAÇÃO COM MÚLTIPLOS CRITÉRIOS")
print("="*50)

# Critérios:
# - Média >= 7
# - Frequência >= 75%
# - Ou média >= 5 e frequência >= 90% (recuperação)

# (Comentado para não travar)
"""
media = float(input("Média final: "))
frequencia = float(input("Frequência (%): "))

if media >= 7 and frequencia >= 75:
    print("Aprovado direto! 🎉")
elif media >= 5 and frequencia >= 90:
    print("Aprovado com recuperação! 📚")
else:
    print("Reprovado 😢")
"""

# ==========================================
# 7. ARMADILHAS COMUNS
# ==========================================

print("\n" + "="*50)
print("7. ARMADILHAS COMUNS")
print("="*50)

# 7.1. Ordem das condições importa!
print("\n--- Ordem importa! ---")
x = 5

# ERRADO: a primeira condição pega tudo
if x > 2:
    print("Maior que 2")
elif x > 4:
    print("Maior que 4")  # NUNCA executa!

# CERTO: do mais específico para o mais geral
if x > 4:
    print("Maior que 4")
elif x > 2:
    print("Maior que 2")

# 7.2. Comparações encadeadas (feature legal do Python)
print("\n--- Comparações encadeadas ---")
idade = 25
if 18 <= idade <= 60:  # Isso funciona em Python!
    print("Idade entre 18 e 60")

## realmente é uma feature legal, no SQL tem que usar idade between 18 and 60 ou idade >= 18 and idade <= 60

# Em outras linguagens seria: if idade >= 18 and idade <= 60

# 7.3. Cuidado com and/or misturados
print("\n--- Precedência ---")
a = True
b = False
c = True

# Sem parênteses, pode confundir
resultado = a and b or c
print(f"a and b or c = {resultado}")

# Com parênteses, fica claro
resultado = (a and b) or c
print(f"(a and b) or c = {resultado}")

# REGRA: AND tem precedência sobre OR (como multiplicação)
# Mas use parênteses para legibilidade!

# ======================================================================================================================
#                                                      EXERCÍCIOS
# ======================================================================================================================
print('-' * 45, 'EXERCÍCIOS', '-' * 45, '\n')

####################################################
# NÍVEL 1-3: Aquecimento
####################################################
"""
1. Classificação de notas (com elif)

    Peça uma nota de 0 a 10

    Classifique:

        9 a 10: "Excelente"

        7 a 8.9: "Bom"

        5 a 6.9: "Regular"

        Abaixo de 5: "Insuficiente"
"""
"""
nota = float(input('Informe uma nota (entre 0 e 10): '))

if nota > 9:
    print('Excelente!')
elif 7 < nota < 8.9:
    print('Bom!')
elif 5 < nota < 6.9:
    print('Regular!')
elif nota < 5:
    print('Insuficiente!')
else:
    print('Nota inválida!')
"""
####################################################
"""
2. Dia da semana (versão simples)

    Peça um número de 1 a 7

    Use elif para mostrar o dia correspondente

    Se for 1: "Domingo", 2: "Segunda", ..., 7: "Sábado"

    Se for outro número: "Dia inválido"
"""
"""
num_dia = int(input('Informe um número de 1 à 7: '))

if num_dia == 1:
    print('Domingo!')
elif num_dia == 2:
    print('Segunda!')
elif num_dia == 3:
    print('Terça!')
elif num_dia == 4:
    print('Quarta!')
elif num_dia == 5:
    print('Quinta!')
elif num_dia == 6:
    print('Sexta!')
elif num_dia == 7:
    print('Sábado!')
else:
    print('Número não equivale a um dia da semana')
"""
####################################################
"""
3. Par ou ímpar com validação

    Peça um número

    Use .isdigit() para validar

    Se for número, diga se é par ou ímpar

    Senão: "Entrada inválida"
"""
"""
num = input('Informe um número: ')

if num.isdigit():
    num = float(num)
    if num % 2 == 0:
        print('Seu número é par!')
    elif num % 2 != 0:
        print('Seu número é ímpar!')
    else:
        print('Seu número é zero!')
else:
    print('Entrada inválida!')
"""
####################################################
# NÍVEL 4-6: Aplicação
####################################################
"""
4.Calculadora de IMC completa

    Peça peso e altura

    Calcule IMC

    Classifique em todas as faixas:

        < 18.5: Abaixo do peso

        18.5 a 24.9: Peso normal

        25 a 29.9: Sobrepeso

        30 a 34.9: Obesidade Grau I

        35 a 39.9: Obesidade Grau II

            = 40: Obesidade Grau III
"""
"""
print('Informe o peso e a altura!')
peso = float(input('Peso (Kg): '))
altura = float(input('Altura (m): '))

IMC = peso / (altura ** 2)
print(f'Seu IMC é {IMC}')

if IMC < 18.5:
    print('Abaixo do peso!')
elif 18.5 <= IMC < 25:
    print('Peso normal!')
elif 25 <= IMC < 30:
    print('Sobrepeso!')
elif 30 <= IMC < 35:
    print('Obesidade Grau I!')
elif 35 <= IMC < 40:
    print('Obesidade Grau II!')
elif IMC >= 40:
    print('Obesidade Grau III!')
"""
####################################################
"""
5. Acesso permitido

    Peça idade e se tem autorização (sim/não)

    Considere: "sim" como True, "não" como False

    Permite se: idade >= 18 OU (idade < 18 E autorização == "sim")

    Mostre: "Acesso permitido" ou "Acesso negado"
"""
"""
idade = int(input('Informe sua idade: '))
autorizacao = input('Você tem autorização (sim/não): ').strip().lower()

if autorizacao == 'sim':
    autorizacao = True
elif (autorizacao == 'não') or (autorizacao == 'nao'):
    autorizacao = False

if (idade >= 18) or (autorizacao and idade < 18 ): # pq não da pra colocar "OR" e "AND" maiúsculo?
    print('Acesso permitido!')
else:
    print('Acesso negado!')
"""
####################################################
"""
6.Desconto progressivo

    Peça valor da compra e tipo de cliente (comum, vip, funcionario)

    Descontos:

        comum: sem desconto

        vip: 5%

        funcionario: 10%

    Mostre valor final
"""
"""
desconto_func = 10 # %
desconto_vip = 5   # %

valor_compra = float(input('Informe o valor da compra: '))
tipo_cliente = input('Informe o tipo de cliente: ').strip().lower()

if tipo_cliente == 'funcionario' or tipo_cliente == 'funcionário':
    valor_compra = valor_compra * (1 - desconto_func / 100)
    print(f'Valor a ser pago: R$ {valor_compra:.2f}')
elif tipo_cliente == 'vip':
    valor_compra = valor_compra * (1 - desconto_vip / 100)
    print(f'Valor a ser pago: R$ {valor_compra:.2f}')
elif tipo_cliente == 'comum':
    print(f'Valor a ser pago: R$ {valor_compra:.2f}')
"""
####################################################
# NÍVEL 7-8: Manipulação
####################################################
"""
7.Validação de senha forte

    Peça uma senha

    Verifique se tem:

        Pelo menos 8 caracteres (len())

        Pelo menos 1 número (pesquise o método .isdigit() em cada caractere? Dica: loop ainda não vimos, pense em outra forma)

    (Simplificado: podemos verificar se a string NÃO é só letras)
"""
"""
senha = input('Informe uma senha (apenas letras e números): ')

if (len(senha) >= 8) and (not (senha.isalpha()) and not (senha.isdigit())): # pesquisei se existia algo tipo isdigit só que para letras...
    print('Senha forte!')
else:
    print('Senha fraca!')
"""
####################################################
"""
8. Calculadora de imposto

    Peça renda anual

    Calcule imposto conforme:

        até 22.847,76: isento

        de 22.847,77 até 33.919,80: 7,5%

        de 33.919,81 até 45.012,60: 15%

        de 45.012,61 até 55.976,16: 22,5%

        acima: 27,5%

    Mostre valor do imposto
"""
"""
imp1 = 7.5  # %
imp2 = 15   # %
imp3 = 22.5 # %
imp4 = 27.5 # %

renda_anual = float(input('Informe renda anual: '))

if renda_anual < 22_847.76:
    print('Isento de imposto!')
elif 22_847.77 <= renda_anual <= 33_919.80:
    print(f'Imposto de: {imp1}%')
elif 33_919.81 <= renda_anual <= 45_012.60:
    print(f'Imposto de: {imp2}%')
elif 45_012.61 <= renda_anual <= 55_976.16:
    print(f'Imposto de: {imp3}%')
elif renda_anual > 55_976.16:
    print(f'Imposto de: {imp4}%')
"""
####################################################
# NÍVEL 9-10: Desafios
####################################################
"""
9. Validador de triângulo (completo)

    Peça 3 lados

    Primeiro, verifique se formam triângulo

    Se formarem, classifique:

        3 lados iguais: "Equilátero"

        2 lados iguais: "Isósceles"

        Todos diferentes: "Escaleno"

    Se não formarem: "Não é triângulo"
"""
"""
print('Validador de triângulo, forneça três valores para os lados: ')
lado1 = float(input('lado 1: '))
lado2 = float(input('lado 2: '))
lado3 = float(input('lado 3: '))

if lado1 < (lado2 + lado3) and lado2 < (lado1 + lado3) and lado3 < (lado1 + lado2):
    print('Os três lados formam um triângulo!')
    if lado1 == lado2 == lado3:
        print('Um triângulo equilátero!')
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        print('Um triângulo isóceles!')
    else:
        print('Um triângulo escaleno!')
else:
    print('Os três lados não formam um triângulo :(')
"""
####################################################
"""
10.DESAFIO FINAL: Sistema de notas com recuperação

    Peça 3 notas (0 a 10)

    Calcule média

    Regras:

        Média >= 7: "Aprovado direto"

        Média >= 5 e < 7: "Recuperação"

        Média < 5: "Reprovado direto"

    Se for recuperação, peça a nota da prova de recuperação

    Nova média = (média_original + nota_rec) / 2

    Se nova média >= 6: "Aprovado após recuperação"

    Senão: "Reprovado após recuperação"
"""
print('Informe as três notas:')
nota1 = float(input('nota 1: '))
nota2 = float(input('nota 2: '))
nota3 = float(input('nota 3: '))

media = (nota1 + nota2 + nota3)/3

if media >= 7:
    print('Aprovado Direto!')
elif 5 <= media < 7:
    print('Recuperação!')
    nota_recuperacao = float(input('Informe a nota da recuperação: '))
    nova_media = (media + nota_recuperacao) / 2
    if nova_media >= 6:
        print('Aprovado após recuperação!')
    else:
        print('Reprovado após recuperação!')
elif media < 5:
    print('Reprovado direto!')


