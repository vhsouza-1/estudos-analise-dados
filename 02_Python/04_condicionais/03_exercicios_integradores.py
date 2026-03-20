"""
Módulo 4: Condicionais
Exercícios Integradores
Data: 19/03/2026
Objetivo: Resolver problemas que misturam tudo que vimos
"""

"""
Exercício 1: Calculadora de Aposentadoria

Tema: Regras de transição

O usuário vai digitar:

    Idade

    Tempo de contribuição (anos)

    Sexo (M/F)

Regras:

    Homem: pode aposentar se idade >= 65 OU (idade >= 60 E tempo >= 35)

    Mulher: pode aposentar se idade >= 62 OU (idade >= 57 E tempo >= 30)

Saída: "Pode aposentar" ou "Não pode aposentar"

Desafio extra: Se não puder, mostre quantos anos faltam para a opção mais próxima.
"""
"""
idade = int(input('Informe a idade: '))
tempo = int(input('Informe o tempo de contribuição (anos): '))
sexo = input('Informe o gênero (M/F): ').strip().lower()

if sexo == 'm':
    if idade >= 65 or (idade >= 60 and tempo >= 35):
        print('Pode aposentar!')
    else:
        print('Não pode aposentar!')
        if idade >= 60:
            if (65 - idade) < (35 - tempo):
                print(f'Espere mais {65 - idade} anos! ')
            elif (65 - idade) > (35 - tempo):
                print(f'Contribua mais {35 - tempo} anos!')
            else:
                print(f'Espere mais {65 - idade} anos ou contribua mais {35 - tempo} anos!')
        elif idade < 60:
            if (65 - idade) < (60 - idade and 35 - tempo):
                print(f'Espere mais {65 - idade} anos!')
            elif (65 - idade) > (60 - idade and 35 - tempo):
                print(f'Espere mais {60 - idade} anos e contribua mais {35 - tempo} anos!')
            else:
                print(f'Espere mais {65 - idade} ou contribua mais {35 - tempo} anos!')
elif sexo == 'f':
    if idade >= 62 or (idade >= 57 and tempo >= 30):
        print('Pode aposentar!')
    else:
        print('Não pode aposentar!')
        if idade >= 57:
            if (62 - idade) < (30 - tempo):
                print(f'Espere mais {62 - idade} anos! ')
            elif (62 - idade) > (30 - tempo):
                print(f'Contribua mais {30 - tempo} anos!')
            else:
                print(f'Espere mais {62 - idade} anos ou contribua mais {30 - tempo} anos!')
        elif idade < 57:
            if (62 - idade) < (57 - idade and 30 - tempo):
                print(f'Espere mais {62 - idade} anos!')
            elif (62 - idade) > (57 - idade and 30 - tempo):
                print(f'Espere mais {57 - idade} anos e contribua mais {30 - tempo} anos!')
            else:
                print(f'Espere mais {62 - idade} ou contribua mais {30 - tempo} anos!')
else:
    print('Erro ao especificar gênero, tente novamente')
"""

###################################################################

"""
Exercício 2: Classificador de Triângulos com Validação Robusta

Tema: Validação + lógica + classificação

Peça 3 valores (podem ser decimais). Antes de classificar:

    Valide se são números (use .replace('.', '').isdigit() para permitir decimais)

    Valide se são positivos (todos > 0)

    Valide se formam triângulo (cada lado < soma dos outros dois)

Se passar em todas:

    Classifique em Equilátero, Isósceles ou Escaleno

Se falhar em qualquer validação, mostre qual foi o problema:

    "Entrada inválida: use apenas números"

    "Lados devem ser positivos"

    "Não forma triângulo"
"""
"""
def is_number(string):
    string_original = string
    string_limpa = string.strip()
    if not string_limpa:
        return False
    string_teste = string_limpa
    if string_teste[0] == '-':
        string_teste = string_teste[1:]
    if string_teste.count('.') == 1 and string_teste.replace('.', '').isdigit():
        return True
    return string_teste.isdigit()

# Cara eu não só tive que usar uma coisa que eu não sei o que é, como eu ainda tive que descobrir sozinho que ela estava errada
# e tive que pedir pra outro chat do deepseek corrigir a função pra mim pq ela não reconhecia numeros negativos como números...
# por favor, nunca mais faça isso de novo. Não adianta as coisas, não me faz usar coisas que eu ainda não estudei...


print('Validação de triângulo, informe 3 lados: ')
lado1 = input('lado 1: ')
lado2 = input('lado 2: ')
lado3 = input('lado 3: ')

if is_number(lado1) and is_number(lado2) and is_number(lado3):
    print('Todos os valores informados são números!')
    lado1 = float(lado1)
    lado2 = float(lado2)
    lado3 = float(lado3)
    if (lado1 > 0) and (lado2 > 0) and (lado3 > 0):
        print('Todos os valores informados são positivos não nulos!')
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
    else:
        print('Lados devem ser positivos!')
else:
    print('Entrada inválida: use apenas números!')
"""
###################################################################
"""
3.Exercício 3: Sistema de Empréstimo

Tema: Múltiplos critérios + taxas

Peça:

    Renda mensal

    Valor do empréstimo solicitado

    Número de parcelas

    Score de crédito (0 a 1000)

Regras:

    Valor da parcela = empréstimo / parcelas

    Parcela não pode ultrapassar 30% da renda

Aprovação:

    Se parcela > 30% da renda → "Reprovado: comprometimento alto"

    Senão, verifica score:

        Score >= 800: "Aprovado com taxa 5%"

        Score >= 600: "Aprovado com taxa 10%"

        Score >= 400: "Aprovado com taxa 15%"

        Score < 400: "Reprovado: score baixo"

Mostre: valor da parcela e taxa aplicada (se aprovado)
"""
"""
renda = float(input('Informe a renda mensal: '))
valor_emprestimo = float(input('Informe o valor do empréstimo solicitado: '))
num_parcelas = int(input('Informe o número de parcelas: '))
score = float(input('Informe o score (0 a 1000): '))

valor_parcela = valor_emprestimo / num_parcelas

if valor_parcela > 0.3 * renda:
    print('Reprovado: comprometimento alto')
else:
    if score >= 800:
        print('Aprovado com taxa 5%')
        print(f'valor da parcela: R$ {1.05 * valor_parcela}')
    elif score >= 600:
        print('Aprovado com taxa 10%')
        print(f'valor da parcela: R$ {1.10 * valor_parcela}')
    elif score >= 400:
        print('Aprovado com taxa 15%')
        print(f'valor da parcela: R$ {1.15 * valor_parcela}')
    elif score < 400:
        print('Reprovado: score baixo')
"""
#################################################################
"""
Exercício 4: Calculadora de Honorários Médicos

Tema: Tabela progressiva com regras

Médicos cobram por consulta com base no convênio:
Convênio	Valor base
Particular	R$ 300
Unimed	    R$ 200
SulAmérica	R$ 180
Outros	    R$ 150

Regras:

    Se for particular, valor base é fixo

    Para convênios, se paciente tiver menos de 18 anos, acréscimo de 20%

    Se tiver mais de 60 anos, acréscimo de 15%

    Se tiver plano especial (True/False), acréscimo de 10% sobre o valor já ajustado

Peça:

    Convênio (digite: particular, unimed, sulamerica, outros)

    Idade

    Plano especial? (sim/não)

Mostre o valor final da consulta.
"""
"""
v_particular = 300
v_unimed = 200
v_sulamerica = 180
v_outros = 150

convenio = input('Informe o convênio (se não tiver: particular): ').strip().lower()
idade = int(input('Informe a idade: '))
especial = input('Plano especial? (s/n)').strip().lower()

if especial == 's':
    especial = True
elif especial == 'n':
    especial = False

if convenio == 'particular':
    print(f'O valor da consulta é: R$ {v_particular}')
else:
    if idade < 18:
        if convenio == 'unimed':
            if especial:
                print(f'O valor da consulta é: R$ {(v_unimed * 1.2) * 1.10}')
            else:
                print(f'O valor da consulta é: R$ {v_unimed * 1.2}')
        elif convenio == 'sulamerica':
            if especial:
                print(f'O valor da consulta é: R$ {(v_sulamerica * 1.2)*1.1}')
            else:
                print(f'O valor da consulta é: R$ {v_sulamerica * 1.2}')
        elif convenio == 'outros':
            if especial:
                print(f'O valor da consulta é: R$ {(v_outros * 1.2) * 1.10}')
            else:
                print(f'O valor da consulta é: R$ {v_outros * 1.2}')
    elif 18 <= idade <= 60:
        if convenio == 'unimed':
            if especial:
                print(f'O valor da consulta é: R$ {(v_unimed) * 1.10}')
            else:
                print(f'O valor da consulta é: R$ {v_unimed}')
        elif convenio == 'sulamerica':
            if especial:
                print(f'O valor da consulta é: R$ {v_sulamerica*1.1}')
            else:
                print(f'O valor da consulta é: R$ {v_sulamerica}')
        elif convenio == 'outros':
            if especial:
                print(f'O valor da consulta é: R$ {v_outros*1.1}')
            else:
                print(f'O valor da consulta é: R$ {v_outros}')
    elif idade > 60:
        if convenio == 'unimed':
            if especial:
                print(f'O valor da consulta é: R$ {v_unimed * 1.15 * 1.1}')
            else:
                print(f'O valor da consulta é: R$ {v_unimed * 1.15}')
        elif convenio == 'sulamerica':
            if especial:
                print(f'O valor da consulta é: R$ {v_sulamerica * 1.15 * 1.1}')
            else:
                print(f'O valor da consulta é: R$ {v_sulamerica * 1.15}')
        elif convenio == 'outros':
            if especial:
                print(f'O valor da consulta é: R$ {v_outros * 1.15 * 1.1}')
            else:
                print(f'O valor da consulta é: R$ {v_outros * 1.15}')
"""
#####################################################################
"""
Exercício 5: Analisador de Desempenho Escolar com Recuperação e Conceitos

Tema: Decisões aninhadas + médias ponderadas

Peça:

    Nome do aluno

    3 notas (com pesos diferentes: peso 2, 3, 5)

    Frequência (%)

Calcule a média ponderada: (n1*2 + n2*3 + n3*5) / 10

Regras:

    Se frequência < 75%: "Reprovado por falta"

    Senão, analisa média:

        Média >= 8: "Aprovado com conceito A"

        Média >= 7: "Aprovado com conceito B"

        Média >= 6: "Aprovado com conceito C"

        Média >= 5: "Recuperação"

        Média < 5: "Reprovado por nota"

Se for recuperação:

    Peça nota da prova de recuperação (peso 1)

    Nova média = (média_original * 10 + nota_rec) / 11 (média ponderada considerando recuperação como peso 1 extra)

    Se nova média >= 6: "Aprovado após recuperação"

    Senão: "Reprovado após recuperação"

Extra: No final, mostre um resumo:
text

Aluno: João
Média: 7.3
Frequência: 80%
Resultado: Aprovado com conceito B
"""
peso1 = 2
peso2 = 3
peso3 = 5
peso_rec = 1
soma_peso = peso1 + peso2 + peso3

nome = input('Informe o nome do/a aluno/a: ')
print('Agora informe as três notas: ')
nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
nota3 = float(input('Nota 3: '))
frequencia = float(input('Informe a frequência(%): '))

media_pond = (nota1*peso1 + nota2*peso2 + nota3*peso3)/soma_peso

if frequencia < 75:
    print('Reprovado por falta!')
    estado = 'Reprovado por falta!'
else:
    if media_pond >= 8:
        estado = 'Aprovado com conceito A!'
    elif media_pond >= 7:
        estado = 'Aprovado com conceito B!'
    elif media_pond >= 6:
        estado = 'Aprovado com conceito C!'
    elif media_pond >= 5:
        print('Recuperação!')
        nota_rec = float(input('Informe a nota da prova de recuperação: '))
        media_rec = (media_pond * soma_peso + nota_rec)/(soma_peso + peso_rec)
        media_pond = media_rec
        if media_pond >= 6:
            estado = 'Aprovado após recuperação!'
        else:
            estado = 'Reprovado após a recuperação!'
    elif media_pond < 5:
        estado = 'Reprovado por nota!'

print(f'\nAluno/a: {nome}')
print(f'Média: {media_pond:.1f}')
print(f'Frequência: {frequencia:.2f}%')
print(f'Resultado: {estado}')

# Se a média do aluno for 5, quando ele for para a recuperação, mesmo que ele tire 10 a média dele vai ser no max 5.5
# Fazendo a conta no papel descobri qual o valor que a média deve ter para a recuperação ser viável:
# media_pond >= (6*(soma_peso + peso_rec) - nota_rec * peso_rec)/soma_peso
# O problema é que a nota_rec só é fornecida depois, então a gente teria que usar essa expressão para calcular qual range
# da nota dele e da nota de recuperação nós consideramos viável para passar.
# Implicitamente você está considerando que ele pode recuperar se a nota estiver entre 5 e 5.99
# Mas qual a nota na recuperação ele tem que tirar pra passar com 5, por exemplo? pq se ele tirar 10, ele não passa com 5...
# Como podemos implementar isso? Podemos mexer no peso da recuperação por exemplo...











