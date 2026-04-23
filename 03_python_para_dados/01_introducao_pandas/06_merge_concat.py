"""
Bloco 3: Python para Dados
Módulo 1: Introdução ao Pandas
Aula 6: Merge e Concatenação
Data: 23/04/2026
Objetivo: Aprender a combinar DataFrames
"""
from json.decoder import NaN

import pandas as pd

# ==========================================
# 1. CONCAT - EMPILHAR DATAFRAMES
# ==========================================

print("="*50)
print("1. CONCAT - EMPILHAR DATAFRAMES")
print("="*50)

# Dois DataFrames com as mesmas colunas
df1 = pd.DataFrame({
    'nome': ['Ana', 'Bruno'],
    'idade': [25, 30],
    'cidade': ['SP', 'RJ']
})

df2 = pd.DataFrame({
    'nome': ['Carla', 'Daniel'],
    'idade': [22, 28],
    'cidade': ['BH', 'POA']
})

print("DataFrame 1:")
print(df1)
print("\nDataFrame 2:")
print(df2)

# Empilhando (concatenando)
print('\n Concat (empilhar):')
df_concat = pd.concat([df1, df2])
print(df_concat)

# ==========================================
# 2. CONCAT COM IGNORE_INDEX
# ==========================================

print("\n" + "="*50)
print("2. CONCAT COM ignore_index")
print("="*50)

# Por padrão, o índice original é mantido
print("Com índice original:")
print(pd.concat([df1, df2]))

# Com ignore_index=True, reinicia o índice
print("\nCom ignore_index=True (índice reiniciado):")
print(pd.concat([df1, df2], ignore_index=True))

# ==========================================
# 3. MERGE - JUNTANDO DATAFRAMES (JOIN)
# ==========================================

print("\n" + "="*50)
print("3. MERGE - JUNTANDO DATAFRAMES")
print("="*50)

# Tabela de alunos
alunos = pd.DataFrame({
    'id_aluno': [1, 2, 3],
    'nome': ['Ana', 'Bruno', 'Carla'],
    'cidade': ['SP', 'RJ', 'BH']
})

# Tabela de notas
notas = pd.DataFrame({
    'id_aluno': [1, 2, 4],
    'nota': [8.5, 7.0, 9.0],
    'disciplina': ['Matemática', 'Matemática', 'Matemática']
})

print("Tabela de alunos:")
print(alunos)
print("\nTabela de notas:")
print(notas)

# ==========================================
# 4. INNER MERGE (SÓ O QUE ESTÁ NAS DUAS)
# ==========================================

print("\n" + "="*50)
print("4. INNER MERGE")
print("="*50)

# Equivalente ao INNER JOIN do SQL
# Só aparecem alunos que têm nota (id presente nas duas tabelas)

df_inner = pd.merge(alunos, notas, on='id_aluno', how='inner')
print('INNER JOIN (só quem tem nota): ')
print(df_inner)

# ==========================================
# 5. LEFT MERGE (TUDO DA ESQUERDA)
# ==========================================

print("\n" + "="*50)
print("5. LEFT MERGE")
print("="*50)

# Equivalente ao LEFT JOIN do SQL
# Todos os alunos aparecem (quem não tem nota fica NaN)

df_left = pd.merge(alunos, notas, on='id_aluno', how='left')
print('LEFT JOIN (todos os alunos):')
print(df_left)

# ==========================================
# 6. RIGHT MERGE (TUDO DA DIREITA)
# ==========================================

print("\n" + "="*50)
print("6. RIGHT MERGE")
print("="*50)

# Equivalente ao RIGHT JOIN do SQL
# Todas as notas aparecem (aluno 4 não tem nome, fica NaN)

df_right = pd.merge(alunos, notas, on='id_aluno', how='right')
print("RIGHT JOIN (todas as notas):")
print(df_right)

# ==========================================
# 7. OUTER MERGE (TUDO DE AMBAS)
# ==========================================

print("\n" + "="*50)
print("7. OUTER MERGE")
print("="*50)

# Equivalente ao FULL OUTER JOIN do SQL
# Todos os alunos e todas as notas
df_outer = pd.merge(alunos, notas, on='id_aluno', how='outer')
print("OUTER JOIN (todos os alunos e todas as notas):")
print(df_outer)

# ==========================================
# 8. MERGE COM CHAVES DIFERENTES
# ==========================================

print("\n" + "="*50)
print("8. MERGE COM CHAVES DIFERENTES")
print("="*50)

# Quando as colunas de junção têm nomes diferentes
vendas = pd.DataFrame({
    'produto_id': [1, 2, 3],
    'quantidade': [10, 20, 30]
})

produtos = pd.DataFrame({
    'id': [1, 2, 4],
    'nome': ['celular', 'fone', 'notebook'],
    'preco': [1500, 200, 3500]
})

print("Vendas (produto_id):")
print(vendas)
print("\nProdutos (id):")
print(produtos)

# left_on e right_on especificam as colunas de junção
df_merge = pd.merge(vendas, produtos, left_on='produto_id', right_on='id', how='left')
print("\nMerge com chaves diferentes:")
print(df_merge)

# ==========================================
# 9. RESUMO DOS TIPOS DE MERGE
# ==========================================

print("\n" + "="*50)
print("9. RESUMO DOS TIPOS DE MERGE")
print("="*50)

"""
| how       | Equivalente SQL        | O que faz                                      |
|-----------|------------------------|------------------------------------------------|
| 'inner'   | INNER JOIN             | Só registros que existem nas duas tabelas     |
| 'left'    | LEFT JOIN              | Todos da esquerda + correspondentes da direita |
| 'right'   | RIGHT JOIN             | Todos da direita + correspondentes da esquerda |
| 'outer'   | FULL OUTER JOIN        | Todos os registros das duas tabelas            |
"""

# ==========================================
# 10. RESUMO GERAL
# ==========================================

print("\n" + "="*50)
print("10. RESUMO")
print("="*50)

"""
✅ concat(): empilhar DataFrames (um em cima do outro)
   - pd.concat([df1, df2])
   - ignore_index=True para reiniciar o índice

✅ merge(): juntar DataFrames por colunas (JOIN)
   - pd.merge(df1, df2, on='coluna')
   - pd.merge(df1, df2, left_on='col1', right_on='col2')
   - how='inner' (padrão), 'left', 'right', 'outer'

📌 Comparação com SQL:
- INNER JOIN → how='inner'
- LEFT JOIN  → how='left'
- RIGHT JOIN → how='right'
- FULL OUTER JOIN → how='outer'
- UNION      → pd.concat()
"""
################################################################
# EXERCÍCIOS - AULA 6
################################################################
#Dados para os exercícios:
import pandas as pd

# Tabela de clientes
clientes = pd.DataFrame({
    'id_cliente': [1, 2, 3, 4, 5],
    'nome': ['Ana', 'Bruno', 'Carla', 'Daniel', 'Eduarda'],
    'cidade': ['SP', 'RJ', 'BH', 'POA', 'SP']
})

# Tabela de compras
compras = pd.DataFrame({
    'id_compra': [101, 102, 103, 104, 105],
    'id_cliente': [1, 2, 1, 4, 6],
    'produto': ['celular', 'fone', 'notebook', 'mouse', 'teclado'],
    'valor': [1500, 200, 3500, 50, 120]
})

# Tabela de endereços (para exercício de merge com chaves diferentes)
enderecos = pd.DataFrame({
    'cliente_id': [1, 2, 3, 4],
    'rua': ['Av. Paulista', 'Rua das Flores', 'Av. Afonso Pena', 'Rua da Praia'],
    'bairro': ['Centro', 'Jardins', 'Centro', 'Copacabana']
})
################################################################
# NÍVEL 1-3: Aquecimento
################################################################
"""
1. Concat simples

# Crie dois DataFrames pequenos com as mesmas colunas
# Use pd.concat() para empilhá-los
# Mostre o resultado
"""
"""
df_estoque1 = pd.DataFrame({
    'id_produto': [1, 2, 3],
    'produto': ['XRE', 'Intruder', 'Fazer']
})

df_estoque2 = pd.DataFrame({
    'id_produto': [4, 5, 6],
    'produto': ['Hornet', 'Bis', 'PCX']
})

print(df_estoque1)
print(df_estoque2)

df_estoque = pd.concat([df_estoque1, df_estoque2])

print(df_estoque)
"""
################################################################
"""
2. Concat com ignore_index

# Use os DataFrames do exercício 1
# Use pd.concat() com ignore_index=True
# Compare com o resultado do exercício 1
"""
"""
df_estoque1 = pd.DataFrame({
    'id_produto': [1, 2, 3],
    'produto': ['XRE', 'Intruder', 'Fazer']
})

df_estoque2 = pd.DataFrame({
    'id_produto': [4, 5, 6],
    'produto': ['Hornet', 'Bis', 'PCX']
})

df_estoque = pd.concat([df_estoque1, df_estoque2], ignore_index=True)

print(df_estoque)
"""
################################################################
"""
3. Inner merge

# Use as tabelas clientes e compras
# Faça um inner merge por id_cliente
# Mostre o resultado (clientes que compraram)
"""
"""
print(clientes)
print(compras)

tabela = pd.merge(clientes, compras, on='id_cliente', how='inner')

print(tabela)

"""
################################################################
# NÍVEL 4-6: Aplicação
################################################################
"""
4. Left merge

# Use as tabelas clientes e compras
# Faça um left merge por id_cliente
# Mostre todos os clientes (quem não comprou fica NaN)
"""
"""
left_merge = pd.merge(clientes, compras, on='id_cliente', how='left')

print(left_merge)
"""
################################################################
"""
5. Right merge

# Use as tabelas clientes e compras
# Faça um right merge por id_cliente
# Mostre todas as compras (cliente 6 não tem nome)
"""
"""
right_merge = pd.merge(clientes, compras, on='id_cliente', how='right')

print(right_merge)
"""
################################################################
"""
6. Outer merge

# Use as tabelas clientes e compras
# Faça um outer merge por id_cliente
# Mostre todos os clientes e todas as compras
"""
"""
outer_merge = pd.merge(clientes, compras, on='id_cliente', how='outer')

print(outer_merge)
"""
################################################################
# NÍVEL 7-8: Manipulação
################################################################
"""
7. Merge com chaves diferentes

# Use as tabelas clientes e enderecos
# Faça um left merge onde:
#   - clientes tem 'id_cliente'
#   - enderecos tem 'cliente_id'
# Mostre todos os clientes com seus endereços (se existirem)
"""
"""
chaves_diferentes = pd.merge(clientes, enderecos, left_on='id_cliente', right_on='cliente_id', how='left')

print(chaves_diferentes)
"""
################################################################
"""
8. Merge com múltiplas colunas

# Crie duas tabelas com duas colunas de chave
# Exemplo: ano e mês
# Faça um merge usando as duas colunas
"""
"""
vendas = pd.DataFrame({
    'ano': [2024, 2024, 2024, 2025, 2025],
    'mes': [1, 2, 3, 1, 2],
    'valor': [100, 150, 200, 300, 250]
})

metas = pd.DataFrame({
    'ano': [2024, 2024, 2024, 2025, 2025],
    'mes': [1, 2, 3, 1, 2],
    'meta': [120, 160, 180, 280, 260]
})

duas_colunas = pd.merge(vendas, metas, on=['ano', 'mes'])

print(duas_colunas)
"""
################################################################
# NÍVEL 9-10: Desafios
################################################################
"""
9. Relatório completo com múltiplos merges

# Use as três tabelas: clientes, compras, enderecos
# Crie um relatório que mostre:
# - nome do cliente
# - cidade
# - rua e bairro (se existir)
# - produto comprado (se existir)
# - valor da compra (se existir)
# 
# Dica: faça um merge primeiro, depois outro
"""
"""
print(clientes)
print(compras)
print(enderecos)

merge1 = pd.merge(clientes, enderecos, left_on='id_cliente', right_on='cliente_id', how='left')

merge2 = pd.merge(merge1, compras, on='id_cliente', how='left')

print(merge2.to_string())

relatorio = merge2.drop(columns=['id_cliente', 'cliente_id', 'id_compra']) # Fui pesquisar e descobri. COmo você esperaava que eu fizesse? Com iterrows?

print(relatorio)
"""
################################################################
"""
10. DESAFIO FINAL: Análise de clientes

# Use as tabelas clientes, compras e enderecos
# 
# Responda:
# 1. Quantos clientes fizeram compras?
# 2. Qual o valor total gasto por cliente? (mostrar nome e total)
# 3. Quais clientes não têm endereço cadastrado?
# 4. Qual o produto mais caro comprado por cliente de SP?
# 
# Mostre os resultados de forma clara
"""
compras_clientes_inner = pd.merge(compras, clientes, on='id_cliente', how='inner')

nome_agrupado = compras_clientes_inner.groupby('nome')['nome'].count()

qnt_clientes_compras = nome_agrupado.count()

print(f'Quantos clientes fizeram compras? {qnt_clientes_compras}')

total_cliente = compras_clientes_inner.groupby('nome')['valor'].sum().reset_index()

print('\nQual valor total gasto por cliente: ')
for _, row in total_cliente.iterrows():
    print(f'{row['nome']}: R${row['valor']:,.2f}')

cliente_enderecos = pd.merge(clientes, enderecos, left_on='id_cliente', right_on='cliente_id', how='left')
print(cliente_enderecos)

print('\nClientes que não tem o endereço cadastrado: ')
for _, row in cliente_enderecos.iterrows():
    if row['id_cliente'] != row['cliente_id']:
        print(f' - {row['nome']}')

compras_clientes_left = pd.merge(compras, clientes, on='id_cliente', how='left')

compras_clientes_left_sp = compras_clientes_left[compras_clientes_left['cidade'] == 'SP']

compras_clientes_left_sp = compras_clientes_left_sp.sort_values('valor', ascending=False)

compras_clientes_left_sp_1 = compras_clientes_left_sp.iloc[0]

print(f'Qual o produto mais caro comprado por cliente de SP? {compras_clientes_left_sp_1['produto']}')