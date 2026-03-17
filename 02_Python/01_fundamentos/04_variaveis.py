"""
Módulo 1: Fundamentos (Primeiros Passos)
Aula 1.4: Variáveis
Data: 17/03/2026
"""

# ======================================================================================================================
#                                                        TEORIA
# ======================================================================================================================
print('-' * 45, 'TEORIA', '-' * 45)
# ===========================================================
# 1. CRIANDO VARIÁVEIS
# ===========================================================

nome = 'Vinícius'
idade_calculada = 26
altura = 1.75
estudante = True

print(nome)
print(idade_calculada)
print(altura)
print(estudante)

# ===========================================================
# 2. REATRIBUIÇÃO (a variável pode variar)
# ===========================================================

x = 10
print(f'x vale: {x}') #tipo INT

x = 'nome'
print(f'x vale: {x}') #tipo STR

x = 3.14
print(f'x vale: {x}') #tipo FLOAT

# ===========================================================
# 3. REGRAS PARA NOMES DE VARIÁVEIS
# ===========================================================

#Válidos
nome_completo = 'Vinícius Henrique Souza'
idade2 = 26
_privado = 'Não use fora de classes' # o que seria isso?
camelCase = 'Também funciona' #no caso você está se referindo à letra maiúscula no meio da string?
minhaVariavelLonga = 'ok'

## Inválidos (testar descomentando):

#2idade = 10 #não pode começar com número
#meu-nome = 'Vinícius' #não pode contar hífen
#class = 'Python' #a palavra 'class' é reservada
#nome completo = 'Maria' #não pode ter espaço

## Por convenção (não é obrigatório, mas se enquadra em boas práticas)
# Usar snake_case: nome_da_variavel #também usamos no SQL para nomear as colunas no SELECT
# Constante em MIÚSCULAS: PI = 3.14
# Nomes significativos (não utilizar a, b, c para nome das variáveis)

# ===========================================================
# 4. TIPOS QUE JÁ CONHECEMOS
# ===========================================================

# int (número inteiros)
ano = 2026
populacao = 8_000_000_000 #underline para legibilidade #muito interessante isso!
print(f'Ano: {ano}, tipo: {type(ano)}')
print(f'População: {populacao}, tipo: {type(populacao)}')

# float (números decimais)
pi = 3.1415926
temperatura = -5.5
print(f'Pi: {pi}, tipo: {type(pi)}')
print(f'temperatura = {temperatura}, tipo: {type(temperatura)}')

# str (strings - texto)
nome = 'Vinícius'
frase = 'Python é legal!'
multilinha = """Texto
com várias
linhas
"""
print(f'nome: {nome}, tipo: {type(nome)}')
print(f'frase: {frase}, tipo: {type(frase)}')
print(f'multilinha: {multilinha}, tipo: {type(multilinha)}')

# bool (booleanos - True/False)
ativo = True # é case-sensitive?
inativo = False
print(f'Ativo: {ativo}, tipo: {type(ativo)}')
print(f'Inativo: {inativo}, tipo: {type(inativo)}')

# type() - função que mostra o tipo
print(f'O tipo de ano é: {type(ano)}')

# ===========================================================
# 5. ATRIBUIÇÃO MÚLTIPLA (feature legal do Python)
# ===========================================================

# Jeito tradicional:
a = 1
b = 2
c = 3
print(a, b, c)

# Jeito Pythonico:
x, y, z = 10, 20, 30
print(x, y, z)

#troca de valores
a, b = 5, 10
print(f'Antes a = {a}, b = {b}')
a, b = b, a
print(f'Depois a = {a}, b = {b}')

#Em outras linguagens precisaríamos de uma variável temporária.

# ===========================================================
# 5. CONSTANTES (Não existem de verdade)
# ===========================================================

# Por convenção, usamos MAIÚSCULAS para "constantes"
PI = 3.1415
GRAVIDADE = 9.8
NOME_CURSO = 'Python para Dados'
print(f'PI = {PI}')
# Mas isso é apenas convenção - Python permite mudar:
PI = 3.14
print(f'PI foi alterado para {PI}')

# ======================================================================================================================
#                                                      EXERCÍCIOS
# ======================================================================================================================
print('-' * 45, 'EXERCÍCIOS', '-' * 45, end='\n\n')

#NÍVEL 1-3: Aquecimento

# 1. Crie variáveis para: o seu nome, ano que nasceu, cidade onde mora. Depois imprima uma frase com todas.

meu_nome = 'Vinicius'
ano_nascimento = 1999
cidade_nascimento = 'Lavras'

print(f'Me chamo {meu_nome}, nasci na cidade de {cidade_nascimento} no ano de {ano_nascimento}')


# 2. Crie uma variável preco com valor 49.90 e outra quantidade com 3. Calcule e imprima o total.

preco = 49.90
quantidade = 3

print(f'o valor total em estoque é: {preco * quantidade}')

# 3. Troque os valores de duas variáveis x e y usando atribuição múltipla.

x, y = 13, 27
print(f'x = {x} e y = {y}')
x, y = y, x
print(f'Agora x = {x} e y = {y}')

#NÍVEL 4-6: Aplicação

"""
4. Crie um conversor de temperatura:

        Variável celsius com um valor

        Calcule fahrenheit = celsius * 9/5 + 32

        Imprima: "X°C equivale a Y°F"
"""

celsius = 25.0
fahrenheit = (9/5) * celsius + 32 #organizei a fórmula no formato ax+b
print(f'{celsius}°C equivale a {fahrenheit}°F')

"""
5.Cálculo de IMC:

        Variáveis: peso (kg) e altura (m)

        Calcule imc = peso / altura**2

        Imprima com 2 casas decimais
"""
peso = 75 #(kg)
altura=1.76 #(m)
imc = peso / altura ** 2 #elevado à 2?
print(f'Meu IMC é {imc:.2f}')

"""
6. Calculadora de dias de vida:

        Variável idade em anos

        Calcule dias aproximadamente (idade * 365)

        Imprima: "Você tem aproximadamente X dias de vida"
"""
idade_calculada = 26 #anos
dias_vida = idade_calculada * 365
print(f'Eu tenho aproximadamente {dias_vida} dias de vida')

#NÍVEL 7-8: Manipulação

# 7. Crie 3 variáveis com nomes RUINS (ex: a, b, c) e depois renomeie para nomes bons nos comentários
a = 26 # minha_idade = 26
b = 2026 # ano_atual = 2026
c = 1999 # ano_nascimento = 1999

"""
8. Faça um programa que:

    Guarde o ano atual em uma variável

    Guarde seu ano de nascimento

    Calcule sua idade

    Verifique se você já fez aniversário esse ano (use uma variável boolean)

"""
ano_atual = 2026
ano_nascimento = 1999
idade_calculada = ano_atual - ano_nascimento
idade_atual = 26
print(f'Minha idade atual é {idade_atual}, esse ano eu faço {idade_calculada}')
#você queria que eu usasse algum tipo de lógica condicional aqui? Por favor, não vamos pular etapas.

#NÍVEL 9-10: Desafio

"""
    9. Crie um programa que calcula o tempo necessário para ler um livro:

        Variáveis: paginas (total), paginas_por_dia

        Calcule dias necessários

        Depois calcule semanas e dias_restantes

        Use divisão inteira (//) e resto (%)
"""
paginas_total = 370
paginas_por_dia = 15
dias_necessarios = paginas_total // paginas_por_dia

print(f'Dias necessários para a leitura completa: {dias_necessarios + 1}')
#mais 1 pq nesse caso específico o número é quebrado. E como estamos utilizando um caso fixo, creio não haver problema. Sei que na verdade preciso usar condicional aqui.


pagina_atual = 120
paginas_restantes = paginas_total - pagina_atual
dias_restantes = paginas_restantes // paginas_por_dia


print(f'Dias para terminar a leitura: {dias_restantes + 1}')


"""
10. DESAFIO FINAL: Cálculo de estatísticas básicas

        Crie 4 variáveis com notas de provas (ex: 7.5, 8.0, 6.5, 9.0)

        Calcule:

            Soma total

            Média

            Maior nota (sem usar max - pense em comparações)

            Menor nota (sem usar min)

        Imprima tudo formatado
"""
n1, n2, n3, n4 = 7.5, 8.0, 6.5, 9.0

soma_total = n1 + n2 + n3 + n4

media = soma_total / 4

print(f'As notas foram: {n1}, {n2}, {n3} e {n4}')
print(f'A soma total das notas foi: {soma_total}')
print(f'A média das notas foi: {media}')
print(f'A maior nota foi: {n4} e a menor foi: {n3}' ) #fiz manualmente, novamente, pois não acredito que não tenho o ferramental necessário ainda...