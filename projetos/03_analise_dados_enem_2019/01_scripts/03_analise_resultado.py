"""
Script: 03_analise_resultado.py
Projeto: 03_analise_dados_enem_2019
Objetivo: Realizar análise estatística inicial dos resultados
Autor: vhsouza
Data: 22/05/2026
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

relatorio.append('############################################################')
###################### Total de acertos
relatorio.append('Análise do total de acertos:')
relatorio.append(f' - Média do total de acertos: {df['total_acertos'].mean():.0f}')
relatorio.append(f' - Mediana do total de acertos: {df['total_acertos'].median():.0f}')
relatorio.append(f' - Moda do total de acertos: {df['total_acertos'].mode()[0]:.0f}')
relatorio.append(f' - Desvio Padrão do total de acertos: {df['total_acertos'].std():.0f}')
relatorio.append(f' - Mínimo do total de acertos: {df['total_acertos'].min()}')
relatorio.append(f' - Máximo do total de acertos: {df['total_acertos'].max()}')
relatorio.append(f' - Q1 do total de acertos: {df['total_acertos'].quantile(0.25):.0f}')
relatorio.append(f' - Q3 do total de acertos: {df['total_acertos'].quantile(0.75):.0f}')

# Identificação de Outliers:

Q1 = df['total_acertos'].quantile(0.25)
Q3 = df['total_acertos'].quantile(0.75)
IQR = Q3 - Q1
lim_sup = Q3 + 1.5*IQR
lim_inf = Q1 - 1.5*IQR

outliers_sup_mask = df['total_acertos'] > lim_sup
outliers_inf_mask = df['total_acertos'] < lim_inf

qnt_outliers_sup = len(df[outliers_sup_mask])
pct_outliers_sup = qnt_outliers_sup/len(df)

qnt_outliers_inf = len(df[outliers_inf_mask])
pct_outliers_inf = qnt_outliers_inf/len(df)

relatorio.append(f' - Total de Outliers em total de acertos: {qnt_outliers_sup + qnt_outliers_inf} ({pct_outliers_sup + pct_outliers_inf:.3%})')
relatorio.append(f' - Total de Outliers Sup.: {qnt_outliers_sup} ({pct_outliers_sup:.3%})')
relatorio.append(f' - Total de Outliers Inf.: {qnt_outliers_inf} ({pct_outliers_inf:.3%})')

# Histograma do total de acertos

plt.figure(figsize=(10, 6))
sns.set_style('whitegrid')

sns.histplot(data=df, x='total_acertos', stat='percent', bins=52, edgecolor='black')
plt.axvline(df['total_acertos'].median(), color='red', linestyle='--', label=f'Mediana: {df['total_acertos'].median():.0f}')
plt.axvline(df['total_acertos'].mean(), color='purple', linestyle='--', label=f'Média: {df['total_acertos'].mean():.0f}')
plt.axvline(df['total_acertos'].mode()[0], color='blue', linestyle='--', label=f'Moda: {df['total_acertos'].mode()[0]:.0f}')
plt.axvline(df['total_acertos'].min(), color='black', linestyle=':', label=f'Mínimo: {df['total_acertos'].min():.0f}')
plt.axvline(df['total_acertos'].max(), color='black', linestyle=':', label=f'Máximo: {df['total_acertos'].max():.0f}')

plt.title('Distribuição do total de acertos - Histograma')
plt.ylabel('Porcentagem (%)')
plt.xlabel('Total de acertos')
plt.legend()

plt.tight_layout()
plt.savefig(OUTPUT_DIR / 'histograma_total_acertos.png')
relatorio.append(f'Gráfico "histograma_total_acertos.png" salvo em {OUTPUT_DIR}')
plt.close()

# Boxplot do total de acertos

plt.figure(figsize=(6, 6))
sns.boxplot(data=df, y='total_acertos', width=0.3, color='lightblue')

plt.axhline(df['total_acertos'].median(), color='red', linestyle='--', label=f'Mediana: {df['total_acertos'].median():.0f}')
plt.axhline(df['total_acertos'].mean(), color='purple', linestyle='--', label=f'Média: {df['total_acertos'].mean():.0f}')
plt.axhline(df['total_acertos'].mode()[0], color='blue', linestyle='--', label=f'Moda: {df['total_acertos'].mode()[0]:.0f}')
plt.axhline(df['total_acertos'].min(), color='black', linestyle=':', label=f'Mínimo: {df['total_acertos'].min():.0f}')
plt.axhline(df['total_acertos'].max(), color='black', linestyle=':', label=f'Máximo: {df['total_acertos'].max():.0f}')

plt.title('Distribuição do total de acertos - Boxplot')
plt.ylabel('Total de acertos')
plt.legend()

plt.tight_layout()
plt.savefig(OUTPUT_DIR / 'boxplot_total_acertos.png')
relatorio.append(f'Gráfico "boxplot_total_acertos.png" salvo em {OUTPUT_DIR}')
plt.close()
relatorio.append('############################################################')
###################### Nota Redação

relatorio.append('Análise da nota da redação:')
relatorio.append(f' - Média da nota da redação: {df['nota_redacao'].mean():.0f}')
relatorio.append(f' - Mediana da nota da redação: {df['nota_redacao'].median():.0f}')
relatorio.append(f' - Moda da nota da redação: {df['nota_redacao'].mode()[0]:.0f}')
relatorio.append(f' - Desvio Padrão da nota da redação: {df['nota_redacao'].std():.0f}')
relatorio.append(f' - Mínimo da nota da redação: {df['nota_redacao'].min()}')
relatorio.append(f' - Máximo da nota da redação: {df['nota_redacao'].max()}')
relatorio.append(f' - Q1 da nota da redação: {df['nota_redacao'].quantile(0.25):.0f}')
relatorio.append(f' - Q3 da nota da redação: {df['nota_redacao'].quantile(0.75):.0f}')

# Identificação de Outliers:

Q1 = df['nota_redacao'].quantile(0.25)
Q3 = df['nota_redacao'].quantile(0.75)
IQR = Q3 - Q1
lim_sup = Q3 + 1.5*IQR
lim_inf = Q1 - 1.5*IQR

outliers_sup_mask = df['nota_redacao'] > lim_sup
outliers_inf_mask = df['nota_redacao'] < lim_inf

qnt_outliers_sup = len(df[outliers_sup_mask])
pct_outliers_sup = qnt_outliers_sup/len(df)

qnt_outliers_inf = len(df[outliers_inf_mask])
pct_outliers_inf = qnt_outliers_inf/len(df)

relatorio.append(f' - Total de Outliers em nota da redação: {qnt_outliers_sup + qnt_outliers_inf} ({pct_outliers_sup + pct_outliers_inf:.3%})')
relatorio.append(f' - Total de Outliers Sup.: {qnt_outliers_sup} ({pct_outliers_sup:.3%})')
relatorio.append(f' - Total de Outliers Inf.: {qnt_outliers_inf} ({pct_outliers_inf:.3%})')

# Histograma da nota da redação

plt.figure(figsize=(10, 6))
sns.set_style('whitegrid')

sns.histplot(data=df, x='nota_redacao', stat='percent', bins=51, edgecolor='black')
plt.axvline(df['nota_redacao'].median(), color='red', linestyle='--', label=f'Mediana: {df['nota_redacao'].median():.0f}')
plt.axvline(df['nota_redacao'].mean(), color='purple', linestyle='--', label=f'Média: {df['nota_redacao'].mean():.0f}')
plt.axvline(df['nota_redacao'].mode()[0], color='blue', linestyle='--', label=f'Moda: {df['nota_redacao'].mode()[0]:.0f}')
plt.axvline(df['nota_redacao'].min(), color='black', linestyle=':', label=f'Mínimo: {df['nota_redacao'].min():.0f}')
plt.axvline(df['nota_redacao'].max(), color='black', linestyle=':', label=f'Máximo: {df['nota_redacao'].max():.0f}')

plt.title('Distribuição da Nota da Redação - Histograma')
plt.ylabel('Porcentagem (%)')
plt.xlabel('Nota da Redação')
plt.legend()

plt.tight_layout()
plt.savefig(OUTPUT_DIR / 'histograma_nota_redacao.png')
relatorio.append(f'Gráfico "histograma_nota_redacao.png" salvo em {OUTPUT_DIR}')
plt.close()

# Boxplot do total de acertos

plt.figure(figsize=(6, 6))
sns.boxplot(data=df, y='nota_redacao', width=0.3, color='lightblue')

plt.axhline(df['nota_redacao'].median(), color='red', linestyle='--', label=f'Mediana: {df['nota_redacao'].median():.0f}')
plt.axhline(df['nota_redacao'].mean(), color='purple', linestyle='--', label=f'Média: {df['nota_redacao'].mean():.0f}')
plt.axhline(df['nota_redacao'].mode()[0], color='blue', linestyle='--', label=f'Moda: {df['nota_redacao'].mode()[0]:.0f}')
plt.axhline(df['nota_redacao'].min(), color='black', linestyle=':', label=f'Mínimo: {df['nota_redacao'].min():.0f}')
plt.axhline(df['nota_redacao'].max(), color='black', linestyle=':', label=f'Máximo: {df['nota_redacao'].max():.0f}')

plt.title('Distribuição da Nota da Redação - Boxplot')
plt.ylabel('Nota da Redação')
plt.legend()

plt.tight_layout()
plt.savefig(OUTPUT_DIR / 'boxplot_nota_redacao.png')
relatorio.append(f'Gráfico "boxplot_nota_redacao.png" salvo em {OUTPUT_DIR}')
plt.close()
relatorio.append('############################################################')

###################### Nota Média

relatorio.append('Análise da nota média:')
relatorio.append(f' - Média da nota média: {df['nota_media'].mean():.0f}')
relatorio.append(f' - Mediana da nota média: {df['nota_media'].median():.0f}')
relatorio.append(f' - Moda da nota da média: {df['nota_media'].mode()[0]:.0f}')
relatorio.append(f' - Desvio Padrão da nota da média: {df['nota_media'].std():.0f}')
relatorio.append(f' - Mínimo da nota da média: {df['nota_media'].min()}')
relatorio.append(f' - Máximo da nota da média: {df['nota_media'].max():.2f}')
relatorio.append(f' - Q1 da nota da média: {df['nota_media'].quantile(0.25):.0f}')
relatorio.append(f' - Q3 da nota da média: {df['nota_media'].quantile(0.75):.0f}')

# Identificação de Outliers:

Q1 = df['nota_media'].quantile(0.25)
Q3 = df['nota_media'].quantile(0.75)
IQR = Q3 - Q1
lim_sup = Q3 + 1.5*IQR
lim_inf = Q1 - 1.5*IQR

outliers_sup_mask = df['nota_media'] > lim_sup
outliers_inf_mask = df['nota_media'] < lim_inf

qnt_outliers_sup = len(df[outliers_sup_mask])
pct_outliers_sup = qnt_outliers_sup/len(df)

qnt_outliers_inf = len(df[outliers_inf_mask])
pct_outliers_inf = qnt_outliers_inf/len(df)

relatorio.append(f' - Total de Outliers em nota da redação: {qnt_outliers_sup + qnt_outliers_inf} ({pct_outliers_sup + pct_outliers_inf:.3%})')
relatorio.append(f' - Total de Outliers Sup.: {qnt_outliers_sup} ({pct_outliers_sup:.3%})')
relatorio.append(f' - Total de Outliers Inf.: {qnt_outliers_inf} ({pct_outliers_inf:.3%})')

# Histograma do total de acertos

plt.figure(figsize=(10, 6))
sns.set_style('whitegrid')

sns.histplot(data=df, x='nota_media', stat='percent', bins=90, edgecolor='black')
plt.axvline(df['nota_media'].median(), color='red', linestyle='--', label=f'Mediana: {df['nota_media'].median():.0f}')
plt.axvline(df['nota_media'].mean(), color='purple', linestyle='--', label=f'Média: {df['nota_media'].mean():.0f}')
plt.axvline(df['nota_media'].mode()[0], color='blue', linestyle='--', label=f'Moda: {df['nota_media'].mode()[0]:.0f}')
plt.axvline(df['nota_media'].min(), color='black', linestyle=':', label=f'Mínimo: {df['nota_media'].min():.0f}')
plt.axvline(df['nota_media'].max(), color='black', linestyle=':', label=f'Máximo: {df['nota_media'].max():.0f}')

plt.title('Distribuição da Nota da Média - Histograma')
plt.ylabel('Porcentagem (%)')
plt.xlabel('Nota da Média')
plt.legend()

plt.tight_layout()
plt.savefig(OUTPUT_DIR / 'histograma_nota_media.png')
relatorio.append(f'Gráfico "histograma_nota_media.png" salvo em {OUTPUT_DIR}')
plt.close()

# Boxplot da nota média

plt.figure(figsize=(6, 6))
sns.boxplot(data=df, y='nota_media', width=0.3, color='lightblue')

plt.axhline(df['nota_media'].median(), color='red', linestyle='--', label=f'Mediana: {df['nota_media'].median():.0f}')
plt.axhline(df['nota_media'].mean(), color='purple', linestyle='--', label=f'Média: {df['nota_media'].mean():.0f}')
plt.axhline(df['nota_media'].mode()[0], color='blue', linestyle='--', label=f'Moda: {df['nota_media'].mode()[0]:.0f}')
plt.axhline(df['nota_media'].min(), color='black', linestyle=':', label=f'Mínimo: {df['nota_media'].min():.0f}')
plt.axhline(df['nota_media'].max(), color='black', linestyle=':', label=f'Máximo: {df['nota_media'].max():.0f}')

plt.title('Distribuição da Nota Média - Boxplot')
plt.ylabel('Nota Média')
plt.legend()

plt.tight_layout()
plt.savefig(OUTPUT_DIR / 'boxplot_nota_media.png')
relatorio.append(f'Gráfico "boxplot_nota_media.png" salvo em {OUTPUT_DIR}')
plt.close()









######################

with open(OUTPUT_DIR / 'relatorio_analise_resultado.txt', 'w', encoding='utf-8') as f:
    f.write('=== RELATÓRIO DO SCRIPT DE ANÁLISE DO RESULTADO ===\n')
    f.write(f'Data: {pd.Timestamp.now()}\n')
    f.write(f'===============================================================\n')

    for i, linha in enumerate(relatorio, 1):
        f.write(f'{i} - {linha}\n')

    f.write(f'===============================================================\n')
