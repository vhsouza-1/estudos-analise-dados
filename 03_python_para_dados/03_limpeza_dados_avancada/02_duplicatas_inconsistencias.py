"""
Bloco 3: Python para Dados
Módulo 3: Limpeza de Dados Avançada
Aula 2: Duplicatas e Inconsistências
Data: 05/05/2026
Objetivo: Aprender a identificar e tratar dados duplicados e inconsistentes
"""

import pandas as pd
import numpy as np
import seaborn as sns

# ==========================================
# 1. O QUE SÃO DUPLICATAS?
# ==========================================

print("="*50)
print("1. O QUE SÃO DUPLICATAS?")
print("="*50)

"""
DUPLICATAS: linhas (ou valores) que aparecem mais de uma vez no DataFrame.

Por que ocorrem?
- Erro na coleta de dados
- Múltiplas fontes combinadas
- Erro humano (digitar duas vezes)
- Bugs em sistemas

Por que remover?
- Distorcem análises (médias, contagens)
- Causam overfitting em modelos
- Inflam números incorretamente
"""
# DataFrame com duplicatas
df_duplicado = pd.DataFrame({
    'id': [1, 2, 3, 2, 4, 1],
    'nome': ['Ana', 'Bruno', 'Carlos', 'Bruno', 'Daniela', 'Ana'],
    'idade': [25, 30, 35, 30, 28, 25],
    'cidade': ['SP', 'RJ', 'BH', 'RJ', 'POA', 'SP']
})

print("DataFrame com duplicatas:")
print(df_duplicado)

# ==========================================
# 2. IDENTIFICANDO DUPLICATAS
# ==========================================

print("\n" + "="*50)
print("2. IDENTIFICANDO DUPLICATAS")
print("="*50)

# 2.1 duplicated() - retorna boolean mask
print("--- duplicated() (marca duplicatas a partir da 2ª ocorrência) ---")
print(df_duplicado.duplicated())

print("\n--- duplicated(keep='first') (padrão) ---")
print(f"Linhas duplicadas: {df_duplicado[df_duplicado.duplicated(keep='first')]}")

print("\n--- duplicated(keep='last') (marca primeiras como duplicadas) ---")
print(f"Linhas duplicadas: {df_duplicado[df_duplicado.duplicated(keep='last')]}")

print("\n--- duplicated(keep=False) (marca TODAS as duplicadas) ---")
print(f"Linhas duplicadas: {df_duplicado[df_duplicado.duplicated(keep=False)]}")

# 2.2 duplicated() com subset - considerar apenas colunas específicas
print("\n--- duplicated(subset=['nome', 'idade']) (duplicatas baseadas nessas colunas) ---")
print(df_duplicado.duplicated(subset=['nome', 'idade']))

# ==========================================
# 3. REMOVENDO DUPLICATAS
# ==========================================

print("\n" + "="*50)
print("3. REMOVENDO DUPLICATAS (drop_duplicates)")
print("="*50)

# 3.1 drop_duplicates básico
print("--- drop_duplicates() (mantém primeira ocorrência) ---")
df_sem_duplicatas = df_duplicado.drop_duplicates()
print(df_sem_duplicatas)

# 3.2 drop_duplicates(keep='last') - mantém última
print("\n--- drop_duplicates(keep='last') ---")
print(df_duplicado.drop_duplicates(keep='last'))

# 3.3 drop_duplicates(keep=False) - remove TODAS as duplicatas
print("\n--- drop_duplicates(keep=False) (remove todas as ocorrências) ---")
print(df_duplicado.drop_duplicates(keep=False))

# 3.4 drop_duplicates com subset
print("\n--- drop_duplicates(subset=['nome', 'idade']) ---")
print(df_duplicado.drop_duplicates(subset=['nome', 'idade']))

# ==========================================
# 4. DUPLICATAS EM COLUNAS ESPECÍFICAS
# ==========================================

print("\n" + "="*50)
print("4. TRABALHANDO COM DUPLICATAS EM COLUNAS ESPECÍFICAS")
print("="*50)

# Caso: ID que deveria ser único mas tem duplicatas
df_ids = pd.DataFrame({
    'id_cliente': [101, 102, 103, 101, 104, 102],
    'nome': ['João', 'Maria', 'José', 'João', 'Ana', 'Maria'],
    'compra': [100, 200, 150, 300, 250, 180]
})

print("DataFrame com IDs duplicados:")
print(df_ids)

print("\n--- Verificando se 'id_cliente' é único ---")
print(f"ID único? {df_ids['id_cliente'].is_unique}")
print(f"IDs duplicados: {df_ids[df_ids['id_cliente'].duplicated()]['id_cliente'].unique()}")

print("\n--- Agrupando por ID para consolidar (soma de compras) ---")
df_consolidado = df_ids.groupby('id_cliente').agg({
    'nome': 'first',  # primeiro nome
    'compra': 'sum'   # soma das compras
}).reset_index()

# ==========================================
# 5. INCONSISTÊNCIAS EM DADOS CATEGÓRICOS
# ==========================================

print("\n" + "="*50)
print("5. INCONSISTÊNCIAS EM DADOS CATEGÓRICOS")
print("="*50)

"""
O que são inconsistências?
- Mesma categoria escrita de formas diferentes (SP, sp, São Paulo, S.P.)
- Erros de digitação (Teconologia em vez de Tecnologia)
- Variantes (Masculino, M, Male, Homem)

Como tratar?
1. Identificar valores únicos (.unique())
2. Verificar frequência (.value_counts())
3. Padronizar (minúsculas, remover espaços)
4. Mapear (map, replace)
"""

# Dados com inconsistências
df_categorias = pd.DataFrame({
    'produto': ['Celular', 'NOTEBOOK', 'celular', 'Tablet', 'notebook', 'CELULAR', 'tablet', 'Smartphone'],
    'vendas': [100, 200, 150, 80, 180, 120, 90, 250]
})

print("DataFrame com categorias inconsistentes:")
print(df_categorias)

print("\n--- Valores únicos (problema: maiúsculas/minúsculas) ---")
print(df_categorias['produto'].unique())

print("\n--- Frequência (mesmo produto aparece diferentes) ---")
print(df_categorias['produto'].value_counts())

# 5.1 Padronizar para minúsculas
print("\n--- Padronizando para minúsculas ---")
df_categorias['produto_pad'] = df_categorias['produto'].str.lower()
print(df_categorias[['produto', 'produto_pad']].head())

print("\n--- Agora sim, valores únicos padronizados ---")
print(df_categorias['produto_pad'].unique())

# 5.2 Remover espaços extras
df_espacos = pd.DataFrame({
    'cidade': ['São Paulo', 'Rio de Janeiro', 'São Paulo ', ' Rio de Janeiro', 'Belo Horizonte']
})

print("\n--- DataFrame com espaços extras ---")
print(df_espacos)

df_espacos['cidade_limpa'] = df_espacos['cidade'].str.strip()
print("\n--- Após .str.strip() (remove espaços antes/depois) ---")
print(df_espacos)

# 5.3 Mapeamento de sinônimos
print("\n--- Mapeamento de sinônimos (estados) ---")
df_estados = pd.DataFrame({
    'estado': ['SP', 'São Paulo', 'Sao Paulo', 'sp', 'RJ', 'Rio de Janeiro', 'rj', 'MG']
})

print("Antes:")
print(df_estados['estado'].value_counts())

# Criar mapeamento
mapeamento_estados = {
    'SP': 'São Paulo',
    'São Paulo': 'São Paulo',
    'Sao Paulo': 'São Paulo',
    'sp': 'São Paulo',
    'RJ': 'Rio de Janeiro',
    'Rio de Janeiro': 'Rio de Janeiro',
    'rj': 'Rio de Janeiro',
    'MG': 'Minas Gerais'
}

df_estados['estado_pad'] = df_estados['estado'].map(mapeamento_estados)
print("\nDepois do mapeamento:")
print(df_estados['estado_pad'].value_counts())

# ==========================================
# 6. VALORES INCONSISTENTES (OUTLIERS APARENTES)
# ==========================================

print("\n" + "="*50)
print("6. VALORES INCONSISTENTES (OUTLIERS APARENTES)")
print("="*50)

"""
Nem todo valor diferente é erro, mas alguns claramente são inconsistentes.

Exemplos:
- Idade = 999 anos
- Salário negativo
- Data de nascimento no futuro
- CEP com letras
"""

df_inconsistente = pd.DataFrame({
    'nome': ['Ana', 'Bruno', 'Carlos', 'Daniel'],
    'idade': [25, 999, 30, -5],
    'salario': [3000, 5000, -1000, 8000],
    'data_nasc': ['1999-01-01', '1890-05-20', '2025-12-31', '1995-03-15']
})

print("DataFrame com valores inconsistentes:")
print(df_inconsistente)

# 6.1 Identificar inconsistências numéricas
print("\n--- Verificando idades impossíveis (<0 ou >120) ---")
mascara_idade = (df_inconsistente['idade'] < 0) | (df_inconsistente['idade'] > 120)
print(f"Idades inconsistentes:\n{df_inconsistente[mascara_idade]}")

print("\n--- Verificando salários negativos ---")
mascara_salario = df_inconsistente['salario'] < 0
print(f"Salários negativos:\n{df_inconsistente[mascara_salario]}")

# 6.2 Tratar inconsistências (substituir por np.nan)
print("\n--- Substituindo inconsistentes por np.nan ---")
df_inconsistente_tratado = df_inconsistente.copy()
df_inconsistente_tratado.loc[mascara_idade, 'idade'] = np.nan
df_inconsistente_tratado.loc[mascara_salario, 'salario'] = np.nan
print(df_inconsistente_tratado)

# 6.3 Verificar datas no futuro
print("\n--- Verificando datas no futuro ---")
df_inconsistente_tratado['data_nasc'] = pd.to_datetime(df_inconsistente_tratado['data_nasc'])
data_hoje = pd.Timestamp.now()
mascara_data_futuro = df_inconsistente_tratado['data_nasc'] > data_hoje
print(f"Datas no futuro:\n{df_inconsistente_tratado[mascara_data_futuro]}")

# ==========================================
# 7. PADRONIZAÇÃO COM replace() E map()
# ==========================================

print("\n" + "="*50)
print("7. PADRONIZAÇÃO COM replace() E map()")
print("="*50)

# 7.1 replace() para correções simples
df_replace = pd.DataFrame({
    'status': ['APROVADO', 'aprovado', 'Reprovado', 'Aprovado', 'reprovado', 'APROVADO']
})

print("Antes do replace:")
print(df_replace['status'].value_counts())

df_replace['status_pad'] = df_replace['status'].str.lower().replace({
    'aprovado': 'Aprovado',
    'reprovado': 'Reprovado'
})

print("\nDepois do replace:")
print(df_replace['status_pad'].value_counts())

# 7.2 Usar replace com dicionário (mais eficiente para muitos valores)
correcoes = {
    'SP': 'São Paulo',
    'Sao Paulo': 'São Paulo',
    'S. Paulo': 'São Paulo',
    'RJ': 'Rio de Janeiro',
    'Rio': 'Rio de Janeiro'
}

df_cidades = pd.DataFrame({'cidade': ['SP', 'RJ', 'Sao Paulo', 'Rio', 'SP', 'MG']})
df_cidades['cidade_corrigida'] = df_cidades['cidade'].replace(correcoes)

print("\n--- Corrigindo cidades com replace ---")
print(df_cidades)

# ==========================================
# 8. CASO PRÁTICO: LIMPEZA DE CATEGORIAS
# ==========================================

print("\n" + "="*50)
print("8. CASO PRÁTICO - Limpeza de Categorias de Produtos")
print("="*50)

# Dados reais simulados (com problemas comuns)
df_produtos = pd.DataFrame({
    'produto': ['Camiseta', 'camiseta', 'CAMISETA', 'Calça', 'calça', 'CALÇA', 'Tênis', 'tenis', 'TENIS'],
    'cor': ['Azul', 'azul', 'AZUL', 'Preto', 'preto', 'PRETO', 'Branco', 'branco', 'BRANCO'],
    'tamanho': ['P', 'p', 'P', 'M', 'm', 'M', 'G', 'g', 'G'],
    'vendas': [100, 150, 120, 200, 180, 220, 80, 90, 100]
})

print("Dados brutos (com inconsistências):")
print(df_produtos)
print(f"\nProdutos únicos (PROBLEMA): {df_produtos['produto'].unique()}")

# Pipeline de limpeza
df_limpo = df_produtos.copy()

df_limpo['produto'] = df_limpo['produto'].str.lower().str.strip()
df_limpo['cor'] = df_limpo['cor'].str.lower().str.strip()
df_limpo['tamanho'] = df_limpo['tamanho'].str.upper().str.strip()

# Passo 2: Corrigir variações
correcao_tamanho = {'P': 'P', 'p': 'P', 'M': 'M', 'm': 'M', 'G': 'G', 'g': 'G'} # n precisa disso, o df_limpo['tamanho'] = df_limpo['tamanho'].str.upper().str.strip() já faz isso.
df_limpo['tamanho'] = df_limpo['tamanho'].replace(correcao_tamanho)
correcao_produto = {'tenis': 'tênis'}
df_limpo['produto'] = df_limpo['produto'].replace(correcao_produto) # falou fazer isso aqui...

# Passo 3: Agrupar para consolidar (já que temos duplicatas após padronização)
print("\n--- Após padronização (ainda com linhas duplicadas) ---")
print(df_limpo)

print("\n--- Consolidando vendas por produto/cor/tamanho ---")
df_consolidado = df_limpo.groupby(['produto', 'cor', 'tamanho'])['vendas'].sum().reset_index()
print(df_consolidado)

print(f"\n✅ Limpeza concluída! {len(df_produtos)} linhas -> {len(df_consolidado)} linhas")

# ==========================================
# 9. RESUMO DA AULA
# ==========================================

print("\n" + "=" * 50)
print("9. RESUMO DA AULA")
print("=" * 50)

"""
✅ DUPLICATAS:
   - df.duplicated()              # identificar duplicatas
   - df.duplicated(keep='last')   # marcar primeiras como duplicadas
   - df.duplicated(keep=False)    # marcar todas as duplicadas
   - df.duplicated(subset=['col']) # considerar apenas algumas colunas

   - df.drop_duplicates()              # remover (mantém primeira)
   - df.drop_duplicates(keep='last')   # mantém última
   - df.drop_duplicates(keep=False)    # remove todas
   - df.drop_duplicates(subset=['col']) # baseado em colunas específicas

✅ INCONSISTÊNCIAS EM CATEGORIAS:
   - df['col'].str.lower()         # padronizar minúsculas
   - df['col'].str.upper()         # padronizar maiúsculas
   - df['col'].str.strip()         # remover espaços
   - df['col'].str.replace(' ', '') # remover espaços internos

   - df['col'].map(dicionario)     # mapear valores
   - df['col'].replace(dicionario) # substituir múltiplos valores

✅ VALORES INCONSISTENTES:
   - df[(df['col'] < 0) | (df['col'] > 100)]  # identificar fora dos limites
   - pd.to_datetime(df['col'], errors='coerce') # converter datas, erros viram NaT
   - df['col'] > pd.Timestamp.now()            # datas no futuro

📌 BOAS PRÁTICAS:
   1. SEMPRE verifique .unique() e .value_counts() antes de limpar
   2. Documente suas transformações
   3. Teste se a coluna deveria ser única (.is_unique)
   4. Crie cópias antes de modificar (df.copy())
"""
# ==========================================
# EXERCÍCIOS - AULA 2
# ==========================================

print("\n" + "="*50)
print("EXERCÍCIOS - DUPLICATAS E INCONSISTÊNCIAS")
print("="*50)

# Dados para todos os exercícios
np.random.seed(42)

df_estoque = pd.DataFrame({
    'id_produto': [101, 102, 103, 101, 104, 102, 105, 103, 106, 107],
    'nome_produto': ['Notebook', 'Mouse', 'Teclado', 'Notebook', 'Monitor', 'Mouse', 'Webcam', 'Teclado', 'Impressora', 'Cadeira'],
    'categoria': ['eletrônico', 'periférico', 'periférico', 'eletrônico', 'eletrônico', 'PERIFÉRICO', 'eletrônico', 'Periférico', 'eletrônico', 'móvel'],
    'preco': [2500, 150, 300, 2600, 1200, 160, 350, 310, 800, 450],
    'estoque': [10, 50, 30, 8, 15, 45, 20, 28, 5, 12]
})

# Adicionar algumas inconsistências
df_estoque.loc[8, 'preco'] = -100  # preço negativo
df_estoque.loc[9, 'categoria'] = 'MÓVEL'  # maiúsculo

########################################################################
# NÍVEL 1-3: Aquecimento
########################################################################

"""
1. Identificando duplicatas

# Mostre:
# - Quantas linhas duplicadas existem (baseado em todas as colunas)
# - Quais são as linhas duplicadas
# - Use keep=False para ver todas as ocorrências
"""

"""
print(f'Linhas duplicadas: {df_estoque.duplicated().sum()}') # antes do tratamento dos dados, nem sempre é possível saber se existem linhas duplicadas!
# Também há o fato de que algumas linhas diferem apenas nas colunas 'preco' e 'estoque'. Que pode significar coisas diferentes dependendo da construção do df!

print(f'\nQuais são as linhas duplicadas:\n{df_estoque[df_estoque.duplicated()]}')

print(f'\nTodas as linhas duplicadas (keep=False):\n{df_estoque[df_estoque.duplicated(keep=False)]}')
"""
########################################################################

"""
2. Removendo duplicatas

# Remova as duplicatas mantendo a primeira ocorrência
# Mostre quantas linhas foram removidas
# Mostre o DataFrame resultante
"""
"""
df = df_estoque.copy()

df = df.drop_duplicates(keep='first')

print(f'\nForam removidas {len(df_estoque) - len(df)} linhas!')

print(f'DataFrame resultante:\n{df}')
"""
########################################################################

"""
3. Duplicatas baseadas em colunas específicas

# Considere que 'id_produto' deveria ser único
# Identifique quantos IDs estão duplicados
# Quais produtos têm o mesmo ID?
"""

"""
df = df_estoque.copy()

print(f'Com Python puro:')
qnt_id_duplicados = 0
quais_id_duplicados = []
for id, qnt in dict(df['id_produto'].value_counts()).items():
    if qnt > 1:
        qnt_id_duplicados += 1
        quais_id_duplicados.append(id)
print(f'Quantidade de IDs duplicados: {qnt_id_duplicados}')
print(f'Quais IDs estão duplicados: {quais_id_duplicados}')

print(f'\nCom pandas: ')
print(f'Quantidade de IDs duplicados {df.duplicated(subset='id_produto').sum()}')
print(f'Quais IDS estão duplicados: {df[df.duplicated(subset='id_produto')]['id_produto'].unique()}')

# quis fazer os dois para testar.
"""
########################################################################
# NÍVEL 4-6: Aplicação
########################################################################

"""
4. Padronizando categorias

# A coluna 'categoria' tem inconsistências:
# - "periférico" vs "PERIFÉRICO" vs "Periférico"
# - "móvel" vs "MÓVEL"
#
# Padronize para minúsculas e mostre os valores únicos após a correção
"""

"""
df = df_estoque.copy()

print(f'Valores únicos antes da correção:\n{df['categoria'].unique()}')

df['categoria'] = df['categoria'].str.lower().str.strip()

print(f'\nValores únicos após da correção:\n{df['categoria'].unique()}')
"""
########################################################################

"""
5. Corrigindo valores inconsistentes

# Identifique e corrija:
# - Preços negativos (transforme em np.nan)
# - Depois, preencha os preços nulos com a mediana dos preços
"""

"""
df = df_estoque.copy()

preco_mask = (df['preco'] < 0)

df.loc[preco_mask, 'preco'] = np.nan

df['preco'] = df['preco'].fillna(df['preco'].median())

print(df)
"""
########################################################################

"""
6. Consolidando dados duplicados

# Agrupe os dados por 'id_produto' e 'nome_produto'
# Some os valores de 'estoque' (caso um produto apareça mais de uma vez)
# Calcule a média dos preços (ou mantenha o primeiro preço)
# Mostre o DataFrame consolidado
"""

"""
df = df_estoque.copy()

# Primeiro corrigir o preço negativo
preco_mask = (df['preco'] < 0)
df.loc[preco_mask, 'preco'] = np.nan
df['preco'] = df['preco'].fillna(df['preco'].median())

df_consolidado = df.groupby(['id_produto', 'nome_produto']).agg(
    estoque_total=('estoque', 'sum'),
    preco_medio=('preco', 'mean')
).reset_index()

print(df_consolidado)
"""

########################################################################
# NÍVEL 7-8: Manipulação
########################################################################

"""
7. Limpeza completa de categorias

# Crie uma função que:
# 1. Padroniza categoria para minúsculas e remove espaços
# 2. Corrige sinônimos (periférico, periferico, periferico) # dois periféricos iguais aqui no seu exemplo.
# 3. Corrige "eletrônico" (possíveis variações como "eletronico")
# 4. Agrupa categorias muito pequenas como "Outros"
#
# Aplique no DataFrame original
"""

"""
def pipeline_limpeza(df):

    df['categoria'] = df['categoria'].str.lower().str.strip()

    sinonimos = {
        'periferico': 'periférico',
        'eletronico': 'eletrônico'
    }

    df['categoria'] = df['categoria'].replace(sinonimos)

    # Agrupar estoque por categoria
    estoque_categoria = df.groupby('categoria')['estoque'].sum()

    # loop para verificar se o estoque da categoria é <10% do estoque total
    for categoria in estoque_categoria.reset_index()['categoria']:
        if estoque_categoria[categoria] / df['estoque'].sum() < 0.1:
            df['categoria'] = df['categoria'].replace(categoria, 'Outros') # Se for, troca por Outros.

    return df

df_limpo = pipeline_limpeza(df_estoque)

print(df_limpo)
"""
########################################################################

"""
8. Encontrando registros órfãos

# Imagine que você tem uma tabela de produtos e uma de vendas
# Identifique produtos que nunca venderam (não aparecem na tabela de vendas)
"""

"""
df_produtos_vendas = pd.DataFrame({
    'id_produto': [1, 2, 3, 4, 5],
    'produto': ['A', 'B', 'C', 'D', 'E']
})

df_vendas = pd.DataFrame({
    'id_venda': [100, 101, 102],
    'id_produto': [1, 2, 4],
    'quantidade': [10, 5, 8]
})

# Eu tava tentando fazer isso aqui:
# id_produto_mask = (df_produtos_vendas['id_produto']) & ~(df_vendas['id_produto']) (pq me pareceu intuitivo isso)
# fui pesquisar e descobri que isso não funciona e que o certo era usar .isin(), a questão é que eu n conhecia .isin()
# dei uma pesquisada e acho que entendi o básico.

id_produto_mask = ~df_produtos_vendas['id_produto'].isin(df_vendas['id_produto'])

print(f'Produtos não vendidos:\n{df_produtos_vendas.loc[id_produto_mask, 'produto'].unique()}')
"""

########################################################################
# NÍVEL 9-10: Desafios
########################################################################

"""
9. Pipeline de limpeza para categorias (nível real)

# Limpe o DataFrame abaixo com várias inconsistências:
# - Maiúsculas/minúsculas
# - Espaços extras
# - Variações (ex: "Tecnologia", "tech", "TI" - todos devem virar "Tecnologia")
# - Abreviações ("RH" -> "Recursos Humanos")
# - Valores vazios ou 'NA' tratados como nulos
#
# Crie um dicionário de mapeamento e aplique
"""

"""
df_categorias_reais = pd.DataFrame({
    'departamento': ['TI', 'Tecnologia', 'tech', 'RH', 'Recursos Humanos', 'r h', 'Financeiro', 'Finanças', 'fin', 'Marketing', 'MKT', ''],
    'funcionarios': [10, 12, 8, 5, 6, 4, 15, 14, 13, 7, 9, 11]
})

print("DataFrame com problemas reais:")
print(df_categorias_reais)
print(f"\nValores únicos: {df_categorias_reais['departamento'].unique()}")

df = df_categorias_reais.copy()

df['departamento'] = df['departamento'].str.lower().str.strip()

dicionario_substituicao = {
    'ti': 'Tecnologia',
    'tecnologia': 'Tecnologia',
    'tech': 'Tecnologia',
    'rh': 'Recursos Humanos',
    'recursos humanos': 'Recursos Humanos',
    'r h': 'Recursos Humanos',
    'financeiro': 'Finanças',
    'finanças': 'Finanças',
    'fin': 'Finanças',
    'marketing': 'Marketing',
    'mkt': 'Marketing',
    '': np.nan,
    'NA': np.nan
}

df['departamento'] = df['departamento'].map(dicionario_substituicao)

print(df)
"""
########################################################################

"""
10. DESAFIO FINAL: Análise de qualidade de dados

# Crie um relatório de qualidade para o DataFrame abaixo.
# O relatório deve incluir:
#
# 1. Para CADA coluna:
#    - Total de valores únicos
#    - Quantidade de valores nulos
#    - Quantidade de valores inconsistentes (defina você o que é inconsistente para cada coluna)
#    - Sugestão de correção
#
# 2. Para o DataFrame inteiro:
#    - Quantidade de linhas duplicadas
#    - Porcentagem de células problemáticas (nulos + inconsistentes)
#
# 3. Aplique as correções sugeridas e retorne o DataFrame limpo
#
# Use o DataFrame abaixo (dados de clientes)
"""

df_clientes = pd.DataFrame({
    'id_cliente': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'nome': ['João Silva', 'MARIA SANTOS', 'Pedro', 'Ana Paula', 'José', 'CARLA', 'Roberto', 'Fernanda', 'Rafael', 'TATIANE'],
    'email': ['joao@email.com', 'maria@email', 'pedro@', 'ana@email.com', 'jose@email.com', 'carla@email.com', 'roberto@email.com', 'fernanda@email.com', 'rafael@email.com', 'tati@email.com'],
    'idade': [25, -5, 32, 150, 28, 35, 999, 42, 31, 29],
    'cidade': ['São Paulo', 'sp', 'Rio de Janeiro', 'RJ', 'Belo Horizonte', 'BH', 'Curitiba', 'CWB', 'Porto Alegre', 'POA'],
    'renda': [3000, 4000, -1000, 5000, 6000, 7000, 8000, -500, 9000, 10000],
    'data_cadastro': ['2023-01-01', '2023-02-15', '2026-12-31', '2023-03-20', '2023-04-10', '2023-05-05', '2023-06-12', '2023-07-01', '2023-08-20', '2023-09-15']
})

print("DataFrame para análise de qualidade:")
# print(df_clientes.to_string())

df=df_clientes.copy()

def relatorio_limpeza(df):

    with open('relatorio.txt', 'w', newline='') as f: # Tava confuso sobre como escrever o relatório, então decidi fazer um .txt externo

        n_celulas_problematicas = df.isnull().sum().sum()

        f.write(f'Coluna "id_cliente":\n')
        f.write(f' - Total de valores únicos: {df['id_cliente'].nunique()}\n')
        f.write(f' - Quantidade de valores nulos: {df['id_cliente'].isnull().sum()}\n')
        f.write(f' - Quantidade de valores inconsistentes: {df['id_cliente'][df['id_cliente'] < 0].count()}\n')
        n_celulas_problematicas += df['id_cliente'][df['id_cliente'] < 0].count()
        f.write('\n')
        f.write(f'Coluna "nome":\n')
        f.write(f' - Total de valores únicos: {df['nome'].nunique()}\n')
        f.write(f' - Quantidade de valores nulos: {df['nome'].isnull().sum()}\n')
        f.write(f' - Quantidade de valores inconsistentes: {3}\n') # as string eu contei na mão pois não sabia como fazer
        n_celulas_problematicas += 3
        f.write(f' - Sugestão de correção: Capitalizar os nomes\n')
        f.write('\n')
        f.write(f'Coluna "email":\n')
        f.write(f' - Total de valores únicos: {df['email'].nunique()}\n')
        f.write(f' - Quantidade de valores nulos: {df['email'].isnull().sum()}\n')
        f.write(f' - Quantidade de valores inconsistentes: {2}\n')
        n_celulas_problematicas += 2
        f.write(f' - Sugestão de correção: Completar emails\n')
        f.write('\n')
        f.write(f'Coluna "idade":\n')
        f.write(f' - Total de valores únicos: {df['idade'].nunique()}\n')
        f.write(f' - Quantidade de valores nulos: {df['idade'].isnull().sum()}\n')
        f.write(f' - Quantidade de valores inconsistentes: {df['idade'][(df['idade'] < 0)|(df['idade'] > 120)].count()}\n')
        n_celulas_problematicas += df['idade'][(df['idade'] < 0)|(df['idade'] > 120)].count()
        f.write(f' - Sugestão de correção: Substituir pela mediana\n')
        f.write('\n')
        f.write(f'Coluna "cidade":\n')
        f.write(f' - Total de valores únicos: {df['cidade'].nunique()}\n')
        f.write(f' - Quantidade de valores nulos: {df['cidade'].isnull().sum()}\n')
        f.write(f' - Quantidade de valores inconsistentes: {5}\n')
        n_celulas_problematicas += 5
        f.write(f' - Sugestão de correção: Substituir pelo nome completo da cidade\n')
        f.write('\n')
        f.write(f'Coluna "renda":\n')
        f.write(f' - Total de valores únicos: {df['renda'].nunique()}\n')
        f.write(f' - Quantidade de valores nulos: {df['renda'].isnull().sum()}\n')
        f.write(f' - Quantidade de valores inconsistentes: {df['renda'][df['renda'] < 0].count()}\n')
        n_celulas_problematicas += df['renda'][df['renda'] < 0].count()
        f.write(f' - Sugestão de correção: Substituir pela mediana\n')
        f.write('\n')
        f.write(f'Coluna "data_cadastro":\n')
        f.write(f' - Total de valores únicos: {df['data_cadastro'].nunique()}\n')
        f.write(f' - Quantidade de valores nulos: {df['data_cadastro'].isnull().sum()}\n')
        f.write(f' - Quantidade de valores inconsistentes: {df['data_cadastro'][pd.to_datetime(df['data_cadastro']) > pd.Timestamp.now()].count()}\n')
        n_celulas_problematicas += df['data_cadastro'][pd.to_datetime(df['data_cadastro']) > pd.Timestamp.now()].count()
        f.write(f' - Sugestão de correção: Substituir por data atual\n')
        f.write('\n')
        f.write(f'DataFrame geral:\n')
        f.write(f' - Quantidade de linhas duplicadas: {df.duplicated().count()}\n')
        f.write(f' - Porcentagem de células problemáticas: {n_celulas_problematicas/df.count().sum()*100:.2f}%\n')

    df_limpo = df.copy()

    df_limpo['nome'] = df_limpo['nome'].str.strip().str.title()
    df_limpo['email'] = df_limpo['email'].apply(lambda x: x.split('@')[0]+'@email.com')

    idade_mask = (df['idade'] < 0) | (df['idade'] > 120)
    df_limpo.loc[idade_mask, 'idade'] = np.nan
    df_limpo['idade'] = df_limpo['idade'].fillna(df_limpo['idade'].median())

    cidade_dicionario = {
        'sp': 'São Paulo',
        'RJ': 'Rio de Janeiro',
        'BH': 'Belo Horizonte',
        'CWB': 'Curitiba',
        'POA': 'Porto Alegre'
    }

    df_limpo['cidade'] = df_limpo['cidade'].replace(cidade_dicionario)

    renda_mask = (df['renda'] < 0)
    df_limpo.loc[renda_mask, 'renda'] = np.nan
    df_limpo['renda'] = df_limpo['renda'].fillna(df_limpo['renda'].median())

    data_mask = pd.to_datetime(df['data_cadastro']) > pd.Timestamp.now()
    df_limpo.loc[data_mask, 'data_cadastro'] = np.nan
    df_limpo['data_cadastro'] = df_limpo['data_cadastro'].fillna(pd.Timestamp.now().date())

    return df_limpo

df_limpo = relatorio_limpeza(df_clientes)

print(df_limpo.to_string())

# Não ficou perfeito, mas fiquei feliz com o resultado :)