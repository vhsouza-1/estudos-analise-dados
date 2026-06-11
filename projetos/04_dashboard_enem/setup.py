"""
Script: setup.py
Projeto: 04_dashboard_enem_2019
Objetivo: Gerar estrutura de pastas para o projeto e importar os dados tratados do projeto 03_analise_dados_enem
Autor: vhsouza
Data: 10/06/2026
"""
# Criar estrutura de pastas
from pathlib import Path

import pandas as pd

PROJECT_ROOT = Path(__file__).parent

pastas = [
    PROJECT_ROOT / '01_data',
    PROJECT_ROOT / '02_dashboard',
    PROJECT_ROOT / '03_documentacao',
]

for pasta in pastas:
    pasta.mkdir(parents=True, exist_ok=True)

# Pegar DataSet do projeto 03_analise_dados_enem_2019
df_caminho = PROJECT_ROOT / '../03_analise_dados_enem_2019/02_data/02_processed/enem2019_basico.csv'

df = pd.read_csv(df_caminho)

df.to_csv(PROJECT_ROOT / '01_data' / 'enem2019_basico.csv', index=False, encoding='latin1', sep=';', decimal=',')