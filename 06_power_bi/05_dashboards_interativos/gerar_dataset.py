"""
Script: gerar_dataset.py
Aula: 05 - Dashboards Interativos
Objetivo: Gerar dataset de vendas para criar dashboards interativos
"""

import pandas as pd
import numpy as np
from pathlib import Path

PASTA_ATUAL = Path(__file__).parent
np.random.seed(42)

# ==========================================
# TABELA 1: VENDAS (Tabela Fato)
# ==========================================
n_vendas = 2000

df_vendas = pd.DataFrame({
    'id_venda': range(1, n_vendas + 1),
    'id_produto': np.random.randint(1, 11, n_vendas),
    'id_vendedor': np.random.randint(1, 6, n_vendas),
    'data': pd.date_range('2023-01-01', periods=n_vendas, freq='D').strftime('%d/%m/%Y'),
    'quantidade': np.random.randint(1, 20, n_vendas),
    'preco_unitario': np.random.randint(30, 200, n_vendas)
})

df_vendas['valor_total'] = df_vendas['quantidade'] * df_vendas['preco_unitario']
df_vendas['custo'] = df_vendas['quantidade'] * np.random.randint(15, 100, n_vendas)
df_vendas['lucro'] = df_vendas['valor_total'] - df_vendas['custo']

# ==========================================
# TABELA 2: PRODUTOS (Dimensão)
# ==========================================
df_produtos = pd.DataFrame({
    'id_produto': range(1, 11),
    'produto': ['Camiseta', 'Calça Jeans', 'Tênis', 'Boné', 'Moletom',
                'Bermuda', 'Jaqueta', 'Regata', 'Meia', 'Cinto'],
    'categoria': np.random.choice(['Vestuário', 'Calçados', 'Acessórios'], 10)
})

# ==========================================
# TABELA 3: VENDEDORES (Dimensão)
# ==========================================
df_vendedores = pd.DataFrame({
    'id_vendedor': range(1, 6),
    'vendedor': ['Ana', 'Bruno', 'Carla', 'Daniel', 'Elisa'],
    'regiao': ['Sul', 'Sudeste', 'Nordeste', 'Norte', 'Centro-Oeste']
})

# ==========================================
# TABELA 4: CALENDÁRIO
# ==========================================
df_calendario = pd.DataFrame({
    'data': pd.date_range('2023-01-01', '2028-12-31', freq='D'),
    'ano': pd.date_range('2023-01-01', '2028-12-31', freq='D').year,
    'mes': pd.date_range('2023-01-01', '2028-12-31', freq='D').month,
    'mes_nome': pd.date_range('2023-01-01', '2028-12-31', freq='D').strftime('%b'),
    'trimestre': pd.date_range('2023-01-01', '2028-12-31', freq='D').quarter
})
df_calendario['data_str'] = df_calendario['data'].dt.strftime('%d/%m/%Y')

# ==========================================
# SALVAR CSVs
# ==========================================
df_vendas.to_csv(PASTA_ATUAL / 'vendas.csv', index=False, sep=';', decimal=',', encoding='latin1')
df_produtos.to_csv(PASTA_ATUAL / 'produtos.csv', index=False, sep=';', decimal=',', encoding='latin1')
df_vendedores.to_csv(PASTA_ATUAL / 'vendedores.csv', index=False, sep=';', decimal=',', encoding='latin1')
df_calendario[['data_str', 'ano', 'mes', 'mes_nome', 'trimestre']].to_csv(
    PASTA_ATUAL / 'calendario.csv', index=False, sep=';', decimal=',', encoding='latin1'
)

print("Datasets criados com sucesso!")