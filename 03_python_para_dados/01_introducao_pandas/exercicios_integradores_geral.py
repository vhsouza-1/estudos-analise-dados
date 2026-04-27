#######################################################
# EXERCÍCIO 1: Análise de Vendas
#######################################################
"""
Tarefas:

Parte 1 - Limpeza
1. Verifique valores nulos em vendas
2. Remova linhas onde preco é nulo
3. Preencha quantidade nula com a mediana das quantidades
4. Remova duplicatas (se houver)

Parte 2 - Enriquecimento
5. Adicione a coluna total (quantidade * preco)
6. Junte (merge) a tabela vendas com funcionarios para adicionar departamento

Parte 3 - Análises
7. Calcule o faturamento total por produto
8. Calcule o faturamento total por vendedor
9. Calcule o faturamento total por dia (data)
10. Qual foi o dia com maior faturamento?

Parte 4 - Relatório final
11. Crie um relatório com: vendedor, departamento, total_vendido (quantidade), faturamento_total, ticket_medio
12. Ordene por faturamento_total decrescente
13. Mostre o produto mais vendido (em quantidade) no período
"""
"""
# Dados:

import pandas as pd
import numpy as np

# Arquivo de vendas (simulado)
vendas_raw = pd.DataFrame({
    'id_venda': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'produto': ['celular', 'fone', 'notebook', 'mouse', 'celular', 'fone', 'notebook', 'mouse', 'celular', 'fone'],
    'quantidade': [10, 30, 5, 100, 8, None, 3, 80, 12, 25],
    'preco': [1500, 200, 3500, 50, 1500, 200, None, 50, 1500, 200],
    'vendedor': ['Ana', 'Bruno', 'Carla', 'Ana', 'Bruno', 'Carla', 'Ana', 'Bruno', 'Carla', 'Ana'],
    'data': ['2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02', '2024-01-03',
             '2024-01-03', '2024-01-04', '2024-01-04', '2024-01-05', '2024-01-05']
})

# Tabela de funcionários (vendedores)
funcionarios = pd.DataFrame({
    'vendedor': ['Ana', 'Bruno', 'Carla', 'Daniel'],
    'departamento': ['Vendas', 'Vendas', 'Vendas', 'Marketing'],
    'data_admissao': ['2023-01-01', '2023-06-01', '2024-01-01', '2023-03-01']
})

# Remova linhas onde preco é nulo
vendas = vendas_raw.dropna(subset='preco')

# Preencha quantidade nula com a mediana das quantidades
vendas['quantidade'] = vendas['quantidade'].fillna(round(vendas['quantidade'].median())) # round pra n ficar quantidade quebrada.

# Remova duplicatas (se houver)
vendas = vendas.drop_duplicates()

# Adicione a coluna total (quantidade * preco)
vendas['total'] = vendas['quantidade'] * vendas['preco']

# Junte (merge) a tabela vendas com funcionarios para adicionar departamento
vendas = pd.merge(vendas, funcionarios, on='vendedor', how='left')
vendas = vendas[['id_venda', 'produto', 'quantidade', 'preco', 'vendedor', 'data', 'departamento', 'total']]

# Calcule o faturamento total por produto
faturamento_produto = vendas.groupby('produto')['total'].sum().reset_index()
print('Faturamento total por produto: ')
print(faturamento_produto)

# Calcule o faturamento total por vendedor
faturamento_vendedor = vendas.groupby('vendedor')['total'].sum().reset_index()
print('\nFaturamento total por vendedor:')
print(faturamento_vendedor)

# Calcule o faturamento total por dia (data)
faturamento_data = vendas.groupby('data')['total'].sum().reset_index()
print('\nFaturamento total por data: ')
print(faturamento_data)

# Qual foi o dia com maior faturamento?
print(f'\nDia com maior faturamento: \n{faturamento_data.max()}')

# Crie um relatório com: vendedor, departamento, total_vendido (quantidade), faturamento_total, ticket_medio
vendas['ticket_medio'] = vendas['total']/vendas['quantidade']
vendas = vendas.rename(columns={
    'quantidade': 'total_vendido',
    'total': 'faturamento_total'
})

relatorio = vendas[['vendedor', 'departamento', 'total_vendido', 'faturamento_total', 'ticket_medio']]

print('\nRelatório: ')
print(relatorio.to_string())
"""
#######################################################
# EXERCÍCIO 2: Análise de Clientes
#######################################################
"""
Tarefas:

Parte 1 - Limpeza
1. clientes: remova linhas onde nome é nulo
2. enderecos: preencha valores nulos com "Não informado"
3. enderecos: padronize a coluna cidade (lowercase, sem acentos - simplifique manualmente)
4. clientes e enderecos: faça um merge para adicionar endereço aos clientes (left join)

Parte 2 - Análise de clientes
5. Junte clientes e compras para saber quais clientes compraram (inner join)
6. Quais clientes NUNCA compraram? (left join com condição)
7. Calcule o valor total gasto por cliente (mostrar nome e total)
8. Qual cliente gastou mais?

Parte 3 - Análise temporal
9. Calcule o total de compras por mês (extraia o mês da data_compra)
10. Qual mês teve maior faturamento?

Parte 4 - Relatório final
11. Crie um DataFrame com: cliente, cidade, total_gasto, numero_compras
12. Mostre apenas clientes com total_gasto > 1000
13. Ordene por total_gasto decrescente
"""
"""
import pandas as pd
# Dados:

# Tabela de clientes
clientes_raw = pd.DataFrame({
    'id_cliente': [1, 2, 3, 4, 5, 6],
    'nome': ['Ana', 'Bruno', 'Carla', 'Daniel', 'Eduarda', None],
    'cidade': ['SP', 'RJ', 'BH', 'POA', 'SP', 'SP'],
    'data_cadastro': ['2023-01-01', '2023-06-01', '2024-01-01', '2023-03-01', '2023-10-01', '2024-02-01']
})

# Tabela de compras
compras_raw = pd.DataFrame({
    'id_compra': [101, 102, 103, 104, 105, 106, 107],
    'id_cliente': [1, 2, 1, 3, 4, 1, 5],
    'produto': ['celular', 'fone', 'notebook', 'mouse', 'teclado', 'fone', 'celular'],
    'valor': [1500, 200, 3500, 50, 120, 200, 1500],
    'data_compra': ['2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02',
                    '2024-01-03', '2024-01-03', '2024-01-04']
})

# Tabela de endereços (dados sujos)
enderecos_raw = pd.DataFrame({
    'cliente_id': [1, 2, 3, 5, 6],
    'rua': ['Av. Paulista', 'Rua das Flores', 'Av. Afonso Pena', 'Rua da Praia', None],
    'bairro': ['Centro', 'Jardins', 'Centro', 'Copacabana', None],
    'cidade': ['SAO PAULO', 'RIO DE JANEIRO', 'BELO HORIZONTE', 'PORTO ALEGRE', 'SAO PAULO']
})

# Parte 1 - Limpeza

# clientes: remova linhas onde nome é nulo
clientes = clientes_raw.dropna(subset='nome').reset_index(drop=True)

# enderecos: preencha valores nulos com "Não informado"
enderecos = enderecos_raw.fillna('Não informado')

# enderecos: padronize a coluna cidade (lowercase, sem acentos - simplifique manualmente)
enderecos['cidade'] = enderecos['cidade'].str.strip().str.upper()
enderecos['cidade'] = enderecos['cidade'].str.split()

for cidade in enderecos['cidade']:
    if 'DE' in cidade:
        cidade.remove('DE')

siglas = []

for cidade in enderecos['cidade']:
    a = ''
    for palavra in cidade:
        a += palavra[:1]

    if cidade == ['PORTO', 'ALEGRE']:
        a = 'POA'

    siglas.append(f'{a}')

enderecos['cidade'] = siglas

# clientes e enderecos: faça um merge para adicionar endereço aos clientes (left join)

clientes = pd.merge(clientes, enderecos, left_on='id_cliente', right_on='cliente_id', how="left")

clientes = clientes[['id_cliente', 'nome', 'cidade_x', 'rua', 'bairro', 'data_cadastro']]

clientes = clientes.fillna('Não Informado')

# Parte 2 - Análise de clientes
# Junte clientes e compras para saber quais clientes compraram (inner join)

analise_clientes = pd.merge(clientes, compras_raw, on='id_cliente', how='inner')

analise_clientes = analise_clientes.groupby('nome')['id_cliente'].count()

print(f'Quantos clientes já compraram: {analise_clientes.count()}')

# Quais clientes NUNCA compraram? (left join com condição)

clientes_compras = clientes.merge(compras_raw, on='id_cliente', how='left', indicator=True)

clientes_sem_compra = clientes_compras[clientes_compras['_merge']=='left_only']

print('\nClientes que nunca compraram: ')
print(clientes_sem_compra)

# Calcule o valor total gasto por cliente (mostrar nome e total)

cliente_total = clientes_compras.groupby('nome')['valor'].sum().reset_index()

print('Total gasto por cliente: ')
print(cliente_total)

# Qual cliente gastou mais?

cliente_total = cliente_total.sort_values('valor', ascending=False)

print('\nCliente que gastou mais: ')
print(cliente_total.iloc[0])

# Parte 3 - Análise temporal
# Calcule o total de compras por mês (extraia o mês da data_compra)


compras_raw['mes'] = compras_raw['data_compra'].str[:7]

total_mes = compras_raw.groupby('mes')['valor'].sum().reset_index()

print('\nTotal de compras por mês:')
print(total_mes)

print('\nMês com maior faturamento: ')
total_mes = total_mes.sort_values('valor', ascending=False)
print(total_mes.iloc[0])

# Parte 4 - Relatório final
# Crie um DataFrame com: cliente, cidade, total_gasto, numero_compras

relatorio = clientes_compras[['nome', 'cidade_x', 'produto', 'valor']]

relatorio = relatorio.groupby(['nome', 'cidade_x']).agg(
    total_gasto=('valor', 'sum'),
    numero_compras=('nome', 'count')
).reset_index()

relatorio = relatorio.rename(columns={
    'nome': 'cliente',
    'cidade_x': 'cidade'
})

print('\nRelatorio completo: ')
print(relatorio)

print('\nClientes com total_gasto > 1000:')
print(relatorio[relatorio['total_gasto']>1000])

relatorio = relatorio.sort_values('total_gasto', ascending=False).reset_index(drop=True)
print('\nRelatório ordenado por total_gasto decrescente')
print(relatorio)
"""
#######################################################
# EXERCÍCIO 3: DESAFIO FINAL - Dashboard de RH
#######################################################
"""
Tarefas:

Parte 1 - Limpeza
1. Converta salario para float (remover ponto, substituir vírgula por ponto)
2. Converta gestor para booleano (Sim=True, Não=False)
3. Benefícios: preencha plano_saude nulo com "Não"
4. Benefícios: preencha vale_refeicao nulo com a média
5. Junte (merge) as três tabelas (funcionarios, avaliacoes, beneficios) em um único DataFrame

Parte 2 - Indicadores
6. Calcule a média salarial por departamento
7. Calcule a média das notas de avaliação por departamento
8. Qual departamento tem a maior média salarial?
9. Qual funcionário tem a maior média de notas (considerando todas as avaliações)?
10. Calcule o total gasto com vale_refeicao por mês (suponha 20 dias úteis: total = valor * 20)

Parte 3 - Análises cruzadas
11. Relação entre ser gestor e salário médio (gestores vs não gestores)
12. Funcionários que ganham acima da média do departamento
13. Funcionários com nota média abaixo de 7 (em algum ano)

Parte 4 - Relatório executivo
14. Crie um relatório final com: nome, departamento, salario, nota_media, plano_saude, gestor
15. Mostre apenas os 3 funcionários com maior salário
16. Mostre quantos funcionários por departamento (contagem)
"""
import pandas as pd
# Dados:

# Funcionários (dados sujos)
funcionarios = pd.DataFrame({
    'id_func': [1, 2, 3, 4, 5, 6, 7, 8],
    'nome': ['Ana', 'Bruno', 'Carla', 'Daniel', 'Eduarda', 'Felipe', 'Gabriela', 'Henrique'],
    'departamento': ['Vendas', 'TI', 'Vendas', 'RH', 'TI', 'Vendas', 'RH', 'TI'],
    'salario': ['5.000,00', '6.200,00', '4.800,00', '3.800,00', '5.800,00', '4.700,00', '4.200,00', '6.500,00'],
    'data_admissao': ['2023-01-01', '2023-06-01', '2024-01-01', '2023-03-01',
                      '2023-10-01', '2024-02-01', '2023-11-01', '2023-07-01'],
    'gestor': ['Sim', 'Não', 'Não', 'Sim', 'Não', 'Não', 'Não', 'Sim']
})

# Avaliações de desempenho
avaliacoes = pd.DataFrame({
    'id_func': [1, 1, 2, 2, 3, 4, 5, 6, 7, 8],
    'ano': [2023, 2024, 2023, 2024, 2024, 2023, 2024, 2024, 2023, 2024],
    'nota': [8.5, 9.0, 7.0, 7.5, 8.0, 6.5, 9.0, 7.0, 7.5, 8.5]
})

# Benefícios (dados com nulos)
beneficios = pd.DataFrame({
    'id_func': [1, 2, 3, 4, 5, 6, 7, 8],
    'plano_saude': ['Sim', 'Sim', None, 'Sim', 'Não', 'Sim', None, 'Sim'],
    'vale_refeicao': [30, 25, 25, 20, None, 30, 20, 35],
    'vale_transporte': ['Sim', 'Sim', 'Não', 'Sim', 'Sim', 'Não', 'Sim', 'Sim']
})

# Parte 1 - Limpeza
# 1. Converta salario para float (remover ponto, substituir vírgula por ponto)
funcionarios_limpo = funcionarios.copy()
funcionarios_limpo['salario'] = funcionarios_limpo['salario'].str.replace('.','').str.replace(',','.').astype(float)

# 2. Converta gestor para booleano (Sim=True, Não=False)
funcionarios_limpo['gestor'] = funcionarios_limpo['gestor'].str.replace('Não', '').astype(bool)

# 3. Benefícios: preencha plano_saude nulo com "Não"
beneficios_limpo = beneficios.copy()
beneficios_limpo['plano_saude'] = beneficios_limpo['plano_saude'].fillna('Não')

# 4. Benefícios: preencha vale_refeicao nulo com a média
media_vale_refeicao = round(beneficios_limpo['vale_refeicao'].mean(), 2)
beneficios_limpo['vale_refeicao'] = beneficios_limpo['vale_refeicao'].fillna(media_vale_refeicao)

# 5. Junte (merge) as três tabelas (funcionarios, avaliacoes, beneficios) em um único DataFrame
df_parc = pd.merge(funcionarios_limpo, avaliacoes, on='id_func', how='outer')
df_completo = pd.merge(df_parc, beneficios_limpo, on='id_func', how='outer')

# Parte 2 - Indicadores
# 6. Calcule a média salarial por departamento
med_sal_dept = df_completo.groupby('departamento')['salario'].mean()
print('Média salarial por departamento:')
print(med_sal_dept)

# 7. Calcule a média das notas de avaliação por departamento
med_nota_dept = df_completo.groupby('departamento')['nota'].mean()
print('\nMédia nota por departamento:')
print(med_nota_dept)

# 8. Qual departamento tem a maior média salarial?
print(f'\nDepartamento com a maior média salarial: {med_sal_dept.idxmax()} (R${med_sal_dept.max()})')

# 9. Qual funcionário tem a maior média de notas (considerando todas as avaliações)?
med_nota_nome = df_completo.groupby('nome')['nota'].mean()
print(f'\nFuncionário com a maior média de notas: {med_nota_nome.idxmax()} ({med_nota_nome.max()})')

# 10. Calcule o total gasto com vale_refeicao por mês (suponha 20 dias úteis: total = valor * 20)

vale_ref_nome = df_completo[['nome', 'vale_refeicao']].groupby('nome')['vale_refeicao'].mean().reset_index()
vale_ref_nome['vr_mensal'] = vale_ref_nome['vale_refeicao'] * 20
print(f'\nTotal gasto com vale refeição por mês: R${vale_ref_nome['vr_mensal'].sum()}')

# Parte 3 - Análises cruzadas
# 11. Relação entre ser gestor e salário médio (gestores vs não gestores)

nome_gestor_salario = df_completo.groupby('nome').agg(
    salario=('salario', 'mean'),
    gestor=('gestor', 'max')
)

salario_gestor = nome_gestor_salario.groupby('gestor')['salario'].mean()

print('\nRelação entre gestor e salário médio: ')
print(salario_gestor)

# 12. Funcionários que ganham acima da média do departamento
nome_sal_dept = df_completo[['nome', 'salario', 'departamento']].drop_duplicates().reset_index(drop=True)

med_sal_dept = nome_sal_dept.groupby('departamento')['salario'].mean().reset_index()

nome_sal_dept_meddept = pd.merge(nome_sal_dept, med_sal_dept, on='departamento', how='outer')

nome_sal_dept_meddept = nome_sal_dept_meddept.rename(columns={
    'salario_x': 'salario',
    'salario_y': 'med_sal_dept'
})

print('\nFuncionários que ganham acima da média do departamento: ')
print(nome_sal_dept_meddept[nome_sal_dept_meddept['salario'] > nome_sal_dept_meddept['med_sal_dept']].reset_index(drop=True))

# 13. Funcionários com nota média abaixo de 7 (em algum ano)'
print('\nFuncionários com nota média abaixo de 7 (em algum ano)')
print(df_completo[['nome', 'nota', 'ano']][df_completo['nota'] < 7].reset_index(drop=True))

# Parte 4 - Relatório executivo
# 14. Crie um relatório final com: nome, departamento, salario, nota_media, plano_saude, gestor
relatorio = df_completo.groupby('nome').agg(
    nome=('nome', 'max'),
    departamento=('departamento', 'max'),
    salario=('salario', 'max'),
    nota_media=('nota', 'mean'),
    plano_saude=('plano_saude', 'max'),
    gestor=('gestor', 'max')
).reset_index(drop=True)

print('\nRelatório final: ')
print(relatorio)

# 15. Mostre apenas os 3 funcionários com maior salário
relatorio_ord = relatorio.sort_values('salario', ascending=False).reset_index(drop=True)
print('\n3 funcionários com maior salário: ')
print(relatorio_ord.head(3))

# 16. Mostre quantos funcionários por departamento (contagem)
nome_dept_cont = relatorio.groupby('departamento').agg(
    departamento=('departamento', 'max'),
    qnt_func=('nome', 'count')
).reset_index(drop=True)

print('\nQuantidade de funcionários por departamento: ')
print(nome_dept_cont)

