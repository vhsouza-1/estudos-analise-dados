"""
Módulo 2: Tipos de Dados - Aprofundamento
Data: 18/03/2026
Objetivo: ir além do básico de int, float, str e bool
"""

# ======================================================================================================================
#                                                        TEORIA
# ======================================================================================================================
print('-' * 45, 'TEORIA', '-' * 45)

# ====================================================
# 1. REVISÃO RÁPIDA
# ====================================================

# int
idade = 26
print(f'int: {idade}, tipo {type(idade)}')

# floar
altura = 1.75
print(f'floar: {altura}, tipo {type(altura)}')

# str
nome = 'Vinícius'
print(f'str: {nome}, tipo {type(nome)}')

# bool
estudante = True
print(f'bool: {estudante}, tipo {type(estudante)}')

print("\n" + "="*50 + "\n")

# ====================================================
# 2. APROFUNDAMENTO INT
# ====================================================

print('APROFUNDAMENTO INT' + '\n')

# 2.1 Diferentes bases numéricas

decimal = 42
binario = 0b101010 # prefixo 0b para binário
octal = 0o52       # prefixo 0o para octal
hexadecimal = 0x2A # prefixo 0x para hexadecimal

print(f'Decimal: {decimal}')
print(f'Binário: {binario}')
print(f'Octal: {octal}')
print(f'Hexadecimal: {hexadecimal}')

# 2.2 Números muito grandes (Python não tem limite prático)

numero_gigante = 10 ** 100
print(f'\nNúmero gigante: {numero_gigante}')
print(f'Tipo continua sendo: {type(numero_gigante)}')

# 2.3 Operador de divisão inteira vs resto

dividendo = 17
divisor = 5
quociente = dividendo // divisor
resto = dividendo % divisor
print(f'\n{dividendo} // {divisor} = {quociente} (divisão inteira)')
print(f'{dividendo} % {divisor} = {resto} (resto da divisão)')

# 2.4 Cuidado com divisão que parece inteira

print(f'\n10 / 2 = {10 / 2} (Sempre float, mesmo sendo exato)')

# ====================================================
# 3. APROFUNDAMENTO FLOAT
# ====================================================

print("\n" + "="*50 + "\n")
print('APROFUNDAMENTO FLOAT' + '\n')

# 3.1 O problema da precisão (clássico!)

print(f'\nPROBLEMA DA PRECISÃO:')
print(0.1 + 0.2)
print(f'0.1 + 0.2 == 0.3? {0.1 + 0.2 == 0.3}')

# 3.2 Como lidar com isso (para análise de dados)
# Solução 1: arredondar
resultado = 0.1 + 0.2
print(f'Arredondado: {round(resultado, 2)}') # mesma syntax do MySQL

# Solução 2: tolerância (para comparações)
def quase_iguais(a, b, tolerancia = 1e-10):
    return abs(a - b) < tolerancia

print(f'Comparação com tolerância: {quase_iguais(0.1 + 0.2, 0.3)}') # favor explicar brevemente haha

# 3.3 Notação científica
massa_terra = 5.97e24 # 5.97 * 10^24 # achei bem clean a forma de escrever
print(f'\nMassa da Terra: {massa_terra} kg')

# 3.4 Infinity e NaN (para tratamento de erros)
infinito_positivo = float('inf')
infinito_negativo = float('-inf')
nao_numero = float('nan') # por que tem aspas aqui?

print(f'\nInfinito positivo: {infinito_positivo}')
print(f'Infinito negativo: {infinito_negativo}')
print(f'Não é número: {nao_numero}') # o que essas coisas significam de fato?

# ====================================================
# 4. APROFUNDAMENTO STR
# ====================================================

print("\n" + "="*50 + "\n")
print('APROFUNDAMENTO STR' + '\n')

# 4.1 Diferentes formas de criar strings
simples = 'aspas simples'
duplas = "aspas duplas"
triplas = """aspas triplas
múltiplas linhas
"""
print(f'Simples: {simples}')
print(f'Duplas: {duplas}')
print(f'Triplas: {triplas}')

# 4.2 Caracteres de escape
print('\nCaracteres de escape:')
print('Linha 1\nLinha 2') # \n = nova linha
print('Colina 1\tColuna 2') # \t = tab
print(f'C:\\Users\\Code') # \\ = \ simples

# 4.3 Strings raw (ignoram escapes)
caminho_raw = r'C:\Users\Code\Documents'
print(f'\nString raw: {caminho_raw}') # as barras não escapam # pq elas escapam normalmente?

# 4.4 Métodos básicos de string (essenciais)
texto = '  Python para Análise de Dados   '
print(f'\nTexto original: "{texto}"')
print(f'upper(): "{texto.upper()}"') # maiúsculas
print(f'lower(): "{texto.lower()}"') # minúsculas
print(f'strip(): "{texto.strip()}"') # remove espaços nas pontas # no SQL é trim()
print(f'replace(): "{texto.replace('Python', 'Pandas')}"') # substitui
print(f'len(): {len(texto)} caracteres') # tamanho

# Nesses exemplos do 4.4 percebi que em algumas situações não é necessário fazer upper(texto), pode: texto.upper()
# O que é bem interessante... novidade para mim. Mas tem casos como o len(texto) que não pode ser feito texto.len()
# fale mais sobre isso, por favor.

# 4.5 Fatiamento de string (slicing) -
frase = 'Análise de Dados'
print(f'\nFrase: {frase}')
print(f'Primeiros 7 caracteres: "{frase[:7]}"') # do início até pos 7
print(f'A partir do 8° caracter: "{frase[8:]}"') # da pos 8 até o fim
print(f'Do 3° ao 10°: "{frase[3:11]}"') # intervalo
print(f'Últimos 5 caracteres: "{frase[-5:]}"') # índice negativo

# ====================================================
# 5. APROFUNDAMENTO BOOL
# ====================================================

print("\n" + "="*50 + "\n")
print('APROFUNDAMENTO BOOL' + '\n')

# 5.1 Tudo pode ser convertido para bool
print(f'Valores que são False:')
print(f'bool(0): {bool(0)}')
print(f'bool(0.0): {bool(0.0)}')
print(f'bool(""): {bool("")}')
print(f'bool(None): {bool(None)}') # o que é esse None?
print(f'bool([]): {bool([])}') # lista vazia (veremos depois)

print(f'\nValores que são True:')
print(f'bool(42): {bool(42)}')
print(f'bool(-1): {bool(-1)}')
print(f'bool("texto"): {bool("texto")}')
print(f'bool(" "): {bool(" ")}') # espaço em branco é True

# 5.2 Operadores lógicos com tipos não-bool
print(f'\nOperadores lógicos com tipos:')
print(f'"texto" and 42: {"texto" and 42}') # retorna 42 # pq? só por definição mesmo? já que os dois são True
print(f'"" or "alternativa": {"" or "alternativa"}') # faz sentido, pois "" é False

# 5.3 Curto-circuito (short-circuit)
def funcao_demorada():
    print('Executando função demorada...')
    return True
# Não entendi o 5.3

#O Python NÃO executa o lado direito se o esquerdo já define o resultado
print(f'False and funcao_demorada(): {False and funcao_demorada()}') # não executa
print(f'True or funcao_demorada(): {True or funcao_demorada()}') # não executa

# ====================================================
# 6. CONVERSÃO ENTRE TIPOS (casting)
# ====================================================

print("\n" + "="*50 + "\n")
print('APROFUNDAMENTO BOOL' + '\n')

# 6.1 str para int/float (cuidado!)
numero_str = '42'
print(f'"{numero_str}" para int: {int(numero_str)}')
print(f'"{numero_str}" para float: {float(numero_str)}')

# 6.2 int/float para str
numero = 3.14
print(f'\n{numero} para str: "{str(numero)}"')

# 6.3 bool para int (True=1, False=0)
print(f'\nbool(True) para int: {int(True)}')
print(f'bool(False) para int: {int(False)}')

# 6.4 Conversões que podem dar erro (descomente para testar)
# int("42.5")  # ValueError: invalid literal for int()
# int("texto")  # ValueError
# float("3,14")  # vírgula não funciona, precisa de ponto

# ====================================================
# 7. ARMADILHAS COMUNS (blindspots)
# ====================================================

print("\n" + "="*50 + "\n")
print('ARMADILHAS COMUNS' + '\n')

# 7.1 Tipo muda sem você perceber
x = 10
print(f'x = {x}, type: {type(x)}')
x = x / 2  # divisão sempre retorna float
print(f'x / 2 = {x}, type: {type(x)} (virou float!)')

# 7.2 Comparação de tipos diferentes
print("\n10 == '10'?", 10 == "10")  # False (tipos diferentes)
print("10 == 10.0?", 10 == 10.0)    # True (valores iguais, tipos diferentes) # no caso quando comparar int e float ele sempre vai olhar o valor ao inves do tipo?

# 7.3 Strings e números não se misturam
# print("10" + 5)  # TypeError!

# 7.4 Divisão por zero (já vimos)
# print(10 / 0)  # ZeroDivisionError

# 7.5 Precedência de operadores (lembre-se)
print(f"\n10 + 5 * 2 = {10 + 5 * 2}")  # multiplicação primeiro
print(f"(10 + 5) * 2 = {(10 + 5) * 2}")  # parênteses mudam

# ======================================================================================================================
#                                                      EXERCÍCIOS
# ======================================================================================================================
print('-' * 45, 'EXERCÍCIOS', '-' * 45, '\n\n')

#NÍVEL 1-3: Aquecimento

#1. Crie uma variável com o seu nome em MAIÚSCULAS. Use métodos de string para transformar em minúsculas e depois capitalize (primeira letra maiúscula).

meu_nome = 'VINICIUS'
print(f'Meu nome em maiúsculas: {meu_nome}')
print(f'Meu nome em minúsculas: {meu_nome.lower()}')
print(f'Meu nome formatado: {meu_nome[:1]}{meu_nome[1:].lower()}')


#2. Peça para o Python calcular 0.1 + 0.2 + 0.3 e depois 0.6. Eles são iguais? Por quê?

calc = 0.1 + 0.2 + 0.3
result = 0.6
print(f'{calc} e {result}, a diferença é: {result - calc}')
# eles são diferentes, pois existe uma flutuação devido ao problema de precisão.


#3. Teste bool("False") e bool(""). Explique por que são diferentes.

print(bool(False))
print(bool(""))
print(bool(False) == bool("")) # Na verdade, em certo sentido, eles são iguais...
#Na primeira é uma definição direta, pois False já é o próprio valor da bool,
#No segundo caso o operador bool() retorna False para uma string vazia.

# NÍVEL 4-6: Aplicação
"""
4.Crie uma calculadora de resto:

    Variável dividendo = 17, divisor = 5

    Calcule quantas vezes o divisor cabe no dividendo (divisão inteira)

    Calcule quanto sobra (resto)

    Imprima: "17 ÷ 5 = 3 inteiros e sobram 2"
"""
dividendo = 17
divisor = 5
div_inteira = 17 // 5
div_sobra = 17 % 5
print(f'17 ÷ 5 = {div_inteira} e sobram {div_sobra}')

"""
5.Extraia partes de uma string:

    texto = "Aprendendo Python para Análise de Dados"

    Extraia apenas a palavra "Python"

    Extraia apenas "Análise de Dados"
"""
texto = "Aprendendo Python para Análise de Dados"

print(f'Extraia apenas a palavra "{texto[11:17]}"')
print(f'Extraia apenas "{texto[23:]}"')

"""
6. Conversão perigosa:

    Peça para o usuário digitar um número (simule com variável fixa: "3.14")

    Tente converter para int (vai dar erro!)

    Depois converta para float corretamente
"""
VAR_FIXA = "3.14"
# print(int(VAR_FIXA)) # ValueError: invalid literal for int() with base 10: '3.14'
print(float(VAR_FIXA))

## NÍVEL 7-8: Manipulação

"""
7. Crie um programa que:

    Guarde uma temperatura em Celsius como string: "36.5"

    Converta para float

    Converta para Fahrenheit

    Imprima: "36.5°C equivale a X.X°F" (com 1 casa decimal)
"""
temp_celsius_str = '36.5'
temp_celsius = float(temp_celsius_str)
temp_fahrenheit = (9/5) * temp_celsius + 32
print(f'{temp_celsius:.1f}°C equivale a {temp_fahrenheit:.1f}°F') # ja saiu com uma casa, mas delimitei de qqr forma.

"""
8. Validação simples (sem if, só com bool):

    Crie uma variável entrada = "42"

    Verifique se a string é numérica (pesquise o método .isdigit())

    Se for, converta para int e mostre o dobro
"""
entrada = '42'
print(f'Entrada é numérica? {entrada.isdigit()}')
entrada_int = int(entrada)
print(f'O dobro da entrada é {2 * entrada_int}')

#NÍVEL 9-10: Desafios

"""
9. Detector de tipos:

    Crie 5 variáveis com tipos diferentes

    Para cada uma, imprima: "O valor X é do tipo Y"

    Use a função type() e formatação
"""
nome = 'Vinícius'
ano_nascimento = 1999
idade = 26
altura = 1.76
estudante = True

print(f'O valor de {nome} é do tipo {type(nome)}')
print(f'O valor de {ano_nascimento} é do tipo {type(ano_nascimento)}')
print(f'O valor de {idade} é do tipo {type(idade)}')
print(f'O valor de {altura} é do tipo {type(altura)}')
print(f'O valor de {estudante} é do tipo {type(estudante)}')

"""
10. DESAFIO FINAL: Calculadora de precisão

    Crie duas variáveis float com valores problemáticos: a = 0.1, b = 0.2

    Calcule soma = a + b

    Mostre a soma com 1, 5, 10 e 20 casas decimais

    Explique (em comentário) por que as casas decimais mudam
"""
a = 0.1
b = 0.2
soma = a + b
print(f'Soma com 1 casas decimais: {soma:.1f}')
print(f'Soma com 5 casas decimais: {soma:.5f}')
print(f'Soma com 10 casas decimais: {soma:.10f}')
print(f'Soma com 20 casas decimais: {soma:.20f}')

# As casas decimais mudam, mais especificamente de 10 para 20 casas decimais devido à própria natureza do tipo
# de variável que é o float, que é uma adaptação do computador que faz as contas baseado em binários