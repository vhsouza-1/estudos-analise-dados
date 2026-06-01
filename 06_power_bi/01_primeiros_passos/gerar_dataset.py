"""
Script: gerar_dataset.py
Aula: 01 - Primeiros Passos no Power BI
Objetivo: Gerar dataset simples de vendas para primeiro contato com Power BI
Data: 01/06/2026
"""

import pandas as pd
import numpy as np
from pathlib import Path

PASTA_ATUAL = Path(__file__).parent
np.random.seed(42)

# Dataset simples de vendas
n = 200
df = pd.DataFrame({
    'data': pd.date_range('2024-01-01', periods=n, freq='D').strftime('%d/%m/%Y'),
    'produto': np.random.choice(['Camiseta', 'Calça', 'Tênis', 'Boné', 'Moletom'], n),
    'categoria': np.random.choice(['Vestuário', 'Calçados', 'Acessórios'], n),
    'vendas': np.random.randint(100, 5000, n),
    'quantidade': np.random.randint(1, 20, n),
    'vendedor': np.random.choice(['Ana', 'Bruno', 'Carla', 'Daniel', 'Elisa'], n),
    'regiao': np.random.choice(['Norte', 'Sul', 'Leste', 'Oeste', 'Centro-Oeste'], n)
})

# Calcular valor total
df['valor_total'] = df['vendas'] * df['quantidade']

df.to_csv(PASTA_ATUAL / 'vendas.csv', index=False, encoding='latin1', sep=';', decimal=',')

print(f"Dataset criado com {len(df)} linhas")
print(f"Arquivo salvo em: {PASTA_ATUAL / 'vendas.csv'}")
print("\nColunas disponíveis:")
print(df.columns.tolist())