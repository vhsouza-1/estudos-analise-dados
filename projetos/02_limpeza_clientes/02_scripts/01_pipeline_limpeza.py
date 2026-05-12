"""
Script: 01_pipeline_limpeza.py
Projeto: 02_limpeza_clientes
Objetivo: Aplicar pipeline completo de limpeza no dataset de clientes
Autor: vhsouza
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

df = df_sujo.copy()

#############################################
# ETAPA 1: PADRONIZAR FORMATOS
#############################################

########## 1.1 Padronizar nomes, strip + title ##########
df['nome'] = df['nome'].str.strip().str.title()

########## 1.2 Padronizar categoria ##########

# print(df['categoria'].nunique()) # 22
df['categoria'] = df['categoria'].str.strip().str.lower()
# print(df['categoria'].nunique()) # 12 - caiu em 10 o número de categorias únicas.

#  Mapear sinônimos de categoria

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

########## 1.3 Padronizar emails ##########

df['email'] = df['email'].str.strip().str.lower()

# Tratar emails sem arroba:

mascara_sem_arroba = (~df['email'].str.contains('@')) & (df['email'].notna())

emails_sem_arroba = df.loc[mascara_sem_arroba, 'email']

for idx, email in emails_sem_arroba.items():
    dominio = email[-9:]
    usuario = email.replace('email.com', '')
    novo_email = usuario+'@'+dominio
    df.loc[idx, 'email'] = novo_email

# Tratar emails sem .com

mascara_sem_pontocom = (~df['email'].str.contains('.com')) & (df['email'].notna())

emails_sem_pontocom = df.loc[mascara_sem_pontocom, 'email']

# dominios_errados = [emails.split('@')[1] for emails in emails_sem_pontocom]
# print(pd.Series(dominios_errados).unique())
# ['email.c', 'empresa', 'email', ''] # Tipos de erro

mascara_erro1 = mascara_sem_pontocom & df['email'].str.contains('email.c', regex=False)
mascara_erro2 = mascara_sem_pontocom & df['email'].str.contains('empresa')
mascara_erro3 = mascara_sem_pontocom & df['email'].str.contains('email') & ~mascara_erro1
mascara_erro4 = mascara_sem_pontocom & ~(mascara_erro1|mascara_erro2|mascara_erro3)

for idx, email in df.loc[mascara_erro1, 'email'].items():
    novo_email = email.replace('email.c', 'email.com')
    df.loc[idx, 'email'] = novo_email

for idx, email in df.loc[mascara_erro2, 'email'].items():
    novo_email = email.replace('empresa', 'empresa.com')
    df.loc[idx, 'email'] = novo_email

for idx, email in df.loc[mascara_erro3, 'email'].items():
    novo_email = email.replace('email', 'email.com')
    df.loc[idx, 'email'] = novo_email

for idx, email in df.loc[mascara_erro4, 'email'].items():
    novo_email = email + 'email.com'
    df.loc[idx, 'email'] = novo_email

# Nova verificação:
# print(df['email'][~df['email'].str.contains('@')].count()) # 0

# dominios = [email.split('@')[1] for email in df['email']]
# print(pd.Series(dominios).unique()) # ['email.com', '.com', 'email.com.br', 'empresa.com']

# Tratar emails no formato "@.com"

mascara_erro5 = df['email'].str.contains('@.com', regex=False)

for idx, email in df.loc[mascara_erro5, 'email'].items():
    novo_email = email.replace('@.com', '@email.com')
    df.loc[idx, 'email'] = novo_email

########## 1.4 Padronizar Telefones ##########

# 3.2 Limpeza de telefones

df['telefone'] = df['telefone'].str.strip()

# Limpar todos os caracteres adicionais (tudo que não é número)

regex_telefone = r'\D'
df['telefone'] = df['telefone'].replace(regex_telefone, '', regex=True)

# Substituir telefones com quantidade de números inválida por NaN:
mascara_tel = ((df['telefone'].str.len() > 11) | (df['telefone'].str.len() < 10)) & (df['telefone'].notna())
df.loc[mascara_tel, 'telefone'] = np.nan

# Padronizar os demais telefones não nulos:
# Formato (XX) XXXXX-XXXX (11 dígitos) ou (XX) XXXX-XXXX (10 dígitos)

mascara_tel_notna = df['telefone'].notna()

telefones_nao_nulos = df.loc[mascara_tel_notna, 'telefone']

for idx, telefone in telefones_nao_nulos.items():

    if len(telefone) == 10:
        ddd = telefone[:2]
        tel_part1 = telefone[2:6]
        tel_part2 = telefone[6:10]
        novo_telefone = f'({ddd}) {tel_part1}-{tel_part2}'
        df.loc[idx, 'telefone'] = novo_telefone

    if len(telefone) == 11:
        ddd = telefone[:2]
        tel_part1 = telefone[2:7]
        tel_part2 = telefone[7:11]
        novo_telefone = f'({ddd}) {tel_part1}-{tel_part2}'
        df.loc[idx, 'telefone'] = novo_telefone

########## 1.5 Padronizar Datas ##########

df['data_nascimento'] = df['data_nascimento'].str.strip()
df['data_cadastro'] = df['data_cadastro'].str.strip()

# Verificar quantidade de nulos:
# print(df['data_nascimento'].isna().sum()) # 0
# print(df['data_cadastro'].isna().sum())   # 0

# Converter para datetime com format='mixed'
df['data_nascimento'] = pd.to_datetime(df['data_nascimento'], format='mixed', errors='coerce')
df['data_cadastro'] = pd.to_datetime(df['data_cadastro'], format='mixed', errors='coerce')

# Quantidade de datas inválidas identificadas após conversão:
# print(df['data_nascimento'].isna().sum()) # 16
# print(df['data_cadastro'].isna().sum())   # 9

# Substituir datas futuras por NaT:
data_atual = pd.Timestamp.now().normalize()
df['data_nascimento'] = df['data_nascimento'].mask(df['data_nascimento'] > data_atual, pd.NaT)
df['data_cadastro'] = df['data_cadastro'].mask(df['data_cadastro'] > data_atual, pd.NaT)

# Quantidade de datas inválidas identificadas após tratar datas futuras:
# print(df['data_nascimento'].isna().sum()) # 29
# print(df['data_cadastro'].isna().sum())   # 16

# Substituir datas muito antigas por NaT:
data_antiga = pd.Timestamp('1900').normalize()
df['data_nascimento'] = df['data_nascimento'].mask(df['data_nascimento'] < data_antiga, pd.NaT)
df['data_cadastro'] = df['data_cadastro'].mask(df['data_cadastro'] < data_antiga, pd.NaT)

# Quantidade de datas inválidas identificadas após tratar datas futuras:
# print(df['data_nascimento'].isna().sum()) # 29
# print(df['data_cadastro'].isna().sum())   # 16

########## 1.6 Padronizar Renda ##########

# Verificar nulos na coluna renda
# print(df['renda'].isna().sum()) # 34

# Tratar valores menores ou iguais a zero
mascara_renda = (df['renda'] <= 0) & (df['renda'].notna())
df.loc[mascara_renda, 'renda'] = np.nan

# Substituir nulos por mediana
df['renda'] = df['renda'].fillna(df['renda'].median())

# Verificar nulos na coluna renda após tratamento
# print(df['renda'].isna().sum()) # 0

########## 1.7 Padronizar Compras ##########

# Verificar nulos na coluna Compras
# print(df['compras'].isna().sum()) # 65

# Tratar valores menores que zero
mascara_compras = df['compras'] < 0
df.loc[mascara_compras, 'compras'] = np.nan

# Verificar nulos na coluna Compras após tratar valores menores que zero
# print(df['compras'].isna().sum()) # 137

# Substituir nulos pela mediana
df['compras'] = df['compras'].fillna(df['compras'].median())

# Transformar compras em int
df['compras'] = df['compras'].astype(int)

# Verificar nulos na coluna Compras após tratamento
# print(df['compras'].isna().sum()) # 0

#############################################
# ETAPA 2: NULOS E DUPLICATAS
#############################################

# 2.1 Remover linhas completamente duplicadas
# print(df.duplicated().sum()) # 5
df = df.drop_duplicates().reset_index(drop=True)
# print(df.duplicated().sum()) # 0

# 2.2 Verificar duplicatas de id_cliente
# print(df['id_cliente'].is_unique) # True

# 2.3 Nulos de email, preencher com desconhecido@email.com:
df['email'] = df['email'].fillna('desconhecido@email.com')

# 2.4 Nulos de telefone, preencher com (00) 00000-0000:
df['telefone'] = df['telefone'].fillna('(00) 00000-0000')

# 2.5 Nulos de data_nascimento, preencher com a mediana.
df['data_nascimento'] = df['data_nascimento'].fillna(df['data_nascimento'].median())

# 2.6 Nulos de data_cadastro, preencher com a mediana.
df['data_cadastro'] = df['data_cadastro'].fillna(df['data_cadastro'].median())

# 2.7 Nulos de categoria, preencher com "Não informado":
df['categoria'] = df['categoria'].fillna('Não informado')

# Verificar se ainda existe, nulos:
# print(df.isna().sum().sum()) # 0

#############################################
# ETAPA 3: TRANSFORMAÇÕES E PADRONIZAÇÃO
#############################################

# 3.1 Criar renda_anual
df['renda_anual'] = df['renda'] * 12

# 3.2 Normalizar renda
def normalizar(coluna):
    return (coluna - coluna.min())/(coluna.max() - coluna.min())

df['renda_norm'] = normalizar(df['renda'])

# 3.3 Calcular idade
df['idade'] = (data_atual - df['data_nascimento']).dt.days//365

# 3.4 Criar score_cliente: (compras_normalizado * 0.4) + (renda_normalizada * 0.4) + (idade_normalizada * 0.2)

df['compras_norm'] = normalizar(df['compras'])
df['idade_norm'] = normalizar(df['idade'])

df['score_cliente'] = (df['compras_norm'] * 0.4 + df['renda_norm'] * 0.4 + df['idade_norm'] * 0.2).round(2)


# 3.5 Criar faixa_renda com pd.cut
faixas_renda = [0, 3000, 8000, float('inf')]
rotulos_renda = ['Baixa', 'Média', 'Alta']
df['faixa_renda'] = pd.cut(df['renda'], bins=faixas_renda, labels=rotulos_renda)


# 3.6 Criar categoria_cliente baseado no score

def categorizar_score(score):
    if score > 0.7:
        return 'Premium'
    elif score > 0.4:
        return 'Regular'
    elif score <= 0.4:
        return 'Bronze'
    else:
        return None

df['categoria_cliente'] = df['score_cliente'].apply(categorizar_score)

# ==========================================
# ETAPA 4: VERIFICAÇÃO FINAL
# ==========================================

# Dropar colunas _norm usadas para análises
df = df.drop(['renda_norm', 'idade_norm', 'compras_norm'], axis=1)

# Verificar existência de nulos e duplicatas:
# print(df.isna().sum().sum()) # 0
# print(df.duplicated().sum()) # 0

print(f'Shape Final: {df.shape}')

print(df.head().to_string())

# ==========================================
# EXPORTAÇÃO
# ==========================================

df.to_csv(PROCESSED_DIR / 'cliente_limpo.csv', index=False)

