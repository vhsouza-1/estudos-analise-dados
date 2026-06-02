"""
Script: gerar_dataset.py
Aula: 03 - Modelagem e Relacionamentos (Power BI)
Objetivo: Gerar múltiplas tabelas para aprender relacionamentos
Data: 02/06/2026
"""

import pandas as pd
import numpy as np
from pathlib import Path

PASTA_ATUAL = Path(__file__).parent
np.random.seed(42)

# ==========================================
# TABELA 1: VENDAS (Tabela Fato)
# ==========================================
n_vendas = 1000

df_vendas = pd.DataFrame({
    'id_venda': range(1, n_vendas + 1),
    'id_produto': np.random.randint(1, 11, n_vendas),
    'id_vendedor': np.random.randint(1, 6, n_vendas),
    'id_cliente': np.random.randint(1, 101, n_vendas),
    'data': pd.date_range('2024-01-01', periods=n_vendas, freq='D').strftime('%d/%m/%Y'),
    'quantidade': np.random.randint(1, 20, n_vendas),
    'preco_unitario': np.random.randint(30, 200, n_vendas)
})

df_vendas['valor_total'] = df_vendas['quantidade'] * df_vendas['preco_unitario']

# ==========================================
# TABELA 2: PRODUTOS (Tabela Dimensão)
# ==========================================
df_produtos = pd.DataFrame({
    'id_produto': range(1, 11),
    'produto': ['Camiseta', 'Calça Jeans', 'Tênis', 'Boné', 'Moletom',
                'Bermuda', 'Jaqueta', 'Regata', 'Meia', 'Cinto'],
    'categoria': np.random.choice(['Vestuário', 'Calçados', 'Acessórios'], 10),
    'custo_unitario': np.random.randint(15, 100, 10),
    'fornecedor': np.random.choice(['Fornecedor A', 'Fornecedor B', 'Fornecedor C'], 10)
})

# ==========================================
# TABELA 3: VENDEDORES (Tabela Dimensão)
# ==========================================
df_vendedores = pd.DataFrame({
    'id_vendedor': range(1, 6),
    'vendedor': ['Ana', 'Bruno', 'Carla', 'Daniel', 'Elisa'],
    'regiao': ['Sul', 'Sudeste', 'Nordeste', 'Norte', 'Centro-Oeste'],
    'data_admissao': ['10/01/2020', '15/03/2021', '20/02/2019', '05/07/2022', '12/11/2018']
})

# ==========================================
# TABELA 4: CLIENTES (Tabela Dimensão)
# ==========================================
df_clientes = pd.DataFrame({
    'id_cliente': range(1, 101),
    'cliente': [f'Cliente_{i}' for i in range(1, 101)],
    'cidade': np.random.choice(['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Porto Alegre', 'Brasília'], 100),
    'segmento': np.random.choice(['Varejo', 'Atacado', 'Governo'], 100)
})

# ==========================================
# SALVAR CSVs (sep=';', decimal=',', encoding='latin1')
# ==========================================
df_vendas.to_csv(PASTA_ATUAL / 'vendas.csv', index=False, sep=';', decimal=',', encoding='latin1')
df_produtos.to_csv(PASTA_ATUAL / 'produtos.csv', index=False, sep=';', decimal=',', encoding='latin1')
df_vendedores.to_csv(PASTA_ATUAL / 'vendedores.csv', index=False, sep=';', decimal=',', encoding='latin1')
df_clientes.to_csv(PASTA_ATUAL / 'clientes.csv', index=False, sep=';', decimal=',', encoding='latin1')

print("Datasets criados com sucesso!")
print(f"  - vendas.csv: {len(df_vendas)} linhas (tabela fato)")
print(f"  - produtos.csv: {len(df_produtos)} linhas (dimensão)")
print(f"  - vendedores.csv: {len(df_vendedores)} linhas (dimensão)")
print(f"  - clientes.csv: {len(df_clientes)} linhas (dimensão)")
print("\nRelacionamentos:")
print("  - vendas.id_produto → produtos.id_produto")
print("  - vendas.id_vendedor → vendedores.id_vendedor")
print("  - vendas.id_cliente → clientes.id_cliente")