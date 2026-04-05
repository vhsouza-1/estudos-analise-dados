"""
Módulo 7: dicionários
Exercícios Integradores
Data: 05/04
Objetivo: Resolver problemas que misturam tudo que vimos
"""
from collections import defaultdict, Counter

"""
Exercício 1: Análise de Vendas por Região

Tema: Lista de dicionários, defaultdict, agrupamento
python

# Dados de vendas de uma empresa
vendas = [
    {"produto": "celular", "regiao": "Norte", "quantidade": 10, "preco": 1500},
    {"produto": "fone", "regiao": "Sul", "quantidade": 30, "preco": 200},
    {"produto": "celular", "regiao": "Norte", "quantidade": 5, "preco": 1500},
    {"produto": "notebook", "regiao": "Sul", "quantidade": 3, "preco": 3500},
    {"produto": "fone", "regiao": "Norte", "quantidade": 15, "preco": 200},
    {"produto": "celular", "regiao": "Sul", "quantidade": 8, "preco": 1500},
    {"produto": "notebook", "regiao": "Norte", "quantidade": 2, "preco": 3500},
    {"produto": "fone", "regiao": "Sul", "quantidade": 20, "preco": 200}
]

# Tarefas:
# 1. Calcule o faturamento total por região (use defaultdict)
# 2. Calcule o faturamento total por produto
# 3. Encontre o produto mais vendido (em quantidade) no Norte
# 4. Crie um relatório formatado: Região | Produto | Quantidade | Faturamento
#    (use sorted para ordenar por região e depois por faturamento decrescente)
"""
"""
vendas = [
    {"produto": "celular", "regiao": "Norte", "quantidade": 10, "preco": 1500},
    {"produto": "fone", "regiao": "Sul", "quantidade": 30, "preco": 200},
    {"produto": "celular", "regiao": "Norte", "quantidade": 5, "preco": 1500},
    {"produto": "notebook", "regiao": "Sul", "quantidade": 3, "preco": 3500},
    {"produto": "fone", "regiao": "Norte", "quantidade": 15, "preco": 200},
    {"produto": "celular", "regiao": "Sul", "quantidade": 8, "preco": 1500},
    {"produto": "notebook", "regiao": "Norte", "quantidade": 2, "preco": 3500},
    {"produto": "fone", "regiao": "Sul", "quantidade": 20, "preco": 200}
]

faturamento_regiao = defaultdict(float)
faturamento_produto = defaultdict(float)

indice = float('-inf')
for venda in vendas:
    produto = venda['produto']
    regiao = venda['regiao']
    quantidade = venda['quantidade']
    preco = venda['preco']

    faturamento_regiao[regiao] += preco * quantidade

    faturamento_produto[produto] += preco * quantidade

    if regiao == 'Norte':
        if quantidade > indice:
            indice = quantidade
            produto_mais_vend_norte = produto

    venda['faturamento'] = venda['quantidade'] * venda['preco']

print(f'O faturamento total por região foi: {dict(faturamento_regiao)}')
print(f'O faturamento total por produto foi: {dict(faturamento_produto)}')
print(f'O produto mais vendido no Norte foi: {produto_mais_vend_norte}')

vendas_ord = sorted(vendas, key=lambda x: (x['regiao'], -x['faturamento'])) # tive que pesquisar esse sinal de menos...

print(f'{'Região': <7}{'Produto': >10}{'Qtd': >5}{'Fatur.': >8}')
for venda in vendas_ord:
    print(f'{venda['regiao']: <7}{venda['produto']: >10}{venda['quantidade']: >5}{venda['faturamento']: >8}')
"""
########################################################################
"""
Exercício 2: Análise de Texto Avançada

Tema: Counter, defaultdict, tratamento de texto

# Texto para análise
# texto = O Python é uma linguagem de programação de alto nível.
Python é interpretado e tem uma sintaxe clara.
Python é usado em análise de dados, inteligência artificial e desenvolvimento web.
Aprender Python é um excelente investimento para profissionais de dados.

# Tarefas:
# 1. Use Counter para contar a frequência de cada palavra (ignore pontuação e case)
# 2. Use defaultdict para agrupar palavras por tamanho (ex: 3: ["são", "tem"], 4: ["dados"])
# 3. Encontre a palavra mais longa
# 4. Encontre a palavra mais curta
# 5. Calcule a densidade de palavras por frase (número de palavras / número de frases)
"""
"""texto = ""O Python é uma linguagem de programação de alto nível.
Python é interpretado e tem uma sintaxe clara.
Python é usado em análise de dados, inteligência artificial e desenvolvimento web.
Aprender Python é um excelente investimento para profissionais de dados.""

palavras = texto.lower().split()
palavras = [p.strip('.,') for p in palavras]

contador_palavras = Counter(palavras)
print(contador_palavras)

tamanhos = defaultdict(list)

for palavra in palavras:

    tamanhos[len(palavra)].append(palavra)

print(f'Frequência das palavras: {dict(contador_palavras)}')
print(f'Palavras agrupadas por tamanho: {dict(tamanhos)}')
print(f'Palavra mais longa: {tamanhos[max(tamanhos)]}')
print(f'Palavra mais curta: {tamanhos[min(tamanhos)]}')

qnt_frases = len(texto) - len(texto.replace('.', ''))
qnt_palavras = len(palavras)

print(f'Densidade de palavras por frase: {qnt_palavras/qnt_frases} pal./frase')"""
#######################################################################
"""
Exercício 3: Sistema de Alunos com Frequência

Tema: Lista de dicionários, dict comprehension, filtros

# Dados de alunos
alunos = [
    {"nome": "Ana", "notas": [8.5, 7.0, 9.0], "faltas": 3},
    {"nome": "Bruno", "notas": [6.0, 5.5, 7.0], "faltas": 8},
    {"nome": "Carla", "notas": [9.0, 8.5, 9.5], "faltas": 1},
    {"nome": "Daniel", "notas": [5.0, 4.5, 6.0], "faltas": 12},
    {"nome": "Eduarda", "notas": [7.5, 8.0, 7.0], "faltas": 5}
]

# Regras:
# - Média = soma das notas / 3
# - Aprovado por nota: média >= 7
# - Aprovado por frequência: faltas <= 6
# - Aprovado final: aprovado por nota E por frequência

# Tarefas:
# 1. Calcule a média de cada aluno e adicione como nova chave "media"
# 2. Adicione a chave "status" com "Aprovado" ou "Reprovado"
# 3. Use dict comprehension para criar um dicionário apenas com alunos aprovados (nome: média)
# 4. Calcule a média geral da turma (apenas dos aprovados? sua escolha)
# 5. Crie um relatório ordenado por média (decrescente)
"""
"""
alunos = [
    {"nome": "Ana", "notas": [8.5, 7.0, 9.0], "faltas": 3},
    {"nome": "Bruno", "notas": [6.0, 5.5, 7.0], "faltas": 8},
    {"nome": "Carla", "notas": [9.0, 8.5, 9.5], "faltas": 1},
    {"nome": "Daniel", "notas": [5.0, 4.5, 6.0], "faltas": 12},
    {"nome": "Eduarda", "notas": [7.5, 8.0, 7.0], "faltas": 5}
]

soma_geral = 0

for aluno in alunos:

    aluno['media'] = round(sum(aluno['notas'])/3, 2)

    aluno['status'] = 'Aprovado' if aluno['media'] >= 7 and aluno['faltas'] <= 6 else 'Reprovado'

    soma_geral += aluno['media']

aprovados = {aluno['nome']: aluno['media'] for aluno in alunos if aluno['status'] == 'Aprovado'}

media_geral = soma_geral/len(alunos)

alunos_ord = sorted(alunos, key=lambda x: x['media'], reverse=True)

print(f'Tabela alunos depois da adição de média e status:')
for aluno in alunos:
    print(aluno)

print(f'Alunos aprovados e sua média: {aprovados}')

print(f'Média geral da turma: {media_geral:.2f}')

print()
print(f'{'Nome': <9}{'Média': >5}{'Faltas': >8}{'Status': >11}')
for aluno in alunos_ord:
    print(f'{aluno['nome']: <9}{aluno['media']: >5}{aluno['faltas']:>8}{aluno['status']:>11}')
"""
#######################################################################
"""
Exercício 4: Agenda de Contatos Avançada

Tema: Dicionários aninhados, setdefault, defaultdict

# Lista de contatos (pode ter múltiplos telefones por pessoa)
contatos_raw = [
    {"nome": "Ana", "telefone": "11999999999", "email": "ana@email.com"},
    {"nome": "Bruno", "telefone": "11888888888", "email": "bruno@email.com"},
    {"nome": "Ana", "telefone": "11777777777", "email": "ana2@email.com"},
    {"nome": "Carla", "telefone": "11666666666", "email": "carla@email.com"},
    {"nome": "Bruno", "telefone": "11555555555", "email": "bruno2@email.com"}
]

# Tarefas:
# 1. Use defaultdict para agrupar os dados por nome
#    Resultado esperado: {"Ana": {"telefones": ["119...", "117..."], "emails": ["ana@...", "ana2@..."]}}
# 2. Use setdefault para fazer o mesmo agrupamento (sem defaultdict)
# 3. Crie uma função de busca que retorna todos os dados de um contato
# 4. Adicione um novo contato (se já existir, adiciona telefone/email aos existentes)
"""
"""
contatos_raw = [
    {"nome": "Ana", "telefone": "11999999999", "email": "ana@email.com"},
    {"nome": "Bruno", "telefone": "11888888888", "email": "bruno@email.com"},
    {"nome": "Ana", "telefone": "11777777777", "email": "ana2@email.com"},
    {"nome": "Carla", "telefone": "11666666666", "email": "carla@email.com"},
    {"nome": "Bruno", "telefone": "11555555555", "email": "bruno2@email.com"}
]

contatos = defaultdict(lambda: {'telefones': [], 'emails': []}) # mestre, como você esperava que eu descobrisse isso sozinho????? Tive que pesquisar. Seu plano era esse?? Seja mais claro quando quiser que eu pesquise algo.

for contato in contatos_raw:

    nome = contato['nome']
    telefone = contato['telefone']
    email = contato['email']

    contatos[nome]['telefones'].append(telefone)
    contatos[nome]['emails'].append(email)

while True:
    entrada = input('Informações 1, Adicionar contato 2: ')
    if not entrada.isdigit():
        print('Apenas números!')
    elif int(entrada) not in [1, 2]:
        print('Apenas números do menu!')
    elif int(entrada) == 1:
        contato = input('Informe o nome a ser consultado: ')
        print(contatos[contato])
    elif int(entrada) == 2:
        contato = input('Informe o contato a ser adicionado: ')
        if contato in list(contatos.keys()):
            print(f'Adicionando informações à contato existente')
            telefone = input('Informe o número: ')
            email = input('Informe o email: ')
            contatos[contato]['telefones'].append(telefone)
            contatos[contato]['emails'].append(email)
        else:
            print(f'Adicionando novo contato')
            telefone = input('Informe o telefone: ')
            email = input('Informe o email: ')
            contatos[contato]['telefones'].append(telefone)
            contatos[contato]['emails'].append(email)
"""
###################################################################################
"""
Exercício 5: DESAFIO FINAL - Dashboard de Vendas

Tema: Todos os conceitos do módulo 7
python

# Dados de vendas completos
vendas = [
    {"produto": "celular", "categoria": "eletrônicos", "quantidade": 10, "preco": 1500, "vendedor": "Ana", "data": "2024-01-15"},
    {"produto": "fone", "categoria": "eletrônicos", "quantidade": 30, "preco": 200, "vendedor": "Bruno", "data": "2024-01-15"},
    {"produto": "camiseta", "categoria": "vestuário", "quantidade": 20, "preco": 50, "vendedor": "Ana", "data": "2024-01-15"},
    {"produto": "celular", "categoria": "eletrônicos", "quantidade": 5, "preco": 1500, "vendedor": "Ana", "data": "2024-01-16"},
    {"produto": "notebook", "categoria": "eletrônicos", "quantidade": 3, "preco": 3500, "vendedor": "Carla", "data": "2024-01-16"},
    {"produto": "calça", "categoria": "vestuário", "quantidade": 15, "preco": 120, "vendedor": "Bruno", "data": "2024-01-16"},
    {"produto": "fone", "categoria": "eletrônicos", "quantidade": 15, "preco": 200, "vendedor": "Bruno", "data": "2024-01-17"},
    {"produto": "celular", "categoria": "eletrônicos", "quantidade": 8, "preco": 1500, "vendedor": "Carla", "data": "2024-01-17"},
    {"produto": "bone", "categoria": "vestuário", "quantidade": 25, "preco": 30, "vendedor": "Ana", "data": "2024-01-17"}
]

# Tarefas - Crie um dashboard que responda:

# 1. VISÃO GERAL
#    - Faturamento total do período
#    - Quantidade total de itens vendidos
#    - Ticket médio (faturamento / quantidade)

# 2. ANÁLISE POR CATEGORIA
#    - Faturamento por categoria (use defaultdict)
#    - Quantidade vendida por categoria
#    - Categoria com maior faturamento
#    - Categoria com maior volume de vendas

# 3. ANÁLISE POR PRODUTO
#    - Produto mais vendido (em quantidade)
#    - Produto com maior faturamento
#    - Use Counter para encontrar os 3 produtos mais vendidos

# 4. ANÁLISE POR VENDEDOR
#    - Faturamento por vendedor
#    - Vendedor com maior faturamento
#    - Vendedor com maior volume de vendas

# 5. ANÁLISE POR DIA
#    - Faturamento por dia (use defaultdict)
#    - Dia com maior faturamento
#    - Quantidade de vendas por dia

# 6. RELATÓRIO FORMATADO
#    - Crie um dicionário final com todas as estatísticas calculadas
#    - Mostre o relatório de forma organizada (use prints com separadores)
"""
vendas = [
    {"produto": "celular", "categoria": "eletrônicos", "quantidade": 10, "preco": 1500, "vendedor": "Ana", "data": "2024-01-15"},
    {"produto": "fone", "categoria": "eletrônicos", "quantidade": 30, "preco": 200, "vendedor": "Bruno", "data": "2024-01-15"},
    {"produto": "camiseta", "categoria": "vestuário", "quantidade": 20, "preco": 50, "vendedor": "Ana", "data": "2024-01-15"},
    {"produto": "celular", "categoria": "eletrônicos", "quantidade": 5, "preco": 1500, "vendedor": "Ana", "data": "2024-01-16"},
    {"produto": "notebook", "categoria": "eletrônicos", "quantidade": 3, "preco": 3500, "vendedor": "Carla", "data": "2024-01-16"},
    {"produto": "calça", "categoria": "vestuário", "quantidade": 15, "preco": 120, "vendedor": "Bruno", "data": "2024-01-16"},
    {"produto": "fone", "categoria": "eletrônicos", "quantidade": 15, "preco": 200, "vendedor": "Bruno", "data": "2024-01-17"},
    {"produto": "celular", "categoria": "eletrônicos", "quantidade": 8, "preco": 1500, "vendedor": "Carla", "data": "2024-01-17"},
    {"produto": "bone", "categoria": "vestuário", "quantidade": 25, "preco": 30, "vendedor": "Ana", "data": "2024-01-17"}
]

faturamento_total = 0
quantidade_total = 0

faturamento_categoria = defaultdict(float)
quantidade_categoria = defaultdict(int)

quantidade_produto = defaultdict(int)
faturamento_produto = defaultdict(float)

faturamento_vendedor = defaultdict(float)
quantidade_vendedor = defaultdict(int)

faturamento_data = defaultdict(float)
quantidade_data = defaultdict(int)

for venda in vendas:
    faturamento_total += venda['quantidade'] * venda['preco']
    quantidade_total += venda['quantidade']

    faturamento_categoria[venda['categoria']] += venda['quantidade'] * venda['preco']
    quantidade_categoria[venda['categoria']] += venda['quantidade']

    quantidade_produto[venda['produto']] += venda['quantidade']
    faturamento_produto[venda['produto']] += venda['quantidade'] * venda['preco']

    faturamento_vendedor[venda['vendedor']] += venda['quantidade'] * venda['preco']
    quantidade_vendedor[venda['vendedor']] += venda['quantidade']

    faturamento_data[venda['data']] += venda['quantidade'] * venda['preco']
    quantidade_data[venda['data']] += venda['quantidade']

ticket_medio = faturamento_total/quantidade_total

contador_produtos = Counter(quantidade_produto)

print(f'O faturamento total do período foi: {faturamento_total}')
print(f'A quantidade total vendida no período foi: {quantidade_total}')
print(f'O ticket médio do período foi: {ticket_medio:.2f}')

print(f'Faturamento por categoria: {dict(faturamento_categoria)}')
print(f'Quantidade por categoria: {dict(quantidade_categoria)}')

print(f'Categoria com maior faturamento: {max(faturamento_categoria, key= lambda x: x[1])}')
print(f'Categoria com maior volume de vendas: {max(quantidade_categoria, key= lambda x: x[1])}')

print(f'Produto mais vendido: {max(quantidade_produto.items(), key= lambda x: x[1])}')
print(f'Produto com maior faturamento: {max(faturamento_produto.items(), key= lambda x: x[1])}')
print(f'Os 3 produtos mais vendidos foram: {contador_produtos.most_common(3)}')

print(f'Faturamento por vendedor: {faturamento_vendedor}')
print(f'Vendedor com maior faturamento: {max(faturamento_vendedor.items(), key=lambda x: x[1])}')
print(f'Vendedor com maior volume de vendas: {max(quantidade_vendedor.items(), key=lambda x: x[1])}')

print(f'Faturamento por dia: {dict(faturamento_data)}')
print(f'Dia com maior faturamento: {max(faturamento_data.items(), key=lambda x: x[1])}')
print(f'Quantidade de vendas por dia: {dict(quantidade_data)}')

# Precisei terminar rapido, então não fiz o relatório formatado, mas ta tudo organizado pra cima.
