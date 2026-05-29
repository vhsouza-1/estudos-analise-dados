"""
Script: gerar_dataset.py
Aula: 04 - Formatação Condicional (Excel)
Objetivo: Gerar dataset de vendas para exercícios de formatação condicional
Data: 29/05/2026
"""

import pandas as pd
import numpy as np
from pathlib import Path

PASTA_ATUAL = Path(__file__).parent
np.random.seed(42)

# ==========================================
# DATASET: VENDAS COM MÉTRICAS
# ==========================================
n = 100

df = pd.DataFrame({
    'vendedor': np.random.choice(['Ana', 'Bruno', 'Carla', 'Daniel', 'Elisa'], n),
    'produto': np.random.choice(['Camiseta', 'Calça Jeans', 'Tênis', 'Boné', 'Moletom'], n),
    'categoria': np.random.choice(['Vestuário', 'Calçados', 'Acessórios'], n),
    'vendas': np.random.randint(500, 5000, n),
    'meta': 2500,
    'percentual_meta': np.random.uniform(0.5, 1.5, n),
    'qtde_clientes': np.random.randint(10, 100, n),
    'ticket_medio': np.random.randint(50, 200, n),
    'avaliacao': np.random.choice([1, 2, 3, 4, 5], n, p=[0.05, 0.10, 0.20, 0.40, 0.25]),
})

# Calcular percentual_meta real a partir de vendas
df['percentual_meta'] = (df['vendas'] / df['meta']).round(2)

# Adicionar alguns outliers
df.loc[5, 'vendas'] = 15000  # outlier alto
df.loc[12, 'vendas'] = 50    # outlier baixo

# Salvar CSV
df.to_csv(PASTA_ATUAL / 'vendas_metricas.csv', index=False, encoding='latin1', sep=';', decimal=',')

print(f"Dataset criado com {len(df)} linhas")
print(f"Arquivo salvo em: {PASTA_ATUAL / 'vendas_metricas.csv'}")
print("\nColunas disponíveis:")
print(df.columns.tolist())
print(f"\nExemplo de dados:")
print(df.head(10).to_string())