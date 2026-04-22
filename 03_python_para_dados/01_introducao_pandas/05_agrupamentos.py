"""
Bloco 3: Python para Dados
Módulo 1: Introdução ao Pandas
Aula 5: Agrupamentos (groupby)
Data: 22/04/2026
Objetivo: Aprender a agrupar dados com groupby
"""

import pandas as pd

# Dados do exemplo

df = pd.DataFrame({
    'vendedor': ['Ana', 'Bruno', 'Ana', 'Bruno', 'Carla', 'Ana'],
    'produto': ['celular', 'fone', 'notebook', 'mouse', 'teclado', 'fone'],
    'quantidade': [10, 30, 5, 100, 50, 20],
    'preco': [1500, 200, 3500, 50, 120, 200]
})

print('Dataframe Original:')
print(df)

# ==========================================
# 1. GROUPBY BÁSICO (UMA COLUNA)
# ==========================================

print("\n" + "="*50)
print("1. GROUPBY BÁSICO")
print("="*50)

# Agrupar por vendedor e somar as quantidade
grupo_vendedor = df.groupby('vendedor')['quantidade'].sum()
print('Total vendido por vendedor:')
print(grupo_vendedor)

# o que acontece se eu fizer só df.groupby('vendedor')? No SQL a gente arruma a tabela assim, aqui n da pra printar se fizer isso

# Agrupar por produto e somar as quantidade
grupo_produto = df.groupby('produto')['quantidade'].sum()
print('Total vendidor por produto:')
print(grupo_produto)

# ==========================================
# 2. MÚLTIPLAS AGRUPAMENTOS
# ==========================================

print("\n" + "="*50)
print("2. MÚLTIPLAS COLUNAS")
print("="*50)

# Agrupar por vendedor e produto
grupo_duplo = df.groupby(['vendedor', 'produto'])['quantidade'].sum()
print('Vendas por vendedor e produto: ')
print(grupo_duplo)

# ==========================================
# 3. DIFERENTES OPERAÇÕES
# ==========================================

print("\n" + "="*50)
print("3. DIFERENTES OPERAÇÕES")
print("="*50)

# Soma
soma = df.groupby('vendedor')['quantidade'].sum()
print('Soma por vendedor:')
print(soma)

# Média
media = df.groupby('vendedor')['quantidade'].mean()
print('\nMédia por vendedor:')
print(media)

# Contagem
contagem = df.groupby('vendedor')['quantidade'].count()
print('\nContagem por vendedor:')
print(contagem)

# ==========================================
# 4. RESULTADO COMPLETO (AGGREGATE)
# ==========================================

print("\n" + "="*50)
print("4. MÚLTIPLAS OPERAÇÕES")
print("="*50)

# Aplicar várias operações de uma vez
resultado = df.groupby('vendedor')['quantidade'].agg(['sum', 'mean', 'count'])
print('Múltiplas operações por vendedor:')
print(resultado)

# ==========================================
# 5. RESUMO
# ==========================================

print("\n" + "="*50)
print("5. RESUMO")
print("="*50)

"""
✅ df.groupby('coluna')['outra_coluna'].sum() - soma por grupo
✅ df.groupby('coluna')['outra_coluna'].mean() - média por grupo
✅ df.groupby('coluna')['outra_coluna'].count() - contagem por grupo
✅ df.groupby(['col1', 'col2']) - agrupar por múltiplas colunas
✅ .agg(['sum', 'mean', 'count']) - múltiplas operações de uma vez
"""

###################################################################
# EXERCÍCIOS - AULA 5
###################################################################
#Dados para todos os exercícios:

import pandas as pd

df = pd.DataFrame({
    'vendedor': ['Ana', 'Bruno', 'Ana', 'Bruno', 'Carla', 'Ana', 'Carla', 'Bruno'],
    'produto': ['celular', 'fone', 'notebook', 'mouse', 'teclado', 'fone', 'celular', 'mouse'],
    'quantidade': [10, 30, 5, 100, 50, 20, 8, 25],
    'preco': [1500, 200, 3500, 50, 120, 200, 1500, 50]
})
###################################################################
# NÍVEL 1-3
###################################################################
"""
1. Soma por vendedor

# Agrupe por 'vendedor' e calcule a soma da coluna 'quantidade'
"""
"""
soma_quantidade_vendedor = df.groupby('vendedor')['quantidade'].sum()
print(soma_quantidade_vendedor)
"""
###################################################################
"""
2. Média por produto

# Agrupe por 'produto' e calcule a média da coluna 'preco'
"""
"""
media_preco_produto = df.groupby('produto')['preco'].mean()
print('Media do preço por produto: ')
print(media_preco_produto)
"""
###################################################################
"""
3. Contagem por vendedor

# Agrupe por 'vendedor' e conte quantas vendas cada um fez
"""
"""
cont_vendas_vendedor = df.groupby('vendedor')['quantidade'].count()
print('Quantidade de vendas por vendedor:')
print(cont_vendas_vendedor)
"""
###################################################################
# NÍVEL 4-6
###################################################################
"""
4. Múltiplas operações

# Agrupe por 'vendedor' e use .agg() para mostrar:
# - soma da quantidade
# - média da quantidade
# - contagem das vendas
"""
"""
result_vendedor = df.groupby('vendedor')['quantidade'].agg(['sum', 'mean', 'count'])
print('Resultados por vendedor:')
print(result_vendedor)
"""
###################################################################
"""
5. Agrupamento duplo

# Agrupe por ['vendedor', 'produto'] e calcule a soma da quantidade
"""
"""
count_vendas_vendedor_produto = df.groupby(['vendedor', 'produto'])['quantidade'].count()

print('Contagem das vendas por vendedor e produto:')
print(count_vendas_vendedor_produto)

# esses dados referentes à contagem da quantidade são meio sem sentido, pq da a entender que as vendas foram feitas todas de uma vez.
# Por exemplo, a linha Ana, celular, 10, dá a entender que em uma venda a Ana vendeu 10 celulares de uma vez. O que provavelmente n foi o que aconteceu.
"""
###################################################################
"""
6. Faturamento por vendedor

# Primeiro, crie uma coluna 'total' (quantidade * preco)
# Depois, agrupe por 'vendedor' e some a coluna 'total'
"""
"""
df['total'] = df['quantidade'] * df['preco']

total_vendedor = df.groupby('vendedor')['total'].sum()

print('Faturamento total por vendedor:')
print(total_vendedor)
"""
###################################################################
# NÍVEL 7-8
###################################################################
"""
7. Produto mais vendido por vendedor

# Para cada vendedor, encontre qual produto ele mais vendeu (em quantidade)
# Dica: agrupe por ['vendedor', 'produto'], some as quantidades,
#       depois use .idxmax() ou resolva manualmente
"""
"""
sqvp = df.groupby(['vendedor', 'produto'])['quantidade'].sum() # sqvp = soma_quantidade_vendedor_produto

# gerei o sqvp com o multindice vendedor-produto.

idx_max = sqvp.groupby('vendedor').idxmax() # aqui eu filtrando os indiceis que me dão os maiores valores de quantidade.sum()

produto_mais_vendido = sqvp[idx_max] # aqui eu to criando uma nova series a partir do filtro com os indices de maiores valores calculado anteriormente
print("\nProduto mais vendido por vendedor:")
print(produto_mais_vendido)

# Esse exercício precisei pesquisar como faz. Gastei um tempo nele, acho que entendi, mas é meio confuso ainda sim pra mim no momento.
"""
###################################################################
"""
8. Comparação de médias

# Calcule a média de preço por produto
# Mostre apenas os produtos cuja média de preço é maior que 500
"""
"""
media_preco_produto = df.groupby('produto')['preco'].mean()

mpp_maior = media_preco_produto[media_preco_produto>500] # tentei e deu certo. Isso funciona pq quando faço mpp>500 o Pandas trata como uma serie ne

print(mpp_maior)
"""
###################################################################
# NÍVEL 9-10
###################################################################
"""
9. Ranking de vendedores

# Calcule o faturamento total por vendedor
# Ordene do maior para o menor faturamento
# Mostre: 1º Ana: R$ X, 2º Bruno: R$ Y, 3º Carla: R$ Z
"""
"""
df['faturamento'] = df['quantidade'] * df['preco']

faturamento_vendedor = df.groupby('vendedor')['faturamento'].sum()

faturamento_vendedor_ordenado = faturamento_vendedor.sort_values(ascending=False) # .sort_values('faturamento', ascending=False) bizarro assim, n deu certo, mas sem o 'faturamento' deu certo, pq?

print(faturamento_vendedor_ordenado)

for i, (nome, faturamento) in enumerate(faturamento_vendedor_ordenado.items()): # descobri que tenho que desempacotar como tupla (nome, faturamento) muito estranho.
    print(f'{i+1}° {nome}: R${faturamento:,.2f} ')
"""
###################################################################
"""
10. DESAFIO FINAL: Relatório completo

# Usando os dados fornecidos, crie um relatório que mostre:
# 
# 1. Tabela com: vendedor, total_vendido (quantidade), faturamento_total, ticket_medio (faturamento/quantidade)
# 
# 2. Produto mais vendido (em quantidade) no geral
# 
# 3. Vendedor que mais faturou
# 
# 4. Para cada vendedor, o produto que ele mais vendeu (em quantidade)
# 
# Use APENAS groupby e operações básicas (sem loops manuais)
"""

# 1. Tabela com: vendedor, total_vendido (quantidade), faturamento_total, ticket_medio (faturamento/quantidade)

df['faturamento'] = df['quantidade'] * df['preco']

relatorio_vendedor = df.groupby('vendedor').agg(
    total_vendido=('quantidade', 'sum'),
    faturamento_total=('faturamento', 'sum')

).reset_index()

# Pesquisando descobri que o .agg é meu grande aliado na feitura dos relatórios. Posso usar aliases na forma desses parametros e usar as tuplas pra indicar qual coluna e qual operacao a ser feita na coluna.
# Também descobri o uso do .reset_index() ao final do group by para transformar o nome do vendedor em uma coluna novamente.

relatorio_vendedor['ticket_medio'] = round(relatorio_vendedor['faturamento_total'] / relatorio_vendedor['total_vendido'], 2)
# Descobri que para fazer o ticket_medio que vc pediu, como utiliza duas colunas, eu tenho que fazer dessa forma.

print(relatorio_vendedor)

# 2. Produto mais vendido (em quantidade) no geral
print()

relatorio_produto = df.groupby('produto')['quantidade'].sum()

print(f'Produto mais vendido: "{relatorio_produto.idxmax()}" {relatorio_produto.max()} vendas')

# 3. Vendedor que mais faturou

faturamento_vendedor = df.groupby('vendedor')['faturamento'].sum()

print(f'Vendedor que mais faturou: "{faturamento_vendedor.idxmax()}" R${faturamento_vendedor.max():,.2f}')

# 4. Para cada vendedor, o produto que ele mais vendeu (em quantidade)

produto_vendedor = df.groupby(['vendedor', 'produto'])['quantidade'].sum()

idx_max = produto_vendedor.groupby('vendedor').idxmax()

produto_maisvendido_vendedor = produto_vendedor[idx_max].reset_index()

print(produto_maisvendido_vendedor)