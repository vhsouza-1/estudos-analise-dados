"""
Módulo 7: Dicionários
Aula 7.2: Percorrendo Dicionários
Data: 31/03/2026
Objetivo: Aprender a percorrer e explorar dicionários
"""
# ==========================================
# 1. PERCORRENDO CHAVES
# ==========================================

print("="*50)
print("1. PERCORRENDO CHAVES")
print("="*50)

pessoa = {"nome": "Ana", "idade": 25, "cidade": "São Paulo"}

# Jeito 1: for direto (percorre as chaves)
print('--- Percorrendo chaves ---')
for chave in pessoa:
    print(f'Chave: {chave} -> Valor: {pessoa[chave]}')

# Jeito 2: usando .keys() (mais explícito)
print('\n--- Usando .keys() ---')
for chave in pessoa.keys():
    print(f'Chave: {chave} -> {pessoa[chave]}')

# ==========================================
# 2. PERCORRENDO VALORES
# ==========================================

print("\n" + "="*50)
print("2. PERCORRENDO VALORES")
print("="*50)

# Quando só precisamos dos valores, não das chaves
print('--- Apenas os valores ---')
for valor in pessoa.values():
    print(f'Valor: {valor}')

# Útil para cálculos
print('\n--- Soma de idades (exemplo) ---')
idades = {'Ana': 25, 'Bruno': 30, 'Carla': 22}
soma = 0
for idade in idades.values():
    soma += idade
print(f'Soma das idades: {soma}')
print(f'Média: {soma/len(idades):.2f}')

# ==========================================
# 3. PERCORRENDO PARES (CHAVE E VALOR)
# ==========================================

print("\n" + "="*50)
print("3. PERCORRENDO PARES")
print("="*50)

# .items() retorna tuplas (chave, valor)
print('--- Usando .items() ---')
for chave, valor in pessoa.items():
    print(f'{chave}: {valor}')

# Útil para criar relatórios
print('\n--- Relatórios de notas ---')
notas = {"Ana": 8.5, "Bruno": 6.0, "Carla": 9.0, "Daniel": 7.5}

print(f"{'Aluno':<10} {'Nota':>6} {'Status':>10}")
print("-" * 30)

for aluno, nota in notas.items():
    status = 'Aprovado' if nota >= 7 else 'Recuperação' if nota >= 5 else 'Reprovado' # dá pra usar essa estrutura aqui tbm???????
    print(f'{aluno:<10} {nota:>6.1f} {status:>10}')

# ==========================================
# 4. VERIFICANDO EXISTÊNCIA (IN)
# ==========================================

print("\n" + "="*50)
print("4. VERIFICANDO EXISTÊNCIA (IN)")
print("="*50)

pessoa = {"nome": "Ana", "idade": 25, "cidade": "São Paulo"}

# Verificando se a chave existe
print(f'"nome" está no dicionário? {'nome' in pessoa}')
print(f'"telefone" está no dicionário? {'telefone' in pessoa}')

# Verificando se valor existe
print(f"'Ana' está nos valores? {'Ana' in pessoa.values()}")
print(f"'Rio' está nos valores? {'Rio' in pessoa.values()}")

# Uso prático: evitar erros ao acessar
# print("\n--- Uso prático ---")
# chave = input("Digite uma chave para buscar: ")
# if chave in pessoa:
#     print(f"Valor encontrado: {pessoa[chave]}")
# else:
#     print("Chave não encontrada")

# ==========================================
# 5. DICIONÁRIOS ANINHADOS
# ==========================================

print("\n" + "="*50)
print("5. DICIONÁRIOS ANINHADOS")
print("="*50)

# Dicionário com valores que são outros dicionários
contatos = {
    "Ana": {
        "telefone": "11999999999",
        "email": "ana@email.com",
        "idade": 25
    },
    "Bruno": {
        "telefone": "11888888888",
        "email": "bruno@email.com",
        "idade": 30
    }
}

print("--- Estrutura de contatos ---")
print(contatos)

# Acessando elementos aninhados
print(f"\nTelefone da Ana: {contatos['Ana']['telefone']}")
print(f"Email do Bruno: {contatos['Bruno']['email']}")

# Percorrendo dicionário aninhado
print("\n--- Todos os contatos ---")
for nome, dados in contatos.items():
    print(f"\n{nome}:")
    for campo, valor in dados.items():
        print(f"  {campo}: {valor}")

# ==========================================
# 6. EXEMPLOS PRÁTICOS
# ==========================================

print("\n" + "="*50)
print("6. EXEMPLOS PRÁTICOS")
print("="*50)

# 6.1. Contando frequência com dicionário (revisão)
print("\n--- Contagem de palavras ---")
texto = "python é incrível python é simples python é poderoso"
palavras = texto.split()
frequencia = {}

for palavra in palavras:
    if palavra in frequencia:
        frequencia[palavra] += 1
    else:
        frequencia[palavra] = 1

print(frequencia)

# 6.2. Agrupamento por categoria
print("\n--- Produtos por categoria ---")
produtos = [
    {"nome": "Notebook", "categoria": "Eletrônicos"},
    {"nome": "Camiseta", "categoria": "Vestuário"},
    {"nome": "Mouse", "categoria": "Eletrônicos"},
    {"nome": "Calça", "categoria": "Vestuário"},
    {"nome": "Teclado", "categoria": "Eletrônicos"}
]

categorias = {}

for produto in produtos:
    nome = produto['nome']
    cat = produto['categoria']

    if cat in categorias:
        categorias[cat].append(nome)
    else:
        categorias[cat] = [nome]

for categoria, itens in categorias.items():
    print(f'{categoria}: {itens}')

# 6.3. Busca em dicionário aninhado
print("\n--- Busca de contato ---")
contatos = {
    "Ana": {"telefone": "11999999999", "email": "ana@email.com"},
    "Bruno": {"telefone": "11888888888", "email": "bruno@email.com"},
    "Carla": {"telefone": "11777777777", "email": "carla@email.com"}
}

# nome_busca = input("\nDigite um nome para buscar: ")
# if nome_busca in contatos:
#     dados = contatos[nome_busca]
#     print(f"Telefone: {dados['telefone']}")
#     print(f"Email: {dados['email']}")
# else:
#     print("Contato não encontrado")

# ==========================================
# 7. RESUMO
# ==========================================

print("\n" + "="*50)
print("7. RESUMO")
print("="*50)

"""
✅ Percorrer chaves: for chave in dicionario:
✅ Percorrer chaves (explícito): for chave in dicionario.keys():
✅ Percorrer valores: for valor in dicionario.values():
✅ Percorrer pares: for chave, valor in dicionario.items():
✅ Verificar existência: chave in dicionario
✅ Dicionários aninhados: dicionario[chave1][chave2]

📌 Dicas:
- .items() é o mais usado para percorrer
- 'in' verifica chaves, não valores (a menos que use .values())
- Dicionários aninhados são ótimos para dados hierárquicos
"""
############################################
# EXERCÍCIOS - AULA 7.2
############################################
# NÍVEL 1-3: Aquecimento
############################################
"""
1. Percorrendo chaves

# Dado o dicionário: pessoa = {"nome": "Ana", "idade": 25, "cidade": "SP"}
# Use um loop for para imprimir todas as chaves
"""
"""

pessoa = {"nome": "Ana", "idade": 25, "cidade": "SP"}

for dados in pessoa.keys():
    print(dados)

# 2. Use o mesmo dicionário para imprimir todos os valores
print()
for valores in pessoa.values():
    print(valores)

# 3. Use .items() para imprimir "chave: valor" para cada par
print()
for chave, valor in pessoa.items():
    print(f'{chave}: {valor}')
"""
############################################
# NÍVEL 4-6: Aplicação
############################################
"""
4. Verificando existência

# Crie um dicionário com 5 contatos (nome: telefone)
# Peça ao usuário um nome
# Se existir, mostre o telefone; senão, mostre "Contato não encontrado"
"""
"""
contatos = {
    'Ana': 3599999999,
    'Bruno': 3588888888,
    'Carlos': 3577777777,
    'Daniel': 3566666666,
    'Enzo': 3555555555
}

nome = input('Informe um nome: ')
if nome in contatos:
    print(f'Telefone de {nome}: {contatos[nome]}')
else:
    print('Contato não encontrado')
"""
######################################################
"""
5. Relatório de vendas

# Dado o dicionário: vendas = {"segunda": 120, "terça": 150, "quarta": 90, "quinta": 200, "sexta": 180}
# Calcule e mostre:
# - O total de vendas na semana
# - O dia com maior venda
# - O dia com menor venda
# - A média diária de vendas
"""
"""
vendas = {
    "segunda": 120,
    "terça": 150,
    "quarta": 90,
    "quinta": 200,
    "sexta": 180
}

total_semana = 0
for dia, venda in vendas.items():
    total_semana += venda
print(f'Total de vendas na semana: {total_semana}')

index = float('-inf')
for dia, venda in vendas.items():
    if venda > index:
        dia_maior = dia
        index = venda
print(f'O dia com mais vendas na semana: {dia_maior}')

index = float('inf')
for dia, venda in vendas.items():
    if venda < index:
        dia_menor = dia
        index = venda
print(f'O dia com mais menor na semana: {dia_menor}')

print(f'A média diária de vendas: {total_semana/len(vendas)}')
"""
###############################################################
"""
6. Dicionário aninhado simples

# Crie um dicionário de alunos onde cada aluno tem nome e nota
# Exemplo: {"Ana": {"nota1": 8, "nota2": 7}, "Bruno": {"nota1": 6, "nota2": 9}}
# Calcule e mostre a média de cada aluno
"""
"""
alunos = {
    "Ana": {"nota1": 10, "nota2": 7},
    "Bruno": {"nota1": 6, "nota2": 9}
}

for nome, dados in alunos.items():
    print(nome)
    soma_notas = 0
    for nota in dados.values():
        soma_notas += nota
    print(f'Média de {nome} é {soma_notas/len(dados)}')
"""
############################################
# NÍVEL 7-8: Manipulação
############################################
"""
7. Agrupamento por primeira letra

# Dada a lista de palavras: ["casa", "carro", "banana", "cachorro", "bicicleta", "aviao"]
# Crie um dicionário onde a chave é a primeira letra e o valor é uma lista de palavras
# Resultado esperado: {"c": ["casa", "carro", "cachorro"], "b": ["banana", "bicicleta"], "a": ["aviao"]}
"""
"""
palavras = ["casa", "carro", "banana", "cachorro", "bicicleta", "aviao"]

resultado = {}

for palavra in palavras:
    primeira = palavra[0]

    if primeira in resultado:
        resultado[primeira].append(palavra)
    else:
        resultado[primeira] = [palavra]

print(resultado)
"""
###############################################
"""
8. Contador de vogais

# Peça uma frase ao usuário
# Use um dicionário para contar quantas vezes cada vogal aparece (a, e, i, o, u)
# Ignore maiúsculas/minúsculas
# Mostre o resultado
"""
"""
frase = input('Informe uma frase: ')
letras = list(frase.lower().replace(' ', ''))

vogais = {}

for letra in letras:
    if letra in ['a', 'e', 'i', 'o', 'u']:
        if letra in vogais:
            vogais[letra] += 1
        else:
            vogais[letra] = 1

print(vogais)
"""
############################################
# NÍVEL 9-10: Desafios
############################################
"""
9. Agenda com dicionário aninhado

# Crie uma agenda com os seguintes contatos:
# Ana: telefone 1111-1111, email ana@email.com, aniversario 15/05
# Bruno: telefone 2222-2222, email bruno@email.com, aniversario 20/08
# Carla: telefone 3333-3333, email carla@email.com, aniversario 10/12

# Implemente um menu com:
# 1. Listar todos os contatos (mostrar nome e telefone)
# 2. Buscar contato (mostrar todas as informações)
# 3. Adicionar novo contato
# 4. Sair
"""
"""
agenda = {
    'Ana': {'telefone': '1111-1111', 'email': 'ana@email.com', 'aniversario': '15/05'},
    'Bruno': {'telefone': '2222-2222', 'email': 'bruno@email.com', 'aniversario': '20/08'},
    'Carla': {'telefone': '3333-3333', 'email': 'carla@email.com', 'aniversario': '10/12'}
}

print(""--- MENU ---
# 1. Listar todos os contatos
# 2. Buscar contato
# 3. Adicionar novo contato
# 4. Sair
"")

while True:
    print()
    entrada = input('Informe uma opção do menu: ')
    if not entrada.isdigit():
        print('Informe apenas números!')
    elif not int(entrada) in [1, 2, 3, 4]:
        print('Informe um número do menu!')
    elif int(entrada) == 1:
        print()
        print('Listar todos os contatos!')
        for nome, dados in agenda.items():
            print(f'{nome}: {dados['telefone']}')
    elif int(entrada) == 2:
        print('Buscar contato!')
        contato = input('Informe o contato a ser buscado: ')
        if contato in agenda:
            print(agenda[contato])
        else:
            print('Contato não encontrado')
    elif int(entrada) == 3:
        print('Adicionar novo contato!')
        contato = input('Informe o nome do contato a ser adicionado: ')
        if contato not in agenda:
            tel = input(f'Informe o telefone de {contato}(XXXX-XXXX): ')
            email = input(f'Informe o email de {contato}: ')
            aniv = input(f'Informe o aniversário de {contato}(XX/XX): ')
            agenda[contato] = {'telefone': tel, 'email': email, 'aniversario': aniv}
            print('Contato adicionado!')
        else:
            print('Esse contato já está na agenda!')
    elif int(entrada) == 4:
        print('Saindo!')
        break

"""
#####################################################################
"""
10. DESAFIO FINAL: Analisador de texto avançado

# Peça ao usuário para digitar um texto (pode ser várias linhas, digite "FIM" para terminar)
# Use um dicionário para armazenar estatísticas:
# - Contagem de palavras
# - Contagem de letras (total)
# - Contagem de cada letra (a-z)
# - Contagem de cada palavra
# - Palavra mais longa
# - Palavra mais curta

# Depois que o usuário digitar "FIM", mostre todas as estatísticas formatadas
"""
frase = input('Informe uma frase: ')
palavras = frase.split()
letras = list(frase.lower().replace(' ', ''))

estatisticas = {
    'contagem de palavras': len(palavras),
    'conta de letras': len(letras),
    'contagem de cada letra (a-z)' : {},
    'contagem de cada palavra': {},
    'palavra mais longa': '',
    'palavra mais curta': ''
} # Essa técnica de criação prévia do dicionário está correta?

a = 'contagem de cada letra (a-z)'

for letra in letras:
    if letra in estatisticas[a]:
        estatisticas[a][letra] += 1
    else:
        estatisticas[a][letra] = 1


b = 'contagem de cada palavra'

for palavra in palavras:
    if palavra in estatisticas[b]:
        estatisticas[b][palavra] += 1
    else:
        estatisticas[b][palavra] = 1

c = 'palavra mais longa'
index = float('-inf')
for palavra in palavras:
    if len(palavra) > index:
        estatisticas[c] = palavra
        index = len(palavra)

d = 'palavra mais curta'
index = float('inf')
for palavra in palavras:
    if len(palavra) < index:
        estatisticas[d] = palavra
        index = len(palavra)

print(estatisticas)

# Fiz uma versão para frases, acho que já atendia o desafio.
# Outra coisa, não fiz o negócio de tratar as letras com acento e sem acento na mesma contagem, acho que daria bastante trabalho para fazer manualmente com o conhecimento que eu tenho