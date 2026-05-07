"""
Bloco 3: Python para Dados
Módulo 3: Limpeza de Dados Avançada
Aula 4: Limpeza e Tratamento de Datas
Data: 07/05/2026
Objetivo: Aprender a converter, validar e limpar datas inconsistentes
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# 1. O PROBLEMA DAS DATAS SUJAS
# ==========================================

print("="*50)
print("1. O PROBLEMA DAS DATAS SUJAS")
print("="*50)

"""
No dia a dia do analista de dados, as datas vêm em formatos HORRÍVEIS:

Problemas comuns:
1. Formatos diferentes: "2024-01-15", "15/01/2024", "Jan 15, 2024"
2. Datas escritas como string: "2024-01-15" (não podemos calcular diferença)
3. Datas inválidas: "31/02/2024", "30/02/2023"
4. Datas futuras (erro de digitação): "2050-01-01" quando deveria ser "2025-01-01"
5. Datas com hora: "2024-01-15 14:30:00" mas precisamos só da data
6. Valores como "NaN", "NA", "desconhecido"

OBJETIVO DESTA AULA: transformar tudo em datetime válido ou NaT.
"""

# Cenário realista
df_sujo = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'data_registro': [
        '2024-01-15',           # formato ISO (bom)
        '15/02/2024',           # formato BR (dia/mês/ano)
        '2024-13-01',           # mês 13 (inválido)
        '31/02/2024',           # fevereiro não tem 31 (inválido)
        '2024-02-30',           # fevereiro não tem 30 (inválido)
        '2026-12-31',           # data futura (será que é erro?)
        'hoje',                 # texto não padronizado
        '2024/03/20',           # formato com barra
        '20.Mar.2024',          # formato com abreviação do mês
        'NaN'                   # valor nulo como string
    ],
    'valor': [100, 200, 150, 300, 250, 400, 350, 500, 450, 600]
})

print("DataFrame com datas problemáticas:")
print(df_sujo)

# ==========================================
# 2. CONVERTENDO DATAS COM pd.to_datetime()
# ==========================================

print("\n" + "="*50)
print("2. CONVERTENDO DATAS COM pd.to_datetime()")
print("="*50)

"""
pd.to_datetime() é a ferramenta principal para converter strings em datas.

Parâmetros importantes:
- errors='coerce': valores inválidos viram NaT (Not a Time) em vez de erro
- format: especifica o formato (mais rápido e preciso)
- dayfirst=True: interpreta DD/MM/AAAA (importante para dados brasileiros)
"""

# 2.1 Conversão básica (pandas tenta adivinhar)
print("--- Conversão básica (pandas tenta adivinhar) ---")
df_sujo['data_convertida'] = pd.to_datetime(df_sujo['data_registro'], format='mixed',errors='coerce')
print(df_sujo[['data_registro', 'data_convertida']])

print(f"\nQuantos NaTs (datas inválidas): {df_sujo['data_convertida'].isna().sum()}")

# 2.2 Usando dayfirst=True (crucial para dados brasileiros)
print("\n--- Usando dayfirst=True (importante para Brasil) ---")
df_teste = pd.DataFrame({'data': ['01/02/2024', '15/03/2024', '30/12/2024']})

print("Sem dayfirst (padrão americano MM/DD/AAAA):")
df_teste['sem_dayfirst'] = pd.to_datetime(df_teste['data'],errors='coerce')
print(df_teste['sem_dayfirst'].dt.strftime('%d/%m/%Y'))

print("\nCom dayfirst=True (formato brasileiro DD/MM/AAAA):")
df_teste['com_dayfirst'] = pd.to_datetime(df_teste['data'], dayfirst=True, errors='coerce')
print(df_teste['com_dayfirst'].dt.strftime('%d/%m/%Y'))

# 2.3 Especificando formato com format= (mais confiável e rápido)
print("\n--- Especificando formato com format= ---")
df_formatos = pd.DataFrame({
    'data1': ['15/01/2024', '20/02/2024', '25/03/2024'],
    'data2': ['2024-01-15', '2024-02-20', '2024-03-25'],
    'data3': ['15-Jan-2024', '20-Feb-2024', '25-Mar-2024']
})

print("Data no formato BR (DD/MM/AAAA):")
df_formatos['data1_conv'] = pd.to_datetime(df_formatos['data1'], format='%d/%m/%Y', errors='coerce')
print(df_formatos['data1_conv'])

print("\nData no formato ISO (AAAA-MM-DD):")
df_formatos['data2_conv'] = pd.to_datetime(df_formatos['data2'], format='%Y-%m-%d', errors='coerce')
print(df_formatos['data2_conv'])

print("\nData com mês abreviado em inglês:")
df_formatos['data3_conv'] = pd.to_datetime(df_formatos['data3'], format='%d-%b-%Y', errors='coerce')
print(df_formatos['data3_conv'])

# ==========================================
# 3. CÓDIGOS DE FORMATAÇÃO (REFERÊNCIA)
# ==========================================

print("\n" + "="*50)
print("3. CÓDIGOS DE FORMATAÇÃO - REFERÊNCIA RÁPIDA")
print("="*50)

"""
CÓDIGOS MAIS USADOS (strftime/strptime):

| Código | Significado | Exemplo |
|--------|-------------|---------|
| %Y     | Ano com 4 dígitos | 2024 |
| %y     | Ano com 2 dígitos | 24 |
| %m     | Mês com 2 dígitos | 01 a 12 |
| %d     | Dia com 2 dígitos | 01 a 31 |
| %b     | Mês abreviado (inglês) | Jan, Feb |
| %B     | Mês completo (inglês) | January |
| %H     | Hora (24h) | 00 a 23 |
| %M     | Minuto | 00 a 59 |
| %S     | Segundo | 00 a 59 |

EXEMPLOS PRÁTICOS:
- '%d/%m/%Y'    → 25/12/2024
- '%Y-%m-%d'    → 2024-12-25
- '%d-%b-%Y'    → 25-Dec-2024
- '%d.%m.%Y'    → 25.12.2024
- '%Y%m%d'      → 20241225
"""

# ==========================================
# 4. IDENTIFICANDO DATAS INVÁLIDAS
# ==========================================

print("\n" + "="*50)
print("4. IDENTIFICANDO DATAS INVÁLIDAS")
print("="*50)

df_validacao = pd.DataFrame({
    'data_original': [
        '2024-01-15',      # válida
        '31/02/2024',      # inválida (fevereiro)
        '2024-02-30',      # inválida (fevereiro)
        '2024-04-31',      # inválida (abril)
        '2024-13-01',      # inválida (mês)
        '15/03/2024',      # válida
        '2024-05-10',      # válida
        '30/06/2024'       # válida
    ]
})

df_validacao['data_datetime'] = pd.to_datetime(df_validacao['data_original'], format='mixed', errors='coerce')
df_validacao['is_valida'] = df_validacao['data_datetime'].notna()
df_validacao['is_invalida'] = df_validacao['data_datetime'].isna()

print("Validação de datas:")
print(df_validacao)

print(f"\nTotal de datas válidas: {df_validacao['is_valida'].sum()}")
print(f"Total de datas inválidas: {df_validacao['is_invalida'].sum()}")

# ==========================================
# 5. DATAS FUTURAS (COMUM EM BASES SUJAS)
# ==========================================

print("\n" + "="*50)
print("5. DATAS FUTURAS - IDENTIFICANDO E TRATANDO")
print("="*50)

"""
Datas futuras são um problema comum:
- Digitação errada: 2050 em vez de 2025
- Sistema com data errada
- Previsões misturadas com históricos

REGRAS GERAIS:
- Datas de NASCIMENTO: não devem ser futuras (óbvio)
- Datas de TRANSAÇÃO/PEDIDO: não devem ser futuras
- Datas de PREVISÃO/PROJEÇÃO: podem ser futuras (identificar contexto)
"""

df_futuro = pd.DataFrame({
    'cliente': ['Ana', 'Bruno', 'Carlos', 'Daniela', 'Eduardo'],
    'data_nascimento': ['1990-01-01', '1985-05-20', '2026-12-31', '1995-03-15', '2050-01-01'],
    'valor': [1000, 2000, 1500, 3000, 2500]
})

# Converter para datetime
df_futuro['data_nasc'] = pd.to_datetime(df_futuro['data_nascimento'], format='mixed', errors='coerce')

# Data atual (sem hora para comparação)
data_atual = pd.Timestamp.now().normalize()
print(f"Data de referência (hoje): {data_atual.date()}")

# Identificar datas futuras
df_futuro['is_futuro'] = df_futuro['data_nasc'] > data_atual
print("\n--- Identificando datas futuras ---")
print(df_futuro)

# Opção 1: Substituir datas futuras por NaN
print("\n--- Opção 1: Substituir futuras por NaT ---")
df_futuro['data_corrigida'] = df_futuro['data_nasc'].where(df_futuro['data_nasc'] <= data_atual, pd.NaT)
print(df_futuro[['data_nasc', 'data_corrigida']])

# Opção 2: Usando .mask() (mais intuitivo para alguns)
print("\n--- Opção 2: Usando .mask() (inverso do .where) ---")
df_futuro['data_mask'] = df_futuro['data_nasc'].mask(df_futuro['data_nasc'] > data_atual, pd.NaT)
print(df_futuro[['data_nasc', 'data_mask']])

# ==========================================
# 6. REMOVENDO HORAS (NORMALIZANDO)
# ==========================================

print("\n" + "="*50)
print("6. REMOVENDO HORAS - .normalize()")
print("="*50)

"""
Muitas vezes as datas vêm com hora, mas você só precisa da data pura.
Exemplo: "2024-01-15 14:30:00" vs "2024-01-15"

Problemas de manter a hora:
- Duas entradas do mesmo dia com horas diferentes são consideradas diferentes
- Dificulta agrupamentos (ex: groupby por data)
- .normalize() zera a hora (00:00:00)
"""

df_com_hora = pd.DataFrame({
    'data_hora': pd.to_datetime([
        '2024-01-15 08:30:00',
        '2024-01-15 14:45:00',
        '2024-01-16 09:00:00',
        '2024-01-16 18:30:00'
    ])
})

print("Datas com hora:")
print(df_com_hora)

df_com_hora['data_sem_hora'] = df_com_hora['data_hora'].dt.normalize()

print("\nApós .normalize() (hora zerada):")
print(df_com_hora)

# Comparação de igualdade
print("\n--- Comparação após normalização ---")
print(f"Datas iguais? {df_com_hora['data_hora'].iloc[0] == df_com_hora['data_hora'].iloc[1]}")
print(f"Datas normalizadas iguais? {df_com_hora['data_sem_hora'].iloc[0] == df_com_hora['data_sem_hora'].iloc[1]}")

# ==========================================
# 7. TRATANDO VALORES NULOS EM DATAS
# ==========================================

print("\n" + "="*50)
print("7. TRATANDO VALORES NULOS EM DATAS")
print("="*50)

df_nulos = pd.DataFrame({
    'id': [1, 2, 3, 4, 5],
    'data': pd.to_datetime([
        '2024-01-01',
        '2024-01-02',
        None,
        pd.NaT,
        '2024-01-05'
    ], errors='coerce'),
    'valor': [100, 200, 150, 300, 250]
})

print("DataFrame com datas nulas (NaN e NaT):")
print(df_nulos)
print(f"\nNulos na coluna data: {df_nulos['data'].isna().sum()}")

# Estratégias para lidar com nulos em datas
print("\n--- Estratégia 1: Remover linhas com data nula ---")
df_sem_nulos = df_nulos.dropna(subset=['data'])
print(df_sem_nulos)

print("\n--- Estratégia 2: Preencher com data padrão (ex: 2024-01-01) ---")
data_padrao = pd.Timestamp('2024-01-01')
df_nulos['data_preenchida'] = df_nulos['data'].fillna(data_padrao)
print(df_nulos[['data', 'data_preenchida']])

print("\n--- Estratégia 3: Preencher com a data mais frequente (moda) ---")
moda_data = df_nulos['data'].mode()[0] if len(df_nulos['data'].mode()) > 0 else data_padrao
df_nulos['data_moda'] = df_nulos['data'].fillna(moda_data)
print(df_nulos[['data', 'data_moda']])

# ==========================================
# 8. EXEMPLO PRÁTICO: PIPELINE DE LIMPEZA
# ==========================================

print("\n" + "="*50)
print("8. EXEMPLO PRÁTICO - PIPELINE DE LIMPEZA DE DATAS")
print("="*50)

# Dataset realista com problemas múltiplos
df_logistica = pd.DataFrame({
    'pedido_id': range(1, 11),
    'data_pedido': [
        '2024-01-15',
        '15/02/2024',
        '2024-13-01',
        '31/02/2024',
        '2024-02-30',
        '2026-12-31',
        '2024/03/20',
        '20.Mar.2024',
        None,
        '2024-05-10'
    ],
    'data_entrega': [
        '2024-01-20',
        '20/02/2024',
        pd.NaT,
        '2024-03-05',
        '2024-03-10',
        '2027-01-15',
        '2024-03-28',
        '25.Mar.2024',
        '2024-05-20',
        '2024-05-18'
    ]
})

print("Dados brutos de logística:")
print(df_logistica)


# Pipeline de limpeza de datas
def limpar_coluna_data(df, coluna):
    """
    Pipeline de limpeza para uma coluna de data:
    1. Converte string para datetime com dayfirst=True (formato BR)
    2. Trata erros com errors='coerce'
    3. Identifica e trata datas futuras (> hoje)
    4. Retorna coluna limpa
    """
    df_limpo = df.copy()

    # Passo 1: Converter para datetime (tentando formato BR primeiro)
    df_limpo[f'{coluna}_convertida'] = pd.to_datetime(df_limpo[coluna], dayfirst=True, errors='coerce')

    # Se ainda tem muitos NaTs, tenta formato automático
    if df_limpo[f'{coluna}_convertida'].isna().sum() > 0:
        # Tenta conversão automática para os que ficaram como string
        mascara_nao_convertidos = df_limpo[coluna].notna() & df_limpo[f'{coluna}_convertida'].isna()
        if mascara_nao_convertidos.any():
            df_limpo.loc[mascara_nao_convertidos, f'{coluna}_convertida'] = pd.to_datetime(
                df_limpo.loc[mascara_nao_convertidos, coluna], errors='coerce'
            )

    # Passo 2: Identificar datas futuras
    hoje = pd.Timestamp.now().normalize()
    mascara_futuro = df_limpo[f'{coluna}_convertida'] > hoje
    df_limpo[f'{coluna}_is_futuro'] = mascara_futuro

    # Passo 3: Tratar datas futuras (substituir por NaT, ou você pode optar por manter)
    df_limpo[f'{coluna}_limpa'] = df_limpo[f'{coluna}_convertida'].mask(mascara_futuro, pd.NaT)

    return df_limpo[f'{coluna}_limpa']

# # Aplicar pipeline
# df_logistica['data_pedido_limpa'] = limpar_coluna_data(df_logistica, 'data_pedido')
# df_logistica['data_entrega_limpa'] = limpar_coluna_data(df_logistica, 'data_entrega')
#
# print("\n--- Após pipeline de limpeza ---")
# print(df_logistica[['data_pedido', 'data_pedido_limpa', 'data_entrega', 'data_entrega_limpa']])

# ==========================================
# 9. RESUMO DA AULA
# ==========================================

print("\n" + "="*50)
print("9. RESUMO DA AULA - LIMPEZA DE DATAS")
print("="*50)

"""
✅ CONVERSÃO BÁSICA:
   - pd.to_datetime(df['col'], format='mixed', errors='coerce')
   - dayfirst=True (essencial para dados brasileiros)
   - format='%d/%m/%Y' (mais rápido e preciso)

✅ CÓDIGOS DE FORMATAÇÃO:
   - %Y (ano 4 dígitos), %m (mês), %d (dia)
   - Exemplo: '%d/%m/%Y' para 25/12/2024

✅ IDENTIFICAÇÃO DE PROBLEMAS:
   - df['data'].isna() → datas inválidas viraram NaT
   - df['data'] > hoje → datas futuras
   - df['data'].dt.normalize() → remove horas

✅ TRATAMENTO DE NULOS:
   - df.dropna(subset=['data']) → remove linhas
   - df['data'].fillna(data_padrao) → preenche com padrão
   - df['data'].fillna(df['data'].mode()[0]) → preenche com moda

✅ TRATAMENTO DE DATAS FUTURAS:
   - df['data'].mask(df['data'] > hoje, pd.NaT)
   - df['data'].where(df['data'] <= hoje, pd.NaT)

📌 BOAS PRÁTICAS:
   1. SEMPRE use errors='coerce' na conversão
   2. SEMPRE normalize timestamps se não precisar de horas
   3. Datas futuras são quase sempre erro (exceto previsões)
   4. Para Brasil, dayfirst=True é obrigatório
"""

# ==========================================
# EXERCÍCIOS - AULA 4 (LIMPEZA DE DATAS)
# ==========================================

print("\n" + "="*50)
print("EXERCÍCIOS - LIMPEZA DE DATAS")
print("="*50)

# Dados para todos os exercícios
np.random.seed(42)

df_clientes = pd.DataFrame({
    'id_cliente': range(1, 21),
    'nome': [f'Cliente_{i}' for i in range(1, 21)],
    'data_nascimento': [
        '1990-01-15', '1985/05/20', '15/03/1992', '1993-07-08', '25/12/1988',
        '1991-02-30', '31/04/1994', '1995-13-01', '20/09/1996', '1899-12-31',
        '1998-11-15', '2050-01-01', '1990-06-20', '2026-12-31', '1987-03-25',
        '1900-02-29', '1999-08-15', '2000-13-45', '2025-01-15', '1994-10-30'
    ],
    'data_cadastro': [
        '2020-01-01', '01/02/2020', '2020-03-15', '15/04/2020', '2020-05-20',
        '20/06/2020', '2020-07-10', '10/08/2020', '2020-09-05', '05/10/2020',
        '2020-11-25', '25/12/2020', '2021-01-01', '01/02/2021', '2021-03-15',
        '15/04/2021', '2021-05-20', '20/06/2021', '2021-07-10', '2025-12-31'
    ],
    'ultima_compra': [
        '2023-01-15', '2023-02-20', '15/03/2023', '2023-04-10', '10/05/2023',
        '2023-06-25', '25/07/2023', '2023-08-01', '01/09/2023', '2023-10-15',
        '15/11/2023', '2023-12-20', '20/01/2024', '2024-02-10', '10/03/2024',
        '2024-04-15', '15/05/2024', '2024-06-01', None, '2026-12-31'
    ]
})

########################################################################
# NÍVEL 1-3: Aquecimento
########################################################################

"""
1. Primeira conversão

# Converta a coluna 'data_nascimento' para datetime
# Use errors='coerce' e dayfirst=True (dados podem estar em formato BR)
# Mostre:
# - Quantas datas inválidas foram encontradas
# - Quais são os valores que viraram NaT
"""

"""
df = df_clientes.copy()

df['data_nascimento_limpa'] = pd.to_datetime(df['data_nascimento'], format='mixed', errors='coerce')

print(f'Quantidade de datas inválidas encontradas: {df['data_nascimento_limpa'].isnull().sum()}')

print('Valores que viraram NaT:')
print(df.loc[df['data_nascimento_limpa'].isnull(), 'data_nascimento'])
"""

########################################################################

"""
2. Testando formatos diferentes

# A coluna 'data_cadastro' tem formatos mistos
# Converta para datetime usando:
# - Primeiro tente com dayfirst=True
# - Depois mostre quantas datas ainda são inválidas
# - Quais clientes têm data_cadastro inválida?
"""

"""
df = df_clientes.copy()

df['data_cadastro_limpa'] = pd.to_datetime(df['data_cadastro'], format='mixed', errors='coerce')

print(f'Quantas datas são inválidas: {df['data_cadastro_limpa'].isna().sum()}')

print(f'Quais clientes têm data_cadastro inválida:')
print(df.loc[df['data_cadastro_limpa'].isna(), 'nome'])
"""

########################################################################

"""
3. Identificando datas futuras

# Use a data atual (hoje) como referência
# Identifique na coluna 'ultima_compra':
# - Quantas são futuras
# - Quais clientes têm data futura
# - Crie uma coluna 'ultima_compra_valida' substituindo futuras por NaT
"""

"""
df = df_clientes.copy()

df['ultima_compra_limpa'] = pd.to_datetime(df['ultima_compra'], format='mixed', errors='coerce')

data_atual = pd.Timestamp.now().normalize()
mascara_data = df['ultima_compra_limpa'] > data_atual

print(f'Quantas são futuras: {len(df[mascara_data])}')
print(f'Quais clientes tem data futura:')
print(df[mascara_data]['nome'])
"""

########################################################################
# NÍVEL 4-6: Aplicação
########################################################################

"""
4. Datas muito antigas (possível erro)

# Para data de nascimento, considere que valores anteriores a 1900 são inválidos
# Identifique e substitua essas datas por NaT
# Mostre quantas foram removidas
"""

"""
df = df_clientes.copy()

df['data_nascimento_limpa'] = pd.to_datetime(df['data_nascimento'], format='mixed', errors='coerce')
data_invalida = df['data_nascimento_limpa'].isnull().sum()

data_antiga = pd.Timestamp('1900').normalize()
mascara_data = df['data_nascimento_limpa'] < data_antiga

print(f'datas de nascimento muito antigas:')
print(df[mascara_data].to_string())

df['data_nascimento_limpa'] = df['data_nascimento_limpa'].mask(mascara_data, pd.NaT)
print(f'Quantas foram removidas: {df['data_nascimento_limpa'].isnull().sum() - data_invalida}')
"""

########################################################################

"""
5. Normalizando datas com hora

# A coluna 'data_cadastro' pode ter vindo com hora em alguns registros
# Use .normalize() para garantir que todas tenham apenas data (sem hora)
# Mostre a diferença antes/depois
"""

"""
df = df_clientes.copy()

df['data_cadastro_limpa'] = pd.to_datetime(df['data_cadastro'], format='mixed', errors='coerce')
df['data_cadastro_limpa_normalize'] = df['data_cadastro_limpa'].dt.normalize()

print(df[['data_cadastro', 'data_cadastro_limpa', 'data_cadastro_limpa_normalize']])
"""

########################################################################

"""
6. Tratando nulos em datas

# A coluna 'ultima_compra' tem valores nulos
# Decida uma estratégia para tratar:
# - Remover os clientes sem compra? (dropna)
# - Preencher com uma data padrão? (qual?)
# - Preencher com a moda?
#
# Justifique sua escolha e implemente
"""

"""
df = df_clientes.copy()

df['ultima_compra_limpa'] = pd.to_datetime(df['ultima_compra'], format='mixed', errors='coerce')

print(df['ultima_compra_limpa'])

# sns.scatterplot(data=df, x='nome', y='ultima_compra_limpa', hue='nome')
# plt.show()

# De acordo com o scatterplot acima percebi a presença de um outlier nos dados, logo já descartamos a média das datas.
# Como a distribuição das datas não apresenta nenhuma concentração específica, vou descartar a moda e usar a mediana

mediana_datas = df['ultima_compra_limpa'].median()
df['ultima_compra_limpa_tratada'] = df['ultima_compra_limpa'].fillna(mediana_datas)

print(df['ultima_compra_limpa_tratada'])
"""

########################################################################
# NÍVEL 7-8: Manipulação
########################################################################

"""
7. Pipeline de validação de datas

# Crie uma função valida_data(df, coluna, data_min=None, data_max=None)
# que:
# 1. Converte a coluna para datetime
# 2. Remove datas fora dos limites (se fornecidos)
# 3. Remove datas futuras (se não for contexto de previsão)
# 4. Retorna a coluna limpa e um dicionário com estatísticas
#
# Aplique na coluna 'data_nascimento' com data_min='1900-01-01'
"""
"""
def valida_data(df_sujo, coluna, data_min=None, data_max=None):
    
    df = df_sujo.copy()
    
    df[coluna] = pd.to_datetime(df[coluna], format='mixed', errors='coerce')

    estatisticas = {}

    if data_min is not None:
        data_min = pd.to_datetime(data_min, format='mixed', errors='coerce')
        data_min = data_min.normalize()
        removido_antes = (df[coluna] < data_min).sum()
        df[coluna] = df[coluna].mask(df[coluna] < data_min, pd.NaT)
        estatisticas[f'data inferior à {data_min}'] = f'Removido {removido_antes}'

    if data_max is not None:
        data_max = pd.to_datetime(data_max, format='mixed', errors='coerce')
        data_max = data_max.normalize()
        removido_depois = (df[coluna] > data_max).sum()
        df[coluna] = df[coluna].mask(df[coluna] > data_max, pd.NaT)
        estatisticas[f'data superior à {data_max}'] = f'Removido {removido_depois}'

    return df[coluna], estatisticas


df_coluna, estatistica = valida_data(df_clientes, 'data_nascimento', '01/01/1900')

print(df_coluna)
print(estatistica)

"""

########################################################################

"""
8. Corrigindo ano em datas comuns (2 dígitos)

# Em alguns sistemas, anos vêm com 2 dígitos (24 em vez de 2024)
# Converta a lista abaixo para datetime, assumindo que 24 = 2024
# Dica: você pode precisar de uma função personalizada

df_ano_2digitos = pd.DataFrame({
    'data': ['01/01/24', '15/02/23', '20/03/22', '10/04/21', '05/05/20']
})
"""
"""
df_ano_2digitos = pd.DataFrame({
    'data': ['01/01/24', '15/02/23', '20/03/22', '10/04/21', '05/05/20']
})

df = df_ano_2digitos.copy()

df['data_limpa'] = pd.to_datetime(df['data'], format='mixed', errors='coerce')

print(df)

"""

########################################################################
# NÍVEL 9-10: Desafios
########################################################################

"""
9. Dashboard de qualidade das datas

# Para o df_clientes, crie um relatório completo que mostre:
# - Para CADA coluna de data:
#   * Total de registros
#   * Quantos são válidos
#   * Quantos são inválidos (NaT)
#   * Quantos são futuros
#   * Quantos são muito antigos (antes de 1900)
#   * Sugestão de correção
#
# - Para o DataFrame inteiro:
#   * Porcentagem de células de data problemáticas
"""

"""
df = df_clientes.copy()

colunas_datas = ['data_nascimento', 'data_cadastro', 'ultima_compra']

celulas_problematicas = 0

for coluna in colunas_datas:
    print(f'Coluna: {coluna}')
    print(f' - Total de registros: {df[coluna].notna().sum()}')

    df[f'{coluna}_limpa'] = pd.to_datetime(df[coluna], format='mixed', errors='coerce')

    print(f' - Quantos registros são válidos: {df[f'{coluna}_limpa'].notna().sum()}')
    print(f' - Quantos registros são inválidos: {df[f'{coluna}_limpa'].isna().sum()}')

    celulas_problematicas += df[f'{coluna}_limpa'].isna().sum()

    data_atual = pd.Timestamp.now().normalize()
    mascara_futuro = df[f'{coluna}_limpa'] > data_atual
    print(f' - Quantos registros são futuros: {mascara_futuro.sum()}')

    celulas_problematicas += mascara_futuro.sum()

    data_antiga = pd.Timestamp('1900').normalize()
    mascara_antiga = df[f'{coluna}_limpa'] < data_antiga
    print(f' - Quantos registros são muito antigos: {mascara_antiga.sum()}')

    celulas_problematicas += mascara_antiga.sum()

    print('Sugestões de correção: ')
    if df[f'{coluna}_limpa'].isna().sum() > 0:
        print(' - Dropar linhas com registros inválidos')

    if mascara_futuro.sum() > 0:
        print(' - Substituir registros futuros pela mediana dos registros')

    if mascara_antiga.sum() > 0:
        print(' - Substitui registros muito antigos pela mediana dos registros')

    print('----')

print(f'Porcentagem de células com datas problemáticas: {celulas_problematicas/(df.shape[0]*df.shape[1])*100}%')
"""

########################################################################

"""
10. DESAFIO FINAL: Pipeline completa de datas

# Crie uma função pipeline_limpeza_datas(df) que:
# 1. Identifica automaticamente colunas que parecem datas (nome com 'data' ou 'date')
# 2. Para cada coluna:
#    - Converte para datetime
#    - Aplica dayfirst=True
#    - Remove futurOs (se não for coluna de previsão - use um parâmetro)
#    - Remove datas muito antigas (parâmetro min_date)
#    - Normaliza (remove hora)
#    - Trata nulos (parâmetro fillna_strategy)
# 3. Retorna DataFrame limpo e relatório detalhado
#
# Teste no df_clientes
"""

def pipeline_limpeza_datas(df_sujo, drop_futuras=True, min_data='1900-01-01', fillna_strategy='drop'):
    df = df_sujo.copy()
    relatorio = {}
    for coluna in df.columns:

        if 'data' in coluna or 'compra' in coluna:
            relatorio[coluna] = []
            df[coluna] = pd.to_datetime(df[coluna], format='mixed', errors='coerce')

            if drop_futuras and ('prev' not in coluna and 'futur' not in coluna):
                data_atual = pd.Timestamp.now().normalize()
                mascara_futuro = df[coluna] > data_atual
                if not df[mascara_futuro].empty:
                    relatorio[coluna].append(f'Linhas com datas futuras: {df[mascara_futuro]}')
                df = df[~mascara_futuro]


            if min_data:
                min_data = pd.to_datetime(min_data, format='mixed', errors='coerce')
                mascara_min_data = df[coluna] < min_data
                if not df[mascara_min_data].empty:
                    relatorio[coluna].append(f'Linhas com datas muito antigas: {df[mascara_min_data]}')
                df = df[~mascara_min_data]

            if fillna_strategy == 'drop':
                mascara_nulo = df[coluna].isna()
                if not mascara_nulo.empty:
                    relatorio[coluna].append(f'Linhas dropadas com nulos: {df[mascara_nulo]}')
                df = df.dropna()

    return df, relatorio

df, relatorio = pipeline_limpeza_datas(df_clientes)

print(df.to_string)
print(relatorio)

# esse pipeline funciona, mas o relatorio ficou feio ''/ como a gente poderia melhorá-lo?