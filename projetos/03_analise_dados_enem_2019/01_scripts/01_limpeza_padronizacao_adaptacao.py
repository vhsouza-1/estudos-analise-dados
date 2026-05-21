"""
Script: 01_limpeza_padronizacao_adaptacao.py
Projeto: 03_analise_dados_enem_2019
Objetivo: Realizar a limpeza, padronização e adapdatação do dataset a ser utilizado
Autor: vhsouza
Data: 21/05/2026
"""

import pandas as pd
from pathlib import Path

# Criar caminhos de entrada e saída:

PROJECT_DIR = Path(__file__).parent.parent
RAW_DIR = PROJECT_DIR / '02_data' / '01_raw'
PROCESSED_DIR = PROJECT_DIR / '02_data' / '02_processed'
OUTPUT_DIR = PROJECT_DIR / '03_output'

# Criar relatório:
relatorio = []

# Carregar DataSet:
df = pd.read_csv(RAW_DIR / 'enem2019_final_filter.csv', nrows=100000) # Vou utilizar 100.000 linhas.
relatorio.append(f'arquivo csv importado de: {RAW_DIR}\\"enem2019_final_filter.csv" com 100.000 linhas')

# Verificar existência de linhas duplicadas:
# print(df.duplicated().sum()) # 0
relatorio.append(f'Quantidade de linhas duplicadas: {df.duplicated().sum()}')

# Adaptação:
relatorio.append(f'Quantidade de colunas no relatório: {df.columns.nunique()}')

# Colunas presentes no DataSet:
# print(df.columns)
# ['IN_ATENDIMENTO_ESPECIAL', 'IN_SEM_RECURSO', 'IN_TREINEIRO',
#        'NO_MUNICIPIO_ESC', 'NO_MUNICIPIO_NASCIMENTO', 'NO_MUNICIPIO_PROVA',
#        'NO_MUNICIPIO_RESIDENCIA', 'NU_ACERTOS_CH', 'NU_ACERTOS_CN',
#        'NU_ACERTOS_LC', 'NU_ACERTOS_MT', 'NU_ANO', 'NU_IDADE', 'NU_NOTA_CH',
#        'NU_NOTA_CN', 'NU_NOTA_COMP1', 'NU_NOTA_COMP2', 'NU_NOTA_COMP3',
#        'NU_NOTA_COMP4', 'NU_NOTA_COMP5', 'NU_NOTA_LC', 'NU_NOTA_MEDIA',
#        'NU_NOTA_MT', 'NU_NOTA_REDACAO', 'NU_TOTAL_ACERTOS', 'Q001', 'Q002',
#        'Q003', 'Q004', 'Q005', 'Q006', 'Q007', 'Q008', 'Q009', 'Q010', 'Q011',
#        'Q012', 'Q013', 'Q014', 'Q015', 'Q016', 'Q017', 'Q018', 'Q019', 'Q020',
#        'Q021', 'Q022', 'Q023', 'Q024', 'Q025', 'SG_UF_ESC', 'SG_UF_NASCIMENTO',
#        'SG_UF_PROVA', 'SG_UF_RESIDENCIA', 'TP_ANO_CONCLUIU', 'TP_COR_RACA',
#        'TP_DEPENDENCIA_ADM_ESC', 'TP_ENSINO', 'TP_ESCOLA', 'TP_ESTADO_CIVIL',
#        'TP_LOCALIZACAO_ESC', 'TP_NACIONALIDADE', 'TP_SEXO', 'TP_SIT_FUNC_ESC',
#        'TP_STATUS_REDACAO', 'TP_ST_CONCLUSAO']

# Vamos realizar uma análise simples, para tanto iremos dropar diversas colunas. Vamos manter as seguintes:

# 'TP_COR_RACA', 'TP_SEXO', 'NU_IDADE', 'SG_UF_RESIDENCIA' # para identificação
# 'NU_NOTA_MEDIA', 'NU_NOTA_REDACAO', 'NU_TOTAL_ACERTOS'   # para análise

df = df[['TP_COR_RACA', 'TP_SEXO', 'NU_IDADE', 'SG_UF_RESIDENCIA', 'NU_NOTA_MEDIA', 'NU_NOTA_REDACAO', 'NU_TOTAL_ACERTOS']]
relatorio.append(f'Quantidade de colunas mantidas: {df.columns.nunique()}')
relatorio.append(f'Colunas mantidas: {df.columns.unique().tolist()}')

# Utilizando o Dicionário_Microdados_Enem_2019 vamos trocar os valores para 'TP_COR_RACA' para seus valores categóricos:
relatorio.append(f'Utilizando o Dicionário_Microdados_Enem_2019 vamos trocar os valores de "TP_COR_RACA" para seus valores categóricos:')
relatorio.append("0 -> 'Não declarado', 1 -> 'Branca', 2 -> 'Preta', 3 -> 'Parda', 4 -> 'Amarela', 5 -> 'Indígena'")

dict_tp_cor_raca = {
    0: 'Não declarado',
    1: 'Branca',
    2: 'Preta',
    3: 'Parda',
    4: 'Amarela',
    5: 'Indígena'
}

df['TP_COR_RACA'] = df['TP_COR_RACA'].replace(dict_tp_cor_raca)

# Transformar 'NU_IDADE' em int

df['NU_IDADE'] = df['NU_IDADE'].astype('Int64')
relatorio.append('Coluna "NU_IDADE" convertida para valores inteiros')

# Verificar existência de nulos:

# print(df.isnull().sum())

# TP_COR_RACA         0
# TP_SEXO             0
# NU_IDADE            1
# SG_UF_RESIDENCIA    0
# NU_NOTA_MEDIA       0
# NU_NOTA_REDACAO     0
# NU_TOTAL_ACERTOS    0

relatorio.append(f'Quantidade de nulos células nulas identificadas: {df.isnull().sum().sum()}')
# Como o número de nulos é baixo, vou dropar todas as linhas que contém nulos:

relatorio.append(f'Como a porcentagem de células nulas é ínfima ({df.isnull().sum().sum()/len(df):.3%}), dropamos as linhas')
df = df.dropna()

# Por fim, vamos renomear as colunas:

df = df.rename(columns={
    'TP_COR_RACA': 'cor_raca',
    'TP_SEXO': 'genero',
    'NU_IDADE': 'idade',
    'SG_UF_RESIDENCIA': 'uf',
    'NU_NOTA_MEDIA': 'nota_media',
    'NU_NOTA_REDACAO': 'nota_redacao',
    'NU_TOTAL_ACERTOS': 'total_acertos'
})

relatorio.append("Colunas renomeadas: 'TP_COR_RACA' -> 'cor_raca', 'TP_SEXO' -> 'genero', 'NU_IDADE' -> 'idade', 'SG_UF_RESIDENCIA' -> 'uf', 'NU_NOTA_MEDIA' -> 'nota_media', 'NU_NOTA_REDACAO' -> 'nota_redacao', 'NU_TOTAL_ACERTOS' -> 'total_acertos'")
relatorio.append(f'Nome das novas colunas: {df.columns.unique().tolist()}')

# Salvar df processado:

df.to_csv(PROCESSED_DIR / 'enem2019_basico.csv', index=False)
relatorio.append(f"arquivo csv salvo em: {PROCESSED_DIR}\\'enem2019_basico.csv'")

with open(OUTPUT_DIR / 'relatorio_limpeza_adaptacao.txt', 'w', encoding='utf-8') as f:
    f.write('=== RELATÓRIO DO SCRIPT DE LIMPEZA, PADRONIZAÇÃO E ADAPTAÇÃO ===\n')
    f.write(f'Data: {pd.Timestamp.now()}\n')
    f.write(f'===============================================================\n')

    for i, linha in enumerate(relatorio, 1):
        f.write(f'{i} - {linha}\n')

    f.write(f'===============================================================\n')
