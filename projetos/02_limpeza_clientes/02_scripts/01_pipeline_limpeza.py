"""
Script: 01_pipeline_limpeza.py
Projeto: 02_limpeza_clientes
Objetivo: Aplicar pipeline completo de limpeza no dataset de clientes
Autor: [Seu nome]
Data: 11/05/2026
"""

import pandas as pd
import numpy as np
import re
from pathlib import Path

# ==========================================
# CONFIGURAÇÃO INICIAL
# ==========================================

SCRIPT_DIR = Path(__file__).parent
PROJECT_DIR = SCRIPT_DIR.parent

RAW_DIR = PROJECT_DIR / '01_data' / '01_raw'
PROCESSED_DIR = PROJECT_DIR / '01_data' / '02_processed'
REPORTS_DIR = PROJECT_DIR / '03_reports'
IMAGES_DIR = REPORTS_DIR / '01_imagens'
DOCS_DIR = PROJECT_DIR / '04_docs'

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
IMAGES_DIR.mkdir(parents=True, exist_ok=True)
DOCS_DIR.mkdir(parents=True, exist_ok=True)

df_sujo = pd.read_csv(RAW_DIR / 'clientes_raw.csv')
print(f"Shape inicial: {df_sujo.shape}")

#############################################
# ETAPA 0: EXPLORAÇÃO INICIAL
#############################################

# Primeiras linhas do df_sujo
print(f'Primeiras linhas do df_sujo:')
print(df_sujo.head().to_string())

# Informações gerais do df_sujo
print(f'\nInformações gerais do df_sujo:')
print(df_sujo.info())

# Descrição das colunas numéricas
print(f'\nDescrição das colunas numéricas:')
print(df_sujo.describe())

# quantidade de nulos por coluna
print(f'\nQuantidade de nulos por coluna:')
print(df_sujo.isna().sum())

# quantidade de duplicatas
print(f'\nQuantidade de duplicatas: {df_sujo.duplicated().sum()}')

print('\n#################################\n')

#############################################
# ETAPA 1: TRATAMENTO DE VALORES NULOS
#############################################

df = df_sujo.copy()

# 1.1 Nulos de email, preencher com desconhecido@email.com:
df['email'] = df['email'].fillna('desconhecido@email.com')

# 1.2 Nulos de telefone, preencher com 00000000000:
df['telefone'] = df['telefone'].fillna('00000000000')

# 1.3 Nulos de data_nascimento, sem nulos.

# 1.4 Nulos de data_cadastro, sem nulos.

# 1.5 Nulos de renda, preencher com a mediana:
df['renda'] = df['renda'].fillna(df['renda'].median())

# 1.6 Nulos de categoria, preencher com "Não informado":
df['categoria'] = df['categoria'].fillna('Não informado')

# 1.7 Nulos de compra, preencher com 0
df['compras'] = df['compras'].fillna(0)

# 1.8 Verificar se ainda existe, nulos:
# print(df.isna().sum().sum()) # 0

#############################################
# ETAPA 2: DUPLICATAS E INCONSISTÊNCIAS
#############################################



# 2.1 Remover linhas completamente duplicadas

# print(df.duplicated().sum()) # 5
df = df.drop_duplicates().reset_index(drop=True)
# print(df.duplicated().sum()) # 0

# 2.2 Verificar duplicatas de id_cliente
# print(df['id_cliente'].is_unique) # True, drop_duplicates() resolveu.

# 2.3 Padronizar nomes, strip + title
df['nome'] = df['nome'].str.strip().str.title()

# 2.4 Padronizar categoria

# print(df['categoria'].nunique()) # 22
df['categoria'] = df['categoria'].str.strip().str.lower()
# print(df['categoria'].nunique()) # 12 - caiu em 10 o número de categorias únicas.

# 2.5 Mapear sinônimos de categoria

# print(df['categoria'].unique().tolist())
# ['ouro', 'básico', 'gold', 'platinum', 'basico', 'premium', 'platina', 'basic', 'não informado', 'outro', 'premio', 'diamond']

categorias_map = {
    'ouro': 'Gold',
    'gold': 'Gold',
    'básico': 'Basic',
    'basico': 'Basic',
    'basic': 'Basic',
    'platinum': 'Platinum',
    'platina': 'Platinum',
    'premium': 'Premium',
    'premio': 'Premium',
    'diamond': 'Diamond',
    'outro': 'Outros'
}

df['categoria'] = df['categoria'].replace(categorias_map).str.title()

# print(df['categoria'].nunique()) # 7
# print(df['categoria'].unique().tolist())
# ['Gold', 'Basic', 'Platinum', 'Premium', 'Não Informado', 'Outros', 'Diamond']

#############################################
# ETAPA 3: LIMPEZA COM REGEX
#############################################

# 3.1 Limpeza de emails # Problemas: sem @, sem .com, espaços

df['email'] = df['email'].str.strip().str.lower()

mask_email = df['email'].str.contains('@email.com')

print(df['email'][~mask_email])




# TODO: Crie uma função ou regex para limpar emails
# TODO: Aplique na coluna 'email'

# 3.2 Limpeza de telefones
# Problemas: formatos diferentes, letras
# TODO: Extraia apenas dígitos usando regex (r'\d+')
# TODO: Padronize para formato (XX) XXXXX-XXXX (11 dígitos) ou (XX) XXXX-XXXX (10 dígitos)

# ==========================================
# ETAPA 4: LIMPEZA DE DATAS
# ==========================================



# 4.1 Converter para datetime
# TODO: Converta 'data_nascimento' e 'data_cadastro' com errors='coerce'
# Dica: use dayfirst=True para formato brasileiro

# 4.2 Verificar quantos NaT
# TODO: Mostre quantidade de NaT por coluna

# 4.3 Tratar datas futuras
# TODO: Defina data_atual = pd.Timestamp.now().normalize()
# TODO: Substitua datas futuras por NaT (use .mask())

# 4.4 Tratar datas muito antigas (nascimento < 1900)
# TODO: Substitua datas anteriores a '1900-01-01' por NaT

# 4.5 Normalizar (remover horas)
# TODO: Aplique .dt.normalize()

# 4.6 Preencher nulos restantes
# TODO: Decida se remove ou preenche com data padrão

# ==========================================
# ETAPA 5: TRANSFORMAÇÕES E PADRONIZAÇÃO
# ==========================================



# 5.1 Criar renda_anual
# TODO: Crie coluna 'renda_anual' (renda * 12)

# 5.2 Normalizar renda
# TODO: Crie 'renda_normalizada' usando min-max

# 5.3 Calcular idade
# TODO: Calcule idade a partir de data_nascimento
# Dica: (data_atual - data_nascimento).dt.days // 365

# 5.4 Criar score_cliente
# Score = (compras_normalizado * 0.4) + (renda_normalizada * 0.4) + (idade_normalizada * 0.2)
# TODO: Normalize compras, renda e idade
# TODO: Calcule o score

# 5.5 Criar faixa_renda com pd.cut
# TODO: Use bins=[0, 3000, 8000, float('inf')] e labels=['Baixa', 'Média', 'Alta']

# 5.6 Criar categoria_cliente com np.where baseado no score
# TODO: Score > 0.7 → 'Premium'
# TODO: Score > 0.4 → 'Regular'
# TODO: Score <= 0.4 → 'Bronze'

# ==========================================
# ETAPA 6: VALIDAÇÃO FINAL
# ==========================================



# TODO: Verifique se não há mais nulos
# TODO: Verifique se não há mais duplicatas
# TODO: Mostre shape final
# TODO: Mostre df.head()

# ==========================================
# EXPORTAÇÃO
# ==========================================



# TODO: Salvar dataset limpo em CSV
# TODO: Gerar relatório em TXT com as estatísticas finais
# TODO: (Opcional) Gerar gráficos de comparação

