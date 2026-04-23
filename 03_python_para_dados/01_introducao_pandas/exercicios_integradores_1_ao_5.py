import pandas as pd

# Arquivo de vendas (você pode criar ou já tem)
# Vamos criar um DataFrame diretamente para não depender de arquivo externo

df_vendas = pd.DataFrame({
    'vendedor': ['Ana', 'Bruno', 'Ana', 'Bruno', 'Carla', 'Ana', 'Carla', 'Bruno'],
    'produto': ['celular', 'fone', 'notebook', 'mouse', 'teclado', 'fone', 'celular', 'mouse'],
    'quantidade': [10, 30, 5, 100, 50, 20, 8, 25],
    'preco': [1500, 200, 3500, 50, 120, 200, 1500, 50]
})

############################################################
# EXERCÍCIOS INTEGRADORES
############################################################
"""
Exercício 1: Análise inicial

# 1. Mostre as primeiras 5 linhas do DataFrame (.head())
# 2. Mostre as informações do DataFrame (.info())
# 3. Mostre as estatísticas das colunas numéricas (.describe())
"""
"""
print('Primeiras 5 linhas: ')
print(df_vendas.head())
print('\nInformações do Dataframe:')
df_vendas.info()
print('\nInformações das colunas numéricas: ')
print(df_vendas.describe())
"""
############################################################
"""
Exercício 2: Manipulação de colunas

# 1. Adicione uma coluna 'total' (quantidade * preco)
# 2. Adicione uma coluna 'categoria' com:
#    - 'Premium' se preco > 1000
#    - 'Regular' se preco <= 1000
# 3. Mostre o DataFrame com as novas colunas
"""
"""
df_vendas['total'] = df_vendas['quantidade'] * df_vendas['preco']
df_vendas['categoria'] = df_vendas['preco'].apply(lambda x: 'Premium' if x > 1000 else 'Regular')
print(df_vendas)
"""
############################################################
"""
Exercício 3: Filtros básicos

# 1. Mostre apenas as vendas do vendedor 'Ana'
# 2. Mostre apenas as vendas com quantidade > 20
# 3. Mostre apenas as vendas com total > 5000
"""
"""
df_vendas['total'] = df_vendas['quantidade'] * df_vendas['preco']

df_vendas_ana = df_vendas[df_vendas['vendedor']=='Ana']
print('Vendas da vendedora Ana: ')
print(df_vendas_ana)

df_vendas_qnt20 = df_vendas[df_vendas['quantidade']>20]
print('\nVendas com quantidade maior que 20: ')
print(df_vendas_qnt20)

df_vendas_tot5000 = df_vendas[df_vendas['total']>5000]
print('\nVendas com total maior que 5000')
print(df_vendas_tot5000)
"""
############################################################
"""
Exercício 4: Agrupamentos

# 1. Calcule o total vendido (quantidade) por vendedor
# 2. Calcule o faturamento total por vendedor
# 3. Calcule o ticket médio (faturamento / quantidade) por vendedor
#    (use .agg() para fazer tudo de uma vez)
"""
"""
df_vendas['total'] = df_vendas['quantidade'] * df_vendas['preco']

relatorio = df_vendas.groupby('vendedor').agg(
    total_vendido=('quantidade', 'sum'),
    faturamento=('total', 'sum')
).reset_index()

relatorio['ticket_medio'] = round(relatorio['faturamento'] / relatorio['total_vendido'], 2) # isso aqui era pra fazer dentro do agg? n ne?

print(relatorio)
"""
############################################################
"""
Exercício 5: DESAFIO - Relatório por produto e vendedor

# 1. Calcule o faturamento total por produto
# 2. Qual produto teve o maior faturamento?
# 3. Para cada vendedor, qual produto ele mais vendeu (em quantidade)?
#    (Dica: agrupe por ['vendedor', 'produto'], some quantidades,
#     depois encontre o produto com maior quantidade para cada vendedor)
"""
"""
df_vendas['total'] = df_vendas['quantidade'] * df_vendas['preco']

faturamento_produto = df_vendas.groupby('produto')['total'].sum()

print('Faturamento total por produto: ')
print(faturamento_produto.sort_values(ascending=False).reset_index())

print(f'\nProduto com maior faturamento: {faturamento_produto.idxmax()}')

produto_vendedor = df_vendas.groupby(['vendedor', 'produto'])['quantidade'].sum()

idx_max = produto_vendedor.groupby('vendedor').idxmax()

produto_mais_vendido_vendedor = produto_vendedor[idx_max]

print(produto_mais_vendido_vendedor)
"""
############################################################
# EXERCÍCIOS INTEGRADORES - PARTE 2
############################################################
import pandas as pd

# Dados de uma loja
df = pd.DataFrame({
    'produto': ['celular', 'fone', 'notebook', 'mouse', 'teclado', 'celular', 'fone', 'notebook', 'mouse', 'teclado'],
    'vendedor': ['Ana', 'Bruno', 'Carla', 'Ana', 'Bruno', 'Carla', 'Ana', 'Bruno', 'Carla', 'Ana'],
    'quantidade': [10, 30, 5, 100, 50, 8, 20, 3, 80, 40],
    'preco': [1500, 200, 3500, 50, 120, 1500, 200, 3500, 50, 120]
})
############################################################
"""
Exercício 1: Análise de desempenho por vendedor

# 1. Calcule o faturamento total por vendedor
# 2. Calcule a quantidade total vendida por vendedor
# 3. Calcule o ticket médio (faturamento / quantidade) por vendedor
# 4. Mostre o resultado ordenado por faturamento (do maior para o menor)
"""
"""
# 1. Calcule o faturamento total por vendedor

df['total'] = df['quantidade'] * df['preco']

faturamento_vendedor = df.groupby('vendedor')['total'].sum()

print(faturamento_vendedor.reset_index())

# 2. Calcule a quantidade total vendida por vendedor

quantidade_vendedor = df.groupby('vendedor')['quantidade'].sum()

print(quantidade_vendedor.reset_index())

# 3. Calcule o ticket médio (faturamento / quantidade) por vendedor

relatorio = df.groupby('vendedor').agg(
    faturamento=('total', 'sum'),
    qnt_vendas=('quantidade', 'sum')
).reset_index()

relatorio['ticket_medio'] = round(relatorio['faturamento']/relatorio['qnt_vendas'], 2)

# 4. Mostre o resultado ordenado por faturamento (do maior para o menor)

print(relatorio.sort_values('faturamento', ascending=False))

"""
############################################################
"""
Exercício 2: Produtos com desconto

# 1. Adicione uma coluna 'desconto' com 10% de desconto no preço
# 2. Adicione uma coluna 'total_com_desconto' (quantidade * preco_com_desconto)
# 3. Calcule o faturamento total com desconto
# 4. Calcule quanto a loja "perdeu" com o desconto (faturamento_original - faturamento_com_desconto)
"""
"""
df['preco_desconto'] = df['preco'] * 0.9
df['faturamento_com_desconto'] = df['quantidade'] * df['preco_desconto']
df['faturamento_original'] = df['quantidade'] * df['preco']

perda = df['faturamento_original'].sum() - df['faturamento_com_desconto'].sum()

print(f'A loja "perdeu" com os descontos: R${perda:,.2f}')
"""
############################################################
"""
Exercício 3: Segmentação de produtos

# 1. Adicione uma coluna 'faixa_preco' com:
#    - 'Alto' se preco >= 1000
#    - 'Médio' se 200 <= preco < 1000
#    - 'Baixo' se preco < 200
# 2. Calcule o faturamento total por faixa de preço
# 3. Calcule a quantidade total vendida por faixa de preço
"""
"""
df['faturamento'] = df['quantidade'] * df['preco']
df['faixa_preco'] = df['preco'].apply(lambda x: 'Alto' if x >= 1000 else 'Médio' if 200 <= x < 1000 else 'Baixo')

faturamento_faixa_gp = df.groupby('faixa_preco').agg(
    faturamento=('faturamento', 'sum'),
    quantidade=('quantidade', 'sum')
).reset_index()

print(faturamento_faixa_gp)
"""
############################################################
"""
Exercício 4: Ranking de produtos

# 1. Calcule o faturamento total por produto
# 2. Ordene do maior para o menor faturamento
# 3. Mostre o ranking: "1º celular: R$ 45.000"
# 4. Mostre apenas os 3 produtos com maior faturamento
"""
"""
df['faturamento'] = df['quantidade'] * df['preco']

faturamento_produto = df.groupby('produto')['faturamento'].sum().sort_values(ascending=False)

print('Ranking:')
for i, (nome, faturamento) in enumerate(faturamento_produto.items()):
    print(f'{i+1}° {nome}: R${faturamento:,.2f}')

print('\n3 produtos com maior faturamento:')
print(faturamento_produto.reset_index().head(3))
"""
############################################################
"""
Exercício 5: Comparação entre vendedores

# 1. Calcule o faturamento total por vendedor
# 2. Calcule a quantidade total vendida por vendedor
# 3. Adicione uma coluna 'meta_batida' que seja True se faturamento > 30000
# 4. Mostre: "Ana: R$ 45.000 (Meta batida: Sim)"
"""
"""
df['faturamento'] = df['quantidade'] * df['preco']

faturamento_vendedor = df.groupby('vendedor').agg(
    faturamento=('faturamento', 'sum'),
    quantidade=('quantidade', 'sum')
).reset_index()

faturamento_vendedor['meta_batida'] = faturamento_vendedor['faturamento'].apply(lambda x: 'Sim' if x >= 30000 else 'Não')

print(faturamento_vendedor)

# depois de mto quebrar a cabeça, só consegui fazer assim:
# for valores in faturamento_vendedor.values:
#     print(f'{valores[0]}: R${valores[1]:,.2f} (Meta batida: {valores[3]})')
# depois de pesquisar, descobri o .iterrows() que era o que eu tava querendo sem saber haha.
# antes disso, eu tentei com .items(), tentei com .values, tentei de um monte de jeito, nada deu certo. O iterrows caiu como uma luva.

for _, row in faturamento_vendedor.iterrows():
    print(f'{row['vendedor']}: R${row['faturamento']} (Meta batida: {row['meta_batida']})')
"""
############################################################
"""
Exercício 6: Produto favorito por vendedor

# 1. Para cada vendedor, encontre qual produto ele mais vendeu (em quantidade)
# 2. Mostre: "Ana: celular (45 unidades)"
# 3. Se houver empate, mostre "Ana: celular/fone (45 unidades)"
"""
"""
quantidade_vendedor_produto = df.groupby(['vendedor', 'produto'])['quantidade'].sum()

idx_max = quantidade_vendedor_produto.groupby('vendedor').idxmax()

produtos_favoritos = quantidade_vendedor_produto[idx_max].reset_index()

for _, row in produtos_favoritos.iterrows():
    print(f'{row['vendedor']}: {row['produto']} ({row['quantidade']} unidades)')
"""
############################################################
"""
Exercício 7: Filtros avançados

# 1. Mostre as vendas com quantidade > 30 E preco > 500
# 2. Mostre as vendas do vendedor 'Ana' OU 'Bruno'
# 3. Mostre as vendas de produtos com preco entre 100 e 1000
"""
"""
df_1 = df[(df['preco']>500) & (df['quantidade'] > 30)]

print(df_1) # vazio pq nenhuma linha atende esses requisitos

df_2 = df[(df['vendedor']=='Ana') | (df['vendedor']=='Bruno')]

print(df_2) # esse aqui não fica vazio

df_3 = df[(df['preco'] >= 100) & (df['preco'] <= 1000)]

print(df_3)
"""
############################################################
"""
Exercício 8: Média por vendedor e produto
zxzx
# 1. Calcule a média de preço por vendedor e produto
# 2. Mostre apenas as linhas onde a média de preço é maior que a média geral de preço
"""
"""
media_vendedor_produto = df.groupby(['vendedor', 'produto'])['preco'].mean().reset_index()

media_vendedor_produto_filtro = media_vendedor_produto[media_vendedor_produto['preco'] > df['preco'].mean()]

print(media_vendedor_produto_filtro)
"""
############################################################
"""
Exercício 9: Relatório completo por vendedor

# 1. Crie um DataFrame com:
#    - vendedor
#    - total_vendido (quantidade)
#    - faturamento_total
#    - ticket_medio
#    - produtos_vendidos (lista de produtos únicos que o vendedor vendeu)
# Dica: para a lista de produtos únicos, use .agg com lambda: lambda x: list(x.unique())
"""
"""
df['faturamento'] = df['quantidade'] * df['preco']

relatorio = df.groupby('vendedor').agg(
    total_vendido=('quantidade', 'sum'),
    faturamento_total=('faturamento', 'sum'),
    produtos_vendidos=('produto', lambda x: list(x.unique()))
)

relatorio['ticket_medio'] = relatorio['faturamento_total'] / relatorio['total_vendido']

print(relatorio)

# Não aparece tudo no prompt do pycharm:
#           total_vendido  ...  ticket_medio
# vendedor                 ...
# Ana                 170  ...    169.411765
# Bruno                83  ...    271.084337
# Carla                93  ...    360.215054
# tem como fazer mostrar tudo? Sobra muito espaço ainda sem utilizar...
"""
############################################################
"""
Exercício 10: DESAFIO FINAL - Identificando oportunidades

# 1. Calcule o faturamento total por produto
# 2. Calcule a quantidade total vendida por produto
# 3. Calcule o preço médio por produto
# 4. Adicione uma coluna 'potencial' que seja 'Alto' se:
#    - faturamento > 20000 OU (quantidade > 100 E preco_medio > 500)
# 5. Mostre apenas os produtos com potencial 'Alto'
"""
df['faturamento'] = df['quantidade'] * df['preco']

relatorio = df.groupby('produto').agg(
    faturamento=('faturamento', 'sum'),
    quantidade=('quantidade', 'sum')
).reset_index()

relatorio['preco_medio'] = relatorio['faturamento'] / relatorio['quantidade']

relatorio['potencial'] = relatorio.apply(
    lambda row: 'Alto' if row['faturamento'] > 20000 or (row['quantidade'] > 100 and row['preco_medio'] > 500) else '-', axis=1)

# esse aqui garrei um pouco tbm. tentei fazer o lambda com 3 variaveis, ai descobri que ele só aplica uma variavel por vez, por isso tive que usar o row.
# depois desocbri que precisa do parametro axis=1 pra função ser aplicada da forma correta.
# tbm descobri que tinha que fazer relatorio.apply direto, sem chamar nenhuma coluan especifica (eu tava tentando chamar as 3 que eu usei no lambda)

potencial_alto = relatorio[relatorio['potencial'] == 'Alto']

print(potencial_alto)
