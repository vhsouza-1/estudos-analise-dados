"""
Módulo 6: Listas
Aula 6.4: List Comprehension
Data: 26/03/2026
Objetivo: Aprender a criar listas de forma concisa e elegante
"""
from selectors import SelectSelector

# ==========================================
# 1. O PROBLEMA QUE LIST COMPREHENSION RESOLVE
# ==========================================

print("="*50)
print("1. O PROBLEMA (sem list comprehension)")
print("="*50)

# Queremos criar uma lista com os quadrados de 0 a 9

# Jeito tradicional com loop e append()
quadrados = []
for i in range(10):
    quadrados.append(i**2)
print(f'Quadrados tradicional: {quadrados}')

# Jeito com list comprehension (uma linha!)
quadrados_lc = [i**2 for i in range(10)]
print(f'Quadrados list comp.: {quadrados_lc}')

# ==========================================
# 2. SINTAXE BÁSICA
# ==========================================

print("\n" + "="*50)
print("2. SINTAXE BÁSICA")
print("="*50)

# Estrutura: [expressão for item in iterável]

# Exemplo 1: numeros de 0 a 9
numeros = [i for i in range(10)]
print(f'0 a 9: {numeros}')

# Exemplo 2: o dobro de cada número
dobro = [2*i for i in range(10)]
print(f'Dobro: {dobro}')

# Exemplo 3: caractere maiúsculo de cada letra
palavra = 'python'
maiusculas = [letra.upper() for letra in palavra]
print(f'Maiúsculas: {maiusculas}')

# ==========================================
# 3. COM CONDICIONAL (FILTRO)
# ==========================================

print("\n" + "="*50)
print("3. COM CONDICIONAL - FILTRANDO")
print("="*50)

# Sintaxe: [expressão for item in iterável if condição]

# Exemplo 1: apenas números pares
pares = [i for i in range(20) if i % 2 == 0]
print(f'Pares: {pares}')

# Exemplo 2: apenas palavras com mais de três letras
frutas = ["maçã", "banana", "kiwi", "laranja", "uva"]
longas = [fruta for fruta in frutas if len(fruta) > 3]
print(f'Frutas com mais de três letras: {longas}')

# Exemplo 3: apenas números maiores que 5
maiores = [i for i in range(10) if i > 5]
print(f'Maiores que 5: {maiores}')

# ==========================================
# 4. COM IF-ELSE (OPERADOR TERNÁRIO)
# ==========================================

print("\n" + "="*50)
print("4. COM IF-ELSE - TRANSFORMANDO")
print("="*50)

# Sintaxe: [expressão_if_true if condição else expressão_if_false for item in iterável]
# ATENÇÃO: o if-else vem antes do for!

# Exemplo 1: classificação números como par ou ímpar:
classificacao = ['par' if i % 2 == 0 else 'impar' for i in range(10)]
print(f'Classificação: {classificacao}')

# Exemplo 2: "maçã" vira "maçã doce", outros viram "fruta"
frutas = ["maçã", "banana", "kiwi", "laranja", "uva"]
transformadas = ['maçã doce' if fruta == 'maçã' else 'fruta' for fruta in frutas]
print(f'Transformadas: {transformadas}')

# Exemplo 3: Números positivos mantém, ímpares viram 0
ajustados = [numero if numero % 2 == 0 else 0 for numero in range(10)]
print(f'Ajustados: {ajustados}')

# ==========================================
# 5. DIFERENÇA ENTRE IF (FILTRO) E IF-ELSE (TRANSFORMAÇÃO)
# ==========================================

print("\n" + "="*50)
print("5. IF (FILTRO) vs IF-ELSE (TRANSFORMAÇÃO)")
print("="*50)

numeros = range(10)

# IF no final (filtra) - mantém ou remove itens
pares = [i for i in numeros if i % 2 == 0]
print(f'Pares: {pares}')

# IF-ELSE na expressão (transforma) - mantém TODOS os itens, mas transforma
par_ou_impar = ['par' if i % 2 == 0 else 'ímpar' for i in numeros]
print(f'Par ou ímpar: {par_ou_impar}')

# ==========================================
# 6. LIST COMPREHENSION COM MÚLTIPLOS FORs
# ==========================================

print("\n" + "="*50)
print("6. COM MÚLTIPLOS FORs")
print("="*50)

# Exemplo 1: todos os pares (x, y) onde x e y vão de 0 a 2
pares_xy = [(x,y) for x in range(3) for y in range (3)]
print(f'Pares (x,y): {pares_xy}')

# Exemplo 2: tabuada do 1 ao 3
tabuada = [f'{i} x {j} = {i*j}' for i in range(1,4) for j in range(1,4)]
print(f'Tabuada do 1 ao 3: {tabuada}')

# Exemplo 3: matriz identidade 3x3
identidade = [[1 if i==j else 0 for j in range(4)] for i in range(4)]
print(f'Matriz identidade: {identidade}')


# ==========================================
# 7. LIST COMPREHENSION COM FUNÇÕES
# ==========================================

print("\n" + "="*50)
print("7. COM FUNÇÕES")
print("="*50)

def quadrado(x):
    return x ** 2

def eh_par(x):
    return x % 2 == 0

numeros = [i for i in range(1,6)]

# Usando funções dentro da list comprehension
quadrados = [quadrado(n) for n in numeros]
print(f'Quadrados: {quadrados}')

pares_quadrados = [quadrado(n) for n in numeros if eh_par(n)]
print(f'Quadrado do pares: {pares_quadrados}')

# ==========================================
# 8. QUANDO NÃO USAR LIST COMPREHENSION
# ==========================================

print("\n" + "="*50)
print("8. QUANDO NÃO USAR")
print("="*50)

# 8.1. Muito complexa (difícil de ler):
# Ruim:
resultado = [x * y for x in range(10) for y in range(10) if x % 2 == 0 if y % 3 == 0]

# Bom: usa loop normal:
for x in range(10):
    if x % 2 == 0:
        for y in range(10):
            if y % 3 == 0:
                resultado.append(x * y)


# 8.2 Com efeitos colaterais (print, modificar variáveis externas)

# Ruim:
[print(i) for i in range(5)] # funciona, mas não é pythonico

# Bom:
for i in range(5):
    print(i)

# ==========================================
# 9. EXEMPLOS PRÁTICOS
# ==========================================

print("\n" + "="*50)
print("9. EXEMPLOS PRÁTICOS")
print("="*50)

# 9.1 Processando notas
print('\n--- Processando notas ---')
notas = [5.5, 8.0, 6.5, 9.0, 4.5, 7.0]
aprovados = [n for n in notas if n >= 7]
print(f'Aprovados: {aprovados}')

# 9.2 Arredondando notas
arredondadas = [round(n) for n in notas]
print(f'Notas arredondadas: {arredondadas}') # pq 5.5 arredondou pra 6, mas 6.5 pra 6 e 7.5 pra 7?

# 9.3 Classificando alunos
nomes = ["Ana", "Bruno", "Carla", "Daniel"]
notas = [8.5, 6.0, 7.5, 4.5]
status = ['Aprovado' if n >= 7 else 'Recuperação' if n >= 5 else 'Reprovado' for n in notas]
for nome, s in zip(nomes, status):
    print(f'{nome}: {s}')

# 9.4 Extraindo dados de strings
frase = 'Python é incrível para análise de dados'
palavras = frase.split()
tamanhos = [len(p) for p in palavras]
print(f'Palavras: {palavras}')
print(f'Tamanhos: {tamanhos}')

# ==========================================
# 10. RESUMO
# ==========================================

print("\n" + "="*50)
print("10. RESUMO")
print("="*50)

"""
✅ List comprehension: [expressão for item in iterável]
✅ Com filtro: [expressão for item in iterável if condição]
✅ Com if-else: [valor_if_true if condição else valor_if_false for item in iterável]
✅ Múltiplos for: [expressão for x in seq1 for y in seq2]
✅ Use quando for legível, evite quando ficar muito complexo

📌 Padrões comuns:
- [i for i in range(n)]: criar lista de números
- [f(i) for i in lista]: aplicar função a cada elemento
- [i for i in lista if condição]: filtrar elementos
- [a if cond else b for i in lista]: transformar cada elemento
"""
################################################
# EXERCÍCIOS - AULA 6.4
################################################
# NÍVEL 1-3: Aquecimento
################################################
"""
1. Quadrados perfeitos

# Crie uma lista com os quadrados dos números de 1 a 10 usando list comprehension
# Resultado esperado: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
"""
"""
quadrados = [i**2 for i in range(1,11)]
print(quadrados)
"""
################################################
"""
2. Maiúsculas e minúsculas

# Dada a string "Python é Fantástico"
# Crie uma lista onde cada caractere vira seu oposto:
# maiúsculo vira minúsculo e vice-versa
# Dica: use .upper() e .lower() e uma condicional
"""
"""
rase = 'Python é Fantástico'
caracteres = [a for a in frase]
oposto = [a.lower() if a.isupper() else a.upper() if a.islower() else a for a in caracteres]
print(frase)
print(caracteres)
print(oposto)
"""
#################################################
"""
3. Pares e ímpares

# Crie uma lista com os números de 0 a 20, mas:
# - Se for par, adicione o número
# - Se for ímpar, adicione o número multiplicado por 2
# Use list comprehension com if-else
"""
"""
numeros = [i if i % 2 == 0 else 2*i for i in range(21)]
print(numeros)
"""
################################################
# NÍVEL 4-6: Aplicação
################################################
"""
4. Filtro de temperaturas

# Dada uma lista de temperaturas em Celsius: [22, 18, 30, 15, 25, 28, 19, 32]
# Crie:
# - Lista apenas com temperaturas acima de 25°C
# - Lista com as temperaturas convertidas para Fahrenheit (C * 9/5 + 32)
# - Lista com "Quente" se >= 25, "Frio" se < 20, "Agradável" caso contrário
"""
"""
celsius = [22, 18, 30, 15, 25, 28, 19, 32]
celsius_over25 = [temp for temp in celsius if temp > 25]
celsius_fahr = [(9/5) * temp + 32 for temp in celsius]
celsius_qf = ['Quente' if temp >= 25 else 'Frio' if temp < 20 else 'Agradável' for temp in celsius]

print(celsius)
print(celsius_over25)
print(celsius_fahr)
print(celsius_qf)
"""
##################################################
"""
5. Extraindo dígitos de uma frase

# Dada a frase: "O código 123 foi gerado em 456 segundos"
# Use list comprehension para extrair apenas os dígitos (números) da frase
# Dica: .isdigit() verifica se um caractere é número
# Resultado esperado: ['1', '2', '3', '4', '5', '6']
"""
"""
frase = 'O código 123 foi gerado em 456 segundos'
digitos = [n for n in frase if n.isdigit()]
print(digitos)
"""
######################################################
"""
6. Matriz de multiplicação

# Use list comprehension aninhada para criar uma tabuada 5x5:
# linha 0: [0, 0, 0, 0, 0]
# linha 1: [0, 1, 2, 3, 4]
# linha 2: [0, 2, 4, 6, 8]
# linha 3: [0, 3, 6, 9, 12]
# linha 4: [0, 4, 8, 12, 16]
# Dica: cada elemento da matriz é linha * coluna
"""
"""
tabuada = [[i*j for j in range(5)] for i in range(5)]
print(tabuada)

tabuada = [[f'{i} x {j} = {i*j}' for j in range(5)] for i in range(5)]
for i in tabuada:
    print(i)
"""
################################################
# NÍVEL 7-8: Manipulação
################################################
"""
7. Palíndromos

# Dada uma lista de palavras: ["ana", "casa", "arara", "python", "radar", "carro"]
# Use list comprehension para criar:
# - Lista apenas com palíndromos (palavras que se leem igual ao contrário)
# - Dica: palavra == palavra[::-1]
# - Lista com o tamanho de cada palavra
"""
"""
palavras = ["ana", "casa", "arara", "python", "radar", "carro"]

palindromos = [palavra for palavra in palavras if palavra == palavra[::-1]]
tamanhos = [len(palavra) for palavra in palavras]

print(palindromos)
print(tamanhos)
"""
"""
8. Compras com desconto

# Dadas as listas:
produtos = ["Arroz", "Feijão", "Macarrão", "Leite", "Café"]
precos = [25.00, 8.50, 5.90, 4.50, 12.00]
quantidades = [3, 2, 5, 4, 2]

# Use list comprehension para criar uma lista de strings no formato:
# "Arroz: 3 x R$25.00 = R$75.00 (sem desconto)"
# Regras de desconto:
# - Produtos com preço > 20 têm 5% de desconto
# - Produtos com quantidade > 3 têm 10% de desconto
# - O desconto maior prevalece (se ambos, 10% é maior)
"""
"""
produtos = ["Arroz", "Feijão", "Macarrão", "Leite", "Café"]
precos = [25.00, 8.50, 5.90, 4.50, 12.00]
quantidades = [3, 2, 5, 4, 2]

lista = [f'{prod}: {qtd} x R${pre:.2f} = R${qtd*pre*(0.9):.2f} (com desconto 10%)' if qtd > 3 else
         f'{prod}: {qtd} x R${pre:.2f} = R${qtd*pre*(0.95):.2f} (com desconto 5%)' if pre > 20 else
         f'{prod}: {qtd} x R${pre:.2f} = R${qtd*pre:.2f} (sem desconto)'
         for prod, qtd, pre in zip(produtos, quantidades, precos)]
print(lista)
"""
################################################
# NÍVEL 7-8: Manipulação
################################################
"""
9. Matriz transposta

# Dada a matriz 3x4:
matriz = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

# Use list comprehension aninhada para criar a matriz transposta (4x3)
# Resultado esperado:
# [
#   [1, 5, 9],
#   [2, 6, 10],
#   [3, 7, 11],
#   [4, 8, 12]
# ]
"""
"""
matriz = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

matriz_inv = [[matriz[j][i] for j in range(3)] for i in range(4)]

print(matriz_inv)
"""
###########################################################
"""
10. DESAFIO FINAL: Analisador de texto

# Peça ao usuário para digitar uma frase.
# Use list comprehension (e outras ferramentas) para responder:
# 
# a) Quantas palavras tem a frase
# b) Lista com as palavras em maiúsculo
# c) Lista com o tamanho de cada palavra
# d) Lista com as palavras que têm mais de 5 letras
# e) Lista com a primeira letra de cada palavra
# f) Lista com "longa" se a palavra tiver > 5 letras, "curta" caso contrário
# 
# Mostre todas as respostas formatadas.
"""
"""
frase = input('Informe uma frase: ')
palavras = frase.split()
maiusculas = [palavra.upper() for palavra in palavras]
tamanhos = [len(palavra) for palavra in palavras]
grandes = [palavra for palavra in palavras if len(palavra) > 5]
primeira = [palavra[0] for palavra in palavras]
status = ['Longa' if len(palavra) > 5 else 'curta' for palavra in palavras]

print(f'A frase tem {len(palavras)} palavras!')
print(f'Maiúsculas: {maiusculas}')
print(f'Tamanhos: {tamanhos}')
print(f'Grandes: {grandes}')
print(f'Primeira letra: {primeira}')
print(f'Status: {status}')
"""





