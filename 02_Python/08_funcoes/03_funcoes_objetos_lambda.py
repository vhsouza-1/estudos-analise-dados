"""
Módulo 8: Funções
Aula 8.3: Funções como Objetos e Lambda
Data: 07/04/2026
Objetivo: Aprender a usar funções como objetos e funções lambda
"""

# ==========================================
# 1. FUNÇÕES COMO OBJETOS
# ==========================================

print("="*50)
print("1. FUNÇÕES COMO OBJETOS")
print("="*50)

# Em Python, funções são objetos, podem ser atribuídas a variáveis
def saudacao(nome):
    return f'Olá, {nome}!'

# Atribuindo a função a uma variável (sem parenteses!)
minha_funcao = saudacao

# Agora podemos chamar a função pelo novo nome
print(minha_funcao('Ana'))
print(saudacao('Bruno'))

# Verificando se são o mesmo objeto
print(f'saudacao é minha_funcao? {saudacao is minha_funcao}')

# ==========================================
# 2. FUNÇÕES QUE RECEBEM FUNÇÕES
# ==========================================

print("\n" + "="*50)
print("2. FUNÇÕES QUE RECEBEM FUNÇÕES")
print("="*50)

# Podemos passar funções como argumento para outras funções
def aplicar_operacao(a, b, operacao):
    """Aplica a operação (que é uma função) a a e b"""
    return operacao(a, b)

def soma(x, y):
    return x + y

def multiplica(x, y):
    return x * y

print(f'soma: {aplicar_operacao(5, 3, soma)}')
print(f'multiplica: {aplicar_operacao(5, 3, multiplica)}')

# ==========================================
# 3. LAMBDA - FUNÇÕES ANÔNIMAS
# ==========================================

print("\n" + "="*50)
print("3. LAMBDA - FUNÇÕES ANÔNIMAS")
print("="*50)

# Lambda cria funções de uma linha sem nome

# Sintaxe: lambda parâmetros: expressão

# Função normal
def dobro(x):
    return x * 2

# Lambda equivalente
dobro_lambda = lambda x: x * 2

print(f'dobro(5): {dobro(5)}')
print(f'lambda dobro(5): {dobro_lambda(5)}')

# Lambda usada diretamente (sem atribuir variável)
print(f'lambda direto: {(lambda x: x * 3)(10)}')

# Lambda com múltiplos parâmetros
soma_lambda = lambda a, b: a + b
print(f'lambda soma: {soma_lambda(10, 20)}')

# ==========================================
# 4. USANDO LAMBDA COM sorted (revisão)
# ==========================================

print("\n" + "="*50)
print("4. LAMBDA COM sorted (revisão)")
print("="*50)

# Você já usou isso sem saber!
alunos = [
    {"nome": "Ana", "nota": 8.5},
    {"nome": "Bruno", "nota": 6.0},
    {"nome": "Carla", "nota": 9.0}
]

# Ordenar por nota usando lambda
ordenado = sorted(alunos, key=lambda x: x['nota'])
print('Ordenado por nota (crescente)')
for aluno in ordenado:
    print(f'    {aluno['nome']}: {aluno['nota']}')

# Ordenador por nome
ordenado_nome = sorted(alunos, key= lambda x: x['nome'])
print("\nOrdenado por nome:")
for aluno in ordenado_nome:
    print(f"  {aluno['nome']}: {aluno['nota']}")

# ==========================================
# 5. MAP() - APLICAR FUNÇÃO A CADA ELEMENTO
# ==========================================

print("\n" + "="*50)
print("5. MAP() - APLICAR FUNÇÃO A CADA ELEMENTO")
print("="*50)

# map aplica uma função a cada elemento de uma sequência

numeros = [1, 2, 3, 4, 5]

# Jeito tradicional (com loop)
quadrados = []
for n in numeros:
    quadrados.append(n**2)
print(f"Quadrados (tradicional): {quadrados}")

# Jeito com map (mais elegante)
def quadrado(x):
    return x ** 2

quadrados_map = list(map(quadrado, numeros))
print(f"Quadrados (map): {quadrados_map}")

# Com lambda (mais conciso)
quadrados_lambda = list(map(lambda x: x**2, numeros))
print(f'Quadrados (map + lambda): {quadrados_lambda}')

# map com string
nomes = ['ana', 'bruno', 'carla']
maiusculas = list(map(lambda nome: nome.upper(), nomes))
print(f'Maiúsculas: {maiusculas}')

# ==========================================
# 6. FILTER() - FILTRAR ELEMENTOS
# ==========================================

print("\n" + "="*50)
print("6. FILTER() - FILTRAR ELEMENTOS")
print("="*50)

# filter seleciona elementos que atendem a uma condição

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Jeito tradicional (com loop)
pares = []
for n in numeros:
    if n % 2 == 0:
        pares.append(n)
print(f'Pares (tradicional): {pares}')

# Jeito com filter
def eh_par(x):
    return x % 2 == 0

pares_filter = list(filter(eh_par, numeros))
print(f'Pares (filter): {pares_filter}')

# Com lambda (mais conciso)
pares_lambda = list(filter(lambda x: x % 2 == 0, numeros))
print(f'Pares (filter + lambda): {pares_lambda}')

# Filter com strings
palavras = ['casa', 'carro', 'sol', 'computador', 'gato']
longas = list(filter(lambda p: len(p) > 4, palavras))
print(f'Palavras com mais de 4 letras: {longas}')

# ==========================================
# 7. COMBINANDO MAP E FILTER
# ==========================================

print("\n" + "="*50)
print("7. COMBINANDO MAP E FILTER")
print("="*50)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Pegar os pares e elevar ao quadrado
# Jeito 1, filter depois map
pares_quadrados = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numeros)))
print(f'Pares elevados ao quadrado: {pares_quadrados}')

# Jeito 2: list comprehension, mais legível para esse caso
pares_quadrados_lc = [n**2 for n in numeros if n % 2 == 0]
print(f'Pares elevados ao quadrado com lc: {pares_quadrados_lc}')

# ==========================================
# 8. EXEMPLOS PRÁTICOS
# ==========================================

print("\n" + "="*50)
print("8. EXEMPLOS PRÁTICOS")
print("="*50)

# 8.1 Calculadora flexível com funções
print(f'\n--- Calculadora com funções armazenadas ---')
operacoes = {
    'soma': lambda a, b: a + b,
    'subtracao': lambda a, b: a - b,
    'multiplicacao': lambda a, b: a * b,
    'divisao': lambda a, b: a / b if b != 0 else 'Erro: divisão por zero'
}

print(f'10 + 5 = {operacoes['soma'](10, 5)}')
print(f"10 - 5 = {operacoes['subtracao'](10, 5)}")
print(f"10 * 5 = {operacoes['multiplicacao'](10, 5)}")
print(f"10 / 5 = {operacoes['divisao'](10, 5)}")

# 8.2 Processando lista de notas
print('\n--- Processando notas ---')
notas = [5.5, 8.0, 6.5, 9.0, 4.5, 7.0]

# Apenas aprovados (>= 7)
aprovados = list(filter(lambda n: n >= 7, notas))
print(f'Aprovados: {aprovados}')

# Arredondar todas as notas
arredondadas = list(map(lambda n: round(n), notas))
print(f'Arredondadas: {arredondadas}')

# 8.3 Transformando dados com map
print(f'\n--- Transformando dados ---')

alunos = [
    {'nome': 'ana', 'nota': 8.5},
    {'nome': 'bruno', 'nota': 6.0},
    {'nome': 'carla', 'nota': 9.0}
]

# Capitalizar nomes
alunos_capitalizados = list(map(lambda a: {'nome': a['nome'].capitalize(), 'nota': a['nota']}, alunos))
print(f'Alunos com nome capitalizados')
for a in alunos_capitalizados:
    print(f'  {a['nome']}: {a['nota']}')

# ==========================================
# 9. QUANDO USAR CADA UM
# ==========================================

print("\n" + "="*50)
print("9. QUANDO USAR CADA UM")
print("="*50)

"""
📌 List Comprehension (recomendado para a maioria dos casos):
    [expressão for item in lista if condição]

📌 map (útil quando você já tem uma função definida):
    list(map(funcao, lista))

📌 filter (útil quando você já tem uma função de filtro):
    list(filter(funcao_filtro, lista))

📌 Lambda (útil para funções simples de uma linha):
    lambda x: x * 2

💡 Dica: Prefira list comprehension quando possível - é mais legível.
Use map/filter quando você já tem uma função definida ou está trabalhando com
programação funcional.
"""

# ==========================================
# 10. RESUMO
# ==========================================

print("\n" + "="*50)
print("10. RESUMO")
print("="*50)

"""
✅ Funções são objetos: podem ser atribuídas a variáveis
✅ Funções podem receber outras funções como parâmetro
✅ lambda: função anônima de uma linha (lambda x: x*2)
✅ map(funcao, sequência): aplica função a cada elemento
✅ filter(funcao, sequência): filtra elementos que atendem à condição

📌 map e filter retornam iteradores (precisa converter para lista)
📌 List comprehension geralmente é mais legível que map/filter
📌 Lambda é ótimo para funções simples usadas uma única vez
"""
##########################################################################
# EXERCÍCIOS - AULA 8.3
##########################################################################
# NÍVEL 1-3: Aquecimento
##########################################################################
"""
1. Função como objeto

# Crie uma função "somar" que retorna a soma de dois números
# Atribua essa função a uma variável "calcular"
# Use a variável para calcular 10 + 20
"""
"""
def somar(a, b):
    return a + b

calcular = somar

print(calcular(10, 20))
"""
##########################################################################
"""
2. Lambda básico

# Crie uma lambda que recebe um número e retorna seu quadrado
# Atribua a uma variável e teste com 5
"""
"""
quadrado_lambda = lambda x: x ** 2
print(quadrado_lambda(5))
"""
##########################################################################
"""
3. map com lambda

# Dada a lista: numeros = [1, 2, 3, 4, 5]
# Use map com lambda para criar uma lista com o cubo de cada número
"""
"""
numeros = [1, 2, 3, 4, 5]

cubos = list(map(lambda x: x**3, numeros))
print(cubos)
"""
##########################################################################
# NÍVEL 4-6: Aplicação
##########################################################################
"""
4. filter com lambda

# Dada a lista: idades = [12, 18, 25, 16, 30, 15, 20, 17]
# Use filter para selecionar apenas as idades >= 18
"""
"""
idades = [12, 18, 25, 16, 30, 15, 20, 17]

maiores = list(filter(lambda i: i>=18, idades))
print(maiores)
"""
##########################################################################
"""
5. Função que recebe função

# Crie uma função "aplicar_a_lista" que recebe:
# - uma lista de números
# - uma função
# Retorna uma nova lista com a função aplicada a cada elemento
# Teste com lambda que dobra o número
"""
"""
def aplicar_a_lista(lista, funcao):
    return list(map(funcao, lista))

print(aplicar_a_lista([1, 2, 3, 4, 5], lambda x: x**2))
"""
##########################################################################
"""
6. map e filter combinados

# Dada a lista: numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Use map e filter para criar uma lista com os quadrados dos números ímpares
# Exemplo: [1, 9, 25, 49, 81]
"""
"""
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

quad_impares = list(map(lambda x: x**2, filter(lambda x: x % 2 != 0, numeros)))
print(quad_impares)
"""
##########################################################################
# NÍVEL 7-8: Manipulação
##########################################################################
"""
7. Processando lista de dicionários com map

# Dada a lista de produtos:
produtos = [
    {"nome": "celular", "preco": 1500},
    {"nome": "fone", "preco": 200},
    {"nome": "notebook", "preco": 3500}
]
# Use map para criar uma nova lista com os preços com 10% de desconto
# Mantenha a estrutura de dicionário
"""
"""
produtos = [
    {"nome": "celular", "preco": 1500},
    {"nome": "fone", "preco": 200},
    {"nome": "notebook", "preco": 3500}
]

produtos_10 = list(map(lambda p: {'nome': p['nome'], 'preco': p['preco']*(1 - 10/100)}, produtos))

for p in produtos_10:
    print(p)
"""
##########################################################################
"""
8. Filtrando e transformando strings

# Dada a lista: palavras = ["casa", "carro", "sol", "computador", "gato", "python", "ai"]
# Use filter para selecionar palavras com mais de 3 letras
# Use map para transformar essas palavras em maiúsculas
# Faça em uma única linha (encadeando map e filter)
"""
"""
palavras = ["casa", "carro", "sol", "computador", "gato", "python", "ai"]

palavras_3M = list(map(lambda p: p.upper(), filter(lambda p: len(p) > 3, palavras)))
print(palavras_3M)

"""
##########################################################################
# NÍVEL 9-10: Desafios
##########################################################################
"""
NÍVEL 9: Agendador de tarefas com funções

# Crie um sistema de agendamento de tarefas onde cada tarefa é uma função
# 
# 1. Crie um dicionário "tarefas" onde:
#    - As chaves são nomes das tarefas (strings)
#    - Os valores são funções que executam a tarefa
#
# 2. Crie as seguintes tarefas (use lambda para tarefas simples):
#    - "dobro": recebe um número e retorna o dobro
#    - "quadrado": recebe um número e retorna o quadrado
#    - "par_ou_impar": recebe um número e retorna "par" ou "impar"
#    - "fatorial": recebe um número e retorna o fatorial (use uma função normal para esta)
#
# 3. Crie uma função "executar_tarefa" que recebe:
#    - nome_da_tarefa (str)
#    - *args (argumentos para a tarefa)
#    - **kwargs (argumentos nomeados para a tarefa)
#    
#    A função deve:
#    - Verificar se a tarefa existe no dicionário
#    - Se existir, executar com os argumentos fornecidos e retornar o resultado
#    - Se não existir, retornar uma mensagem de erro
#
# 4. Teste o sistema com diferentes tarefas:
#    - executar_tarefa("dobro", 10)
#    - executar_tarefa("quadrado", 5)
#    - executar_tarefa("par_ou_impar", 7)
#    - executar_tarefa("fatorial", 5)
#    - executar_tarefa("inexistente", 10)
"""
"""
def fatorial(x):
    fat = 1
    for i in range(x, 1, -1):
        fat *= i
    return fat

tarefas = {
    'dobro': lambda x: x * 2,
    'quadrado': lambda x: x ** 2,
    'par_ou_impar': lambda x: 'par' if x % 2 == 0 else 'impar',
    'fatorial': fatorial
}

def executar_tarefa(funcao, num):
    if funcao in tarefas:
        return tarefas[funcao](num)
    else:
        return 'Erro, função não existe!'


print(executar_tarefa("dobro", 10))

print(executar_tarefa("quadrado", 5))

print(executar_tarefa("par_ou_impar", 7))

print(executar_tarefa("fatorial", 5))

print(executar_tarefa("inexistente", 10))
"""
##########################################################################
"""
10. DESAFIO FINAL: Sistema de pipeline de dados

# Crie um sistema que processa uma lista de números através de etapas
# 1. "etapas" é uma lista de funções (use lambda)
# 2. Crie uma função "processar" que recebe:
#    - dados (lista de números)
#    - etapas (lista de funções)
#    - Aplica cada função sequencialmente a TODOS os dados
# 3. Teste com as seguintes etapas:
#    - Filtrar apenas números pares (use filter)
#    - Elevar ao quadrado (use map)
#    - Filtrar apenas números > 10
#    - Somar 10 a cada número
# 
# Exemplo de uso:
# dados = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# etapas = [
#     ("filtro_par", lambda x: x % 2 == 0),
#     ("quadrado", lambda x: x ** 2),
#     ("filtro_maior_10", lambda x: x > 10),
#     ("soma_10", lambda x: x + 10)
# ]
# resultado = processar(dados, etapas)
# Resultado esperado: [26, 50, 74, 110] (explicação: 4²=16+10=26, 6²=36+10=46? Vamos calcular direito...)
"""

dados1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

etapas1 = [
    ("filtro_par", lambda x: x % 2 == 0),
    ("quadrado", lambda x: x ** 2),
    ("filtro_maior_10", lambda x: x > 10),
    ("soma_10", lambda x: x + 10)
]

def processar(etapas, dados):
    for i in range(len(etapas)):
        if type(etapas[i][1](1)) == bool:
            dados = list(filter(etapas[i][1], dados))

        else:
            dados = list(map(etapas[i][1], dados))
    return dados

print(processar(etapas1, dados1))

# Achei esse exercício bem interessante!