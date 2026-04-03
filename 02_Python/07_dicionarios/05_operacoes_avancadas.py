"""
Módulo 7: Dicionários
Aula 7.5: Operações Avançadas
Data: 03/04/2026
Objetivo: Aprender ferramentas avançadas para trabalhar com dicionários
"""

# ==========================================
# 1. O PROBLEMA QUE VAMOS RESOLVER
# ==========================================

print("="*50)
print("1. O PROBLEMA")
print("="*50)

# Sempre que queremos contar ou agrupar, fazemos:
palavras = ["banana", "maçã", "banana", "laranja", "banana", "maçã"]

# Jeito tradicional (verboso)
contagem = {}
for palavra in palavras:
    if palavra in contagem:
        contagem[palavra] += 1
    else:
        contagem[palavra] = 1

print(f"Tradicional: {contagem}")

# Isso funciona, mas é repetitivo.
# Vamos aprender ferramentas que simplificam isso.

from collections import defaultdict

# O defaultdict cria automaticamente um valor padrão para chaves inexistentes
# Você define o tipo do valor padrão (int, list, set, etc.)

# Exemplo 1: Contagem com defaultdict(int)
print('--- Contagem com defaultdict(int) ---')
contagem = defaultdict(int)
for palavra in palavras:
    contagem[palavra] += 1

print(f'Resultado: {dict(contagem)}')

# Exemplo 2: Agrupamento com defaultdict(list)
print("\n--- Agrupamento com defaultdict(list) ---")
pessoas = [("Ana", 25), ("Bruno", 30), ("Ana", 22), ("Carla", 28)]

grupo_por_nome = defaultdict(list)
for nome, idade in pessoas:
    grupo_por_nome[nome].append(idade)

print(f'Idades por nome: {dict(grupo_por_nome)}')

# Exemplo 3: Soma com defaultdict(float)
print('\n--- Soma com defaultdict(float) ---')
vendas = [("celular", 1500), ("fone", 200), ("celular", 800), ("fone", 100)]

total_por_produto = defaultdict(float)
for produto, valor in vendas:
    total_por_produto[produto] += valor

print(f'Total por produto: {dict(total_por_produto)}')

# ==========================================
# 3. COUNTER - Contador de frequências
# ==========================================

print("\n" + "="*50)
print("3. COUNTER - CONTADOR DE FREQUÊNCIAS")
print("="*50)

from collections import Counter

# Counter é um dicionário especializado em contar
palavras = ["banana", "maçã", "banana", "laranja", "banana", "maçã"]

# Criando um Counter
contador = Counter(palavras)
print(f'Counter: {contador}')
print(f'Contagem de "banana": {contador['banana']}')

# Métodos úteis do Counter
print(f'\n3 palavras mais comuns: {contador.most_common(3)}')
print(f'Elementos: {list(contador.elements())}')
print(f'Total de itens: {sum(contador.values())}')

# Counter a partir de uma string
texto = 'banana'
contador_letras = Counter(texto)
print(f'\nContagem de letras em "banana": {contador_letras}')

# Operações entre Counters
c1 = Counter(["a", "b", "a", "c"])
c2 = Counter(["a", "b", "b", "d"])
print(f'\nc1: {c1}')
print(f'c2: {c2}')
print(f'Soma: {c1 + c2}')
print(f'Subtração {c1 - c2}')
print(f'Interseção (mínimo): {c1 & c2}')
print(f'União (máximo): {c1 | c2}')

# ==========================================
# 4. GET APROFUNDADO
# ==========================================

print("\n" + "="*50)
print("4. GET APROFUNDADO")
print("="*50)

# Você já conhece o get básico
pessoa = {'nome': 'Ana', 'idade': 25}
print(f'get("nome"): {pessoa.get('nome')}')
print(f"get('telefone'): {pessoa.get('telefone')}")
print(f"get('telefone', 'não informado'): {pessoa.get('telefone', 'não informado')}")

# get com valores padrão complexos
# Podemos passar qualquer valor padrão, incluindo listas vazias
contatos = {}
telefone = contatos.get('Ana', [])
telefone.append('1199999999')
contatos['Ana'] = telefone
print(f'Contatos: {contatos}')

# Mas atenção: isso cria uma referência compartilhada!
# Cuidado com listas mutáveis como valor padrão
contatos = {}
telefone = contatos.get("Ana", [])  # se não existe, cria uma lista vazia
telefone.append("11999999999")
telefone.append("11888888888")
contatos["Ana"] = telefone
print(f"Ana: {contatos['Ana']}")

# ==========================================
# 5. SETDEFAULT - Inserir se não existir
# ==========================================

print("\n" + "="*50)
print("5. SETDEFAULT - INSERIR SE NÃO EXISTIR")
print("="*50)

# setdefault funciona como get, mas se a chave não existe, INSERE o valor padrão
pessoa = {'nome': 'Ana', 'idade': 25}

# Tenta pegar "telefone", se não existe, insere "não informado"
telefone = pessoa.setdefault('telefone', 'não informado')
print(f"Telefone retornado: {telefone}")
print(f"Dicionário após setdefault: {pessoa}")

# Se a chave já existe, setdefault não modifica
telefone = pessoa.setdefault("telefone", "outro número")
print(f"Telefone retornado: {telefone}")
print(f"Dicionário continua igual: {pessoa}")

# Uso prático: agrupamento com setdefault
print("\n--- Agrupamento com setdefault ---")
pessoas = [("Ana", 25), ("Bruno", 30), ("Ana", 22), ("Carla", 28)]
grupo = {}

for nome, idade in pessoas:
    grupo.setdefault(nome, []).append(idade)

print(f"Grupo: {grupo}")

# ==========================================
# 6. COMPARAÇÃO DAS FERRAMENTAS
# ==========================================

print("\n" + "="*50)
print("6. COMPARAÇÃO DAS FERRAMENTAS")
print("="*50)

dados = ["a", "b", "a", "c", "a", "b", "d"]

print("--- Jeito tradicional ---")
contagem = {}
for item in dados:
    if item in contagem:
        contagem[item] += 1
    else:
        contagem[item] = 1
print(contagem)

print("\n--- Jeito com defaultdict ---")
from collections import defaultdict
contagem = defaultdict(int)
for item in dados:
    contagem[item] += 1
print(dict(contagem))

print("\n--- Jeito com Counter ---")
from collections import Counter
contagem = Counter(dados)
print(contagem)

# Quando usar cada um:
# - Tradicional: para lógicas complexas ou legibilidade específica
# - defaultdict: para agrupamento ou quando precisa de um valor padrão
# - Counter: para contagem de frequências (é a ferramenta certa para isso!)

# ==========================================
# 7. EXEMPLOS PRÁTICOS
# ==========================================

print("\n" + "="*50)
print("7. EXEMPLOS PRÁTICOS")
print("="*50)

# 7.1. Analisando um texto
print("\n--- Análise de texto com Counter ---")
texto = """Python é uma linguagem de programação de alto nível.
Python é interpretado e tem uma sintaxe clara.
Python é usado em análise de dados e inteligência artificial."""

palavras = texto.lower().split()
palavras = [p.strip('.,!?;:') for p in palavras] # remove pontuação

contador = Counter(palavras)
print(f'5 palavras mais comuns: {contador.most_common(5)}')

# 7.2 Agrupando produtos por categoria com defaultdict
print('\n--- Produtos por categoria com defaultdict')
produtos = [
    ("celular", "eletrônicos"),
    ("camiseta", "vestuário"),
    ("notebook", "eletrônicos"),
    ("calça", "vestuário"),
    ("fone", "eletrônicos")
]

categorias = defaultdict(list)

for produto, categoria in produtos:
    categorias[categoria].append(produto)

print(dict(categorias))

# 7.3 Contagem de vendas por produto
print('\n--- Vendas por produto com defaultdict ---')
vendas = [
    ("celular", 1500),
    ("fone", 200),
    ("celular", 800),
    ("notebook", 3500),
    ("fone", 100),
    ("celular", 500)
]

total = defaultdict(int)

for produto, valor in vendas:
    total[produto] += valor

print(total)

# ==========================================
# 8. RESUMO
# ==========================================

print("\n" + "="*50)
print("8. RESUMO")
print("="*50)

"""
✅ defaultdict(tipo): cria valores padrão automáticos
   - defaultdict(int): padrão 0 (para contagem/soma)
   - defaultdict(list): padrão [] (para agrupamento)
   - defaultdict(set): padrão set() (para valores únicos)

✅ Counter: dicionário especializado em contagem
   - Counter(iterável) cria o contador
   - .most_common(n): retorna os n mais comuns
   - .elements(): retorna os elementos repetidos
   - Operações: +, -, &, |

✅ get(): acesso seguro com valor padrão
   - dicionario.get(chave, valor_padrao)

✅ setdefault(): como get, mas INSERE se não existir
   - dicionario.setdefault(chave, valor_padrao)

📌 Dicas:
- Para contagem simples: Counter
- Para agrupamento: defaultdict(list)
- Para soma/acumulação: defaultdict(int)
- Para acesso seguro: get()
"""

# ==========================================
# 9. EXERCÍCIOS
# ==========================================

print("\n" + "="*50)
print("9. EXERCÍCIOS")
print("="*50)

##############################################
# EXERCÍCIOS - AULA 7.5
##############################################
# NÍVEL 1-3: Aquecimento
##############################################
"""
1. Contagem com defaultdict
python

# Dada a lista: palavras = ["casa", "carro", "casa", "cachorro", "carro", "casa"]
# Use defaultdict(int) para contar quantas vezes cada palavra aparece
"""
"""
palavras = ["casa", "carro", "casa", "cachorro", "carro", "casa"]

contagem = defaultdict(int)

for palavra in palavras:
    contagem[palavra] += 1

print(dict(contagem))
"""
###########################################################
"""
2. Agrupamento com defaultdict(list)

# Dada a lista de tuplas: alunos = [("Ana", 8.5), ("Bruno", 6.0), ("Ana", 9.0), ("Carla", 7.5)]
# Use defaultdict(list) para agrupar as notas por aluno
"""
"""
alunos = [("Ana", 8.5), ("Bruno", 6.0), ("Ana", 9.0), ("Carla", 7.5)]

notas = defaultdict(list)

for nome, nota in alunos:
    notas[nome].append(nota)

print(notas)
"""
##############################################################
"""
3. Counter básico

# Dada a string: texto = "banana"
# Use Counter para contar quantas vezes cada letra aparece
# Mostre a letra mais comum
"""
"""
texto = 'banana'
contador_banana = Counter(texto)

print(dict(contador_banana))
print(f'Letra mais comum: {contador_banana.most_common(1)}'
"""
##############################################
# NÍVEL 4-6: Aplicação
##############################################
"""
4. Análise de vendas com defaultdict

# Dadas as vendas:
vendas = [
    ("celular", 1500, 2),  # (produto, preco, quantidade)
    ("fone", 200, 5),
    ("celular", 1500, 3),
    ("notebook", 3500, 1),
    ("fone", 200, 2)
]
# Use defaultdict(float) para calcular o faturamento total por produto
# Use defaultdict(int) para calcular a quantidade total vendida por produto
"""
"""
vendas = [
    ("celular", 1500, 2),  # (produto, preco, quantidade)
    ("fone", 200, 5),
    ("celular", 1500, 3),
    ("notebook", 3500, 1),
    ("fone", 200, 2)
]

faturamento_produto = defaultdict(float)
quantidade_produto = defaultdict(int)

for produto, preco, qnt in vendas:

    faturamento_produto[produto] += qnt * preco

    quantidade_produto[produto] += qnt

print(dict(faturamento_produto))
print(dict(quantidade_produto))

# Realmente isso aqui agiliza bastante o agrupamento...

"""
##################################################
"""
5. Counter com frases

# Peça uma frase ao usuário
# Use Counter para contar a frequência de cada palavra
# Mostre as 3 palavras mais comuns
# Mostre a quantidade total de palavras
"""
"""
frase = input('Informe uma frase: ')
palavras = frase.lower().split()
palavras = [p.strip('.,:?!-()[]{}''""') for p in palavras]

contador = Counter(palavras)

print(f'Frequência de cada palavra: {dict(contador)}')
print(f'3 palavras mais comuns: {contador.most_common(3)}')
print(f'Quantidade total de palavras: {sum(contador.values())}')

"""
########################################################
"""
6. get e setdefault na prática

# Dado o dicionário: estoque = {"celular": 10, "fone": 30}
# Use get para acessar "celular", "notebook" (com valor padrão 0)
# Use setdefault para adicionar "notebook" com valor 5 (se não existir)
# Use setdefault para tentar adicionar "celular" com valor 100 (já existe)
# Mostre o dicionário final
"""
"""
estoque = {"celular": 10, "fone": 30}

print(estoque.get('celular', 0))
print(estoque.get('notebook', 0))

print(estoque.setdefault('notebook', 5))
print(estoque.setdefault('celular', 100))

print(estoque)
"""
##############################################
# NÍVEL 7-8: Manipulação
##############################################
"""
7. Analisador de texto completo

# Peça um texto ao usuário (várias linhas, digite "FIM" para terminar)
# Use Counter para:
# - Contar frequência de palavras
# - Contar frequência de letras (ignorando espaços)
# - Contar frequência de caracteres especiais (.,!?;: etc.)
# Mostre as 5 palavras mais comuns, as 5 letras mais comuns e os 3 caracteres especiais mais comuns
"""
"""
texto = ''
while True:
    frase = input('Informe um texto(várias linhas, digite FIM para terminar): ')
    if frase.lower().strip() == 'fim':
        break
    else:
        texto += ' ' + frase

palavras = texto.lower().split()
palavras = [p.strip('.,:?!-()[]{}''""') for p in palavras]

contador_palavras = Counter(palavras)
print(f'Frequência de palavras: {dict(contador_palavras)}')
print(f'As 5 palavras mais comuns: {contador_palavras.most_common(5)}')

letras = texto.lower().strip('.,:?!-()[]{}''""').replace(' ', '')
letras = list(letras)

contador_letras = Counter(letras)
print(f'Frequência de letras: {dict(contador_letras)}')
print(f'As 5 letras mais comuns: {contador_letras.most_common(5)}')

caracteres = list(texto.lower().strip().replace(' ', ''))
especiais = [caracter for caracter in caracteres if not caracter.isalnum()]

contador_especiais = Counter(especiais)
print(f'Frequência de caracteres especiais: {dict(contador_especiais)}')
print(f'Os 5 caracteres especiais mais comuns: {contador_especiais.most_common(5)}')
"""
#################################################################
"""
8. Matriz de produtos com defaultdict

# Dada a lista de produtos com múltiplas categorias:
produtos = [
    ("celular", "eletrônicos", 1500),
    ("camiseta", "vestuário", 50),
    ("notebook", "eletrônicos", 3500),
    ("calça", "vestuário", 120),
    ("fone", "eletrônicos", 200),
    ("bone", "vestuário", 30)
]
# Use defaultdict(list) para criar um dicionário onde:
# - A chave é a categoria
# - O valor é uma lista de nomes de produtos
# - Crie também um dicionário com a soma dos preços por categoria (usando defaultdict(float))
"""
"""
produtos = [
    ("celular", "eletrônicos", 1500),
    ("camiseta", "vestuário", 50),
    ("notebook", "eletrônicos", 3500),
    ("calça", "vestuário", 120),
    ("fone", "eletrônicos", 200),
    ("bone", "vestuário", 30)
]

produtos_categoria = defaultdict(list)
somapreco_categoria = defaultdict(float)

for produto, categoria, preco in produtos:

    produtos_categoria[categoria].append(produto)

    somapreco_categoria[categoria] += preco

print(f'Produtos por categoria: {dict(produtos_categoria)}')
print(f'\nSoma dos preços por categoria: {dict(somapreco_categoria)}')
"""
##############################################
# NÍVEL 9-10: Desafios
##############################################
"""
9. Log de acessos ao site

# Dado um log de acessos (lista de dicionários):
log = [
    {"ip": "192.168.1.1", "pagina": "/home", "tempo": 10},
    {"ip": "192.168.1.2", "pagina": "/produtos", "tempo": 15},
    {"ip": "192.168.1.1", "pagina": "/contato", "tempo": 5},
    {"ip": "192.168.1.3", "pagina": "/home", "tempo": 8},
    {"ip": "192.168.1.1", "pagina": "/produtos", "tempo": 12},
    {"ip": "192.168.1.2", "pagina": "/home", "tempo": 7}
]
# Use defaultdict para calcular:
# - Total de acessos por IP
# - Total de tempo gasto por IP
# - Páginas visitadas por IP (use defaultdict(set) para valores únicos)
"""
"""
log = [
    {"ip": "192.168.1.1", "pagina": "/home", "tempo": 10},
    {"ip": "192.168.1.2", "pagina": "/produtos", "tempo": 15},
    {"ip": "192.168.1.1", "pagina": "/contato", "tempo": 5},
    {"ip": "192.168.1.3", "pagina": "/home", "tempo": 8},
    {"ip": "192.168.1.1", "pagina": "/produtos", "tempo": 12},
    {"ip": "192.168.1.2", "pagina": "/home", "tempo": 7}
]

acessos_ip = defaultdict(int)
tempo_ip = defaultdict(float)
paginas_ip = defaultdict(set)

for acesso in log:

    acessos_ip[acesso['ip']] += 1

    tempo_ip[acesso['ip']] += acesso['tempo']

    paginas_ip[acesso['ip']].add(acesso['pagina'])

print(acessos_ip)
print(tempo_ip)
print(paginas_ip)

# Você não me explicou o defaultdict(set) nem o .add(), tive que pesquisar pra descobrir como que era pra utilizar isso nesse caso.
# Repare que os elementos na tabela log nem se repetem, então nem tinha como eu descobrir a necessidade do set...
"""
############################################################
"""
10. DESAFIO FINAL: Análise de sentimentos
python

# Dado um dicionário de palavras positivas e negativas:
sentimentos = {
    "positivas": ["bom", "ótimo", "excelente", "maravilhoso", "feliz"],
    "negativas": ["ruim", "péssimo", "terrível", "triste", "horrível"]
}

# Peça ao usuário para digitar um texto (várias linhas, digite "FIM" para terminar)
# Use Counter para contar palavras
# Para cada palavra, verifique se está nas listas de sentimentos
# Calcule:
# - Quantidade de palavras positivas
# - Quantidade de palavras negativas
# - Sentimento geral (positivo se mais palavras positivas, negativo se mais negativas, neutro se empate)
# - Mostre as 3 palavras positivas mais usadas e as 3 negativas mais usadas
"""

sentimentos = {
    "positivas": ["bom", "ótimo", "excelente", "maravilhoso", "feliz"],
    "negativas": ["ruim", "péssimo", "terrível", "triste", "horrível"]
}

texto = ''
while True:
    frase = input('Digite um texto (várias linhas, digite "FIM" para terminar): ').strip()
    if frase.lower().strip() == 'fim':
        break
    else:
        texto += ' ' + frase

palavras = texto.lower().strip().split()
palavras = [p.strip(',.;:?!') for p in palavras]

contador_palavras = Counter(palavras)
print(f'\nContagem de palavras: {dict(contador_palavras)}')

contagem_sentimentos = defaultdict(int)
palavras_sentimentos = defaultdict(list)

for p in palavras:

    if p in sentimentos['positivas']:
        contagem_sentimentos['positivas'] += 1
        palavras_sentimentos['positivas'].append(p)
        
    elif p in sentimentos['negativas']:
        contagem_sentimentos['negativas'] += 1
        palavras_sentimentos['negativas'].append(p)

print(f'Contagem de palavras por sentimento: {dict(contagem_sentimentos)}')
print(f'Palavras por sentimento: {dict(palavras_sentimentos)}')

for sentimento, palavras in palavras_sentimentos.items():
    if sentimento == 'positivas':
        contador_positivas = Counter(palavras)
    elif sentimento == 'negativas':
        contador_negativas = Counter(palavras)

print(f'Contagem de palavras positivas: {dict(contador_positivas)}')
print(f'Contagem de palavras negativas: {dict(contador_negativas)}')

if dict(contagem_sentimentos)['positivas'] > dict(contagem_sentimentos)['negativas']:
    print(f'Sentimento geral: positivo')
elif dict(contagem_sentimentos)['positivas'] < dict(contagem_sentimentos)['negativas']:
    print(f'Sentimento geral: negativo')
else:
    print(f'Sentimento geral: neutro')

print(f'3 palavras positivas mais usadas: {contador_positivas.most_common(3)}')
print(f'3 palavras negativas mais usadas: {contador_negativas.most_common(3)}')