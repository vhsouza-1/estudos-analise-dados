"""
Script: gerar_dataset.py
Aula: 02 - Power Query (Transformando Dados)
Objetivo: Gerar dataset com problemas para treinar limpeza no Power Query
Data: 02/06/2026
"""

import pandas as pd
import numpy as np
from pathlib import Path

PASTA_ATUAL = Path(__file__).parent
np.random.seed(42)

# ==========================================
# DATASET SUJO (com problemas para limpar)
# ==========================================
n = 500

df = pd.DataFrame({
    'id': range(1, n + 1),
    'data': pd.date_range('2024-01-01', periods=n, freq='D').strftime('%d/%m/%Y'),
    'produto': np.random.choice(['Camiseta', 'Calça', 'Tênis', 'Boné', 'Moletom'], n),
    'categoria': np.random.choice(['Vestuário', 'Calçados', 'Acessórios'], n),
    'vendas': np.random.randint(100, 5000, n),
    'quantidade': np.random.randint(1, 20, n),
    'vendedor': np.random.choice(['Ana', 'Bruno', 'Carla', 'Daniel', 'Elisa'], n),
    'regiao': np.random.choice(['Norte', 'Sul', 'Leste', 'Oeste', 'Centro-Oeste'], n)
})

# Adicionar problemas propositais
df.loc[10, 'vendas'] = -999          # valor negativo (erro)
df.loc[25, 'quantidade'] = 0         # zero (possível erro)
df.loc[30, 'produto'] = ''           # vazio
df.loc[45, 'categoria'] = None       # nulo
df.loc[50, 'regiao'] = 'Suld'        # erro de digitação
df.loc[55, 'vendedor'] = '   Ana   ' # espaços extras
df.loc[60, 'produto'] = 'CAMISETA'   # maiúsculo (inconsistente)
df.loc[65, 'categoria'] = 'Vest'     # abreviação

# Calcular valor total
df['valor_total'] = df['vendas'] * df['quantidade']

# Salvar CSV (ponto e vírgula, vírgula decimal, encoding latin1)
df.to_csv(PASTA_ATUAL / 'vendas_sujo.csv', index=False, sep=';', decimal=',', encoding='latin1')

print(f"Dataset sujo criado com {len(df)} linhas")
print(f"Arquivo salvo em: {PASTA_ATUAL / 'vendas_sujo.csv'}")
print("\nProblemas inseridos:")
print("  - Linha 10: vendas = -999 (negativo)")
print("  - Linha 25: quantidade = 0")
print("  - Linha 30: produto vazio")
print("  - Linha 45: categoria nula")
print("  - Linha 50: regiao = 'Suld' (erro)")
print("  - Linha 55: vendedor com espaços extras")
print("  - Linha 60: produto 'CAMISETA' (maiúsculo)")
print("  - Linha 65: categoria 'Vest' (abreviação)")