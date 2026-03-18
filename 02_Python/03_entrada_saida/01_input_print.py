"""
Módulo 3: Entrada e Saída de Dados
Data: 18/03/2026
Objetivo: Aprender a receber dados do usuário e exibir resultados
"""

# ==========================================
# 1. O BÁSICO DO INPUT
# ==========================================

print("="*50)
print("1. INPUT BÁSICO")
print("="*50)

# Exemplo mais simples possível

#nome = input('Digite seu nome: ') # vou ir comentando tudo que é input pq se n vai travando o andamento das coisas
#print(f'Olá, {nome}! Prazer em te conhecer')

# O programa PARA e ESPERA o usuário digitar algo
# Só continua quando apertar ENTER

# ==========================================
# 2. O PROBLEMA FUNDAMENTAL: TUDO É STRING
# ==========================================

print("\n" + "="*50)
print("2. PROBLEMA: INPUT SEMPRE RETORNA STRING")
print("="*50)
"""
idade = input('Digite sua idade: ')
print(f'Você digitou {idade}')
print(f'Tipo: {type(idade)}')

# Solução: converter!
idade_int = int(idade)
print(f'Ano que vem você terá {idade_int+1} anos!')
"""
# ==========================================
# 3. CONVERSÃO SEGURA (o que pode dar errado)
# ==========================================

print("\n" + "="*50)
print("3. CONVERSÃO - CUIDADOS")
print("="*50)

# Exemplo 1: Funciona
# numero_certo = input(f'Digite um número inteiro: ')
# print(f'Convertido: {int(numero_certo)}')

# Exemplo 2: NÃO funciona
# numero_errado = input("Digite um número decimal (ex: 3.14): ")
# print(f"Convertido para int: {int(numero_errado)}")  # ValueError!

# ==========================================
# 4. MÚLTIPLOS INPUTS
# ==========================================

print("\n" + "="*50)
print("4. MÚLTIPLOS VALORES")
print("="*50)

# Jeito tradicional (um por um
# print('--- Cadastro Simples ---')
# nome = input('Nome: ')
# idade = int(input('Idade: ')) #tava em dúvida se poderia fazer isso, ja chamar o input() dentro de um int()
# cidade = input('Cidade: ')

# print("\n--- Dados Cadastrados ---")
# print(f"Nome: {nome}")
# print(f"Idade: {idade}")
# print(f"Cidade: {cidade}")

# ==========================================
# 5. INPUT COM ESPAÇOS (e strip)
# ==========================================

print("\n" + "="*50)
print("5. TRATANDO ESPAÇOS")
print("="*50)

# Usuário pode digitar com espaços sem querer
# nome_sujo = input('Digite seu nome completo: ')
# print(f'Com espaços: {nome_sujo}')
# print(f'Sem espaços: {nome_sujo.strip()}')

# ==========================================
# 6. PRINT AVANÇADO (revisão + novidades)
# ==========================================

print("\n" + "="*50)
print("6. PRINT AVANÇADO")
print("="*50)

# 6.1 sep (separator) - já vimos
print("Python", "é", "legal", sep=" - ")
print("Data", "Hora", "Valor", sep=" | ")

# 6.2 end (final de linha) - já vimos
print("Processando", end=" ")
print(".", end="")
print(".", end="")
print(".", end=" ")
print("Pronto!")

# 6.3 Combinando tudo
print("\n" + "="*30)
print("RELATÓRIO", end="\n\n")
print("Item", "Qtd", "Preço", sep=" | ")

# 6.4 f-strings com formatação (já usamos muito)
preco = 49.90
quantidade = 3
total = preco * quantidade
print(f"Total: R$ {total:.2f}")

# 6.5 Alinhamento (revisão)
print(f"\n{'Produto':<10} {'Preço':>8}")
print(f"{'Arroz':<10} {23.50:>8.2f}")
print(f"{'Feijão':<10} {8.75:>8.2f}")

# ==========================================
# 7. EXEMPLO PRÁTICO: CALCULADORA SIMPLES
# ==========================================

print("\n" + "="*50)
print("7. EXEMPLO PRÁTICO - CALCULADORA SIMPLES")
print("="*50)
"""
print('=== CALCULADORA DE MÉDIA ===')

nome_aluno = input('Nome do aluno: ')
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
nota3 = float(input('Terceira nota: '))

media = (nota1 + nota2 + nota3) / 3

print('\n' + '='*30)
print(f'Aluno: {nome_aluno}')
print(f'Notas: {nota1:.1f} | {nota2:.1f} | {nota3:.1f}')
print(f'Média: {media:.2f}')
print('='*30)
"""
# ======================================================================================================================
#                                                      EXERCÍCIOS
# ======================================================================================================================
print('-' * 45, 'EXERCÍCIOS', '-' * 45, '\n')

# NÍVEL 1-3: Aquecimento

"""
1. Saudação personalizada

    Peça o nome do usuário

    Imprima "Olá, [nome]! Seja bem-vindo!"
"""
# nome_usuario = input('Qual seu nome? ')
# print(f'Olá, {nome_usuario.strip()}! Seja bem-vindo!')

"""
2. Dobro de um número

    Peça um número inteiro

    Mostre o dobro (cuidado com a conversão!)
"""
# numero_int = int(input('Me dê um número inteiro: '))
# print(f'O dobro desse número é {2 * numero_int}!')

"""
3. Calculadora de idade

    Peça o ano de nascimento

    Peça o ano atual

    Calcule e mostre a idade aproximada
"""
# ano_nascimento = int(input('Qual seu ano de nascimento: '))
# ano_atual = int(input('Qual o ano atual: '))
# idade_aprox = ano_atual - ano_nascimento
# print(f'Você tem aproximadamente {idade_aprox} anos!')

# NÍVEL 4-6: Aplicação
"""
4. Conversor de temperatura

    Peça a temperatura em Celsius

    Converta para Fahrenheit

    Mostre com 1 casa decimal
"""
# temp_celsius = float(input('Qual a temperatura (em Celsius): '))
# temp_fahrenheit = (9/5) * temp_celsius + 32
# print(f'Essa temperatura é equivalente à {temp_fahrenheit:.1f}°F!')
"""
5. Calculadora de IMC interativa

    Peça nome, peso (kg) e altura (m)

    Calcule IMC = peso / altura²

    Mostre: "Olá [nome], seu IMC é X.XX"
"""
# nome = input('Informe seu nome: ')
# peso = float(input('Informe seu peso: '))
# altura = float(input('Informe sua altura: '))
# IMC = peso / (altura ** 2) # parentese só por garantia
# print(f'Olá {nome}, seu IMC é {IMC:.2f}')

"""
6.Conta de restaurante

    Peça o valor da conta

    Peça a porcentagem da gorjeta (ex: 10, 15, 20)

    Calcule total + gorjeta

    Mostre: "Total: R$ X.XX | Gorjeta: R$ Y.YY"
"""
# valor_conta = float(input('Informe o valor da conta: '))
# pct_gorjeta = float(input('Informe a porcentagem da gorjeta: '))
# valor_gorjeta = (pct_gorjeta/100) * valor_conta
# valor_total = valor_conta + valor_gorjeta
# print(f'Total: R$ {valor_conta:.2f} | Gorjeta: R$ {valor_gorjeta:.2f} | Total com gorjeta: R$ {valor_total:.2f}')

#NÍVEL 7-8: Manipulação

"""
7. Validação simples (sem if)

    Peça um número

    Tente converter para int

    Use .isdigit() para verificar se é possível (pesquise!)
"""
# num = input('Informe um número: ')
# num_int = int(num)
# print(f'O número informado é um número válido? {num.isdigit()}')
# não encontrei como fazer isso sem o uso de condicional ou while (que tbm não vimos)

"""
8. Calculadora de parcelas

    Peça valor total da compra

    Peça número de parcelas

    Calcule valor por parcela

    Mostre: "X parcelas de R$ Y.YY"
"""
# valor_compra_total = float(input('Informe o valor total da compra: '))
# numero_parcelas = int(input('Informe o número de parcelas: '))
# valor_parcela = valor_compra_total / numero_parcelas
# print(f'{numero_parcelas} de R$ {valor_parcela:.2f}')

# NÍVEL 9-10: Desafios

"""
9. Calculadora de tempo de viagem

    Peça distância (km)

    Peça velocidade média (km/h)

    Calcule tempo = distância / velocidade

    Mostre em horas e minutos (ex: "2h30min")

    Dica: use divisão inteira (//) e resto (%)
"""
# distancia = float(input('Informe a distância (em km): '))
# vel_media = float(input('Informe a velocidade média (em km/h): '))
# tempo_viagem_h = int(distancia // vel_media)
# tempo_viagem_m = int((distancia % vel_media/vel_media) * 60) #pega o resto da divisão e multiplica por 60 para ter o equivalente em min.
# print(f'O tempo de viagem é de {tempo_viagem_h}h{tempo_viagem_m}min') # bem divertido hehe

"""
10. DESAFIO FINAL: Calculadora de troco

    Peça valor total da compra

    Peça valor pago pelo cliente

    Calcule troco = pago - total

    Mostre o troco em notas simuladas (quantas notas de 100, 50, 20, 10, 5, 2, 1)

    Dica: use divisão inteira e resto sucessivamente
"""
valor_compra = float(input('Informe o valor total da compra: '))
valor_pago = float(input('Informe o valor pago pelo cliente: '))

troco_total = valor_pago - valor_compra

qnt_100 = int(troco_total // 100)

qnt_50 = int((troco_total % 100) // 50)

qnt_20 = int(((troco_total % 100) % 50) // 20)

qnt_10 = int((((troco_total % 100) % 50) % 20) // 10)

qnt_5 = int(((((troco_total % 100) % 50) % 20) % 10) // 5)

qnt_2 = int((((((troco_total % 100) % 50) % 20) % 10) % 5) // 2)

qnt_1 = int(((((((troco_total % 100) % 50) % 20) % 10) % 5) % 2) // 1)

print(f'Seu troco pode ser dado em {qnt_100}*100 + {qnt_50}*50 + {qnt_20}*20 + {qnt_10}*10 + {qnt_5}*5 + {qnt_2}*2 + {qnt_1}*1')

# Acho que deu certo esse aqui, bem legal hehe. O print() do final ficou meio preguiçoso, mas deu para entender, né? haha