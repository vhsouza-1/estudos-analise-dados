"""
Bloco 4: Estatística para Dados
Módulo 0: NumPy Essencial (pré-requisito para Estatística)
Aula 0: Fundamentos de NumPy para Análise de Dados
Data: 12/05/2026
Objetivo: Aprender o essencial do NumPy para o dia a dia do analista de dados

CONTEÚDO:
1. O que é NumPy e por que usar
2. Arrays vs listas Python
3. Criando arrays (a partir de listas, ranges, zeros, ones)
4. np.random para simulação de dados
5. Indexação e slicing
6. Operações vetorizadas (sem loops!)
7. Broadcasting (a mágica do NumPy)
8. axis=0 vs axis=1 (O MAIS IMPORTANTE)
9. np.where() - condição vetorizada
10. Funções úteis: mean, std, sum, min, max
11. NumPy vs Pandas (quando usar cada um)
"""

import numpy as np
import pandas as pd

# ==========================================
# 1. O QUE É NUMPY E POR QUE USAR?
# ==========================================

print("="*50)
print("1. O QUE É NUMPY?")
print("="*50)

"""
NUMPY = NUMerical PYthon

É a biblioteca fundamental para computação científica em Python.
TODAS as outras bibliotecas (Pandas, Matplotlib, Scikit-learn) usam NumPy por baixo.

POR QUE USAR?

| Característica | Lista Python | Array NumPy |
|----------------|--------------|-------------|
| Velocidade     | Lenta (loop) | Rápida (vetorizada) |
| Memória        | Mais memória | Menos memória |
| Operações      | +, - só funciona para números | +, -, *, / elemento a elemento |
| Estatística    | Precisa de funções externas | embutidas (.mean(), .std()) |

RESUMO: NumPy é o MOTOR; Pandas é o CARRO.
"""

# ==========================================
# 2. ARRAYS VS LISTAS
# ==========================================

print("\n" + "="*50)
print("2. ARRAYS VS LISTAS - A DIFERENÇA FUNDAMENTAL")
print("="*50)

# Lista Python (você já conhece)
lista = [1, 2, 3, 4, 5]
print(f"Lista: {lista}")
print(f"Lista * 2: {lista * 2}")  # REPETE a lista, não multiplica os números!

# Array NumPy
arr = np.array([1, 2, 3, 4, 5])
print(f"\nArray: {arr}")
print(f"Array * 2: {arr * 2}")  # MULTIPLICA cada elemento!

# Isso é OPERAÇÃO VETORIZADA - o coração do NumPy

# ==========================================
# 3. CRIANDO ARRAYS
# ==========================================

print("\n" + "="*50)
print("3. CRIANDO ARRAYS")
print("="*50)

# 3.1 A partir de lista
arr_lista = np.array([10, 20, 30, 40, 50])
print(f"np.array([10,20,30,40,50]): {arr_lista}")

# 3.2 Arrays especiais
print(f"\nnp.zeros(5): {np.zeros(5)}")        # tudo zero
print(f"np.ones(5): {np.ones(5)}")          # tudo um
print(f"np.arange(10): {np.arange(10)}")     # 0 a 9 (igual range)
print(f"np.arange(2, 10, 2): {np.arange(2, 10, 2)}")  # start, stop, step
print(f"np.linspace(0, 10, 5): {np.linspace(0, 10, 5)}")  # 5 pontos entre 0 e 10

# 3.3 Arrays 2D (matrizes)
matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"\nMatriz 3x3:\n{matriz}")
print(f"Shape da matriz: {matriz.shape}")  # (linhas, colunas)

# ==========================================
# 4. np.random - SIMULANDO DADOS (CRUCIAL!)
# ==========================================

print("\n" + "="*50)
print("4. np.random - SIMULANDO DADOS")
print("="*50)

"""
Para estatística, você vai SIMULAR dados o tempo todo:
- Testar hipóteses
- Criar exemplos
- Validar cálculos
"""

np.random.seed(42)  # Garante resultados reproduzíveis

# 4.1 Distribuição normal (mais importante)
normal = np.random.normal(loc=0, scale=1, size=5)  # média=0, desvio=1, 5 valores
print(f"Normal: {normal.round(2)}")

# 4.2 Distribuição uniforme
uniforme = np.random.uniform(low=0, high=10, size=5)
print(f"Uniforme: {uniforme.round(2)}")

# 4.3 Números inteiros aleatórios
inteiros = np.random.randint(low=1, high=100, size=5)
print(f"Inteiros: {inteiros}")

# 4.4 Escolha aleatória de uma lista
opcoes = ['A', 'B', 'C', 'D']
escolhas = np.random.choice(opcoes, size=5)
print(f"Escolhas: {escolhas}")

# ==========================================
# 5. INDEXAÇÃO E SLICING
# ==========================================

print("\n" + "="*50)
print("5. INDEXAÇÃO E SLICING")
print("="*50)

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
print(f"Array: {arr}")

# Funciona IGUAL listas Python
print(f"arr[0]: {arr[0]}")        # primeiro elemento
print(f"arr[-1]: {arr[-1]}")      # último elemento
print(f"arr[2:5]: {arr[2:5]}")    # índices 2,3,4
print(f"arr[:4]: {arr[:4]}")      # primeiros 4
print(f"arr[5:]: {arr[5:]}")      # a partir do índice 5

# Indexação em 2D
matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"\nMatriz:\n{matriz}")
print(f"matriz[0, 0]: {matriz[0, 0]}")  # linha 0, coluna 0
print(f"matriz[1, 2]: {matriz[1, 2]}")  # linha 1, coluna 2
print(f"matriz[0, :]: {matriz[0, :]}")  # linha 0, todas colunas
print(f"matriz[:, 1]: {matriz[:, 1]}")  # todas linhas, coluna 1

# ==========================================
# 6. OPERAÇÕES VETORIZADAS (SEM LOOPS!)
# ==========================================

print("\n" + "="*50)
print("6. OPERAÇÕES VETORIZADAS")
print("="*50)

"""
Isso é o que torna o NumPy RÁPIDO.
Você opera no array INTEIRO de uma vez.
"""

arr = np.array([1, 2, 3, 4, 5])

# Operações aritméticas (elemento a elemento)
print(f"arr + 10: {arr + 10}")
print(f"arr * 3: {arr * 3}")
print(f"arr ** 2: {arr ** 2}")

# Operações entre arrays
arr2 = np.array([10, 20, 30, 40, 50])
print(f"arr + arr2: {arr + arr2}")
print(f"arr * arr2: {arr * arr2}")

# Comparações (retornam booleanos)
print(f"arr > 3: {arr > 3}")
print(f"arr == 3: {arr == 3}")

# ==========================================
# 7. BROADCASTING (A MÁGICA DO NUMPY)
# ==========================================

print("\n" + "="*50)
print("7. BROADCASTING - OPERANDO COM TAMANHOS DIFERENTES")
print("="*50)

"""
Broadcasting = NumPy expande automaticamente arrays menores para operar com maiores.

Exemplo clássico: subtrair a média de todos os elementos
"""

arr = np.array([10, 20, 30, 40, 50])
media = arr.mean()
print(f"Array: {arr}")
print(f"Média: {media}")

# Com broadcasting, subtrai a média de cada elemento
arr_centralizado = arr - media
print(f"Array - média: {arr_centralizado}")

# Exemplo com matriz (cada linha)
matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"\nMatriz:\n{matriz}")

# Subtrair a média de cada COLUNA
media_colunas = matriz.mean(axis=0)
print(f"Média das colunas: {media_colunas}")
print(f"Matriz - média das colunas:\n{matriz - media_colunas}")

# ==========================================
# 8. axis=0 vs axis=1 (O MAIS IMPORTANTE)
# ==========================================

print("\n" + "="*50)
print("8. axis=0 vs axis=1 - ENTENDA ISSO!")
print("="*50)

"""
Essa é a maior fonte de confusão para iniciantes.

REGRAS DE OURO:
- axis=0 → OPERA NAS LINHAS (vertical) → resultado tem 1 valor POR COLUNA
- axis=1 → OPERA NAS COLUNAS (horizontal) → resultado tem 1 valor POR LINHA
- Sem axis → opera em todos os elementos

IMAGINE UMA PLANILHA:
        Coluna0  Coluna1  Coluna2
Linha0    1        2        3
Linha1    4        5        6
Linha2    7        8        9
"""

matriz = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

print(f"Matriz:\n{matriz}\n")

# Sem axis (todos os elementos)
print(f"np.sum(matriz) SEM axis: {np.sum(matriz)}")  # soma tudo: 45

# axis=0 (operação nas LINHAS → coluna a coluna)
print(f"np.sum(matriz, axis=0): {np.sum(matriz, axis=0)}")  # [12, 15, 18]
# Explicação: col0: 1+4+7=12, col1: 2+5+8=15, col2: 3+6+9=18

# axis=1 (operação nas COLUNAS → linha a linha)
print(f"np.sum(matriz, axis=1): {np.sum(matriz, axis=1)}")  # [6, 15, 24]
# Explicação: linha0: 1+2+3=6, linha1: 4+5+6=15, linha2: 7+8+9=24

print("\n--- MÉDIAS POR COLUNA (axis=0) ---")
print(f"np.mean(matriz, axis=0): {np.mean(matriz, axis=0)}")  # [4., 5., 6.]

print("\n--- MÉDIAS POR LINHA (axis=1) ---")
print(f"np.mean(matriz, axis=1): {np.mean(matriz, axis=1)}")  # [2., 5., 8.]

# ==========================================
# 9. np.where() - CONDICIONAL VETORIZADO
# ==========================================

print("\n" + "="*50)
print("9. np.where() - SE ENTAO VETORIZADO")
print("="*50)

"""
np.where(condicao, valor_se_true, valor_se_false)
"""

arr = np.array([10, 25, 30, 15, 40, 20])

print(f"Array: {arr}")

# Condição simples: se > 20 vira 'Alto', senão 'Baixo'
classificacao = np.where(arr > 20, 'Alto', 'Baixo')
print(f"np.where(arr > 20, 'Alto', 'Baixo'): {classificacao}")

# Condição numérica: manter valores > 20, outros viram 0
filtrado = np.where(arr > 20, arr, 0)
print(f"np.where(arr > 20, arr, 0): {filtrado}")

# ==========================================
# 10. FUNÇÕES ÚTEIS DO NUMPY
# ==========================================

print("\n" + "="*50)
print("10. FUNÇÕES ÚTEIS DO NUMPY")
print("="*50)

arr = np.array([10, 20, 30, 40, 50])

# Estatísticas básicas
print(f"Array: {arr}")
print(f"np.mean(arr): {np.mean(arr)}")      # média
print(f"np.median(arr): {np.median(arr)}")  # mediana
print(f"np.std(arr): {np.std(arr):.2f}")    # desvio padrão
print(f"np.sum(arr): {np.sum(arr)}")        # soma
print(f"np.min(arr): {np.min(arr)}")        # mínimo
print(f"np.max(arr): {np.max(arr)}")        # máximo

# ==========================================
# 11. NUMPY VS PANDAS - QUANDO USAR CADA UM
# ==========================================

print("\n" + "="*50)
print("11. NUMPY VS PANDAS - QUAL USAR?")
print("="*50)

"""
REGRAS PRÁTICAS:

| Situação                                            | Use                 |
|-----------------------------------------------------|---------------------|
| Dados com cabeçalho, colunas nomeadas, tipos mistos | PANDAS              |
| Dados puramente numéricos, sem cabeçalho            | NUMPY               |
| Operações estatísticas em dados limpos              | NUMPY (mais rápido) |
| Limpeza, transformação, merge de dados              | PANDAS              |
| Preparar dados para machine learning                | NUMPY (via .values) |

NA PRÁTICA:
- Você vai usar PANDAS 80% do tempo
- Você vai usar NUMPY 20% do tempo (geralmente dentro do pandas)
"""

# Exemplo: acessar o array numpy por trás de um DataFrame
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
arr_df = df['A'].values  # ou df.to_numpy()
print(f"Array por trás do pandas: {arr_df}")
print(f"Tipo: {type(arr_df)}")

# ==========================================
# 12. RESUMO DA AULA
# ==========================================

print("\n" + "="*50)
print("12. RESUMO - NUMPY ESSENCIAL")
print("="*50)

"""
✅ O QUE VOCÊ APRENDEU:

1. Arrays vs Listas
   - list * 2 → repete
   - array * 2 → multiplica elemento a elemento

2. Criar arrays:
   - np.array(lista)
   - np.zeros(), np.ones(), np.arange(), np.linspace()

3. np.random (CRUCIAL para estatística):
   - np.random.normal(media, desvio, size)
   - np.random.uniform(min, max, size)
   - np.random.randint(min, max, size)
   - np.random.choice(lista, size)

4. Indexação e slicing:
   - Igual listas: arr[0], arr[2:5], arr[:4]
   - Em 2D: matriz[linha, coluna]

5. Operações vetorizadas (SEM LOOPS!):
   - arr + 10, arr * 2, arr ** 2
   - arr1 + arr2, arr1 * arr2

6. Broadcasting:
   - Operar arrays de tamanhos diferentes
   - Ex: arr - arr.mean()

7. axis=0 vs axis=1 (DECORE ISSO!):
   - axis=0 → vertical (por COLUNA)
   - axis=1 → horizontal (por LINHA)

8. np.where(condicao, true, false)

9. Funções: mean, median, std, sum, min, max

10. NumPy vs Pandas:
    - Pandas para dados do mundo real
    - NumPy para operações numéricas puras

📌 PARA O ANALISTA DE DADOS JR:
   - Você NÃO precisa ser expert em NumPy
   - Você PRECISA entender o básico (especialmente axis e broadcasting)
   - O resto você aprende sob demanda
"""

# ==========================================
# EXERCÍCIOS - AULA 0 (NUMPY ESSENCIAL)
# ==========================================

print("\n" + "="*50)
print("EXERCÍCIOS - NUMPY ESSENCIAL")
print("="*50)

# Dados para exercícios
np.random.seed(42)

########################################################################
# NÍVEL 1-3: Aquecimento
########################################################################

"""
1. Criando arrays básicos

# Crie os seguintes arrays usando NumPy:
# a) Um array com os números de 0 a 9
# b) Um array com 5 zeros
# c) Um array com 5 uns
# d) Um array com 8 números espaçados igualmente entre 0 e 100
"""

"""
arr_a = np.arange(1, 10, 1)
print(arr_a)

arr_b = np.zeros(5)
print(arr_b)

arr_c = np.ones(5)
print(arr_c)

arr_d = np.linspace(0, 100, 8)
print(arr_d)
"""

########################################################################

"""
2. Operações básicas

# Dado o array abaixo:
arr = np.array([2, 4, 6, 8, 10])

# Calcule:
# a) arr + 2
# b) arr * 3
# c) arr ** 2
# d) arr / 2
"""

"""
arr = np.array([2, 4, 6, 8, 10])

print(f'arr + 2: {arr + 2}')
print(f'arr * 3: {arr * 3}')
print(f'arr ** 2: {arr ** 2}')
print(f'arr / 2: {arr / 2}')
"""

########################################################################

"""
3. Indexação e slicing

# Dado o array:
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

# Selecione:
# a) O primeiro elemento
# b) Os últimos 3 elementos
# c) Os elementos do índice 2 ao 5
# d) Os elementos nas posições pares (índices 0,2,4,6,8)
"""

"""
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

print(f'O primeiro elemento: {arr[0]}')
print(f'Os últimos 3 elementos: {arr[-3:]}')
print(f'Os elementos do índice 2 ao 5: {arr[2:5]}')
print(f'Os elementos nas posições pares: {arr[range(0, len(arr), 2)]}')
"""

########################################################################
# NÍVEL 4-6: Aplicação
########################################################################

"""
4. Simulando dados com np.random

# Use np.random para simular:
# a) 20 valores de uma distribuição normal com média 50 e desvio 10
# b) 15 valores uniformemente distribuídos entre 0 e 1
# c) 10 números inteiros aleatórios entre 1 e 100
"""

"""
arr_a = np.random.normal(50, 10, 20)
print(f'20 valores de uma distribuição normal com média 50 e desvio 10:\n{arr_a}\n')

arr_b = np.random.uniform(0, 1, 20)
print(f'15 valores uniformemente distribuídos entre 0 e 1:\n{arr_b}\n')

arr_c = np.random.randint(0, 100, 10)
print(f'10 números inteiros aleatórios entre 1 e 100:\n{arr_c}\n')
"""

########################################################################

"""
5. Estatísticas básicas

# Dado o array:
dados = np.array([15, 22, 18, 25, 30, 28, 35, 40, 32, 38])

# Calcule e mostre:
# - Média
# - Mediana
# - Desvio padrão
# - Soma
# - Mínimo e máximo
"""

"""
dados = np.array([15, 22, 18, 25, 30, 28, 35, 40, 32, 38])

print(f'Média: {np.mean(dados)}')
print(f'Mediana: {np.median(dados)}')
print(f'Desvio padrão: {np.std(dados)}')
print(f'Soma: {np.sum(dados)}')
print(f'Mínimo: {np.min(dados)}')
print(f'Máximo: {np.max(dados)}')
"""

########################################################################

"""
6. Compreendendo axis

# Dada a matriz:
matriz = np.array([[5, 10, 15],
                   [20, 25, 30],
                   [35, 40, 45]])

# Calcule:
# a) A soma de todos os elementos (sem axis)
# b) A soma de cada coluna (axis=0)
# c) A soma de cada linha (axis=1)
# d) A média de cada coluna (axis=0)
# e) A média de cada linha (axis=1)
"""

"""
matriz = np.array([[5, 10, 15],
                   [20, 25, 30],
                   [35, 40, 45]])

print(f'Soma de todos os elementos (sem axis): {matriz.sum()}')
print(f'Soma de cada coluna (axis=0): {matriz.sum(axis=0)}')
print(f'Soma de cada linha (axis=1): {matriz.sum(axis=1)}')
print(f'Média de cada coluna (axis=0): {matriz.mean(axis=0)}')
print(f'Média de cada linha (axis=1): {matriz.mean(axis=1)}')
"""

########################################################################
# NÍVEL 7-8: Manipulação
########################################################################

"""
7. np.where() na prática

# Dado o array:
vendas = np.array([100, 250, 180, 300, 90, 450, 120, 350])

# Use np.where() para:
# a) Criar um array 'status' onde valores > 200 são 'Alto' e <= 200 são 'Baixo'
# b) Criar um array 'bonus' onde valores > 200 recebem 10% e <= 200 recebem 5%
"""

"""
vendas = np.array([100, 250, 180, 300, 90, 450, 120, 350])

status = np.where(vendas > 200, 'Alto', 'Baixo')

bonus = np.where(vendas > 200, vendas * 1.1, vendas * 1.05)

print(f'Vendas: {vendas}')
print(f'Status: {status}')
print(f'Valor com Bônus: {bonus}')
"""

########################################################################

"""
8. Broadcasting e normalização

# Dado o array:
arr = np.array([10, 20, 30, 40, 50])

# Use broadcasting para:
# a) Subtrair a média de cada elemento (centralizar)
# b) Dividir pelo desvio padrão (padronizar)
# c) Normalizar para escala 0-1: (x - min) / (max - min)
"""

"""
arr = np.array([10, 20, 30, 40, 50])

print(f'Subtrair a média de cada elemento: ')
arr_centralizada = arr - np.mean(arr)
print(arr_centralizada)

print(f'\nDividir pelo desvio padrão (z-score): ')
arr_padronizada = (arr - np.mean(arr)) / np.std(arr)
print(arr_padronizada)

print(f'\nNormalizar para escala 0-1: ')
arr_normalizada = (arr - np.min(arr))/(np.max(arr) - np.min(arr))
print(arr_normalizada)
"""

########################################################################
# NÍVEL 9-10: Desafios
########################################################################

"""
9. Simulação de dados para estatística

# Simule uma pesquisa com 1000 pessoas:
# - Idade: distribuição normal com média 35 e desvio 10
# - Renda: distribuição normal com média 5000 e desvio 1500 (mas nunca negativa)
# - Avaliação: números inteiros de 1 a 5 (distribuição uniforme)
#
# Depois, calcule:
# - Média, mediana e desvio da idade
# - Média, mediana e desvio da renda
# - Frequência de cada nota de avaliação
"""

"""
idades = np.random.normal(35, 10, 1000)
rendas = np.random.normal(5000, 1500, 1000)
avaliacoes = np.random.randint(1, 6, 1000)

# print(np.sum(idades <= 0)) # 0, nenhuma idade menor ou igual a zero
# print(np.sum(rendas <= 0)) # 0, nenhuma renda menor ou igual a zero

print(f'Idades:')
print(f' - Média: {np.mean(idades):.2f}')
print(f' - Mediana: {np.median(idades):.2f}')
print(f' - Desvio Padrão: {np.std(idades):.2f}')

print(f'\nRendas:')
print(f' - Média: {np.mean(rendas):.2f}')
print(f' - Mediana: {np.median(rendas):.2f}')
print(f' - Desvio Padrão: {np.std(rendas):.2f}')

print(f'\nFrequência de cada nota de avaliação:')

qnts = [np.sum(np.where(avaliacoes == i, True, False)) for i in range(1, 6)]

for i, qnt in enumerate(qnts, 1):
    print(f' - Frequência {i}: {qnt/len(avaliacoes)*100:.2f}%')
"""

########################################################################

"""
10. DESAFIO FINAL: Performance comparada

# Crie uma lista Python e um array NumPy com 1 milhão de elementos
# Compare o tempo para:
# - Multiplicar todos os elementos por 2
# - Calcular a média
# - Calcular a soma
#
# Dica: use time.time() ou %timeit (no notebook)
"""

arr_np = np.random.randint(1, 10, 1000000)
list_python = arr_np.tolist()

import time

inicio_m_p = time.time()

# Primeiro a lista do python

# Multiplicar por 2
list_python2 = []
for i in list_python:
    list_python2.append(i*2)
termino_m_p = time.time()
tempo_m_p = termino_m_p - inicio_m_p

# Calcular a média
inicio_mean_p = time.time()
mean_p = sum(list_python)/len(list_python)
termino_mean_p = time.time()
tempo_mean_p = termino_mean_p - inicio_mean_p

# Calcular a soma
inicio_sum_p = time.time()
soma_p = sum(list_python)
termino_sum_p = time.time()
tempo_sum_p = termino_sum_p - inicio_sum_p

# Agora a array do NumPy
# Multiplicar por 2
inicio_m_np = time.time()
arr_np_2 = arr_np * 2
termino_m_np = time.time()
tempo_m_np = termino_m_np - inicio_m_np

# Calcular a média
inicio_mean_np = time.time()
mean_np = np.mean(arr_np)
termino_mean_np = time.time()
tempo_mean_np = termino_mean_np - inicio_mean_np

# Calcular a soma
inicio_sum_np = time.time()
sum_np = np.sum(arr_np)
termino_sum_np = time.time()
tempo_sum_np = termino_sum_np - inicio_sum_np

print(f'Tempos para multiplicação por 2: ')
print(f' - Python: {tempo_m_p}s')
print(f' - NumPy: {tempo_m_np}s')
print(f' - Diferença: {abs(tempo_m_p - tempo_m_np)}s')
print(f' - Razão: {(tempo_m_np/tempo_m_p)*100:.2f}% do tempo')

print(f'\nTempos para calcular a média: ')
print(f' - Python: {tempo_mean_p}s')
print(f' - NumPy: {tempo_mean_np}s')
print(f' - Diferença: {abs(tempo_mean_p - tempo_mean_np)}')
print(f' - Razão: {(tempo_mean_np/tempo_mean_p)*100:.2f}% do tempo')

print(f'\nTempos para calcular a soma: ')
print(f' - Python: {tempo_sum_p}s')
print(f' - NumPy: {tempo_sum_np}s')
print(f' - Diferença: {abs(tempo_sum_p - tempo_sum_np)}s')
print(f' - Razão: {(tempo_sum_np/tempo_sum_p)*100:.2f}% do tempo')
