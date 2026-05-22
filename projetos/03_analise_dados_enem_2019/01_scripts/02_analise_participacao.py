"""
Script: 02_analise_participacao.py
Projeto: 03_analise_dados_enem_2019
Objetivo: Realizar análise estatística inicial da participação
Autor: vhsouza
Data: 21/05/2026
"""

import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

# Criar caminhos:

PROJECT_DIR = Path(__file__).parent.parent
PROCESSED_DIR = PROJECT_DIR / '02_data' / '02_processed'
OUTPUT_DIR = PROJECT_DIR / '03_output'

# Criar relatório:
relatorio = []

# Importar DataSet processado:
df = pd.read_csv(PROCESSED_DIR / 'enem2019_basico.csv')
relatorio.append(f'df processado importado de {PROCESSED_DIR}\\enem2019_basico.csv')

###################### Exploração inicial da participação ######################

# Por genero
relatorio.append(f'Porcentagem das participações por genero:')
for genero in df['genero'].unique():
    pct_genero = len(df[df['genero']==genero])/len(df)
    relatorio.append(f' - Pessoas autoidentificadas com cor/raça {genero}: {pct_genero:.2%}')

# DF para barplot
genero_pct = df['genero'].value_counts(normalize=True).reset_index()
genero_pct.columns = ['genero', 'porcentagem']
genero_pct['porcentagem'] = genero_pct['porcentagem'] * 100

# barplot
sns.set_style('whitegrid')
sns.barplot(data=genero_pct, x='genero', y='porcentagem', hue='genero', palette=['pink', 'blue'], width=0.3)

plt.title('Participantes por Gênero')
plt.ylabel('Porcentagem (%)')
plt.xlabel('Gênero (F/M)')

for i, v in enumerate(genero_pct['porcentagem']):
    plt.text(i, v+1, f'{v:.2f}%', ha='center')

plt.tight_layout()
plt.savefig(OUTPUT_DIR / 'participao_por_genero.png')
relatorio.append(f'Gráfico "participao_por_genero.png" salvo em {OUTPUT_DIR}')
plt.close()

# Por cor/raça:

relatorio.append(f'Porcentagem das participações por cor e raça:')
for cor_raca in df['cor_raca'].unique():
    pct_cor_raca = len(df[df['cor_raca']==cor_raca])/len(df)
    relatorio.append(f' - Pessoas autoidentificadas com cor/raça {cor_raca}: {pct_cor_raca:.2%}')

# DF para barplot

cor_raca_pct = df['cor_raca'].value_counts(normalize=True).reset_index()
cor_raca_pct.columns = ['cor_raca', 'porcentagem']
cor_raca_pct['porcentagem'] = cor_raca_pct['porcentagem'] * 100

# barplot

sns.barplot(data=cor_raca_pct, x='cor_raca', y='porcentagem', hue='cor_raca', palette='Set1', width=0.5)

plt.title('Participação por Cor/Raça')
plt.ylabel('Porcentagem (%)')
plt.xlabel('Cor/Raça')

for i, v in enumerate(cor_raca_pct['porcentagem']):
    plt.text(i, v+1, f'{v:.2f}%', ha='center')

plt.tight_layout()
plt.savefig(OUTPUT_DIR / 'participao_por_cor_raca.png')
relatorio.append(f'Gráfico "participao_por_cor_raca.png" salvo em {OUTPUT_DIR}')
plt.close()

# Por UF:

relatorio.append(f'Porcentagem das participações por unidade federativa (UF):')
for uf in df['uf'].unique():
    pct_uf = len(df[df['uf']==uf])/len(df)
    relatorio.append(f' - Pessoas residentes de {uf}: {pct_uf:.2%}')


# DF para barplot

uf_pct = df['uf'].value_counts(normalize=True).reset_index()
uf_pct.columns = ['uf', 'porcentagem']
uf_pct['porcentagem'] = uf_pct['porcentagem'] * 100

# barplot

plt.figure(figsize=(12, 6))
sns.barplot(data=uf_pct, x='uf', y='porcentagem', hue='uf', palette='Set1')

plt.title('Participação por Unidade Federativa (UF)')
plt.ylabel('Porcentagem (%)')
plt.xlabel('Unidade Federativa (UF)')

for i, v in enumerate(uf_pct['porcentagem']):
    plt.text(i, v+0.2, f'{v:.2f}%', ha='center')

plt.tight_layout()
plt.savefig(OUTPUT_DIR / 'participao_por_uf.png')
relatorio.append(f'Gráfico "participao_por_uf.png" salvo em {OUTPUT_DIR}')
plt.close()

# Por idade

relatorio.append('Análise da participação por idade:')
relatorio.append(f' - Média das idades: {df['idade'].mean().round(0):.0f}')
relatorio.append(f' - Mediana das idades: {df['idade'].median().round(0):.0f}')
relatorio.append(f' - Moda das idades: {df['idade'].mode()[0].round(0):.0f}')
relatorio.append(f' - Desvio padrão das idades: {df['idade'].std():.2f}')
relatorio.append(f' - Menor valor das idades: {df['idade'].min()}')
relatorio.append(f' - Maior valor das idades: {df['idade'].max()}')

plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='idade', stat='percent',  bins=71, edgecolor='black')

plt.axvline(df['idade'].median(), color='black', linestyle='--', label=f'Mediana {int(df['idade'].median().round(0))}')
plt.axvline(df['idade'].min(), color='red', linestyle='--', label=f'Mínimo: {df['idade'].min()}')
plt.axvline(df['idade'].max(), color='red', linestyle='--', label=f'Máximo: {df['idade'].max()}')

plt.title('Participação por Idade (Distribuição)')
plt.ylabel('Porcentagem (%)')
plt.xlabel('Idades')
plt.legend()

plt.tight_layout()
plt.savefig(OUTPUT_DIR / 'participao_por_idade.png')
relatorio.append(f'Gráfico "participao_por_idade.png" salvo em {OUTPUT_DIR}')
plt.close()

######################

with open(OUTPUT_DIR / 'relatorio_analise_participacao.txt', 'w', encoding='utf-8') as f:
    f.write('=== RELATÓRIO DO SCRIPT DE ANÁLISE DA PARTICIPAÇÃO ===\n')
    f.write(f'Data: {pd.Timestamp.now()}\n')
    f.write(f'===============================================================\n')

    for i, linha in enumerate(relatorio, 1):
        f.write(f'{i} - {linha}\n')

    f.write(f'===============================================================\n')
