"""
Módulo 6: listas
Exercícios Integradores
Data: 27/03/2026
Objetivo: Resolver problemas que misturam tudo que vimos
"""

"""
Exercício 1: Analisador de Vendas

Tema: Listas, zip, list comprehension, estatísticas básicas

# Dados de vendas (produtos, vendas por trimestre)
produtos = ["Notebook", "Mouse", "Teclado", "Monitor", "Webcam"]
vendas_q1 = [120, 350, 280, 95, 180]
vendas_q2 = [135, 420, 310, 110, 210]
vendas_q3 = [150, 380, 295, 105, 195]
vendas_q4 = [165, 450, 330, 125, 225]

# Tarefas:
# 1. Use zip() para criar uma lista de tuplas com (produto, q1, q2, q3, q4)
# 2. Use list comprehension para criar uma lista com o total anual de cada produto
# 3. Use list comprehension para criar uma lista com a média trimestral de cada produto
# 4. Encontre o produto mais vendido no ano (use max com key)
# 5. Encontre o trimestre com maior volume total de vendas (some todas as vendas por trimestre)
# 6. Crie um relatório formatado mostrando:
#    Produto | Q1 | Q2 | Q3 | Q4 | Total | Média
#    (use formatação com f-strings e alinhamento)
"""
"""
produtos = ["Notebook", "Mouse", "Teclado", "Monitor", "Webcam"]
vendas_q1 = [120, 350, 280, 95, 180]
vendas_q2 = [135, 420, 310, 110, 210]
vendas_q3 = [150, 380, 295, 105, 195]
vendas_q4 = [165, 450, 330, 125, 225]

# 1. Use zip() para criar uma lista de tuplas com (produto, q1, q2, q3, q4)
prod_vendas = list(zip(produtos, vendas_q1, vendas_q2, vendas_q3, vendas_q4))
print(f'Produtos e suas vendas nos trimestres: {prod_vendas}')

# 2. Use list comprehension para criar uma lista com o total anual de cada produto
total_anual_produtos = [v1 + v2 + v3 + v4 for v1, v2, v3, v4 in zip(vendas_q1, vendas_q2, vendas_q3, vendas_q4)]
print(f'Lista com total anual de cada produto: {total_anual_produtos}')

# 3. Use list comprehension para criar uma lista com a média trimestral de cada produto
media_trim_prod = [(v1 + v2 + v3 + v4)/4 for v1, v2, v3, v4 in zip(vendas_q1, vendas_q2, vendas_q3, vendas_q4)]
print(f'Lista com a média trimestral de cada produto: {media_trim_prod}')

# 4. Encontre o produto mais vendido no ano (use max com key)
ind = float('-inf')
for nome, total in zip(produtos, total_anual_produtos): # n consegui fazer com max key "/ gosto dessa técnica do -inf hehe
    if total > ind:
        prod_mais_vendido = nome
        ind = total

print(f'Produto mais vendido: {prod_mais_vendido}')

# 5. Encontre o trimestre com maior volume total de vendas (some todas as vendas por trimestre)

soma_trimestre = [sum(vendas_q1), sum(vendas_q2), sum(vendas_q3), sum(vendas_q4)]

ind = float('-inf')
for trimestre, total in enumerate(soma_trimestre):
    if total > ind:
        maior_trimestre = trimestre + 1 # +1 pq começa no zero
        ind = total

print(f'Trimestre com mais vendas: {maior_trimestre}° Trimestre')

# 6. Crie um relatório formatado mostrando:
#    Produto | Q1 | Q2 | Q3 | Q4 | Total | Média
#    (use formatação com f-strings e alinhamento)

print(f'{'Produto': <10}{'Q1': >6}{'Q2': >8}{'Q3': >8}{'Q4': >8}{'Total': >8}{'Média': >8}')
for prod, v1, v2, v3, v4, total, media in zip(produtos, vendas_q1, vendas_q2, vendas_q3, vendas_q4, total_anual_produtos, media_trim_prod):
    print(f'{prod: <8}{v1: >8}{v2: >8}{v3: >8}{v4: >8}{total: >8}{media: >8}')

# Eu optei por não criar uma matriz com todas as vendas_qn, para ver como seria hehe.
"""
#####################################################################################
"""
Exercício 2: Matriz de Distâncias

Tema: Listas aninhadas, list comprehension, loops

# Você tem uma lista de cidades e uma matriz de distâncias entre elas
cidades = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Brasília"]

# Matriz de distâncias (km) - simétrica
distancias = [
    [0, 430, 586, 1015],      # São Paulo para as outras
    [430, 0, 434, 1145],      # Rio de Janeiro
    [586, 434, 0, 716],       # Belo Horizonte
    [1015, 1145, 716, 0]      # Brasília
]

# Tarefas:
# 1. Mostre a matriz formatada com os nomes das cidades (cabeçalho)
# 2. Use list comprehension para criar uma lista com a distância média de cada cidade para as outras
# 3. Encontre o par de cidades mais próximas (menor distância > 0)
# 4. Encontre o par de cidades mais distantes
# 5. Crie uma lista de tuplas com (cidade_origem, cidade_destino, distancia) para todos os pares
# 6. Use sorted() para ordenar essa lista pela distância (do menor para o maior)
# 7. Mostre os 5 pares mais próximos
"""
"""
cidades = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Brasília"]

# Matriz de distâncias (km) - simétrica
distancias = [
    [0, 430, 586, 1015],      # São Paulo para as outras
    [430, 0, 434, 1145],      # Rio de Janeiro
    [586, 434, 0, 716],       # Belo Horizonte
    [1015, 1145, 716, 0]      # Brasília
]
# 1. Mostre a matriz formatada com os nomes das cidades (cabeçalho)
print(f'{'São Paulo':>20}{'Rio de Janeiro':>20}{'Belo Horizonte':>20}{'Brasília':>20}')

for i in range(len(distancias)):
    for j in range(len(distancias[0])):
        print(F'{distancias[i][j]: >20}', end='')
    print()

# 2. Use list comprehension para criar uma lista com a distância média de cada cidade para as outras
medias = [round(sum(distancias[i])/(len(distancias[i])-1), 2) for i in range(len(distancias))] # o sum pega o 0 mas divide por len-1 pra "tirar" a contribuição do zero
print(medias)

# 3. Encontre o par de cidades mais próximas (menor distância > 0)
index = float('inf')
for i, nome_i in zip(range(len(distancias)), cidades): # Tive essa ideia para pegar os nomes, é assim mesmo?
    for j, nome_j in zip(range(len(distancias[0])), cidades):
        if 0 < distancias[i][j] < index:
            menor_dist_nome = [nome_i, nome_j]
            index = distancias[i][j]

print(f'A menor distância está entre o par: {menor_dist_nome}')

# 4. Encontre o par de cidades mais distantes
index = float('-inf')
for i, nome_i in zip(range(len(distancias)), cidades):
    for j, nome_j in zip(range(len(distancias[0])), cidades):
        if distancias[i][j] > index:
            maior_dist_nome = [nome_i, nome_j]
            index = distancias[i][j]

print(f'A maior distância está entre o par: {maior_dist_nome}')

# 5. Crie uma lista de tuplas com (cidade_origem, cidade_destino, distancia) para todos os pares
cidades_dist = []
for i, nome_i in zip(range(len(distancias)), cidades):
    for j, nome_j in zip(range(len(distancias[0])), cidades):
        if distancias[i][j] > 0: # para excluir "viagens" para a mesma cidade.
            tupla = (nome_i, nome_j, distancias[i][j])
            cidades_dist.append(tupla)

# 6. Use sorted() para ordenar essa lista pela distância (do menor para o maior)
cidades_dist_ord = sorted(cidades_dist, key= lambda x: x[2]) # tive que pesquisar como faz, ainda não acostumei com o lambda... não vimos isso muito bem ainda né?

# 7. Mostre os 5 pares mais próximos
print()

for i in range(0, len(cidades_dist_ord)-4, 2): # passo 2 para pular os repetidos, -4 para ajustar para os 4 primeiros.
    print(cidades_dist_ord[i])cidades = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Brasília"]
"""
##########################################################################################
"""
Exercício 3: Sistema de Notas com Análise Avançada

Tema: Listas aninhadas, zip, list comprehension, cópia

# Dados de uma turma: alunos e suas notas em 4 bimestres
alunos = ["Ana", "Bruno", "Carla", "Daniel", "Eduarda", "Felipe"]
notas = [
    [8.5, 7.0, 9.0, 8.5],   # Ana
    [6.0, 5.5, 7.0, 6.5],   # Bruno
    [9.0, 8.5, 9.5, 9.0],   # Carla
    [5.0, 4.5, 6.0, 5.5],   # Daniel
    [7.5, 8.0, 7.0, 8.5],   # Eduarda
    [6.5, 7.5, 6.0, 7.0]    # Felipe
]

# Tarefas:
# 1. Calcule a média de cada aluno e classifique:
#    - Média >= 7: Aprovado
#    - 5 <= Média < 7: Recuperação
#    - Média < 5: Reprovado
# 2. Calcule a média da turma por bimestre
# 3. Use list comprehension para criar uma lista com a maior nota de cada aluno
# 4. Use list comprehension para criar uma lista com a menor nota de cada aluno
# 5. Encontre o aluno com maior média e o com menor média
# 6. Crie uma cópia profunda da matriz de notas
# 7. Na cópia, aplique um bônus de 0.5 ponto para alunos em recuperação (média entre 5 e 7)
#    - Mas a nota não pode ultrapassar 10
# 8. Mostre a matriz original e a modificada (confirmando que a original não mudou)
"""
"""
notas = [
    [8.5, 7.0, 9.0, 8.5],   # Ana
    [6.0, 5.5, 7.0, 6.5],   # Bruno
    [9.0, 8.5, 9.5, 9.0],   # Carla
    [5.0, 4.5, 6.0, 5.5],   # Daniel
    [7.5, 8.0, 7.0, 8.5],   # Eduarda
    [6.5, 7.5, 6.0, 7.0]    # Felipe
]

alunos = ["Ana", "Bruno", "Carla", "Daniel", "Eduarda", "Felipe"]

# 1. Calcule a média de cada aluno e classifique:
#    - Média >= 7: Aprovado
#    - 5 <= Média < 7: Recuperação
#    - Média < 5: Reprovado

medias = [sum(notas[i])/len(notas[0]) for i in range(len(notas))]
print(medias)
print()
for nome, media in zip(alunos, medias):
    if media >= 7:
        print(f'{nome} - {media}: Aprovado!')
    elif 5 <= media < 7:
        print(f'{nome} - {media}: Recuperação!')
    elif media < 5:
        print(f'{nome} - {media}: Reprovado!')

# 2. Calcule a média da turma por bimestre
print()
for i in range(len(notas[0])):
    soma_bimestre = 0
    for j in range(len(notas)):
        soma_bimestre += notas[j][i]
    print(f'Média do {i+1}° Bimestre: {soma_bimestre/len(notas):.2f} ')

# 3. Use list comprehension para criar uma lista com a maior nota de cada aluno
maiores_notas = [max(notas[i]) for i in range(len(notas))]
print(maiores_notas)

# 4. Use list comprehension para criar uma lista com a menor nota de cada aluno
menores_notas = [min(notas[i]) for i in range(len(notas))]
print(menores_notas)

# 5. Encontre o aluno com maior média e o com menor média
print()
index_maior = float('-inf')
index_menor = float('inf')
for nome, media in zip(alunos, medias):
    # encontrar maior media:
    if media > index_maior:
        index_maior = media
        maior_media = (nome, media)
    # encontrar menor media:
    if media < index_menor:
        index_menor = media
        menor_media = (nome, media)
print(f'{maior_media[0]} teve a maior média! {maior_media[1]}') # Eu tava pensando como eu poderia acessar o nome e a média, hehe, criei a tupla e puxei pelas entradas.
print(f'{menor_media[0]} teve a menor média! {menor_media[1]}')

# 6. Crie uma cópia profunda da matriz de notas
print()
import copy
notas_copia = copy.deepcopy(notas)

# 7. Na cópia, aplique um bônus de 0.5 ponto para alunos em recuperação (média entre 5 e 7)
#    - Mas a nota não pode ultrapassar 10
for i, media in zip(range(len(notas_copia)), medias):
    if 5 <= media < 7:
        for j in range(len(notas_copia[0])):
            if notas_copia[i][j] + 0.5 <= 10: # para garantir que não vai estourar 10
                notas_copia[i][j] += 0.5

# 8. Mostre a matriz original e a modificada (confirmando que a original não mudou)
print()
for linha in notas:
    print(linha)

print()
for linha in notas_copia:
    print(linha)
"""
###############################################################################################
"""
Exercício 4: Agrupamento de Dados com Zip e List Comprehension

Tema: Zip, list comprehension, agrupamento

# Dados de funcionários (3 listas paralelas)
nomes = ["Ana", "Bruno", "Carla", "Daniel", "Eduarda", "Felipe", "Gabriela", "Henrique"]
departamentos = ["Vendas", "TI", "Vendas", "RH", "TI", "Vendas", "RH", "TI"]
salarios = [4500, 6200, 4800, 3800, 5800, 4700, 4200, 6500]
idades = [28, 35, 32, 41, 29, 33, 38, 30]

# Tarefas:
# 1. Use zip() para criar uma lista de dicionários? (brincadeira - sem dicionários!)
#    Na verdade, crie uma lista de tuplas com (nome, depto, salario, idade)

# 2. Use list comprehension para criar:
#    a) Lista dos nomes dos funcionários do departamento "TI"
#    b) Lista dos salários dos funcionários de "Vendas"
#    c) Lista das idades dos funcionários com salário > 5000

# 3. Calcule a média salarial por departamento (use list comprehension para filtrar)

# 4. Encontre o funcionário mais velho de cada departamento (pode fazer separado por depto)

# 5. Use list comprehension para criar uma lista com "Júnior" se idade < 30,
#    "Pleno" se 30 <= idade <= 40, "Sênior" se idade > 40

# 6. Crie um relatório formatado mostrando:
#    Nome | Depto | Salário | Idade | Nível
#    (ordenado por salário decrescente)
"""
"""
nomes = ["Ana", "Bruno", "Carla", "Daniel", "Eduarda", "Felipe", "Gabriela", "Henrique"]
departamentos = ["Vendas", "TI", "Vendas", "RH", "TI", "Vendas", "RH", "TI"]
salarios = [4500, 6200, 4800, 3800, 5800, 4700, 4200, 6500]
idades = [28, 35, 32, 41, 29, 33, 38, 30]

# 1. Use zip() para criar uma lista de dicionários? (brincadeira - sem dicionários!) # já ia reclamar hahahah, obrigado pelo respeito e a brincadeira foi engraçada :)
#    Na verdade, crie uma lista de tuplas com (nome, depto, salario, idade)
dados_funcionarios = [(nomes[i], departamentos[i], salarios[i], idades[i]) for i in range(len(nomes))]
# dados_funcionarios = list(zip(nomes, departamentos, salarios, idades)) ou assim né? Acho que assim é melhor... Percebi fazendo a tarefa 6. haha
print(dados_funcionarios)

# 2. Use list comprehension para criar:
#    a) Lista dos nomes dos funcionários do departamento "TI"
print()
funcionarios_ti = [dados_funcionarios[i][0] for i in range(len(dados_funcionarios)) if dados_funcionarios[i][1] == 'TI']
print(f'Funcionários do setor de TI: {funcionarios_ti}')

#    b) Lista dos salários dos funcionários de "Vendas"
print()
funcionarios_vendas = [dados_funcionarios[i][0] for i in range(len(dados_funcionarios)) if dados_funcionarios[i][1] == 'Vendas']
print(f'Funcionários do setor de Vendas: {funcionarios_vendas}')

#    c) Lista das idades dos funcionários com salário > 5000
print()
idades_func_ma5000 = [dados_funcionarios[i][3] for i in range(len(dados_funcionarios)) if dados_funcionarios[i][2] > 5000]
print(f'Idades dos funcionários com salário maior que 5000: {idades_func_ma5000}')

# Essas tarefas aqui me lembraram bastante as consultas em SQL heheh

# 3. Calcule a média salarial por departamento (use list comprehension para filtrar)
print()

media_vendas_lc = [dados_funcionarios[i][2] for i in range(len(dados_funcionarios)) if dados_funcionarios[i][1] == 'Vendas']
print(f'Média salarial do setor de Vendas: {sum(media_vendas_lc)/len(media_vendas_lc):.2f}')

media_ti_lc = [dados_funcionarios[i][2] for i in range(len(dados_funcionarios)) if dados_funcionarios[i][1] == 'TI']
print(f'Média salarial do setor de TI: {sum(media_ti_lc)/len(media_ti_lc):.2f}')

media_rh_lc = [dados_funcionarios[i][2] for i in range(len(dados_funcionarios)) if dados_funcionarios[i][1] == 'RH']
print(f'Média salarial do setor de RH: {sum(media_rh_lc)/len(media_rh_lc):.2f}')

# Esse aqui eu quebrei a cabeça viu... até eu perceber que poderia ser feito dessa forma mais simples.
# Eu estava indo por esse caminho:
# soma_vendas, soma_ti, soma_rh, qtd_vendas, qtd_ti, qtd_rh = 0, 0, 0, 0, 0, 0
# for i in range(len(dados_funcionarios)):
#     if dados_funcionarios[i][1] == 'Vendas':
#         soma_vendas += dados_funcionarios[i][2]
#         qtd_vendas += 1
#     elif dados_funcionarios[i][1] == 'TI':
#         soma_ti += dados_funcionarios[i][2]
#         qtd_ti += 1
#     elif dados_funcionarios[i][1] == 'RH':
#         soma_rh += dados_funcionarios[i][2]
#         qtd_rh += 1
#
# medias_dpt = []...

# 4. Encontre o funcionário mais velho de cada departamento (pode fazer separado por depto):
print()
ind_vendas, ind_ti, ind_rh = float('-inf'), float('-inf'), float('-inf')
for i in range(len(dados_funcionarios)):
    if dados_funcionarios[i][1] == 'Vendas':
        if dados_funcionarios[i][3] > ind_vendas:
            velho_vendas = dados_funcionarios[i][0]
            ind_vendas = dados_funcionarios[i][3]
    elif dados_funcionarios[i][1] == 'TI':
        if dados_funcionarios[i][3] > ind_ti:
            velho_ti = dados_funcionarios[i][0]
            ind_ti = dados_funcionarios[i][3]
    elif dados_funcionarios[i][1] == 'RH':
        if dados_funcionarios[i][3] > ind_rh:
            velho_rh = dados_funcionarios[i][0]
            ind_rh = dados_funcionarios[i][3]
print(f'Funcionário mais velho Vendas: {velho_vendas}')
print(f'Funcionário mais velho TI: {velho_ti}')
print(f'Funcionário mais velho RH: {velho_rh}')

# 5. Use list comprehension para criar uma lista com "Júnior" se idade < 30,
#    "Pleno" se 30 <= idade <= 40, "Sênior" se idade > 40
print()
niveis = ['Júnior' if idade < 30 else 'Pleno' if 30 <= idade <= 40 else 'Sênior' for idade in idades]
print(niveis)

# 6. Crie um relatório formatado mostrando:
#    Nome | Depto | Salário | Idade | Nível
#    (ordenado por salário decrescente)
print()

dados_funcionarios_nivel = list(zip(nomes, departamentos, salarios, idades, niveis))
dados_funcionarios_nivel = sorted(dados_funcionarios_nivel, key = lambda x: x[2], reverse = True)

print(f'{'Nome': <10}{'Depto': >6}{'Salário': >10}{'Idade': >8}{'Nível': >8}')
for nome, dpt, salario, idade, nivel in dados_funcionarios_nivel:
    print(f'{nome: <10}{dpt: >6}{salario: >10}{idade: >8}{nivel: >8}')
    
# Esse exercício inteiro foi basicamente SQL com Python né? hahaha
"""
##################################################################################################
"""
# Você tem um estoque representado como uma matriz:
# - Cada linha é um produto
# - Cada coluna é um mês (Janeiro a Junho)
# - Cada elemento é a quantidade vendida no mês

estoque = [
    [120, 135, 150, 165, 180, 200],  # Produto A: Smartphone
    [80, 85, 90, 95, 100, 110],      # Produto B: Tablet
    [250, 240, 230, 220, 210, 200],  # Produto C: Headphone
    [45, 50, 55, 60, 65, 70],        # Produto D: Power Bank
    [300, 310, 320, 330, 340, 350]   # Produto E: Capa
]

produtos = ["Smartphone", "Tablet", "Headphone", "Power Bank", "Capa"]
meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"]

# Tarefas:

# 1. VISUALIZAÇÃO
#    a) Mostre a matriz formatada (produtos nas linhas, meses nas colunas)

# 2. ANÁLISE POR PRODUTO
#    b) Calcule o total vendido por produto (soma das linhas)
#    c) Calcule a média mensal por produto
#    d) Calcule a variação percentual entre o primeiro e o último mês para cada produto
#       (fórmula: ((último - primeiro) / primeiro) * 100)

# 3. ANÁLISE POR MÊS
#    e) Calcule o total vendido por mês (soma das colunas)
#    f) Encontre o mês com maior venda total
#    g) Encontre o mês com menor venda total

# 4. ANÁLISE DE TENDÊNCIA
#    h) Para cada produto, determine se as vendas estão:
#       - "Crescente" (cada mês >= mês anterior)
#       - "Decrescente" (cada mês <= mês anterior)
#       - "Oscilante" (nenhum dos acima)

# 5. ANÁLISE DE DESEMPENHO
#    i) Encontre o produto mais vendido no período (maior total)
#    j) Encontre o produto com maior média mensal
#    k) Encontre o produto com maior crescimento percentual

# 6. MANIPULAÇÃO COM CÓPIA
#    l) Crie uma cópia profunda da matriz de estoque
#    m) Na cópia, aplique um reajuste:
#       - Produtos com média > 200: redução de 10% nas vendas (redução de estoque)
#       - Produtos com média < 100: aumento de 15% nas vendas (promoção)
#    n) Mostre a matriz original e a modificada (confirmando que a original não mudou)

# 7. RELATÓRIO FINAL
#    o) Gere um relatório resumido usando list comprehension, zip e formatação
#    (use sua criatividade para o formato)
"""
estoque = [
    [120, 135, 150, 165, 180, 200],  # Produto A: Smartphone
    [80, 85, 90, 95, 100, 110],      # Produto B: Tablet
    [250, 240, 230, 220, 210, 200],  # Produto C: Headphone
    [45, 50, 55, 60, 65, 70],        # Produto D: Power Bank
    [300, 310, 320, 330, 340, 350]   # Produto E: Capa
]

produtos = ["Smartphone", "Tablet", "Headphone", "Power Bank", "Capa"]
meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"]

# 1. VISUALIZAÇÃO
#    a) Mostre a matriz formatada (produtos nas linhas, meses nas colunas)

print(f'{'':^10}{'Jan': >6}{'Fev': >6}{'Mar': >6}{'Abr': >6}{'Mai': >6}{'Jun': >6}')
for i in range(len(estoque)):
    print(f'{produtos[i]: <10}', end='')
    for j in range(len(estoque[i])):
        print(f'{estoque[i][j]: >6}', end='')
    print()

## Essa visualização ficou bem melhor que o das distâncias hehe

# 2. ANÁLISE POR PRODUTO
#    b) Calcule o total vendido por produto (soma das linhas)
print()
total_por_produto = [sum(estoque[i]) for i in range(len(estoque))]
print(f'Total vendido por produto: {total_por_produto}')

#    c) Calcule a média mensal por produto
print()
media_mensal_produto = [round(total_por_produto[i]/len(estoque[i]), 2) for i in range(len(estoque))]
print(f'Media mensal por produto: {media_mensal_produto}')

#    d) Calcule a variação percentual entre o primeiro e o último mês para cada produto
#       (fórmula: ((último - primeiro) / primeiro) * 100)
print()
var_pct_produto = [round((estoque[i][len(estoque[i])-1] - estoque[i][0])/estoque[i][0] * 100, 2) for i in range(len(estoque))]
print(f'Variação percentual(%): {var_pct_produto}')

# 3. ANÁLISE POR MÊS
#    e) Calcule o total vendido por mês (soma das colunas)
print()
total_mes = []
for i in range(len(estoque[0])):
    soma_mes = 0
    for j in range(len(estoque)):
        soma_mes += estoque[j][i]
    total_mes.append(soma_mes)
print(f'Total vendido por mês: {total_mes}')

#    f) Encontre o mês com maior venda total
print()
index = float('-inf')
for mes, total in zip(meses, total_mes):
    if total > index:
        maior_mes = mes
        index = total
print(f'Mês com maior venda: {maior_mes}')

#    g) Encontre o mês com menor venda total
print()
index = float('inf')
for mes, total in zip(meses, total_mes):
    if total < index:
        menor_mes = mes
        index = total
print(f'Mês com menor venda: {menor_mes}')

# 4. ANÁLISE DE TENDÊNCIA
#    h) Para cada produto, determine se as vendas estão:
#       - "Crescente" (cada mês >= mês anterior)
#       - "Decrescente" (cada mês <= mês anterior)
#       - "Oscilante" (nenhum dos acima)
print()

tendencia = []

par_cresc = float('-inf')

for i in range(len(estoque)):
    par_cresc = float('-inf')
    cresc_count = 0
    for j in range(len(estoque[i])):
        if estoque[i][j] >= par_cresc:
            cresc_count += 1
            par_cresc = estoque[i][j]
    if cresc_count == 1:
        status = 'Decrescente'
    elif cresc_count == len(estoque[i]):
        status = 'Crescente'
    else:
        status = 'Oscilante'
    tendencia.append(status)
print(f'Tendência de vendas por produto: {tendencia}')

# Meu raciocínio aqui é a seguinte: se crescente == 1 quer dizer que ela só "cresce" 1 vez (do -inf para o primeiro mes), portanto ela é decrescente (pq ela só diminui).
# Se crescente == len(estoque[i]) quer dizer que ela cresce len(estoque[i]) vezes, ou seja, cresce em todos os meses, portanto crescente.
# Agora, se o contador está entre 1 e len(estoque[i]) quer dizer que ela cresce pelo menos 2 vezes e decresce pelo menos 1 vez. Logo oscilante.

# 5. ANÁLISE DE DESEMPENHO
#    i) Encontre o produto mais vendido no período (maior total)
print()
index = float('-inf')
for nome, total in zip(produtos, total_por_produto):
    if total > index:
        maior_total = nome
        index = total
print(f'Produto mais vendido no período: {maior_total}')

#    j) Encontre o produto com maior média mensal
print()
index = float('-inf')
for nome, media in zip(produtos, media_mensal_produto):
    if media > index:
        maior_media = nome
        index = media
print(f'Produto com maior média mensal: {maior_media}')

#    k) Encontre o produto com maior crescimento percentual
print()
index = float('-inf')
for nome, var in zip(produtos, var_pct_produto):
    if var > index:
        maior_var = nome
        index = var
print(f'Produto com maior crescimento percentual: {maior_var}')

# 6. MANIPULAÇÃO COM CÓPIA
#    l) Crie uma cópia profunda da matriz de estoque
import copy
estoque_copia = copy.deepcopy(estoque)

#    m) Na cópia, aplique um reajuste:
#       - Produtos com média > 200: redução de 10% nas vendas (redução de estoque)
#       - Produtos com média < 100: aumento de 15% nas vendas (promoção)
print()

for i in range(len(estoque_copia)):
    for j in range(len(estoque_copia[0])):
        if media_mensal_produto[i] > 200:
            estoque_copia[i][j] = round(0.9 * estoque_copia[i][j], 2)
        elif media_mensal_produto[i] < 100:
            estoque_copia[i][j] = round(1.15 * estoque_copia[i][j], 2)

#    n) Mostre a matriz original e a modificada (confirmando que a original não mudou)

for linha in estoque_copia:
    print(linha)
print()

for linha in estoque:
    print(linha)
print()

# Mestre, não vou fazer o relatório final, pq como já fui printando todos os resultados, já tá meio que estruturado na forma de relatório.

# Percebi que esse desafio tbm lembra bastante mexer com SQL, o que me foi uma boa surpresa, pq eu gosto muito de SQL hehe,
# senti até falta algumas vezes pra resolver alguns problemas de forma mais facil.




