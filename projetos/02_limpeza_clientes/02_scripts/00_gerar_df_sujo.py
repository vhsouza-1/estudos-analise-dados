"""
Script: 00_gerar_df_sujo.py
Projeto: 02_limpeza_clientes
Objetivo: Gerar dataset sujo de clientes para o projeto de limpeza
Autor: vhsouza
Data: 11/05/2026

Uso:
1. Execute este script uma vez
2. O arquivo será salvo em: ../01_data/01_raw/clientes_raw.csv
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
from pathlib import Path

# ==========================================
# CONFIGURAÇÕES
# ==========================================
N_CLIENTES = 200
DATA_ATUAL = pd.Timestamp.now().normalize()

# Nomes para gerar dados
NOMES = ['Ana', 'Bruno', 'Carla', 'Daniel', 'Eduarda', 'Felipe', 'Gabriela', 'Henrique', 'Isabela', 'João',
         'Karina', 'Lucas', 'Mariana', 'Natália', 'Otávio', 'Patrícia', 'Rafael', 'Silvia', 'Thiago', 'Úrsula',
         'Vanessa', 'Wagner', 'Xuxa', 'Yasmin', 'Zeca', 'Alberto', 'Beatriz', 'Carlos', 'Débora', 'Eduardo']

SOBRENOMES = ['Silva', 'Santos', 'Oliveira', 'Souza', 'Rodrigues', 'Ferreira', 'Alves', 'Pereira', 'Lima', 'Gomes',
              'Martins', 'Rocha', 'Ribeiro', 'Almeida', 'Barbosa', 'Carvalho', 'Dias', 'Castro', 'Campos', 'Freitas']


# ==========================================
# FUNÇÕES PARA GERAR DADOS SUJOS
# ==========================================

def gerar_nome_sujo():
    """Gera nomes com problemas: maiúsculas, minúsculas, espaços extras"""
    nome = random.choice(NOMES)
    sobrenome = random.choice(SOBRENOMES)
    nome_completo = f"{nome} {sobrenome}"

    problema = random.choice(['normal', 'maiusculo', 'minusculo', 'espacos', 'misturado'])
    if problema == 'maiusculo':
        return nome_completo.upper()
    elif problema == 'minusculo':
        return nome_completo.lower()
    elif problema == 'espacos':
        return f"  {nome_completo}  "
    elif problema == 'misturado':
        return nome_completo.title()
    return nome_completo


def gerar_email_sujo(nome_base):
    """Gera emails com problemas"""
    nome_limpo = nome_base.strip().lower().split()[0]

    problemas = [
        f"{nome_limpo}@email.com",
        f"{nome_limpo}@email",
        f"{nome_limpo}@.com",
        f"{nome_limpo}email.com",
        f"{nome_limpo}@email.com.br",
        f"{nome_limpo}@empresa",
        f"  {nome_limpo}@email.com  ",
        f"{nome_limpo}@",
        f"{nome_limpo}@email.c",
        f"",
    ]
    return random.choice(problemas)


def gerar_telefone_sujo():
    """Gera telefones com vários formatos"""
    ddd = random.randint(11, 99)
    parte1 = random.randint(1000, 9999)
    parte2 = random.randint(1000, 9999)
    parte1_longo = random.randint(10000, 99999)

    formatos = [
        f"({ddd}) {parte1_longo}-{parte2}",
        f"({ddd}){parte1_longo}-{parte2}",
        f"{ddd}{parte1_longo}{parte2}",
        f"{ddd} {parte1_longo} {parte2}",
        f"({ddd}) {parte1}-{parte2}",
        f"({ddd}){parte1}-{parte2}",
        f"11{parte1_longo}{parte2}",
        f"tel: {parte1_longo}-{parte2}",
        f"",
        np.nan,
    ]
    return random.choice(formatos)


def gerar_data_suja(data_base, prob_futura=0.05, prob_invalida=0.05):
    """Gera datas com problemas"""
    rand = random.random()

    if rand < prob_futura:
        dias_futuro = random.randint(1, 3650)
        data = DATA_ATUAL + timedelta(days=dias_futuro)
        return data.strftime('%Y-%m-%d')

    if rand < prob_futura + prob_invalida:
        ano = random.randint(1950, 2024)
        mes_invalido = random.choice([0, 13, 14, 15])
        return f"{ano}-{mes_invalido:02d}-{random.randint(1, 28):02d}"

    dias_offset = random.randint(-10000, 0)
    data = DATA_ATUAL + timedelta(days=dias_offset)

    formato = random.choice(['iso', 'br', 'br_barra', 'br_ponto'])
    if formato == 'iso':
        return data.strftime('%Y-%m-%d')
    elif formato == 'br':
        return data.strftime('%d/%m/%Y')
    elif formato == 'br_barra':
        return data.strftime('%d/%m/%y')
    else:
        return data.strftime('%d.%m.%Y')


def gerar_renda_suja():
    """Gera renda com valores negativos, nulos, outliers"""
    opcoes = [
        random.randint(1000, 15000),
        random.randint(-5000, -1),
        np.nan,
        random.randint(50000, 200000),
        0,
        random.randint(1, 500),
    ]
    return random.choice(opcoes)


def gerar_categoria_suja():
    """Gera categorias com sinônimos e variações"""
    categorias = [
        'basic', 'basico', 'básico', 'BASIC', 'Basico',
        'premium', 'PREMIUM', 'Premium', 'premio',
        'gold', 'GOLD', 'Gold', 'ouro',
        'platinum', 'PLATINUM', 'Platinum', 'platina',
        'diamond', 'DIAMOND', 'Diamond',
    ]

    if random.random() < 0.05:
        return 'outro'
    if random.random() < 0.03:
        return ''
    if random.random() < 0.02:
        return 'NA'

    return random.choice(categorias)


def gerar_compras_suja():
    """Gera quantidade de compras com nulos e zeros"""
    opcoes = [
        random.randint(0, 50),
        np.nan,
        -random.randint(1, 10),
    ]
    return random.choice(opcoes)


# ==========================================
# GERAR DATASET
# ==========================================

print("=" * 50)
print("GERANDO DATASET SUJO DE CLIENTES")
print("=" * 50)

clientes = []
for i in range(1, N_CLIENTES + 1):
    nome_base = gerar_nome_sujo()
    nome_limpo_temporario = nome_base.strip().split()[0] if isinstance(nome_base, str) else f"cliente_{i}"

    cliente = {
        'id_cliente': i,
        'nome': nome_base,
        'email': gerar_email_sujo(nome_limpo_temporario),
        'telefone': gerar_telefone_sujo(),
        'data_nascimento': gerar_data_suja(DATA_ATUAL, prob_futura=0.08, prob_invalida=0.07),
        'data_cadastro': gerar_data_suja(DATA_ATUAL, prob_futura=0.05, prob_invalida=0.03),
        'renda': gerar_renda_suja(),
        'categoria': gerar_categoria_suja(),
        'compras': gerar_compras_suja(),
    }
    clientes.append(cliente)

df_sujo = pd.DataFrame(clientes)

# Adicionar duplicatas
duplicados = df_sujo.sample(n=5, random_state=42).copy()
df_sujo = pd.concat([df_sujo, duplicados], ignore_index=True)

# Adicionar email repetido
if len(df_sujo) > 0:
    email_repetido = df_sujo.loc[df_sujo['email'].notna(), 'email'].iloc[0]
    cliente_repetido = {
        'id_cliente': N_CLIENTES + 6,
        'nome': 'Cliente Repetido',
        'email': email_repetido,
        'telefone': gerar_telefone_sujo(),
        'data_nascimento': gerar_data_suja(DATA_ATUAL),
        'data_cadastro': gerar_data_suja(DATA_ATUAL),
        'renda': gerar_renda_suja(),
        'categoria': gerar_categoria_suja(),
        'compras': gerar_compras_suja(),
    }
    df_sujo = pd.concat([df_sujo, pd.DataFrame([cliente_repetido])], ignore_index=True)

# ==========================================
# SALVAR DATASET
# ==========================================

# Definir caminhos (script está em 02_scripts/)
SCRIPT_DIR = Path(__file__).parent
PROJECT_DIR = SCRIPT_DIR.parent
RAW_DIR = PROJECT_DIR / '01_data' / '01_raw'

# Criar pasta se não existir
RAW_DIR.mkdir(parents=True, exist_ok=True)

# Salvar
arquivo_saida = RAW_DIR / 'clientes_raw.csv'
df_sujo.to_csv(arquivo_saida, index=False)

# ==========================================
# RELATÓRIO DO DATASET GERADO
# ==========================================

print(f"\n✅ Dataset salvo em: {arquivo_saida}")
print(f"Shape: {df_sujo.shape}")
print(f"Total de registros: {len(df_sujo)}")

print("\n" + "=" * 50)
print("PROBLEMAS INSERIDOS")
print("=" * 50)
print(f"Registros duplicados: {df_sujo.duplicated().sum()}")

print("\nNulos por coluna:")
for col in df_sujo.columns:
    nulos = df_sujo[col].isnull().sum()
    if nulos > 0:
        print(f"  {col}: {nulos} ({nulos / len(df_sujo) * 100:.1f}%)")

print("\nTipos das colunas:")
print(df_sujo.dtypes.to_string())

print("\n" + "=" * 50)
print("PRIMEIRAS LINHAS DO DATASET")
print("=" * 50)
print(df_sujo.head(10).to_string())

print("\n✅ Script concluído! Agora execute o pipeline de limpeza.")