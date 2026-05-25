"""
Script: 04_analises_cruzadas.py
Projeto: 03_analise_dados_enem_2019
Objetivo: Realizar análises estatísticas cruzadas entre genero, etnia, notas e resultado.
Autor: vhsouza
Data: 25/05/2026
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from scipy.stats import f_oneway

# Criar caminhos:

PROJECT_DIR = Path(__file__).parent.parent
PROCESSED_DIR = PROJECT_DIR / '02_data' / '02_processed'
OUTPUT_DIR = PROJECT_DIR / '03_output'

ANALISE_CRUZADA_DIR = OUTPUT_DIR / '03_analises_cruzadas'
ANALISE_CRUZADA_DIR.mkdir(parents=True, exist_ok=True)

# Criar relatório:
relatorio = []

# Importar DataSet processado:
df = pd.read_csv(PROCESSED_DIR / 'enem2019_basico.csv')
relatorio.append(f'df processado importado de {PROCESSED_DIR}\\enem2019_basico.csv')
relatorio.append('###############################################################')

############ Análise entre gênero, etnia e nota média

# Análise da nota entre gêneros

relatorio.append(f'Análise das notas entre gêneros:')
sns.set_style('whitegrid')
sns.boxplot(data=df, x='genero', y='nota_media', hue='genero', palette=['pink', 'skyblue'], width=0.3)

plt.title('Nota Média x Gênero - Boxplot')
plt.ylabel('Nota Média')
plt.xlabel('Gênero')

plt.tight_layout()
plt.savefig(ANALISE_CRUZADA_DIR / 'boxplot_nota_genero.png')
relatorio.append(f'Gráfico "boxplot_nota_genero.png" salvo em {ANALISE_CRUZADA_DIR}')
plt.close()

# Grupos M e F separados:
df_m = df[df['genero']=='M']
df_f = df[df['genero']=='F']

relatorio.append(f'Grupo M: Média das notas: {df_m['nota_media'].mean():.2f} | Desvio padrão: {df_m['nota_media'].std():.2f}')
relatorio.append(f'Grupo F: Média das notas: {df_f['nota_media'].mean():.2f} | Desvio padrão: {df_f['nota_media'].std():.2f}')

# Teste A/B, comparação das médias com ttest

t_stat, p_valor = stats.ttest_ind(df_m['nota_media'], df_f['nota_media'], equal_var=False)

relatorio.append('Resultado do Teste A/B (ttest):')
relatorio.append(f' - Estatística t: {t_stat:.2f}')
relatorio.append(f' - P-valor: {p_valor:.4%} ({p_valor})')

relatorio.append(f'Resultado estatísticamente significativo (p-valor < 0.05)')
relatorio.append(f' - Diferença absoluta das médias : {df_m['nota_media'].mean() - df_f['nota_media'].mean():.2f}')
relatorio.append(f' - Diferença percentual das médias : {(df_m['nota_media'].mean()/df_f['nota_media'].mean())-1:.2%}')

relatorio.append('###############################################################')

# Análise da nota entre etnias
relatorio.append('Análise da nota entre cor/raça:')

sns.boxplot(data=df, x='cor_raca', y='nota_media', hue='cor_raca', palette='Set1')

plt.title('Nota Média x Cor/Raça - Boxplot')
plt.ylabel('Nota Média')
plt.xlabel('Cor/Raça')

plt.tight_layout()
plt.savefig(ANALISE_CRUZADA_DIR / 'boxplot_nota_cor_raca.png')
relatorio.append(f'Gráfico "boxplot_nota_cor_raca.png" salvo em {ANALISE_CRUZADA_DIR}')
plt.close()

racas = df['cor_raca'].unique()
notas_p_raca = []
for raca in racas:
    df_r = df[df['cor_raca']==raca]
    notas_p_raca.append(df_r['nota_media'])
    relatorio.append(f'Grupo Cor/Raça {raca}: Média das notas: {df_r['nota_media'].mean():.2f} | Desvio Padrão: {df_r['nota_media'].std():.2f}')

# Teste ANOVA
f_stat, p_valor = f_oneway(*notas_p_raca)

relatorio.append('Resultados do Teste A/B (ANOVA):')
relatorio.append(f'Estatística f: {f_stat:.2f}')
relatorio.append(f'P-valor: {p_valor:.4%} ({p_valor})')

relatorio.append(f'Resultado estatisticamente significativo (p-valor < 0.05)')
relatorio.append("Comparações par a par:")
for i in range(len(racas)):
    for j in range(i+1, len(racas)):
        t_stat, p_par = stats.ttest_ind(notas_p_raca[i], notas_p_raca[j])
        if p_par < 0.05:
            relatorio.append(f" - {racas[i]} e {racas[j]} (p={p_par:.4f})")

relatorio.append('###############################################################')

relatorio.append(f'Relação entre variáveis numéricas: nota final, número de acertos, nota da redação:')

df_corr = df[['nota_media', 'nota_redacao', 'total_acertos']].corr()

sns.heatmap(df_corr, annot=True, fmt='.2f', cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Relação entre as Variáveis Numéricas - Heatmap')
plt.savefig(ANALISE_CRUZADA_DIR / 'heatmap_variaveis_numericas.png')
relatorio.append(f'Gráfico salvo em {ANALISE_CRUZADA_DIR}\\"heatmap_variaveis_numericas.png"')
plt.close()

relatorio.append('Correlação do número de acertos e da nota da redação na nota final:')

df1 = df_corr['nota_media'].drop('nota_media').sort_values(ascending=False).reset_index()

relatorio.append(f' - Correlação entre Nota da Redação e Nota Final: {df_corr.loc['nota_redacao', 'nota_media']:.2f} (Positiva Forte)')
relatorio.append(f' - Correlação entre Número de Acertos e Nota Final: {df_corr.loc['total_acertos', 'nota_media']:.2f} (Positiva Forte)')

relatorio.append('###############################################################')
# Análises por regressão linear:

relatorio.append(f'Regressão linear entre Nota da Redação e Nota Final:')

a, b, r, p_valor, stderr = stats.linregress(df['nota_redacao'], df['nota_media'])

relatorio.append(f' - Equação da reta: nota_media = {a:.2f} * nota_redacao + {b:.2f}')
relatorio.append(f' - Coeficiente R²: {r**2:.2f}')
relatorio.append(f' - P-valor: {p_valor:.2%} ({p_valor})')

sns.scatterplot(data=df, x='nota_redacao', y='nota_media')
plt.plot(df['nota_redacao'], a*df['nota_redacao']+b, color='red', label='Regressão Linear')
plt.title(f'Distribuição Nota Redação x Nota Final\nRegressão Linear: {a:.2f} * Nota Redação + {b:.2f}')
plt.ylabel(f'Nota Final')
plt.xlabel(f'Nota Redação')
plt.legend()

plt.tight_layout()
plt.savefig(ANALISE_CRUZADA_DIR / 'Regressao_linear_redacao_nota_final.png')
relatorio.append(f'Gráfico salvo em {ANALISE_CRUZADA_DIR}\\ "Regressao_linear_redacao_nota_final.png"')
plt.close()

relatorio.append('###############################################################')

relatorio.append(f'Regressão linear entre Total de Acertos e Nota Final:')

a, b, r, p_valor, stderr = stats.linregress(df['total_acertos'], df['nota_media'])

relatorio.append(f' - Equação da reta: nota_media = {a:.2f} * total_acertos + {b:.2f}')
relatorio.append(f' - Coeficiente R²: {r**2:.2f}')
relatorio.append(f' - P-valor: {p_valor:.2%} ({p_valor})')

sns.scatterplot(data=df, x='total_acertos', y='nota_media')
plt.plot(df['total_acertos'], a*df['total_acertos']+b, color='red', label='Regressão Linear')
plt.title(f'Distribuição Total de Acertos x Nota Final\nRegressão Linear: {a:.2f} * Total de Acertos + {b:.2f}')
plt.ylabel(f'Nota Final')
plt.xlabel(f'Total de Acertos')
plt.legend()

plt.tight_layout()
plt.savefig(ANALISE_CRUZADA_DIR / 'regressao_linear_acertos_nota_final.png')
relatorio.append(f'Gráfico salvo em {ANALISE_CRUZADA_DIR}\\ "regressao_linear_acertos_nota_final.png"')
plt.close()



















######################

with open(ANALISE_CRUZADA_DIR / 'relatorio_analises_cruzadas.txt', 'w', encoding='utf-8') as f:
    f.write('=== RELATÓRIO DO SCRIPT DE ANÁLISES CRUZADAS ===\n')
    f.write(f'Data: {pd.Timestamp.now()}\n')
    f.write(f'===============================================================\n')

    for i, linha in enumerate(relatorio, 1):
        f.write(f'{i} - {linha}\n')

    f.write(f'===============================================================\n')


