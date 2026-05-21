"""
Script: setup.py
Projeto: 03_analise_dados_enem_2019
Objetivo: Gerar estrutura de pastas para o projeto
Autor: vhsouza
Data: 21/05/2026
"""

from pathlib import Path

PROJECT_ROOT = Path(__file__).parent

pastas = [
    PROJECT_ROOT / '01_scripts',
    PROJECT_ROOT / '02_data/01_raw',
    PROJECT_ROOT / '02_data/02_processed',
    PROJECT_ROOT / '03_output'
]

for pasta in pastas:
    pasta.mkdir(parents=True, exist_ok=True)
