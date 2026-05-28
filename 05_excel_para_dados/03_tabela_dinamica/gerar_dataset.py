"""
Script: gerar_dataset.py
Aula: 03 - Tabela Dinâmica (Excel)
Objetivo: Gerar dataset de vendas para exercícios de tabela dinâmica
Data: 28/05/2026
"""

import pandas as pd
import numpy as np
from pathlib import Path

PASTA_ATUAL = Path(__file__).parent
np.random.seed(42)

# ==========================================
# DATASET: VENDAS (para tabela dinâmica)
# ==========================================
n = 500

# Gerar dados
datas = pd.date_range('2024-01-01', '2024-12-31', freq='D')
datas_aleatorias = np.random.choice(datas, n)
datas_aleatorias = pd.Series(datas_aleatorias)

df = pd.DataFrame({
    'data': datas_aleatorias.dt.strftime('%d/%m/%Y'),
    'ano': datas_aleatorias.dt.year,
    'mes': datas_aleatorias.dt.month,
    'trimestre': datas_aleatorias.dt.quarter,
    'produto': np.random.choice(['Camiseta', 'Calça Jeans', 'Tênis', 'Boné', 'Moletom',
                                  'Bermuda', 'Jaqueta', 'Regata', 'Meia', 'Cinto'], n),
    'categoria': np.random.choice(['Vestuário', 'Calçados', 'Acessórios'], n),
    'vendedor': np.random.choice(['Ana', 'Bruno', 'Carla', 'Daniel', 'Elisa'], n),
    'regiao': np.random.choice(['Norte', 'Sul', 'Leste', 'Oeste', 'Centro-Oeste'], n),
    'quantidade': np.random.randint(1, 20, n),
    'preco_unitario': np.random.randint(30, 200, n),
})

# Calcular valor total
df['valor_total'] = df['quantidade'] * df['preco_unitario']

# Adicionar alguns registros com problemas (para exercício de tratamento)
df.loc[10, 'regiao'] = ''  # região vazia
df.loc[25, 'categoria'] = None  # categoria nula
df.loc[50, 'valor_total'] = -999  # valor negativo (possível erro)

# Salvar CSV
df.to_csv(PASTA_ATUAL / 'vendas.csv', index=False, encoding='latin1', sep=';', decimal=',')

print(f"Dataset criado com {len(df)} linhas")
print(f"Arquivo salvo em: {PASTA_ATUAL / 'vendas.csv'}")
print("\nColunas disponíveis:")
print(df.columns.tolist())