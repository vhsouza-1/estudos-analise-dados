"""
Script: gerar_dataset.py
Aula: 02 - PROCV e XLOOKUP (Excel)
Objetivo: Gerar dois datasets para exercícios de busca e junção de tabelas
"""

import pandas as pd
import numpy as np
from pathlib import Path

PASTA_ATUAL = Path(__file__).parent
np.random.seed(42)

# ==========================================
# DATASET 1: VENDAS (tabela principal)
# ==========================================
n = 200
df_vendas = pd.DataFrame({
    'id_venda': range(1, n+1),
    'id_produto': np.random.randint(1, 11, n),
    'quantidade': np.random.randint(1, 10, n),
    'data_venda': pd.date_range('2024-01-01', periods=n, freq='D').strftime('%d/%m/%Y'),
    'vendedor': np.random.choice(['Ana', 'Bruno', 'Carla', 'Daniel', 'Elisa'], n)
})

# ==========================================
# DATASET 2: PRODUTOS (tabela de consulta)
# ==========================================
df_produtos = pd.DataFrame({
    'id_produto': range(1, 11),
    'nome_produto': ['Camiseta', 'Calça Jeans', 'Tênis', 'Boné', 'Moletom',
                     'Bermuda', 'Jaqueta', 'Regata', 'Meia', 'Cinto'],
    'categoria': np.random.choice(['Vestuário', 'Calçados', 'Acessórios'], 10),
    'preco_unitario': np.random.randint(30, 200, 10),
    'custo_unitario': np.random.randint(15, 100, 10)
})

# ==========================================
# DATASET 3: VENDEDORES (outra tabela de consulta)
# ==========================================
df_vendedores = pd.DataFrame({
    'vendedor': ['Ana', 'Bruno', 'Carla', 'Daniel', 'Elisa'],
    'regiao': ['Sul', 'Sudeste', 'Nordeste', 'Norte', 'Centro-Oeste'],
    'meta_mensal': [5000, 6000, 4500, 5500, 7000],
    'data_admissao': ['10/01/2020', '15/03/2021', '20/02/2019', '05/07/2022', '12/11/2018']
})

# Salvar CSVs (com vírgula, encoding latin1)
df_vendas.to_csv(PASTA_ATUAL / 'vendas.csv', index=False, encoding='latin1', sep=';', decimal=',')
df_produtos.to_csv(PASTA_ATUAL / 'produtos.csv', index=False, encoding='latin1', sep=';', decimal=',')
df_vendedores.to_csv(PASTA_ATUAL / 'vendedores.csv', index=False, encoding='latin1', sep=';', decimal=',')

print("Datasets criados com sucesso!")
print(f"  - vendas.csv: {len(df_vendas)} linhas")
print(f"  - produtos.csv: {len(df_produtos)} linhas")
print(f"  - vendedores.csv: {len(df_vendedores)} linhas")