"""
Script: gerar_dataset.py
Aula: 05 - Gráficos no Excel
Objetivo: Gerar dataset de vendas para exercícios de criação de gráficos
Data: 29/05/2026
"""

import pandas as pd
import numpy as np
from pathlib import Path

PASTA_ATUAL = Path(__file__).parent
np.random.seed(42)

# ==========================================
# DATASET 1: VENDAS POR MÊS (série temporal)
# ==========================================

meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
vendas_2023 = np.random.randint(8000, 15000, 12)
vendas_2024 = vendas_2023 + np.random.randint(-1000, 3000, 12)

# Garantir que não fique negativo
vendas_2023 = np.maximum(vendas_2023, 0)
vendas_2024 = np.maximum(vendas_2024, 0)

df_mensal = pd.DataFrame({
    'mes': meses,
    '2023': vendas_2023,
    '2024': vendas_2024
})

# ==========================================
# DATASET 2: VENDAS POR CATEGORIA (para barras/pizza)
# ==========================================
categorias = ['Eletrônicos', 'Vestuário', 'Alimentos', 'Móveis', 'Livros']
valores_categoria = [45200, 38900, 23400, 18700, 9800]

df_categoria = pd.DataFrame({
    'categoria': categorias,
    'vendas': valores_categoria
})

# ==========================================
# DATASET 3: RELAÇÃO MARKETING X VENDAS (dispersão)
# ==========================================
marketing = np.random.randint(1000, 10000, 50)
vendas_disp = marketing * 1.5 + np.random.normal(0, 2000, 50)
vendas_disp = np.maximum(vendas_disp, 0).astype(int)


df_dispersao = pd.DataFrame({
    'investimento_marketing': marketing,
    'vendas': vendas_disp
})

mediana = df_dispersao[df_dispersao['vendas'] != 0]['vendas'].median()
df_dispersao['vendas'] = df_dispersao['vendas'].replace(0, mediana)

# ==========================================
# DATASET 4: COMPOSIÇÃO DE VENDAS (empilhado)
# ==========================================
produtos = ['Camiseta', 'Calça', 'Tênis', 'Boné', 'Moletom']
vendas_online = np.random.randint(500, 3000, 5)
vendas_loja = np.random.randint(200, 2500, 5)

df_composicao = pd.DataFrame({
    'produto': produtos,
    'online': vendas_online,
    'loja_fisica': vendas_loja
})

# Salvar CSVs
df_mensal.to_csv(PASTA_ATUAL / 'vendas_mensal.csv', index=False, encoding='latin1', sep=';', decimal=',')
df_categoria.to_csv(PASTA_ATUAL / 'vendas_categoria.csv', index=False, encoding='latin1', sep=';', decimal=',')
df_dispersao.to_csv(PASTA_ATUAL / 'marketing_vendas.csv', index=False, encoding='latin1', sep=';', decimal=',')
df_composicao.to_csv(PASTA_ATUAL / 'vendas_composicao.csv', index=False, encoding='latin1', sep=';', decimal=',')

print("Datasets criados com sucesso!")
print(f"  - vendas_mensal.csv: {len(df_mensal)} linhas (12 meses)")
print(f"  - vendas_categoria.csv: {len(df_categoria)} linhas (5 categorias)")
print(f"  - marketing_vendas.csv: {len(df_dispersao)} linhas")
print(f"  - vendas_composicao.csv: {len(df_composicao)} linhas")