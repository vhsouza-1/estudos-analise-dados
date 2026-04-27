"""
Bloco 3: Python para Dados
Módulo 1: Introdução ao Pandas
Aula 10: Leitura, Escrita e Pipeline
Data: 27/04/2026
Objetivo: Aprender a ler, processar e salvar arquivos com Pandas + Pathlib
"""

import pandas as pd
from pathlib import Path

# ==========================================
# 1. REVISÃO RÁPIDA: LENDO CSV
# ==========================================

print("="*50)
print("1. LENDO CSV (revisão)")
print("="*50)

# Vamos criar um arquivo CSV de exemplo
with open('exemplo.csv', 'w', newline='') as f:
    f.write('nome,idade,cidade\n')
    f.write('Ana,25,SP\n')
    f.write('Bruno,30,RJ\n')
    f.write('Carla,22,BH\n')

# Lendo com Pandas
df = pd.read_csv('exemplo.csv')
print('Arquivo lido:')
print(df)

# ==========================================
# 2. ESCREVENDO CSV (.to_csv())
# ==========================================

print("\n" + "="*50)
print("2. ESCREVENDO CSV (.to_csv())")
print("="*50)

# Salvar DataFrame em um novo arquivo CSV
df.to_csv('saida.csv', index=False)
print('Arquivo saida.csv criado!')

# Verificando o conteúdo do arquivo criado
print("\nConteúdo do arquivo 'saida.csv':")
with open('saida.csv', 'r') as f:
    print(f.read())

# ==========================================
# 3. PARÂMETROS IMPORTANTES DO .to_csv()
# ==========================================

print("\n" + "="*50)
print("3. PARÂMETROS DO .to_csv()")
print("="*50)

# 3.1 index=False (NÃO salvar o indice como coluna)
print('index=False (padrão é True)')
df.to_csv('sem_indice.csv', index=True)
print("Arquivo 'sem_indice.csv' criado (sem coluna de índice)")

# 3.2. sep (separador diferente de vírgula)
print("\n--- sep=';' (separador ponto e vírgula) ---")
df.to_csv('separador_ponto_virgula.csv', sep=';', index=False)
print("Arquivo 'separador_ponto_virgula.csv' criado")

# 3.3. encoding (para acentos)
print("\n--- encoding='utf-8' ---")
df_com_acento = pd.DataFrame({'nome': ['João', 'Maria'], 'cidade': ['São Paulo', 'Rio de Janeiro']})
df_com_acento.to_csv('com_acento.csv', encoding='utf-8', index=False)
print("Arquivo 'com_acento.csv' criado")

# 3.4. header=False (não escrever cabeçalho)
print("\n--- header=False (sem cabeçalho) ---")
df.to_csv('sem_cabecalho.csv', header=False, index=False)
print("Arquivo 'sem_cabecalho.csv' criado")

# ==========================================
# 4. LENDO E ESCREVENDO EM PASTAS COM PATHLIB
# ==========================================

print("\n" + "="*50)
print("4. LENDO E ESCREVENDO EM PASTAS")
print("="*50)

Path('dados/raw').mkdir(parents=True, exist_ok=True)
Path('dados/processed').mkdir(parents=True, exist_ok=True)

# Salvar um arquivo de exemplo na pasta raw

df_exemplo = pd.DataFrame({
    'produto': ['celular', 'fone', 'notebook'],
    'preco': [1500, 200, 3500]
})

df_exemplo.to_csv('dados/raw/produtos.csv', index=False)
print('Arquivo criado em "dados/raw/produtos.csv"')

# Ler na pasta raw
caminho_origem = Path('dados/raw/produtos.csv')
df_lido = pd.read_csv(caminho_origem)
print('\nArquivo lido da pasta raw:')
print(df_lido)

# Processar (adicionar coluna de desconto)
df_lido['preco_com_desconto'] = df_lido['preco'] * 0.9

# Salvar na pasta processed
caminho_destino = Path('dados/processed/produtos_com_desconto.csv')
df_lido.to_csv(caminho_destino, index=False)
print(f'\nArquivo salvo em {caminho_destino}')

# ==========================================
# 5. PIPELINE: PROCESSANDO MÚLTIPLOS ARQUIVOS
# ==========================================

print("\n" + "="*50)
print("5. PIPELINE - PROCESSANDO MÚLTIPLOS ARQUIVOS")
print("="*50)

dados_vendas = [
    ('vendas_jan.csv', [['celular', 10, 1500], ['fone', 30, 200]]),
    ('vendas_fev.csv', [['celular', 8, 1500], ['notebook', 3, 3500]]),
    ('vendas_mar.csv', [['fone', 20, 200], ['mouse', 100, 50]])
]

for nome, dados in dados_vendas:
    df = pd.DataFrame(dados, columns=['produto', 'quantidade', 'preco'])
    df.to_csv(Path('dados/raw') / nome, index=False)

print("Arquivos criados em 'dados/raw/':")
for arquivo in Path('dados/raw').glob('*.csv'):
    print(f"  - {arquivo.name}")

# Processar cada arquivo
print('\nProcessando cada arquivo:')
for arquivo in Path('dados/raw').glob('vendas*.csv'): # fiz com vendas* pra n pegar o produtos.csv do exemplo passado.

    # Ler
    df = pd.read_csv(arquivo)
    print(f'Arquivo original:\n{df}\n')

    # Processar (adicionar coluna total)
    df['total'] = df['quantidade'] * df['preco']
    print(f'Arquivo processado:\n{df}\n')

    # Salvar na pasta processed com mesmo nome
    caminho_saida = Path('dados/processed') / f'{arquivo.stem}_processed.csv'
    df.to_csv(caminho_saida, index=False)
    print(f'  Salvo em: {caminho_saida}')

# ==========================================
# 6. RELATÓRIO DO PIPELINE
# ==========================================

print("\n" + "="*50)
print("6. RELATÓRIO DO PIPELINE")
print("="*50)

# Listar arquivos processados
arquivos_origem = list(Path('dados/raw').glob('vendas*.csv'))
arquivos_destino = list(Path('dados/processed').glob('vendas*.csv'))

print('Resumo do pipeline')
print(f'  Arquivos lidos: {len(arquivos_origem)}')
print(f'  Arquivos salvos: {len(arquivos_destino)}')

# Mostrar os primeiros registros de cada arquivo processado
print('\nPrimeiras linhas dos arquivos processados: ')
for arquivo in Path('dados/processed').glob('vendas*.csv'):
    df = pd.read_csv(arquivo)
    print(f'\n{arquivo.name}:')
    print(df.head())

# ==========================================
# 7. EXEMPLO PRÁTICO: PROCESSANDO VENDAS
# ==========================================

print("\n" + "="*50)
print("7. EXEMPLO PRÁTICO - PROCESSANDO VENDAS")
print("="*50)

pastas = [
    'vendas/raw',
    'vendas/processed',
    'vendas/output'
]

for pasta in pastas:
    Path(pasta).mkdir(parents=True, exist_ok=True)

# Criar arquivos de vendas por dia
vendas_dias = {
    '2024-01-01.csv': [['celular', 10, 1500, 'Ana'], ['fone', 30, 200, 'Bruno']],
    '2024-01-02.csv': [['celular', 5, 1500, 'Ana'], ['notebook', 3, 3500, 'Carla']],
    '2024-01-03.csv': [['fone', 15, 200, 'Bruno'], ['mouse', 100, 50, 'Ana']]
}

for nome, dados in vendas_dias.items():
    df = pd.DataFrame(dados, columns=['produto', 'quantidade', 'preco', 'vendedor'])
    df.to_csv(Path('vendas/raw') / nome, index=False)

print("Arquivos criados em 'vendas/raw/'")

# Processar cada arquivo
for arquivo in Path('vendas/raw').glob('*.csv'):

    # 1. Ler
    df = pd.read_csv(arquivo)
    print(f'arquivo lido "{arquivo.name}":\n{df}\n')

    # 2. Calcular total
    df['total'] = df['quantidade'] * df['preco']

    # 3. Salvar versão processada
    df.to_csv(Path('vendas/processed') / f'{arquivo.stem}_processed{arquivo.suffix}', index=False)
    print(f'  Salvo em: {arquivo.parent}\\{arquivo.name}')

    # 4. Gerar resumo do dia
    resumo = pd.DataFrame({
        'total_vendas': [df['total'].sum()],
        'total_itens': [df['quantidade'].sum()],
        'num_vendedores': [df['vendedor'].nunique()]
    })
    resumo.to_csv(Path('vendas/output') / f'resumo_{arquivo.name}', index=False)
    print(f'  Resumo salvo em: vendas/output/resumo_{arquivo.name}\n')

# ==========================================
# 8. RESUMO
# ==========================================

print("\n" + "="*50)
print("8. RESUMO")
print("="*50)

"""
✅ LER CSV: pd.read_csv('caminho.csv')

✅ ESCREVER CSV:
   - df.to_csv('caminho.csv', index=False)  # sem índice
   - df.to_csv('caminho.csv', sep=';')      # separador ponto e vírgula
   - df.to_csv('caminho.csv', encoding='utf-8')  # para acentos
   - df.to_csv('caminho.csv', header=False)      # sem cabeçalho

✅ INTEGRAÇÃO COM PATHLIB:
   from pathlib import Path
   df = pd.read_csv(Path('pasta') / 'arquivo.csv')
   df.to_csv(Path('pasta') / 'saida.csv', index=False)

✅ PIPELINE (múltiplos arquivos):
   for arquivo in Path('pasta_raw').glob('*.csv'):
       df = pd.read_csv(arquivo)
       # processar...
       df.to_csv(Path('pasta_processed') / arquivo.name, index=False)
"""
################################################################
# EXERCÍCIOS - AULA 10
################################################################
# Dados iniciais

import pandas as pd
from pathlib import Path

# Criar estrutura de pastas
Path('exercicio/raw').mkdir(parents=True, exist_ok=True)
Path('exercicio/processed').mkdir(parents=True, exist_ok=True)

# Criar arquivos de exemplo
df_clientes = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'nome': ['Ana', 'Bruno', 'Carla', 'Daniel'],
    'cidade': ['SP', 'RJ', 'BH', 'POA']
})
df_clientes.to_csv('exercicio/raw/clientes.csv', index=False)

df_produtos = pd.DataFrame({
    'id': [1, 2, 3],
    'produto': ['celular', 'fone', 'notebook'],
    'preco': [1500, 200, 3500]
})
df_produtos.to_csv('exercicio/raw/produtos.csv', index=False)

################################################################
# NÍVEL 1-3: Aquecimento
################################################################
"""
1. Lendo e escrevendo um CSV

# Leia o arquivo 'exercicio_raw/clientes.csv'
# Adicione uma coluna 'idade' com valores [25, 30, 22, 28]
# Salve o resultado em 'exercicio_processed/clientes_com_idade.csv' (sem índice)
"""
"""
df = pd.read_csv(Path('exercicio/raw/clientes.csv'))

df['idade'] = [25, 30, 22, 28]

print(df)

df.to_csv(Path('exercicio/processed/clientes_com_idade.csv'), index=False)
"""
################################################################
"""
2. Parâmetros do to_csv

# Leia o arquivo 'exercicio_raw/produtos.csv'
# Salve uma cópia em 'exercicio_processed/produtos_sep.csv' usando sep=';'
# Salve outra cópia em 'exercicio_processed/produtos_sem_cabecalho.csv' sem cabeçalho
"""
"""
arquivo = Path('exercicio/raw/produtos.csv')

df = pd.read_csv(arquivo)

print(df)

caminho_sep = Path('exercicio/processed/produtos_sep.csv')
df.to_csv(caminho_sep, sep=';', index=False)

caminho_sem_cabecalho = Path('exercicio/processed/produtos_sem_cabecalho.csv')
df.to_csv(caminho_sem_cabecalho, header=False, index=False)
"""
################################################################
"""
3. Usando pathlib

# Use pathlib para criar o caminho para 'exercicio_raw/clientes.csv'
# Leia o arquivo usando esse caminho
# Mostre o DataFrame
"""
"""
arquivo = Path('exercicio/raw/clientes.csv')
df = pd.read_csv(arquivo)
print(df)
"""
################################################################
# NÍVEL 4-6: Aplicação
################################################################
"""
4. Processando um único arquivo

# Leia 'exercicio_raw/produtos.csv'
# Adicione uma coluna 'preco_com_desconto' com 10% de desconto
# Salve em 'exercicio_processed/produtos_com_desconto.csv'
"""
"""
arquivo = Path('exercicio/raw/produtos.csv')

df = pd.read_csv(arquivo)

print(df)

df['preco_com_desconto'] = df['preco'] * 0.9

caminho = Path('exercicio/processed/produtos_com_desconto.csv')
df.to_csv(caminho, index=False)
"""
################################################################
"""
5. Verificando existência antes de ler

# Use pathlib para verificar se 'exercicio_raw/clientes.csv' existe
# Se existir, leia e mostre as primeiras linhas
# Se não existir, mostre "Arquivo não encontrado"
"""
"""
arquivo = Path('exercicio/raw/clientes.csv')

if arquivo.exists():
    df = pd.read_csv(arquivo)
    print(df.head())
else:
    print(f'{arquivo} não encontrado!')
"""
################################################################
"""
6. Mesclando dois arquivos

# Leia 'exercicio_raw/clientes.csv' e 'exercicio_raw/produtos.csv'
# (Esses arquivos não têm relação direta - para o exercício, apenas leia ambos)
# Mostre os dois DataFrames
"""
"""
clientes = Path('exercicio/raw/clientes.csv')
produtos = Path('exercicio/raw/produtos.csv')

df_clientes = pd.read_csv(clientes)
df_produtos = pd.read_csv(produtos)

print(f'Clientes:\n{df_clientes}\n')
print(f'Produtos:\n{df_produtos}\n')
"""
################################################################
# NÍVEL 7-8: Manipulação
################################################################
"""
7. Pipeline de limpeza

# Crie um arquivo 'exercicio_raw/vendas_sujo.csv' com:
# produto,quantidade,preco
# celular,10,1500
# fone,,200
# notebook,5,
# mouse,100,50
#
# Leia o arquivo
# Remova linhas com preco nulo
# Preencha quantidade nula com a mediana
# Salve o resultado limpo em 'exercicio_processed/vendas_limpo.csv'
"""
"""
arquivo = Path('exercicio/raw/vendas_sujo.csv')

with open(arquivo, 'w', newline='') as f:
    f.write('produto,quantidade,preco\n')
    f.write('celular,10,1500\n')
    f.write('fone,,200\n')
    f.write('notebook,5,\n')
    f.write('mouse,100,50\n')

df_sujo = pd.read_csv(arquivo)

print(f'Vendas sujo:\n{df_sujo}\n')

df_limpo = df_sujo.copy()

df_limpo = df_limpo.dropna(subset='preco')
df_limpo['quantidade'] = df_limpo['quantidade'].fillna(round(df_limpo['quantidade'].median()))

print(f'Vendas limpo:\n{df_limpo}\n')

saida = Path('exercicio/processed/vendas_limpo.csv')
df_limpo.to_csv(saida, index=False)
"""
################################################################
"""
8. Processando múltiplos arquivos

# Crie dois arquivos na pasta 'exercicio_raw/':
# - 'vendas1.csv' com produto,quantidade (celular,10; fone,30)
# - 'vendas2.csv' com produto,quantidade (notebook,5; mouse,100)
#
# Use um loop para ler cada arquivo
# Para cada um, adicione uma coluna 'preco' (celular=1500, fone=200, notebook=3500, mouse=50)
# Salve cada arquivo processado em 'exercicio_processed/com_prECO_INCREMENTA_O_NOME_AQUI'
"""
"""
with open('exercicio/raw/vendas1.csv', 'w', newline='') as f:
    f.write('produto,quantidade\n')
    f.write('celular,10\n')
    f.write('fone,30\n')

with open('exercicio/raw/vendas2.csv', 'w', newline='') as f:
    f.write('produto,quantidade\n')
    f.write('notebook,5\n')
    f.write('mouse,100\n')

for arquivo in Path('exercicio/raw').glob('vendas*.csv'):

    df = pd.read_csv(arquivo)
    print(f'{arquivo}:\n{df}\n')

    df['preco'] = df['produto'].map({
        'celular': 1500,
        'fone': 200,
        'notebook': 3500,
        'mouse': 50
    })

    print(f'{arquivo} com preços:\n{df}\n')

    saida = Path(f'exercicio/processed/{arquivo.stem}_com_preco.csv')
    df.to_csv(saida, index=False)
    print(f'Salvo em {saida}!\n')
"""
################################################################
# NÍVEL 9-10: Desafios
################################################################
"""
9. Pipeline de vendas completo

# Crie a estrutura:
#   vendas1/raw/
#   vendas1/processed/
#   vendas1/output/
#
# Crie 3 arquivos de vendas na pasta raw (diferentes produtos, quantidades)
# Para cada arquivo:
#   1. Leia
#   2. Adicione coluna 'total' (quantidade * preco)
#   3. Salve na pasta processed
#   4. Gere um resumo (total_vendas, total_itens) e salve na pasta output
#
# No final, mostre:
#   - Quantos arquivos foram processados
#   - Total geral de vendas (soma de todos os totais)
"""
"""
pai = Path('01_vendas')

pastas = [
    '01_raw',
    '02_processed',
    '03_output'
]

for pasta in pastas:
    caminho = pai / pasta
    caminho.mkdir(parents=True, exist_ok=True)

precos = {
    'celular': 1500,
    'fone': 200,
    'notebook': 3500,
    'mouse': 50,
    'teclado': 120,
    'monitor': 800,
    'tablet': 1200,
    'camera': 900
}

# Arquivo 1: 01_vendas.csv
df1 = pd.DataFrame({
    'produto': ['celular', 'fone', 'celular', 'mouse'],
    'quantidade': [10, 30, 5, 100],
    'vendedor': ['Ana', 'Bruno', 'Carla', 'Ana']
})
df1.to_csv(pai / '01_raw' / '01_vendas.csv', index=False)

# Arquivo 2: 02_vendas.csv
df2 = pd.DataFrame({
    'produto': ['notebook', 'teclado', 'mouse', 'fone', 'monitor'],
    'quantidade': [3, 15, 50, 25, 2],
    'vendedor': ['Bruno', 'Ana', 'Carla', 'Bruno', 'Daniel']
})
df2.to_csv(pai / '01_raw' / '02_vendas.csv', index=False)

# Arquivo 3: 03_vendas.csv
df3 = pd.DataFrame({
    'produto': ['celular', 'tablet', 'fone', 'camera', 'notebook', 'mouse'],
    'quantidade': [8, 4, 40, 3, 2, 60],
    'vendedor': ['Carla', 'Ana', 'Daniel', 'Bruno', 'Ana', 'Carla']
})
df3.to_csv(pai / '01_raw' / '03_vendas.csv', index=False)

for arquivo in Path('01_vendas/01_raw').glob('*.csv'):

    df = pd.read_csv(arquivo)
    df['preco'] = df['produto'].map(precos)
    df['total'] = df['quantidade']*df['preco']

    saida = Path(f'01_vendas/02_processed/{arquivo.stem}_processed.csv')
    df.to_csv(saida, index=False)

    df_resumo = pd.DataFrame({
        'total_vendas': [df['total'].sum()],
        'total_itens': [df['quantidade'].sum()]
    })

    resumo = Path(f'01_vendas/03_output/{arquivo.stem}_resumo.csv')
    df_resumo.to_csv(resumo, index=False)

arquivos_processados = list(Path('01_vendas/02_processed').glob('*.csv'))

total_vendas = 0
total_itens = 0

for arquivo in Path('01_vendas/03_output').glob('*.csv'):

    df = pd.read_csv(arquivo)
    total_vendas += df['total_vendas']
    total_itens += df['total_itens']

print(f'Arquivos processados: {len(arquivos_processados)}')
print(f'Total geral de vendas: {total_vendas.max()}')
print(f'Total geral de itens: {total_itens.max()}')
"""
################################################################
"""
10. DESAFIO FINAL: ETL completo

# Crie a estrutura:
#   dados/raw/
#   dados/processed/
#   dados/output/
#
# Crie 2 arquivos CSV na pasta raw:
#
# clientes.csv:
# id,nome,cidade
# 1,Ana,SP
# 2,Bruno,RJ
# 3,Carla,BH
#
# vendas.csv:
# id_cliente,produto,quantidade,preco
# 1,celular,10,1500
# 1,fone,30,200
# 2,notebook,5,3500
# 3,mouse,100,50
#
# Tarefas:
# 1. Leia ambos os arquivos
# 2. Faça um merge para adicionar nome e cidade às vendas
# 3. Adicione coluna 'total' (quantidade * preco)
# 4. Salve o resultado em 'dados/processed/vendas_completas.csv'
# 5. Crie um resumo por cliente (nome, total_gasto) e salve em 'dados/output/resumo_clientes.csv'
# 6. Crie um resumo por cidade (cidade, total_gasto) e salve em 'dados/output/resumo_cidades.csv'
#
# Mostre: "Pipeline concluído! X registros processados."
"""
dados = Path('01_dados')

pastas = [
    '01_raw',
    '02_processed',
    '03_output'
]

for pasta in pastas:
    caminho = dados / pasta
    caminho.mkdir(parents=True, exist_ok=True)

with open('01_dados/01_raw/clientes.csv', 'w', newline='') as f:
    f.write('id,nome,cidade\n')
    f.write('1,Ana,SP\n')
    f.write('2,Bruno,RJ\n')
    f.write('3,Carla,BH\n')

with open('01_dados/01_raw/vendas.csv', 'w', newline='') as f:
    f.write('id_cliente,produto,quantidade,preco\n')
    f.write('1,celular,10,1500\n')
    f.write('1,fone,30,200\n')
    f.write('2,notebook,5,3500\n')
    f.write('3,mouse,100,50\n')

###########

df_clientes = pd.read_csv(Path('01_dados/01_raw/clientes.csv'))
df_vendas = pd.read_csv(Path('01_dados/01_raw/vendas.csv'))

df_vendas_completas = pd.merge(df_vendas, df_clientes, left_on='id_cliente', right_on='id', how='left')

df_vendas_completas['total'] = df_vendas_completas['quantidade'] * df_vendas_completas['preco']

df_vendas_completas = df_vendas_completas[['id_cliente', 'nome', 'cidade', 'produto', 'quantidade', 'preco', 'total']]

print(f'df_vendas_completo:\n{df_vendas_completas}\n')
saida_vendas = Path('01_dados/02_processed/vendas_completas.csv')
df_vendas_completas.to_csv(saida_vendas, index=False)

df_resumo_clientes = df_vendas_completas.groupby('nome').agg(total_gasto=('total', 'sum')).reset_index()
print(f'\ndf_resumo_clientes:\n{df_resumo_clientes}\n')
saida_resumo_cliente = Path('01_dados/03_output/resumo_clientes.csv')
df_resumo_clientes.to_csv(saida_resumo_cliente, index=False)

df_resumo_cidades = df_vendas_completas.groupby('cidade').agg(total_gasto=('total', 'sum')).reset_index()
print(f'\ndf_resumo_cidades:\n{df_resumo_cidades}\n')
saida_resumo_cidade = Path('01_dados/03_output/resumo_cidades.csv')
df_resumo_cidades.to_csv(saida_resumo_cidade, index=False)