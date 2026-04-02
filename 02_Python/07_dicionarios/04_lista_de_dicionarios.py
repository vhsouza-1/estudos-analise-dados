"""
Módulo 7: Dicionários
Aula 7.4: Lista de Dicionários - Estrutura Tabular
Data: 02/04/2026
Objetivo: Aprender a trabalhar com listas de dicionários (como tabelas)
"""

# ==========================================
# 1. O QUE É UMA LISTA DE DICIONÁRIOS?
# ==========================================

print("="*50)
print("1. LISTA DE DICIONÁRIOS = TABELA")
print("="*50)

# Cada dicionário é um REGISTRO (linha)
# A lista é a TABELA (coleção de registro)
# as chaves são as COLUNAS

tabela = [
    {"nome": "Ana", "idade": 25, "cidade": "SP"},
    {"nome": "Bruno", "idade": 30, "cidade": "RJ"},
    {"nome": "Carla", "idade": 22, "cidade": "SP"}
]

print("Tabela de alunos:")
for registro in tabela:
    print(registro)

# Isso é EXATAMENTE como o pandas (biblioteca de análise de dados) representa dados!

# ==========================================
# 2. ACESSANDO DADOS
# ==========================================

print("\n" + "="*50)
print("2. ACESSANDO DADOS")
print("="*50)

alunos = [
    {"nome": "Ana", "idade": 25, "nota": 8.5},
    {"nome": "Bruno", "idade": 30, "nota": 6.0},
    {"nome": "Carla", "idade": 22, "nota": 9.0}
]

# Acessando um registro inteiro
print(f'Primeiro aluno: {alunos[0]}')

# Acessando um campo específico
print(f'Nome do segundo aluno: {alunos[1]["nome"]}')
print(f'Nota do terceiro aluno: {alunos[2]["nota"]}')

# Percorrendo e acessando campos
print(f'\n--- Lista de alunos ---')
for aluno in alunos:
    print(f'{aluno['nome']} tem {aluno['idade']} anos e nota {aluno['nota']}')

# ==========================================
# 3. FILTRANDO DADOS (WHERE do SQL)
# ==========================================

print("\n" + "="*50)
print("3. FILTRANDO - EQUIVALENTE AO WHERE")
print("="*50)

alunos = [
    {"nome": "Ana", "idade": 25, "nota": 8.5},
    {"nome": "Bruno", "idade": 30, "nota": 6.0},
    {"nome": "Carla", "idade": 22, "nota": 9.0},
    {"nome": "Daniel", "idade": 28, "nota": 5.5},
    {"nome": "Eduarda", "idade": 35, "nota": 7.5}
]

# Jeito tradicional (com loop)
print('--- Alunos aprovados (nota >= 7) ---')
aprovados = []
for aluno in alunos:
    if aluno['nota'] >= 7:
        aprovados.append(aluno)

for aluno in aprovados:
    print(f'{aluno['nome']}: {aluno['nota']}')

# Jeito com list comprehension (mais pythonico)

print('\n--- List comprehension ---')
aprovados_lc = [aluno for aluno in alunos if aluno['nota'] >= 7]
for aluno in aprovados_lc:
    print(aluno)

# Filtro com múltiplas condições
# print('\n--- Aluno de SP com nota >= 7 ---')
# alunos_sp_aprovados = [aluno for aluno in alunos if aluno['nota'] >= 7 and aluno['cidade'] == 'SP']
#
# for aluno in alunos_sp_aprovados:
#     print(aluno)

# ==========================================
# 4. ORDENANDO DADOS (ORDER BY do SQL)
# ==========================================

print("\n" + "="*50)
print("4. ORDENANDO - EQUIVALENTE AO ORDER BY")
print("="*50)

# Ordenar por nota (crescente)
print('--- Ordenado por nota (crescente) ---')
ordenado_nota = sorted(alunos, key=lambda x: x['nota'])
for aluno in ordenado_nota:
    print(aluno)

# Ordenar por nota (decrescente)
print('--- Ordenado por nota (decrescente) ---')
ordenado_nota_dec = sorted(alunos, key=lambda x: x['nota'], reverse=True)
for aluno in ordenado_nota_dec:
    print(aluno)

# Ordenar por nome (alfabético)
print('--- Ordenar por nome (alfabético) ---')
ordenado_nome = sorted(alunos, key=lambda x: x['nome'])
for aluno in ordenado_nome:
    print(aluno)

# Ordenar por múltiplos critérios (primeiro por cidade, depois por nota)
print("\n--- Ordenado por cidade, depois por nota ---")
alunos_com_cidade = [
    {"nome": "Ana", "idade": 25, "nota": 8.5, "cidade": "SP"},
    {"nome": "Bruno", "idade": 30, "nota": 6.0, "cidade": "RJ"},
    {"nome": "Carla", "idade": 22, "nota": 9.0, "cidade": "SP"},
    {"nome": "Daniel", "idade": 28, "nota": 5.5, "cidade": "RJ"},
    {"nome": "Eduarda", "idade": 35, "nota": 7.5, "cidade": "BH"}
]

ordenado_multiplo = sorted(alunos_com_cidade, key=lambda x: (x['cidade'], x['nota']))
for aluno in ordenado_multiplo:
    print(aluno)

# ==========================================
# 5. AGREGANDO E AGRUPANDO (GROUP BY do SQL)
# ==========================================

print("\n" + "="*50)
print("5. AGRUPANDO - EQUIVALENTE AO GROUP BY")
print("="*50)

# Exemplo: total de vendas por produto
vendas = [
    {"produto": "celular", "quantidade": 10, "preco": 1500},
    {"produto": "fone", "quantidade": 30, "preco": 200},
    {"produto": "celular", "quantidade": 5, "preco": 1500},
    {"produto": "notebook", "quantidade": 3, "preco": 3500},
    {"produto": "fone", "quantidade": 15, "preco": 200}
]

# Agrupando por produto e somando quantidades
print("--- Total de unidades vendidas por produto ---")
total_por_produto = {}

for venda in vendas:
    produto = venda['produto']
    quantidade = venda['quantidade']

    if produto in total_por_produto:
        total_por_produto[produto] += quantidade
    else:
        total_por_produto[produto] = quantidade

for produto, total in total_por_produto.items():
    print(f"{produto}: {total} unidades")

# Agrupando por produto e calculando faturamento
print("\n--- Faturamento por produto ---")
faturamento = {}

for venda in vendas:
    produto = venda['produto']
    quantidade = venda['quantidade']
    preco = venda['preco']

    if produto in faturamento:
        faturamento[produto] += quantidade * preco
    else:
        faturamento[produto] = quantidade * preco

print(faturamento)

# ==========================================
# 6. ADICIONANDO E REMOVENDO REGISTROS
# ==========================================

print("\n" + "="*50)
print("6. ADICIONANDO E REMOVENDO REGISTROS")
print("="*50)

alunos = [
    {"nome": "Ana", "idade": 25, "nota": 8.5},
    {"nome": "Bruno", "idade": 30, "nota": 6.0}
]

print("Original:", alunos)

# Adicionando um novo registro
alunos.append({'nome': 'Carla', 'idade': 22, 'nota': 9.0})
print(f'Após append: {alunos}')

# Removendo pelo índice
alunos.pop(1) # remove Bruno
print(f'Após pop(1): {alunos}')

# Removendo por condição (criar nova lista)
alunos_sem_daniel = [aluno for aluno in alunos if aluno['nome'] != 'Daniel']
print(f'Após remover Daniel por condição: {alunos_sem_daniel}')

# ==========================================
# 7. EXTRAINDO COLUNAS
# ==========================================

print("\n" + "="*50)
print("7. EXTRAINDO COLUNAS (EQUIVALENTE AO SELECT)")
print("="*50)

alunos = [
    {"nome": "Ana", "idade": 25, "nota": 8.5, "cidade": "SP"},
    {"nome": "Bruno", "idade": 30, "nota": 6.0, "cidade": "RJ"},
    {"nome": "Carla", "idade": 22, "nota": 9.0, "cidade": "SP"},
    {"nome": "Daniel", "idade": 28, "nota": 7.5, "cidade": "BH"}
]

# Extrair apenas os nomes
nomes = [aluno['nome'] for aluno in alunos]
print(f'Apenas nomes: {nomes}')

# Extrair pares (nome, nota)
nome_nota = [(aluno['nome'], aluno['nota']) for aluno in alunos]
print(f'pares (nome, nota): {nome_nota}')

# Extrair apenas alunos de SP com nome e nota
alunos_sp = [{'nome': aluno['nome'], 'nota': aluno['nota']} for aluno in alunos if aluno['cidade'] == 'SP']
print(alunos_sp)

# ==========================================
# 8. EXEMPLO PRÁTICO COMPLETO
# ==========================================

print("\n" + "="*50)
print("8. EXEMPLO PRÁTICO COMPLETO")
print("="*50)

# Dados de vendas de uma loja
vendas = [
    {"produto": "celular", "quantidade": 10, "preco": 1500, "vendedor": "Ana"},
    {"produto": "fone", "quantidade": 30, "preco": 200, "vendedor": "Bruno"},
    {"produto": "celular", "quantidade": 5, "preco": 1500, "vendedor": "Ana"},
    {"produto": "notebook", "quantidade": 3, "preco": 3500, "vendedor": "Carla"},
    {"produto": "fone", "quantidade": 15, "preco": 200, "vendedor": "Bruno"},
    {"produto": "celular", "quantidade": 8, "preco": 1500, "vendedor": "Carla"}
]

# 1. Relatório: total vendido por vendedor
print("--- Total vendido por vendedor ---")
total_vendedor = {}

for venda in vendas:
    vendedor = venda['vendedor']
    valor = venda['quantidade']*venda['preco']

    if vendedor in total_vendedor:
        total_vendedor[vendedor] += valor
    else:
        total_vendedor[vendedor] = valor

for vendedor, total in total_vendedor.items():
    print(f"{vendedor}: R${total:,.2f}")

# 2. Relatório: produto mais vendido (por quantidade)
print("\n--- Produto mais vendido ---")
total_produto = {}

for venda in vendas:
    produto = venda['produto']
    quantidade = venda['quantidade']

    if produto in total_produto:
        total_produto[produto] += quantidade
    else:
        total_produto[produto] = quantidade

print(total_produto)

mais_vendido = max(total_produto.items(), key= lambda x: x[1])
print(f"{mais_vendido[0]}: {mais_vendido[1]} unidades")

# 3. Relatório: vendas acima de R$5000
print("\n--- Vendas acima de R$5000 ---")
vendas_acima = [venda for venda in vendas if venda['quantidade'] * venda['preco'] > 5000]
for venda in vendas_acima:
    valor = venda["quantidade"] * venda["preco"]
    print(f"{venda['produto']} vendido por {venda['vendedor']}: R${valor:,.2f}")

# ==========================================
# 9. RESUMO
# ==========================================

print("\n" + "="*50)
print("9. RESUMO")
print("="*50)

"""
✅ Lista de dicionários = tabela de dados (cada dicionário é uma linha)
✅ Acessar: lista[indice][chave]
✅ Filtrar (WHERE): [item for item in lista if condição]
✅ Ordenar (ORDER BY): sorted(lista, key=lambda x: x[chave])
✅ Agrupar (GROUP BY): usar dicionário auxiliar para somar/contar
✅ Extrair colunas (SELECT): [item[chave] for item in lista]
✅ Adicionar: lista.append(novo_dicionario)
✅ Remover: lista.pop(indice) ou list comprehension

📌 Comparação com SQL:
- SELECT * FROM tabela → lista de dicionários
- WHERE → list comprehension com if
- ORDER BY → sorted() com key
- GROUP BY → dicionário auxiliar com agregação
"""
##########################################
# EXERCÍCIOS - AULA 7.4
##########################################
# NÍVEL 1-3: Aquecimento
##########################################
"""
1. Criando uma tabela

# Crie uma lista de dicionários representando 3 produtos com: nome, preco, quantidade
# Mostre todos os produtos
"""
"""
estoque = [
    {'nome': 'Intruder', 'preco': 8000, 'quantidade': 3},
    {'nome': 'Bros', 'preco': 20000, 'quantidade': 5},
    {'nome': 'Factor', 'preco': 15000, 'quantidade': 7}
]

print(estoque)
"""
########################################
"""
2. Acessando campos
python

# Use a lista do exercício 1 para:
# - Mostrar o nome do segundo produto
# - Mostrar o preço do primeiro produto
# - Mostrar a quantidade do terceiro produto
"""
"""
estoque = [
    {'nome': 'Intruder', 'preco': 8000, 'quantidade': 3},
    {'nome': 'Bros', 'preco': 20000, 'quantidade': 5},
    {'nome': 'Factor', 'preco': 15000, 'quantidade': 7}
]

print(f'Nome do segundo produto: {estoque[1]['nome']}')
print(f'Preço do primeiro produto: {estoque[0]['preco']}')
print(f'Quantidade do terceiro produto: {estoque[2]['quantidade']}')
"""
##########################################################
"""
3. Percorrendo a tabela

# Use a lista do exercício 1 e um loop for para mostrar:
# "Produto X custa R$ Y e tem Z unidades em estoque"
"""
"""
estoque = [
    {'nome': 'Intruder', 'preco': 8000, 'quantidade': 3},
    {'nome': 'Bros', 'preco': 20000, 'quantidade': 5},
    {'nome': 'Factor', 'preco': 15000, 'quantidade': 7}
]

for produto in estoque:
    print(f'Produto {produto['nome']} custa R$ {produto['preco']:,.2f} e tem {produto['quantidade']} unidades em estoque')
"""
##############################################
# NÍVEL 4-6: Aplicação
##############################################
"""
4. Filtrando (WHERE)

# Dada a lista de alunos:
alunos = [
    {"nome": "Ana", "idade": 25, "nota": 8.5},
    {"nome": "Bruno", "idade": 30, "nota": 6.0},
    {"nome": "Carla", "idade": 22, "nota": 9.0},
    {"nome": "Daniel", "idade": 28, "nota": 5.5},
    {"nome": "Eduarda", "idade": 35, "nota": 7.5}
]
# Crie listas filtradas para:
# - Alunos com nota >= 7
# - Alunos com idade < 30
# - Alunos com nota >= 7 E idade < 30
"""
"""
alunos = [
    {"nome": "Ana", "idade": 25, "nota": 8.5},
    {"nome": "Bruno", "idade": 30, "nota": 6.0},
    {"nome": "Carla", "idade": 22, "nota": 9.0},
    {"nome": "Daniel", "idade": 28, "nota": 5.5},
    {"nome": "Eduarda", "idade": 35, "nota": 7.5}
]

alunos_aprovados = [aluno for aluno in alunos if aluno['nota'] >= 7]
alunos_novos = [aluno for aluno in alunos if aluno['idade'] < 30]
alunos_novos_aprovados = [aluno for aluno in alunos if aluno['nota'] >= 7 and aluno['idade'] < 30]

print(alunos_aprovados)
print(alunos_novos)
print(alunos_novos_aprovados)
"""
##########################################################
"""
5. Ordenando (ORDER BY)

# Use a lista de alunos do exercício 4 para:
# - Ordenar por nota (crescente)
# - Ordenar por nota (decrescente)
# - Ordenar por nome (alfabético)
# - Ordenar por idade (decrescente)
"""
"""
alunos = [
    {"nome": "Ana", "idade": 25, "nota": 8.5},
    {"nome": "Bruno", "idade": 30, "nota": 6.0},
    {"nome": "Carla", "idade": 22, "nota": 9.0},
    {"nome": "Daniel", "idade": 28, "nota": 5.5},
    {"nome": "Eduarda", "idade": 35, "nota": 7.5}
]

ordem_nota_crescente = sorted(alunos, key=lambda x: x['nota'])
ordem_nota_decrescente = sorted(alunos, key=lambda x: x['nota'], reverse=True)
ordem_nome = sorted(alunos, key=lambda x: x['nome'])
ordem_idade = sorted(alunos, key=lambda x: x['idade'], reverse=True)

print(ordem_nota_crescente)
print(ordem_nota_decrescente)
print(ordem_nome)
print(ordem_idade)
"""

#################################################
"""
6. Extraindo colunas (SELECT)

# Use a lista de alunos do exercício 4 para extrair:
# - Lista apenas com os nomes
# - Lista apenas com as notas
# - Lista de tuplas (nome, nota)
# - Lista de dicionários apenas com nome e nota
"""
"""
alunos = [
    {"nome": "Ana", "idade": 25, "nota": 8.5},
    {"nome": "Bruno", "idade": 30, "nota": 6.0},
    {"nome": "Carla", "idade": 22, "nota": 9.0},
    {"nome": "Daniel", "idade": 28, "nota": 5.5},
    {"nome": "Eduarda", "idade": 35, "nota": 7.5}
]
nomes = [aluno['nome'] for aluno in alunos]
notas = [aluno['nota'] for aluno in alunos]
tuplas = [(aluno['nome'], aluno['nota']) for aluno in alunos]
nome_nota = [{'nome': aluno['nome'], 'nota': aluno['nota']} for aluno in alunos]
"""
#########################################
# NÍVEL 7-8: Manipulação
#########################################
"""
# Dados de vendas:
vendas = [
    {"produto": "celular", "quantidade": 10, "vendedor": "Ana"},
    {"produto": "fone", "quantidade": 30, "vendedor": "Bruno"},
    {"produto": "celular", "quantidade": 5, "vendedor": "Ana"},
    {"produto": "notebook", "quantidade": 3, "vendedor": "Carla"},
    {"produto": "fone", "quantidade": 15, "vendedor": "Bruno"}
]
# Calcule:
# - Total de unidades vendidas por produto
# - Total de unidades vendidas por vendedor
"""
"""vendas = [
    {"produto": "celular", "quantidade": 10, "vendedor": "Ana"},
    {"produto": "fone", "quantidade": 30, "vendedor": "Bruno"},
    {"produto": "celular", "quantidade": 5, "vendedor": "Ana"},
    {"produto": "notebook", "quantidade": 3, "vendedor": "Carla"},
    {"produto": "fone", "quantidade": 15, "vendedor": "Bruno"}
]
produto_quantidade = {}
vendedor_quantidade = {}

for venda in vendas:
    produto = venda['produto']
    vendedor = venda['vendedor']
    quantidade = venda['quantidade']

    if produto in produto_quantidade:
        produto_quantidade[produto] += quantidade
    else:
        produto_quantidade[produto] = quantidade

    if not vendedor in vendedor_quantidade: # inverti só pra ver a legibilidade
        vendedor_quantidade[vendedor] = quantidade
    else:
        vendedor_quantidade[vendedor] += quantidade

print(f'Total de unidades vendidas por produto: {produto_quantidade}')
print(f'Total de unidades vendidas por vendedor: {vendedor_quantidade}')"""

###########################################################################
"""
8. Agrupamento com múltiplas métricas

# Use os dados de vendas do exercício 7 e adicione o campo "preco":
# celular: 1500, fone: 200, notebook: 3500
# Calcule por produto:
# - Quantidade total vendida
# - Faturamento total (quantidade * preco)
# - Preço médio (faturamento / quantidade)
"""
"""
vendas = [
    {"produto": "celular", "quantidade": 10, "vendedor": "Ana"},
    {"produto": "fone", "quantidade": 30, "vendedor": "Bruno"},
    {"produto": "celular", "quantidade": 5, "vendedor": "Ana"},
    {"produto": "notebook", "quantidade": 3, "vendedor": "Carla"},
    {"produto": "fone", "quantidade": 15, "vendedor": "Bruno"}
]

for venda in vendas: # Eu ia fazer manualmente, mas automatizar assim é melhor pra grandes volumes e evita erros
    if venda['produto'] == 'celular':
        venda['preco'] = 1500
    elif venda['produto'] == 'fone':
        venda['preco'] = 200
    elif venda['produto'] == 'notebook':
        venda['preco'] = 3500

quantidade_total_produto = {}
faturamento_total_produto = {}
preco_medio_produto = {}

for venda in vendas:
    produto = venda['produto']
    quantidade = venda['quantidade']
    valor = venda['quantidade'] * venda['preco']

    if produto in quantidade_total_produto:
        quantidade_total_produto[produto] += quantidade
    else:
        quantidade_total_produto[produto] = quantidade

    if produto in faturamento_total_produto:
        faturamento_total_produto[produto] += valor
    else:
        faturamento_total_produto[produto] = valor

preco_medio_produto = {nome: faturamento_total_produto[nome]/quantidade_total_produto[nome] for nome in faturamento_total_produto.keys()} # foi o jeito que eu pensei, tem uma forma mais elegante de fazer isso?
# esse caso do preco_medio_produto me lembrou muito quando a gente tem que criar uma CTE no SQL pq eu preciso de um valor pré-calculado


print(faturamento_total_produto)
print(quantidade_total_produto)

print(preco_medio_produto)
"""
############################################
# NÍVEL 9-10: Desafios
############################################
"""
9. Relatório completo de vendas

# Dados de vendas:
vendas = [
    {"produto": "celular", "quantidade": 10, "preco": 1500, "vendedor": "Ana", "data": "2024-01-15"},
    {"produto": "fone", "quantidade": 30, "preco": 200, "vendedor": "Bruno", "data": "2024-01-15"},
    {"produto": "celular", "quantidade": 5, "preco": 1500, "vendedor": "Ana", "data": "2024-01-16"},
    {"produto": "notebook", "quantidade": 3, "preco": 3500, "vendedor": "Carla", "data": "2024-01-16"},
    {"produto": "fone", "quantidade": 15, "preco": 200, "vendedor": "Bruno", "data": "2024-01-17"},
    {"produto": "celular", "quantidade": 8, "preco": 1500, "vendedor": "Carla", "data": "2024-01-17"}
]
# Crie um relatório que mostre:
# - Vendas totais por dia
# - Vendas totais por vendedor
# - Produto mais vendido (em quantidade) no período
# - Dia com maior faturamento
# - Vendedor com maior faturamento
"""
"""
vendas = [
    {"produto": "celular", "quantidade": 10, "preco": 1500, "vendedor": "Ana", "data": "2024-01-15"},
    {"produto": "fone", "quantidade": 30, "preco": 200, "vendedor": "Bruno", "data": "2024-01-15"},
    {"produto": "celular", "quantidade": 5, "preco": 1500, "vendedor": "Ana", "data": "2024-01-16"},
    {"produto": "notebook", "quantidade": 3, "preco": 3500, "vendedor": "Carla", "data": "2024-01-16"},
    {"produto": "fone", "quantidade": 15, "preco": 200, "vendedor": "Bruno", "data": "2024-01-17"},
    {"produto": "celular", "quantidade": 8, "preco": 1500, "vendedor": "Carla", "data": "2024-01-17"}
]

vendas_dia = {}
vendas_vendedor = {}
quantidade_produto = {}
faturamento_dia = {}
faturamento_vendedor = {}

for venda in vendas:
    produto = venda['produto']
    quantidade = venda['quantidade']
    preco = venda['preco']
    vendedor = venda['vendedor']
    data = venda['data']

    if data in vendas_dia:
        vendas_dia[data] += quantidade
    else:
        vendas_dia[data] = quantidade

    if vendedor in vendas_vendedor:
        vendas_vendedor[vendedor] += quantidade
    else:
        vendas_vendedor[vendedor] = quantidade

    if produto in quantidade_produto:
        quantidade_produto[produto] += quantidade
    else:
        quantidade_produto[produto] = quantidade

    if data in faturamento_dia:
        faturamento_dia[data] += quantidade * preco
    else:
        faturamento_dia[data] = quantidade * preco

    if vendedor in faturamento_vendedor:
        faturamento_vendedor[vendedor] += quantidade * preco
    else:
        faturamento_vendedor[vendedor] = quantidade * preco

print(f'Vendas totais por dia: {vendas_dia}')
print(f'Vendas totais por vendedor: {vendas_vendedor}')
print(f'Quantidade vendida por produto: {quantidade_produto}') # Sei que não pediu, mas já para aproveitar que estava feito...
print(f'Produto mais vendido (por quantidade): {max(quantidade_produto.items(), key=lambda x: x[1])}')
print(f'Faturamento por dia: {faturamento_dia}')
print(f'Dia com maior faturamento: {max(faturamento_dia.items(), key=lambda x: x[1])}')
print(f'Faturamento por vendedor: {faturamento_vendedor}')
print(f'Vendedor com maior faturamento: {max(faturamento_vendedor.items(), key=lambda x: x[1])}')
"""
###################################################################
"""
10. DESAFIO FINAL: Sistema de alunos com notas múltiplas

# Dados de alunos com notas em várias disciplinas:
alunos = [
    {"nome": "Ana", "notas": {"portugues": 8.5, "matematica": 7.0, "ciencias": 9.0}},
    {"nome": "Bruno", "notas": {"portugues": 6.0, "matematica": 5.5, "ciencias": 7.0}},
    {"nome": "Carla", "notas": {"portugues": 9.0, "matematica": 8.5, "ciencias": 9.5}}
]
# Para cada aluno, calcule:
# - Média das notas
# - Maior nota
# - Menor nota
# - Status: "Aprovado" se média >= 7, "Recuperação" se 5 <= média < 7, "Reprovado" se média < 5
# Depois, crie um relatório ordenado por média (do maior para o menor)
"""
alunos = [
    {"nome": "Ana", "notas": {"portugues": 8.5, "matematica": 7.0, "ciencias": 9.0}},
    {"nome": "Bruno", "notas": {"portugues": 6.0, "matematica": 5.5, "ciencias": 7.0}},
    {"nome": "Carla", "notas": {"portugues": 9.0, "matematica": 8.5, "ciencias": 9.5}}
]

medias = {}
maiores_notas = {}
menores_notas = {}


for aluno in alunos:
    nome = aluno['nome']
    notas = aluno['notas']
    soma_notas = 0
    maior_nota = float('-inf')
    menor_nota = float('inf')

    for materia, nota in notas.items():
        soma_notas += nota

        if nota > maior_nota:
            maior_nota = nota
        maiores_notas[nome] = maior_nota

        if nota < menor_nota:
            menor_nota = nota
        menores_notas[nome] = menor_nota


    if nome in medias:
        medias[nome] += round(soma_notas/len(notas), 2)
    else:
        medias[nome] = round(soma_notas/len(notas), 2)

alunos_status = {nome: 'Aprovado' if media >= 7 else 'Recuperação' if 5 <= media < 7 else 'Reprovado' for nome, media in medias.items()}

print(f'Médias: {medias}')
print(f'Maiores notas: {maiores_notas}')
print(f'Menores notas: {menores_notas}')
print(f'Status: {alunos_status}')

relatorio = [{'nome': nome, 'media': medias[nome],'maior_nota': maiores_notas[nome], 'menor_nota': menores_notas[nome], 'status': alunos_status[nome]} for nome in medias.keys()]

relatorio_ord_media = sorted(relatorio, key=lambda x: x['media'], reverse=True)

print('\nRelatório ordenado por média: ')
for aluno in relatorio_ord_media:
    print(aluno)

# Achei muito divertido! Estava com saudade de mexer com SQL, dados e etc. hehe