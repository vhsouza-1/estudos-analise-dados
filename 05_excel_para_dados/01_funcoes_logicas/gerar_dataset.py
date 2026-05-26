"""
Script: gerar_dataset.py
Aula: 01 - Funções Lógicas (Excel)
Objetivo: Gerar dataset de vendas para exercícios de SE, E, OU, SEERRO
"""

import pandas as pd
import numpy as np
from pathlib import Path

# Garantir que está na pasta correta
PASTA_ATUAL = Path(__file__).parent

np.random.seed(42)

# Criar dataset
n = 200
df = pd.DataFrame({
    'vendedor': np.random.choice(['Ana', 'Bruno', 'Carla', 'Daniel', 'Elisa'], n),
    'produto': np.random.choice(['Camiseta', 'Calça', 'Tênis', 'Boné', 'Moletom'], n),
    'vendas': np.random.randint(100, 5000, n).astype(object),
    'meta': 2000,
    'custo': np.random.randint(50, 3000, n).astype(object),
    'regiao': np.random.choice(['Norte', 'Sul', 'Leste', 'Oeste'], n)
})

# Adicionar alguns valores de erro propositais (para treinar SEERRO)
df.loc[5, 'vendas'] = 'erro'
df.loc[12, 'custo'] = 'N/A'
df.loc[18, 'vendas'] = '#DIV/0!'

# Salvar como CSV (padrão Brasil: ponto e vírgula)
df.to_csv(PASTA_ATUAL / 'dataset.csv', index=False, encoding='latin1', sep=';', decimal=',')

print(f"Dataset criado com {len(df)} linhas")
print(f"Arquivo salvo em: {PASTA_ATUAL / 'dataset.csv'}")