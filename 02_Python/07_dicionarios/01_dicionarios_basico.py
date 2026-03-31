"""
Módulo 7: Dicionários
Aula 7.1: Básico - Chave-Valor
Data: 31/03/2026
Objetivo: Aprender a criar e manipular dicionários
"""

# ==========================================
# 1. O QUE SÃO DICIONÁRIOS?
# ==========================================

print("="*50)
print("1. O QUE SÃO DICIONÁRIOS?")
print("="*50)

# Listas: acessamos por índice (posição)
lista = ["Ana", 25, "São Paulo"]
print(f"Lista: {lista}")
print(f"lista[0] = {lista[0]} (acesso por posição)")

# Dicionários: acessamos por chave (nome)
dicionario = {"nome": "Ana", "idade": 25, "cidade": "São Paulo"}
print(f"\nDicionário: {dicionario}")
print(f'dicionario["nome"] = {dicionario["nome"]} (acesso por chave)')

# Analogia:
# - Lista: um armário com números nas gavetas (0, 1, 2...)
# - Dicionário: um armário com etiquetas personalizadas ("nome", "idade"...)

# ==========================================
# 2. CRIANDO DICIONÁRIOS
# ==========================================

print("\n" + "="*50)
print("2. CRIANDO DICIONÁRIOS")
print("="*50)

# Jeito 1: chaves {}
pessoa1 = {'nome': 'Ana', 'idade': 25}
print(f'Jeito 1: {pessoa1}')

# Jeito 2: dict()
pessoa2 = dict(nome='Bruno', idade=30)
print(f'Jeito 2: {pessoa2}')

# Jeito 3: lista de tuplas
pares = [('nome', 'Carla'), ('idade', 22)]
pessoa3 = dict(pares)
print(f'Jeito 3: {pessoa3}')

# Dicionário vazio
vazio = {}
vazio2 = dict()
print(f'Dicionários vazios: {vazio} e {vazio2}')

# ==========================================
# 3. TIPOS DE CHAVES E VALORES
# ==========================================

print("\n" + "="*50)
print("3. TIPOS DE CHAVES E VALORES")
print("="*50)

# Chaves: geralmente strings, mas podem ser números ou tuplas
# Valores: qualquer tipo (int, float, str, list, outro dicionário...)

diverso = {
    'nome': 'Daniel',             # string
    'idade': 28,                  # int
    'altura': 1.75,               # float
    'filhos': ['João', 'Maria'],  # lista
    'endereço': {                 # outro dicionário
        'rua': 'das Flores',
        'numero': 123
    },
    42: 'resposta',               # número como chave
    (1, 2): 'tupla como chave'    # tupla como chave (imutável)
}

print(f'Dicionário com tipos variados: {diverso}')

# ==========================================
# 4. ACESSANDO VALORES
# ==========================================

print("\n" + "="*50)
print("4. ACESSANDO VALORES")
print("="*50)

pessoa = {"nome": "Ana", "idade": 25, "cidade": "São Paulo"}

# Acesso direto (se a chave não existir, dá erro)
print(f'pessoa["nome"] = {pessoa['nome']}')
print(f'pessoa["idade"] = {pessoa['idade']}')

# Acesso seguro com get() (se não existir, retorna None ou valor padrão)
print(f'pessoa.get("cidade") = {pessoa.get("cidade")}')
print(f"pessoa.get('telefone') = {pessoa.get('telefone')}")  # None
print(f"pessoa.get('telefone', 'não informado') = {pessoa.get('telefone', 'não informado')}")

# ==========================================
# 5. ADICIONANDO E MODIFICANDO
# ==========================================

print("\n" + "="*50)
print("5. ADICIONANDO E MODIFICANDO")
print("="*50)

pessoa = {"nome": "Ana", "idade": 25}
print(f"Original: {pessoa}")

# Adicionando nova chave
pessoa['cidade'] = 'São Paulo'
print(f'Após adicionar cidade: {pessoa}')

# Modificando valor existente
pessoa['idade'] = 26
print(f'Após modificar idade: {pessoa}')

# Adicionar várias de uma vez (update)
pessoa.update({'profissão': 'engenharia', 'telefone': '11999999999'})
print(f'Após update: {pessoa}')

# ==========================================
# 6. REMOVENDO ELEMENTOS
# ==========================================

print("\n" + "="*50)
print("6. REMOVENDO ELEMENTOS")
print("="*50)

pessoa = {"nome": "Ana", "idade": 25, "cidade": "São Paulo", "telefone": "11999999999"}
print(f"Original: {pessoa}")

# pop() - remove e retorna o valor
telefone = pessoa.pop('telefone')
print(f'pop("telefone") retornou: {telefone}')
print(f'Após pop(): {pessoa}')

# pop() com valor padrão (evita erro)
resultado = pessoa.pop('inexistente', 'não encontrado')
print(f'pop("inexistente", "não encontrado"): {resultado}')

# del - remove sem retornar
del pessoa['cidade']
print(f'Após del: {pessoa}')

# clear - remove tudo
pessoa.clear()
print(f'Após clear: {pessoa}')

# ==========================================
# 7. LISTAS vs DICIONÁRIOS
# ==========================================

print("\n" + "="*50)
print("7. LISTAS vs DICIONÁRIOS")
print("="*50)

# Quando usar cada um?

# Lista: dados sequenciais, ordem importa
frutas = ['maçã', 'banana', 'laranja']
print(f'Lista de frutas (ordem importa): {frutas}')

# Dicionário: dados relacionados, acesso por nome
aluno = {'nome': 'Ana', 'idade': 25, 'curso': 'Engenharia'}
print(f'Dicionário do aluno (acesso por chave): {aluno}')

# Exemplo prático: cadastro de alunos
# Com listas (difícil de ler e manter)
alunos_lista = [
    ["Ana", 25, "Engenharia"],
    ["Bruno", 30, "Medicina"],
    ["Carla", 22, "Direito"]
]
print(f"\nLista de alunos (qual é a idade de Carla?): {alunos_lista[2][1]}")

# Com dicionários (fácil de ler e manter)
alunos_dict = [
    {"nome": "Ana", "idade": 25, "curso": "Engenharia"},
    {"nome": "Bruno", "idade": 30, "curso": "Medicina"},
    {"nome": "Carla", "idade": 22, "curso": "Direito"}
]
print(f"Lista de dicionários (idade de Carla): {alunos_dict[2]['idade']}")
print("Muito mais claro!")

# ==========================================
# 8. ARMADILHAS COMUNS
# ==========================================

print("\n" + "="*50)
print("8. ARMADILHAS COMUNS")
print("="*50)

# 1. Acessar chave que não existe (sem get)
pessoa = {"nome": "Ana"}
# print(pessoa["idade"])  # KeyError!

# 2. Chaves duplicadas (a última prevalece)
duplicada = {"nome": "Ana", "nome": "Bruno"}
print(f"Chave duplicada: {duplicada}")  # {"nome": "Bruno"}

# 3. Chave imutável (lista não pode ser chave)
# dicionario = {[1, 2]: "lista"}  # TypeError!

# 4. Dicionário não mantém ordem (até Python 3.7)
# Atualmente mantém ordem de inserção, mas não dependa disso

# 5. Copiar dicionário (mesmo problema das listas!)
original = {"a": 1, "b": 2}
copia = original  # Não é cópia!
copia["c"] = 3
print(f"Original após modificar 'cópia': {original}")

# Cópia rasa
copia_rasa = original.copy()
copia_rasa["d"] = 4
print(f"Original após modificar cópia rasa: {original}")

# ==========================================
# 9. EXEMPLOS PRÁTICOS
# ==========================================

print("\n" + "="*50)
print("9. EXEMPLOS PRÁTICOS")
print("="*50)

# 9.1. Catálogo de produtos
print("\n--- Catálogo de produtos ---")
produtos = {
    "celular": 1500,
    "notebook": 3500,
    "fone": 200
}
print(f"Preço do notebook: R${produtos['notebook']}")
print(f"Produtos disponíveis: {list(produtos.keys())}")

# 9.2. Contando ocorrências (simples)
print("\n--- Contando ocorrências ---")
frase = "banana maçã banana laranja banana"
palavras = frase.split()
contagem = {}

for palavra in palavras:
    if palavra in contagem:
        contagem[palavra] += 1
    else:
        contagem[palavra] = 1

print(f"Contagem: {contagem}")

# 9.3. Agenda de contatos
print("\n--- Agenda de contatos ---")
agenda = {}

agenda["Ana"] = {"telefone": "11999999999", "email": "ana@email.com"}
agenda["Bruno"] = {"telefone": "11888888888", "email": "bruno@email.com"}

for contato, dados in agenda.items():
    print(f"{contato}: {dados['telefone']}")

# ==========================================
# 10. RESUMO
# ==========================================

print("\n" + "="*50)
print("10. RESUMO")
print("="*50)

"""
✅ Dicionário: estrutura chave-valor, acesso por chave (não por índice)
✅ Criação: {} ou dict()
✅ Acesso: dicionario[chave] (se não existir, KeyError)
✅ Acesso seguro: dicionario.get(chave, valor_padrao)
✅ Adicionar/Modificar: dicionario[chave] = valor
✅ Remover: pop(chave) ou del dicionario[chave]
✅ Limpar: clear()
✅ Cópia: .copy() (cópia rasa)

📌 Lista vs Dicionário:
- Lista: dados sequenciais, acesso por posição
- Dicionário: dados relacionados, acesso por nome
- Lista de dicionários: padrão para dados tabulares (como uma tabela)
"""
########################################################
# EXERCÍCIOS - AULA 7.1
########################################################
# NÍVEL 1-3: Aquecimento
########################################################
"""
1. Criando dicionário

# Crie um dicionário com seus dados:
# - nome (string)
# - idade (int)
# - altura (float)
# - estudante (bool)
# Mostre o dicionário
"""
"""
meu_dict = {'nome': 'Vinícius', 'idade': 26, 'altura': 1.75, 'estudante': True}
print(meu_dict)
"""
########################################################
"""
2. Acessando valores

# Use o dicionário criado no exercício 1 para:
# - Mostrar seu nome usando a chave
# - Mostrar sua idade usando a chave
# - Usar get() para tentar acessar uma chave que não existe (ex: "profissao")
"""
"""
meu_dict = {'nome': 'Vinícius', 'idade': 26, 'altura': 1.75, 'estudante': True}

print(f'Meu nome: {meu_dict['nome']}')
print(f'Minha idade: {meu_dict['idade']}')
print(f'Minha profissão: {meu_dict.get('profissão')}')
"""
########################################################
"""
3. Adicionando e modificando

# Use o dicionário do exercício 1:
# - Adicione uma nova chave "cidade" com sua cidade
# - Modifique sua idade para um valor diferente
# - Mostre o dicionário após as alterações
"""
"""
meu_dict = {'nome': 'Vinícius', 'idade': 26, 'altura': 1.75, 'estudante': True}

meu_dict['cidade'] = 'Lavras'
meu_dict['idade'] = 27

print(meu_dict)
"""
########################################################
# NÍVEL 4-6: Aplicação
########################################################
"""
4. Agenda de contatos

# Crie um dicionário vazio chamado "agenda"
# Adicione 3 contatos (nome como chave, telefone como valor)
# Mostre todos os contatos
# Peça ao usuário um nome e mostre o telefone (use get para tratar nomes inexistentes)
"""
"""
agenda = {}

agenda['Marcos'] = 35999999999
agenda['Vitória'] = 35988888888

print(agenda)

entrada = input('Informe um nome: ')

print(agenda.get(entrada))
"""
########################################################
"""
5. Contador de letras

# Peça uma palavra ao usuário
# Use um dicionário para contar quantas vezes cada letra aparece
# Dica: percorra a palavra com for e verifique se a letra já está no dicionário
# Mostre o resultado
"""
"""
palavra = input('Informe uma palavra: ')
letras = list(palavra)
contagem = {}

for letra in letras:
    if letra in contagem:
        contagem[letra] += 1
    else:
        contagem[letra] = 1

print(contagem)

# Esse técnica é muito interessante!
"""
########################################################
"""
6. Conversor de notas

# Crie um dicionário com notas de alunos: {"Ana": 8.5, "Bruno": 6.0, "Carla": 9.0}
# Calcule e mostre:
# - A média da turma
# - O aluno com maior nota
# - O aluno com menor nota
# - Quantos alunos tiraram nota >= 7
"""
"""
notas_dic = {"Ana": 8.5, "Bruno": 6.0, "Carla": 9.0}

soma_notas = 0

for nome, nota in notas_dic.items(): # Isso aqui você falou que é conteúdo da segunda aula... Só fiz pq tinha um exemplo parecido
    soma_notas += nota


print(f'A média da turma é: {soma_notas/len(notas_dic)}') # duvida, sempre se calcula média assim? No sql tem uma função avg() aqui não tem isso? estranho...

index = float('-inf')
for nome, nota in notas_dic.items():
    if nota > index:
        maior_nota = nome
        index = nota

print(f'O aluno com maior nota é: {maior_nota}')

index = float('inf')
for nome, nota in notas_dic.items():
    if nota < index:
        menor_nota = nome
        index = nota

print(f'O aluno com menor nota é: {menor_nota}')

alunos_m7 = [nome for nome, nota in notas_dic.items() if nota >=7]
print(f'Alunos que tiraram nota >= 7: {alunos_m7}')

# É assim mesmo que eu deveria fazer esses exercícios? Converter para as técnicas de manipulação de lista?
"""
########################################################
# NÍVEL 7-8: Manipulação
########################################################
"""
7. Atualizando dicionário com update
python

# Crie dois dicionários:
d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"b": 20, "d": 4, "e": 5}

# Use update() para mesclar d2 em d1 (valores de d2 sobrescrevem d1)
# Mostre o resultado
"""
"""
d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"b": 20, "d": 4, "e": 5}

print(d1)

d1.update(d2)

print(d1)
"""
#################################################################
"""
8. Removendo com pop e del

# Crie um dicionário: {"nome": "Ana", "idade": 25, "cidade": "SP", "profissao": "eng"}
# Remova "cidade" usando del
# Remova "profissao" usando pop e guarde o valor removido
# Mostre o dicionário final e o valor removido
"""
"""
pessoa = {"nome": "Ana", "idade": 25, "cidade": "SP", "profissao": "eng"}

del pessoa['cidade']
profissao = pessoa.pop('profissao')
print(pessoa)
print(profissao)
"""
########################################################
# NÍVEL 9-10: Desafios
########################################################
"""
9. Combinando listas e dicionários

# Dadas duas listas:
alunos = ["Ana", "Bruno", "Carla", "Daniel"]
notas = [8.5, 6.0, 9.0, 7.5]

# Crie um dicionário onde a chave é o nome e o valor é a nota
# Depois, crie um novo dicionário apenas com os alunos aprovados (nota >= 7)
# Mostre ambos os dicionários
"""
"""
alunos = ["Ana", "Bruno", "Carla", "Daniel"]
notas = [8.5, 6.0, 9.0, 7.5]

alunos_notas = dict(zip(alunos, notas))

alunos_aprovados = {}
for nome, nota in alunos_notas.items():
    if nota >= 7:
        alunos_aprovados[nome] = nota

print(f'Alunos aprovados: {alunos_aprovados}')
"""
##########################################################################
"""
10. DESAFIO FINAL: Sistema de estoque com dicionário

# Crie um dicionário representando o estoque de uma loja:
# Chave: nome do produto, Valor: quantidade em estoque
# Exemplo: {"arroz": 50, "feijão": 30, "macarrão": 20}

# Implemente um menu com as opções:
# 1. Ver estoque (mostrar todos os produtos e quantidades)
# 2. Adicionar produto (se já existe, aumenta a quantidade; se não, cria novo)
# 3. Remover produto (diminui quantidade; se chegar a zero, remove do dicionário)
# 4. Buscar produto (mostra quantidade ou "não encontrado")
# 5. Sair

# O menu deve continuar até o usuário escolher sair
# Use um loop while e valide as entradas
"""
estoque = {"arroz": 50, "feijão": 30, "macarrão": 20}

print(""" --- MENU ---
1. Ver estoque
2. Adicionar produto
3. Remover produto
4. Buscar produto
5. Sair
""")

while True:
    print()
    entrada = input('Informe a opção desejada: ')
    if not entrada.isdigit():
        print('Informe apenas números!')
    elif not int(entrada) in [1, 2, 3, 4, 5]:
        print('Informe um número do menu!')
    elif int(entrada) == 1:
        print(f'Estoque: {estoque}')
    elif int(entrada) == 2:
        print('Adicionar produto!')
        produto = input('Informe o produto a ser adicionado: ')
        if produto in estoque:
            estoque[produto] += 1
        else:
            estoque[produto] = 1
    elif int(entrada) == 3:
        print('Remover produto!')
        produto = input('Informe o produto a ser removido: ')
        if estoque[produto] > 1:
            estoque[produto] -= 1
        elif estoque[produto] == 1:
            del estoque[produto]
    elif int(entrada) == 4:
        print('Buscar produto!')
        produto = input('Informe o produto a ser buscado: ')
        print(estoque.get(produto, 'não encontrado'))
    elif int(entrada) == 5:
        break

# Na primeira vez que fiz um programa desse foi bem trabalhoso, agora eu fiz praticamente direto, sem travar haha fique feliz!


















































































