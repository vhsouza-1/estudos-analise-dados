"""
Módulo 8: Funções
Aula 8.1: Definindo e Chamando Funções
Data: 06/04/2026
Objetivo: Aprender a criar e usar funções
"""
from collections import Counter

# ==========================================
# 1. O PROBLEMA QUE FUNÇÕES RESOLVEM
# ==========================================

print("="*50)
print("1. O PROBLEMA (sem funções)")
print("="*50)

# Imagine que você precisa calcular a área de um retângulo várias vezes
# Sem funções, você repete o código:

# Retângulo 1: largura 5, altura 3
area1 = 5 * 3
print(f"Área do retângulo 1: {area1}")

# Retângulo 2: largura 7, altura 2
area2 = 7 * 2
print(f"Área do retângulo 2: {area2}")

# Retângulo 3: largura 4, altura 6
area3 = 4 * 6
print(f"Área do retângulo 3: {area3}")

# Problemas:
# 1. Código repetido
# 2. Se a fórmula mudar, precisa mudar em vários lugares
# 3. Difícil de manter

# ==========================================
# 2. CRIANDO UMA FUNÇÃO SIMPLES
# ==========================================

print("\n" + "="*50)
print("2. CRIANDO UMA FUNÇÃO SIMPLES")
print("="*50)

# Definindo uma função (não executa ainda)

def saudacao():
    print('Olá! Bem-vindo ao Python!')

# Chamando a função (aqui executa)
print('--- Chamando a função ---')
saudacao()

# ESTRUTURA
# def nome_da_funcao():
#     bloco de código indentado

# ==========================================
# 3. FUNÇÕES COM PARÂMETROS
# ==========================================

print("\n" + "="*50)
print("3. FUNÇÕES COM PARÂMETROS")
print("="*50)

# Parâmetros são como "vairáveis de entrada" da função:
def saudacao_personalizada(nome):
    print(f'Olá, {nome}!')

# Chamando com diferentes argumentos
saudacao_personalizada('Ana')
saudacao_personalizada('Bruno')

# Função com dois parâmetros
def soma(a, b):
    resultado = a + b
    print(f'{a} + {b} = {resultado}')

soma(5, 3)
soma(10, 20)

# ==========================================
# 4. FUNÇÕES COM RETORNO (return)
# ==========================================

print("\n" + "="*50)
print("4. FUNÇÕES COM RETORNO")
print("="*50)

# Funções podem retornar um valor (em vez de apenas printar)
def area_retangulo(largura, altura):
    return largura * altura

# O valor retornado pode ser usado
area = area_retangulo(5, 3)
print(f'Área: {area}')

# Pode ser usado diretamente em expressões
print(f'Dobro da área: {area_retangulo(5,3) * 2}')

# Pode ser usado em outras funções
def perimetro_retangulo(largura, altura):
    return 2 * (largura + altura)

area = area_retangulo(5, 3)
perimetro = perimetro_retangulo(5, 3)

print(f'Retângulo 5x3 área={area}, perímetro={perimetro}')

# ==========================================
# 5. DIFERENÇA ENTRE print E return
# ==========================================

print("\n" + "="*50)
print("5. print vs return")
print("="*50)

# Função que só printa (não retorna nada)
def saudacao_print(nome):
    print(f'Olá, {nome}!')

# Função que retorna (pode ser usada depois)
def saudacao_return(nome):
    return f'Olá, {nome}!'

print('--- Função com print() ---')
resultado_print =  saudacao_print('Ana')
print(f'Valor retornado: {resultado_print}') # None

# Com return, podemos guardar o resultado
mensagem = saudacao_return('Bruno')
print(mensagem.upper()) # Podemos usar métodos no resultado!

# ==========================================
# 6. FUNÇÕES COM MÚLTIPLOS RETORNOS
# ==========================================

print("\n" + "="*50)
print("6. MÚLTIPLOS RETORNOS")
print("="*50)

# Python permite retornar múltiplos valores (como tupla)
def calcular_retangulo(largura, altura):
    area = largura * altura
    perimetro = 2 * (largura + altura)
    return area, perimetro

# Recebendo os valores:
area, perimetro = calcular_retangulo(5, 3)
print(f'Área: {area}, Perímetro: {perimetro}')

# Ou recebendo como tupla
resultado = calcular_retangulo(5, 3)
print(f'Resultado como tupla: {resultado}')
print(f"Área: {resultado[0]}, Perímetro: {resultado[1]}")

# ==========================================
# 7. FUNÇÕES QUE CHAMAM OUTRAS FUNÇÕES
# ==========================================

print("\n" + "="*50)
print("7. FUNÇÕES QUE CHAMAM FUNÇÕES")
print("="*50)

def quadrado(x):
    return x ** 2

def cubo(x):
    return x ** 3

def soma_quadrado_cubo(x):
    return quadrado(x) + cubo(x)

print(f'quadrado(5): {quadrado(5)}')
print(f'cubo(5): {cubo(5)}')
print(f"soma_quadrado_cubo(5): {soma_quadrado_cubo(5)}")

# ==========================================
# 8. DOCSTRINGS - Documentando funções
# ==========================================

print("\n" + "="*50)
print("8. DOCSTRINGS - DOCUMENTAÇÃO")
print("="*50)

def calcular_imc(peso, altura):
    """
    Calcula o índice de Massa Corporal (IMC).

    Parâmetros:
        peso (float): Peso em quilogramas
        altura (float): Altura em metros

    Retorna:
        float: O valor do IMC
    """
    return peso / (altura ** 2)

# Acessando a documentação
print(calcular_imc.__doc__)

# Ou ainda
print()
help(calcular_imc)

imc = calcular_imc(75, 1.76)
print(f'IMC: {imc:.2f}')

# ==========================================
# 9. EXEMPLOS PRÁTICOS
# ==========================================

print("\n" + "="*50)
print("9. EXEMPLOS PRÁTICOS")
print("="*50)

# 9.1 Validador de idade
def eh_maior_de_idade(idade):
    """ Retorna True se idade >= 18, False caso contrário"""
    return idade >= 18

print(f"25 anos é maior? {eh_maior_de_idade(25)}")
print(f"16 anos é maior? {eh_maior_de_idade(16)}")

# 9.2 Classificador de nota
def classificar_nota(nota):
    """Classifica nota em A, B, C, D, F"""
    if nota >= 8:
        return 'A'
    elif nota >= 7:
        return 'B'
    elif nota >= 5:
        return 'C'
    else:
        return 'F'

print(f"Nota 8.5: {classificar_nota(8.5)}")
print(f"Nota 6.0: {classificar_nota(6.0)}")
print(f"Nota 3.5: {classificar_nota(3.5)}")

# 9.3. Conversor de temperatura
def celsius_para_fahrenheit(celsius):
    """Converte Celsius para Fahrenheit"""
    return celsius * 9/5 + 32

def fahrenheit_para_celsius(fahrenheit):
    """Converte Fahrenheit para Celsius"""
    return (fahrenheit - 32) * 5/9

print(f"25°C = {celsius_para_fahrenheit(25)}°F")
print(f"77°F = {fahrenheit_para_celsius(77)}°C")

# ==========================================
# 10. RESUMO
# ==========================================

print("\n" + "="*50)
print("10. RESUMO")
print("="*50)

"""
✅ Função: bloco de código reutilizável
✅ def: palavra-chave para definir função
✅ Parâmetros: valores de entrada (dentro dos parênteses)
✅ return: valor de saída (se não usar, retorna None)
✅ Chamada: nome_da_funcao(argumentos)
✅ Docstring: documentação da função (entre """ """)

📌 Regras:
- Funções fazem UMA coisa (princípio de responsabilidade única)
- Nomes descritivos (verbos no infinitivo: calcular, obter, validar)
- Use return, evite print dentro de funções (a menos que seja o propósito)
- Documente com docstrings
"""

######################################################
# EXERCÍCIOS - AULA 8.1
######################################################
# NÍVEL 1-3: Aquecimento
######################################################
"""
1. Função simples

# Crie uma função chamada "dizer_oi" que recebe um nome e imprime "Oi, [nome]!"
# Execute a função com seu nome
"""
"""
def dizer_oi(nome):
    print(f'Oi, {nome}!')

dizer_oi('Vinícius')
"""
######################################################
"""
2. Função com return

# Crie uma função "dobro" que recebe um número e retorna o dobro
# Teste com 5, 10 e 0
"""
"""
def dobro(x):
    return 2*x

print(dobro(5))
print(dobro(10))
print(dobro(0))
"""
######################################################
"""
3. Função com dois parâmetros

# Crie uma função "multiplica" que recebe dois números e retorna o produto
# Teste com (3, 4) e (5, 6)
"""
"""
def multiplica(x, y):
    return x * y

print(multiplica(3, 4))
print(multiplica(5, 6))
"""
######################################################
# NÍVEL 4-6: Aplicação
######################################################
"""
4. Conversor de moeda

# Crie uma função "real_para_dolar" que recebe um valor em reais e a cotação do dólar
# Retorna o valor em dólares
# Teste com (100, 5.20) e (250, 5.00)
"""
"""
def real_para_dolar(valor, cotacao):
    return valor * cotacao

print(real_para_dolar(100, 5.2))
print(real_para_dolar(250, 5))
print(real_para_dolar(100, 5.15))
"""
######################################################
"""
5. Calculadora de IMC

# Crie uma função "calcular_imc" que recebe peso e altura
# Retorna o IMC (peso / altura²)
# Crie uma função "classificar_imc" que recebe o IMC e retorna a classificação:
# - < 18.5: "Abaixo do peso"
# - 18.5 a 24.9: "Peso normal"
# - 25 a 29.9: "Sobrepeso"
# - >= 30: "Obesidade"
# Teste as funções
"""
"""
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

peso = 75
altura = 1.76
imc = calcular_imc(peso, altura)

def classificar_imc(imc):
    if imc < 18.5:
        return 'Abaixo do peso'
    elif 18.5 <= imc < 25:
        return 'Peso normal'
    elif 25 <= imc < 30:
        return 'Sobrepeso'
    else:
        return 'Obesidade'

print(classificar_imc(imc))
"""
######################################################
"""
6. Função que chama função

# Crie uma função "area_circulo" que recebe o raio e retorna a área (π * r²)
# Use π = 3.14159
# Crie uma função "volume_cilindro" que recebe raio e altura, e usa area_circulo para calcular o volume (área da base * altura)
# Teste com raio=3, altura=5
"""
"""
PI = 3.14159

def area_circulo(raio):
    return PI * (raio ** 2)

def volume_cilindro(raio, altura):
    area = area_circulo(raio)
    return area * altura

print(volume_cilindro(3, 5))
"""
######################################################
# NÍVEL 7-8: Manipulação
######################################################
"""
7. Validador de senha

# Crie uma função "validar_senha" que recebe uma senha e retorna True se:
# - Tem pelo menos 8 caracteres
# - Tem pelo menos uma letra maiúscula
# - Tem pelo menos um número
# Dica: use .isupper(), .isdigit()
# Teste com "senha123" (False), "Senha123" (True)
"""
"""
def validar_senha(senha):
    caracteres = list(senha)
    maiuscula = False
    numero = False
    if len(caracteres) >= 8:
        for c in caracteres:
            if c.isupper():
                maiuscula = True
            if c.isdigit():
                numero = True
    if maiuscula and numero:
        return True
    else:
        return False

senha = 'Senha123'

print(validar_senha(senha))

# Tive essa ideia. Como se costuma fazer?
"""
######################################################
"""
8. Calculadora de estatísticas

# Crie uma função "estatisticas" que recebe uma lista de números
# Retorna uma tupla com (menor, maior, soma, media)
# Teste com [10, 20, 30, 40, 50]
"""
"""
numeros = [10, 20, 30, 40, 50]

def estatisticas(numeros):
    return min(numeros), max(numeros), sum(numeros), sum(numeros)/len(numeros)

print(estatisticas(numeros))
"""
######################################################
# NÍVEL 9-10: Desafios
######################################################
"""
9. Calculadora de parcelas

# Crie uma função "calcular_parcelas" que recebe:
# - valor_total (float)
# - numero_parcelas (int)
# - juros_ao_mes (float, opcional, padrão 0)
#
# Retorna o valor de cada parcela (com juros compostos)
# Fórmula: parcela = valor_total * (1 + juros)^parcelas / parcelas
# Teste com: (1000, 3, 0.05) e (500, 6) (sem juros)
"""
"""
def calcular_parcelas(total, num_parcelas, juros_mes=0): # pesquisei e descobri o =valor_padrão
    """
 #   :param total: Valor total a ser parcelado
 #   :param num_parcelas: Número de parcelas
 #   :param juros_mes: Juros ao mês
 #   :return: Valor de cada parcela com juros compostos
"""

    parcela = (total * (1 + juros_mes) ** num_parcelas) / num_parcelas

    return parcela

print(calcular_parcelas(1000, 3, 0.05))
print(calcular_parcelas(500, 6))
"""
######################################################
"""
10. DESAFIO FINAL: Sistema de notas

# Crie as seguintes funções:
# 1. calcular_media(notas) - recebe lista de notas, retorna média
# 2. calcular_mediana(notas) - recebe lista ordenada, retorna mediana
# 3. calcular_moda(notas) - recebe lista, retorna o valor que mais aparece
# 4. classificar_aluno(media, faltas, limite_faltas=6, nota_minima=7) - retorna status
# 5. gerar_relatorio(nome, notas, faltas) - usa as funções acima e retorna um dicionário com todas as informações
#
# Teste com um aluno: notas=[8.5, 7.0, 9.0], faltas=3
"""
"""
nome = 'Bruno'
notas = [8.5, 7.0, 9.0, 7.0]
faltas = 3

def calcular_media(notas):
    media = sum(notas)/len(notas)
    return media

notas = sorted(notas)

def calcular_mediana(notas):
    a = len(notas) // 2
    if len(notas) % 2 == 0:
        mediana = (notas[a]+notas[a-1])/2
    else:
        mediana = notas[a]
    return mediana

def calcular_moda(notas):
    contador = Counter(notas)
    moda_qnt = contador.most_common(1)[0]
    moda = moda_qnt[0]
    return moda

def classificar_aluno(media, faltas, limite_faltas=6, nota_minima=7):
    if faltas > limite_faltas:
        status = 'Reprovado'
    else:
        if media >= nota_minima:
            status = 'Aprovado'
        else:
            status = 'Reprovado'
    return status

def gerar_relatorio(nome, notas, faltas):
    media = calcular_media(notas)
    mediana = calcular_mediana(notas)
    moda = calcular_moda(notas)
    status = classificar_aluno(media, faltas, limite_faltas=6, nota_minima=7)

    relatorio = {'nome': nome, 'media': media, 'mediana': mediana, 'moda': moda, 'status': status}
    return relatorio

print(gerar_relatorio(nome, notas, faltas))
"""















































































