"""
Bloco 4: Estatística para Dados
Aula 07: Regressão Linear - Aplicação Prática
Data: 20/05/2026
Objetivo: Aprender a CALCULAR e INTERPRETAR regressão linear, na prática

CONTEÚDO:
1. A função stats.linregress() - explicada passo a passo
2. Como fazer previsões com o modelo
3. Como calcular R² e p-valor
4. Visualização da regressão
5. Interpretação de resultados para o negócio
6. Exercícios práticos
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.metrics import r2_score

print("="*50)
print("AULA 07 - REGRESSÃO LINEAR: APLICAÇÃO PRÁTICA")
print("="*50)

# ==========================================
# 1. A FUNÇÃO stats.linregress()
# ==========================================

print("\n1. A FUNÇÃO stats.linregress()")
print("-"*40)

"""
stats.linregress(x, y) é a função principal para regressão linear simples.

O QUE ELA FAZ:
- Recebe dois arrays (x e y) do mesmo tamanho
- Calcula a melhor reta que se ajusta aos dados
- Retorna: inclinação, intercepto, R², p-valor, erro padrão

PARÂMETROS:
- x: array com a variável independente (o que você USA para prever)
- y: array com a variável dependente (o que você quer PREVER)

O QUE ELA RETORNA (na ordem):
- slope: inclinação (coeficiente angular) - o nosso 'a' em y = a*x + b
- intercept: intercepto (coeficiente linear) - o nosso 'b' em y = a*x + b
- rvalue: coeficiente de correlação de Pearson (r)
- pvalue: p-valor (significância da regressão)
- stderr: erro padrão da inclinação

A PARTIR DISSO CALCULAMOS:
- r_squared = rvalue ** 2 (coeficiente de determinação - R²)
"""

print("--- EXEMPLO 1: HORAS DE ESTUDO E NOTA ---")

# Dados
horas = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
notas = np.array([4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0])

print(f"Horas de estudo: {horas}")
print(f"Notas obtidas: {notas}")

# Aplicando regressão
slope, intercept, rvalue, pvalue, stderr = stats.linregress(horas, notas)

print(f"\n--- RESULTADOS DA REGRESSÃO ---")
print(f"Inclinação (a): {slope:.4f}")
print(f"Intercepto (b): {intercept:.4f}")
print(f"Coeficiente de correlação (r): {rvalue:.4f}")
print(f"R² (r²): {rvalue**2:.4f}")
print(f"P-valor: {pvalue:.6f}")
print(f"Erro padrão da inclinação: {stderr:.4f}")

print(f"\n--- EQUAÇÃO DA RETA ---")
print(f"nota = {slope:.2f} * horas + {intercept:.2f}")

print(f"\n--- INTERPRETAÇÃO ---")
print(f"- A cada 1 hora de estudo, a nota aumenta em {slope:.2f} pontos")
print(f"- Com 0 horas de estudo, a nota prevista é {intercept:.2f}")
print(f"- O modelo explica {rvalue**2*100:.1f}% da variação nas notas (R²)")
print(f"- A relação é significativa? {'SIM' if pvalue < 0.05 else 'NÃO'} (p-valor = {pvalue:.4f})")

# ==========================================
# 2. COMO FAZER PREVISÕES COM O MODELO
# ==========================================

print("\n" + "="*50)
print("2. FAZENDO PREVISÕES COM O MODELO")
print("="*50)

"""
Com a equação y = a*x + b, podemos prever y para qualquer valor de x.

FÓRMULA: y_previsto = a * x_novo + b

ONDE:
- a: inclinação (slope)
- b: intercepto (intercept)
- x_novo: valor que queremos prever
"""

print("--- PREVISÕES ---")

# Prevendo nota para quem estudou 12 horas
horas_novo = 12
nota_prevista = slope * horas_novo + intercept
print(f"Quem estuda {horas_novo} horas: nota prevista = {nota_prevista:.1f}")

# Prevendo nota para quem estudou 0 horas (já temos no intercepto)
print(f"Quem estuda 0 horas: nota prevista = {intercept:.1f}")

# Prevendo quantas horas para tirar nota 10
# 10 = a*x + b → x = (10 - b) / a
nota_alvo = 10
horas_necessarias = (nota_alvo - intercept) / slope
print(f"Para tirar nota {nota_alvo}: precisa estudar {horas_necessarias:.1f} horas")

# ==========================================
# 3. VISUALIZAÇÃO DA REGRESSÃO
# ==========================================

print("\n" + "="*50)
print("3. VISUALIZAÇÃO DA REGRESSÃO")
print("="*50)

# # Plot
# plt.figure(figsize=(10, 6))
#
# # Dados reais
# plt.scatter(horas, notas, color='blue', alpha=0.7, label='Dados reais')
#
# # Reta de regressão
# x_line = np.array([0, 12])
# y_line = slope * x_line + intercept
# plt.plot(x_line, y_line, color='red', linewidth=2, label='Reta de regressão')
#
# # Personalização
# plt.xlabel('Horas de estudo')
# plt.ylabel('Nota')
# plt.title(f'Regressão Linear: Nota vs Horas de Estudo\nR² = {rvalue**2:.3f}, p-valor = {pvalue:.4f}')
# plt.legend()
# plt.grid(True, alpha=0.3)
# plt.tight_layout()
# plt.savefig('regressao_pratica.png')
# plt.show()
#
# print("✅ Gráfico salvo como 'regressao_pratica.png'")

# ==========================================
# 4. EXEMPLO COM DADOS REAIS (MARKETING E VENDAS)
# ==========================================

print("\n" + "="*50)
print("4. EXEMPLO REAL: MARKETING E VENDAS")
print("="*50)

# Dados: investimento em marketing (milhares) e vendas (milhares)
np.random.seed(42)

marketing = np.array([10, 12, 15, 18, 20, 22, 25, 28, 30, 35, 40, 45, 50, 55, 60])
vendas = 50 + 2.5 * marketing + np.random.normal(0, 5, len(marketing))

print("Dados: investimento em marketing (R$ mil) e vendas (R$ mil)")
print(f"Marketing: {marketing}")
print(f"Vendas: {vendas.round(0)}")

# Regressão
slope_m, intercept_m, r_m, p_m, stderr_m = stats.linregress(marketing, vendas)

print(f"\n--- RESULTADOS ---")
print(f"Equação: vendas = {slope_m:.2f} * marketing + {intercept_m:.2f}")
print(f"R²: {r_m**2:.4f}")
print(f"P-valor: {p_m:.6f}")

print(f"\n--- INTERPRETAÇÃO PARA O NEGÓCIO ---")
print(f"A cada R$ 1.000 investido em marketing, as vendas aumentam R$ {slope_m*1000:.0f}")
print(f"Mesmo sem marketing, a empresa venderia R$ {intercept_m*1000:.0f}")
print(f"O modelo explica {r_m**2*100:.1f}% da variação nas vendas")

if p_m < 0.05:
    print("A relação é estatisticamente significativa (p < 0.05)")
    print("✅ RECOMENDAÇÃO: Aumentar investimento em marketing")
else:
    print("A relação NÃO é estatisticamente significativa")
    print("⚠️ Recomendação: Coletar mais dados antes de decidir")

# ==========================================
# 5. REGRESSÃO COM PANDAS DATAFRAME
# ==========================================

print("\n" + "="*50)
print("5. REGRESSÃO COM PANDAS DATAFRAME")
print("="*50)

# Criando DataFrame
df = pd.DataFrame({
    'marketing': marketing,
    'vendas': vendas
})

print("DataFrame de exemplo:")
print(df.head())

# Regressão direto do DataFrame
slope_df, intercept_df, r_df, p_df, stderr_df = stats.linregress(df['marketing'], df['vendas'])

print(f"\nEquação: vendas = {slope_df:.2f} * marketing + {intercept_df:.2f}")
print(f"R²: {r_df**2:.4f}")

# ==========================================
# 6. INTERVALO DE CONFIANÇA PARA PREVISÕES
# ==========================================

print("\n" + "="*50)
print("6. INTERVALO DE CONFIANÇA PARA PREVISÕES")
print("="*50)

"""
Quando fazemos uma previsão, é importante dar uma MARGEM DE ERRO.

Para um nível de confiança de 95%:
- Previsão ± 1.96 * erro_padrao_da_previsao

Isso dá ao gerente uma IDEIA da incerteza.
"""

# ==========================================
# 6. INTERVALO DE CONFIANÇA PARA PREVISÕES
# ==========================================

print("\n" + "="*50)
print("6. INTERVALO DE CONFIANÇA PARA PREVISÕES")
print("="*50)

"""
Quando fazemos uma previsão, é importante dar uma MARGEM DE ERRO.

Para um nível de confiança de 95%:
- Previsão ± 1.96 * erro_padrao_da_previsao

Isso dá ao gerente uma IDEIA da incerteza.
"""

# Prevendo vendas para marketing = R$ 70.000
marketing_novo = 70
vendas_prevista = slope_m * marketing_novo + intercept_m

# Cálculo simplificado do erro padrão da previsão
n = len(marketing)
x_mean = np.mean(marketing)
x_novo = marketing_novo
sxx = np.sum((marketing - x_mean)**2)
mse = np.sum((vendas - (slope_m * marketing + intercept_m))**2) / (n - 2)

# Erro padrão da previsão
se_pred = np.sqrt(mse * (1 + 1/n + (x_novo - x_mean)**2 / sxx))

# Intervalo de confiança de 95%
z = 1.96
ic_lower = vendas_prevista - z * se_pred
ic_upper = vendas_prevista + z * se_pred

print(f"Marketing: R$ {marketing_novo}.000")
print(f"Previsão de vendas: R$ {vendas_prevista:.0f}.000")
print(f"Intervalo de Confiança (95%): R$ {ic_lower:.0f}.000 a R$ {ic_upper:.0f}.000")
print(f"\nTradução: temos 95% de confiança de que as vendas estarão")
print(f"entre R$ {ic_lower*1000:,.2f} e R$ {ic_upper*1000:,.2f}")

# ==========================================
# 7. GUIA RÁPIDO: REGRESSÃO LINEAR
# ==========================================

print("\n" + "="*50)
print("7. GUIA RÁPIDO - REGRESSÃO LINEAR")
print("="*50)

"""
PASSO A PASSO PARA UMA ANÁLISE DE REGRESSÃO:

1. COLETE OS DADOS
   - x: variável independente (ex: investimento)
   - y: variável dependente (ex: vendas)

2. VISUALIZE OS DADOS
   - Gráfico de dispersão (plt.scatter)
   - Verifique se a relação parece linear

3. EXECUTE A REGRESSÃO
   - slope, intercept, r, p, stderr = stats.linregress(x, y)

4. CALCULE R²
   - r_squared = r ** 2

5. INTERPRETE OS RESULTADOS
   - Inclinação (slope): impacto de x em y
   - R²: quanto o modelo explica
   - P-valor: se a relação é significativa

6. FAÇA PREVISÕES (se o modelo for bom)
   - y_pred = slope * x_novo + intercept

7. COMUNIQUE AO NEGÓCIO
   - Em português claro
   - Inclua intervalo de confiança
   - Mencione as limitações

FÓRMULAS IMPORTANTES:

| O que calcular | Como fazer |
|----------------|------------|
| Inclinação (a) | slope = stats.linregress(x, y)[0] |
| Intercepto (b) | intercept = stats.linregress(x, y)[1] |
| R²             | r_squared = stats.linregress(x, y)[2] ** 2 |
| P-valor        | pvalue = stats.linregress(x, y)[3] |
| Previsão       | y_pred = a * x_novo + b |
"""

# ==========================================
# 8. RESUMO DA AULA
# ==========================================

print("\n" + "="*50)
print("8. RESUMO - REGRESSÃO LINEAR (APLICAÇÃO PRÁTICA)")
print("="*50)

"""
✅ FUNÇÃO PRINCIPAL:
   - stats.linregress(x, y)
   - Retorna: (slope, intercept, rvalue, pvalue, stderr)

✅ O QUE CADA RESULTADO SIGNIFICA:
   - slope (a): inclinação - impacto de x em y
   - intercept (b): intercepto - valor de y quando x = 0
   - rvalue: correlação de Pearson
   - r_squared (rvalue²): R² - % da variação explicada
   - pvalue: significância estatística (p < 0.05 é bom)

✅ COMO FAZER PREVISÕES:
   - y_pred = a * x_novo + b
   - Para valores DENTRO do range dos dados (não extrapolar)

✅ O QUE INCLUIR NO RELATÓRIO:
   - Equação da reta
   - R² (explicação do modelo)
   - P-valor (confiabilidade)
   - Previsões com intervalo de confiança

📌 PARA O ANALISTA DE DADOS JR:
   1. SEMPRE visualize os dados ANTES da regressão
   2. R² > 0.7 é bom, mas não é o único critério
   3. P-valor < 0.05 indica relação significativa
   4. NUNCA extrapole além dos dados (ex: prever para x muito maior)
   5. Lembre: regressão mostra ASSOCIAÇÃO, não CAUSALIDADE
"""

# ==========================================
# EXERCÍCIOS - AULA 07 (PRÁTICOS)
# ==========================================

print("\n" + "="*50)
print("EXERCÍCIOS - REGRESSÃO LINEAR (APLICAÇÃO PRÁTICA)")
print("="*50)

# Dados para os exercícios
np.random.seed(42)

# Cenário: Uma empresa quer entender a relação entre tempo de experiência (anos)
# e salário (R$ mil) dos funcionários.

experiencia = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
salario = 3 + 0.8 * experiencia + np.random.normal(0, 0.5, len(experiencia))

# Garantir que salário não fique negativo
salario = np.maximum(salario, 0)

# print("\nDados para os exercícios:")
# print(f"Experiência (anos): {experiencia}")
# print(f"Salário (R$ mil): {salario.round(1)}")

# Criar DataFrame para facilitar
df_exerc = pd.DataFrame({
    'experiencia': experiencia,
    'salario': salario.round(1)
})

########################################################################
# NÍVEL 1-3: Aquecimento
########################################################################

"""
1. Executando regressão básica

# Usando os dados de 'experiencia' e 'salario':
# - Execute a regressão linear com stats.linregress()
# - Mostre: inclinação, intercepto, R², p-valor
# - Escreva a equação da reta
"""

"""
df = df_exerc.copy()

a, b, r, p, stderr = stats.linregress(df['experiencia'], df['salario'])

print(f'Inclinação: {a:.2f}')
print(f'Intercepto: {b:.2f}')
print(f'R²: {r**2:.4f}')
print(f'p-valor: {p:.4f}')
print(f'Equação da reta: salario = {a:.2f} * experiencia + {b:.2f}')


"""

########################################################################

"""
2. Interpretando os resultados

# Com base nos resultados do exercício 1:
# - Qual o impacto de cada ano de experiência no salário?
# - Qual o salário previsto para um funcionário sem experiência?
# - O modelo é significativo? (use α=0.05)
"""

"""
df = df_exerc.copy()

a, b, r, p, stderr = stats.linregress(df['experiencia'], df['salario'])

print(f'Impacto de cada ano de experiência no salário: R$ {a*1000:.2f}')
print(f'Salário previsto para um funcionário sem experiência: R$ {b*1000:.2f}')
print(f'O modelo é significativo? (α=0.05): {'Sim!' if p < 0.05 else 'Não'} (p-valor = {p:.4f})')
"""


########################################################################

"""
3. Fazendo previsões

# Use a equação encontrada para prever:
# - Salário para 20 anos de experiência
# - Salário para 0 anos (confere com intercepto?)
# - Quantos anos para atingir salário de R$ 20.000?
"""

"""
df = df_exerc.copy()

a, b, r, p, stderr = stats.linregress(df['experiencia'], df['salario'])

print(f'Salário para 20 anos de experiência: R$ {(a * 20 + b)*1000:,.2f}') # y = a * x + b
print(f'Salário para 0 anos de experiência: R$ {(a * 0 + b)*1000:,.2f} (intercepto: {b:.4f})')
print(f'Anos para atingir salário de R$ 20.000: {(20-b)/a:.0f} anos') # x = (y-b)/a
"""

########################################################################
# NÍVEL 4-6: Aplicação
########################################################################

"""
4. Visualização da regressão

# Crie um gráfico de dispersão dos dados (experiencia x salario)
# Adicione a reta de regressão
# Adicione título, rótulos e legenda
# Mostre a equação da reta no título do gráfico
"""

"""
df = df_exerc.copy()

a, b, r, p, stderr = stats.linregress(df['experiencia'], df['salario'])

sns.set_style('whitegrid')
sns.scatterplot(data=df, x='experiencia', y='salario')
plt.plot(df['experiencia'], a*df['experiencia']+b, '--r', label='curva regressão linear')

plt.title(f'Gráfico de dispersão - Experiência x Salário\nRegressão Linear: Salário = {a*1000:.2f} x Experiência + {b*1000:.2f}')
plt.ylabel('Salário (R$ mil)')
plt.xlabel('Experiência (anos)')
plt.legend()
plt.xlim(0)
plt.ylim(0)

plt.tight_layout()
plt.show()
"""

########################################################################

"""
5. Intervalo de confiança

# Para um funcionário com 10 anos de experiência:
# - Calcule o salário previsto
# - Calcule o intervalo de confiança de 95%
# - Interprete o resultado em português
"""

"""
df = df_exerc.copy()
a, b, r, p, stderr = stats.linregress(df['experiencia'], df['salario'])

exp_test = 10
salario_prev = a * exp_test + b

print(f'Salário previsto para um funcionário com 10 anos de experiência: R${salario_prev*1000:,.2f}')

# calculo do IC

n = df['experiencia'].count()
x_mean = df['experiencia'].mean()
x_novo = exp_test
sxx = ((df['experiencia'] - x_mean)**2).sum()
mse = ((df['salario'] - (a * df['experiencia'] + b))**2).sum()/(n-2)
se_pred = (mse * (1 + 1/n + (x_novo - x_mean)**2 / sxx))**(1/2)

z = 1.96
ic_lower = salario_prev - z * se_pred
ic_upper = salario_prev + z * se_pred

print(f'O intervalo de confiança (95%) dessa previsão é: R${ic_lower*1000:,.2f} a R${ic_upper*1000:,.2f}')

"""

########################################################################

"""
6. Comparação com dados reais

# Um funcionário com 8 anos de experiência ganha R$ 12.000
# O modelo superestimou ou subestimou? Por quanto?
# Isso é aceitável? (erro vs resíduo)
"""

"""
df = df_exerc.copy()
a, b, r, p, stderr = stats.linregress(df['experiencia'], df['salario'])

salario_8_prev = a * 8 + b

salario_8_dado = 12

print(f'O modelo superestimou ou subestimou? Por quanto?')
if salario_8_prev < salario_8_dado:
    print(f'O modelo subestimou por R${(salario_8_prev-salario_8_dado)*1000:,.2f}')
elif salario_8_prev > salario_8_dado:
    print(f'O modelo superestimou por R${(salario_8_prev-salario_8_dado)*1000:,.2f}')
else:
    print(f'Correspondência perfeita entre dado e modelo')

print('\nIsso é aceitável?')

exp_test = 8
salario_prev = a * exp_test + b

print(f' - Salário previsto para um funcionário com 10 anos de experiência: R${salario_prev*1000:,.2f}')

# calculo do IC

n = df['experiencia'].count()
x_mean = df['experiencia'].mean()
x_novo = exp_test
sxx = ((df['experiencia'] - x_mean)**2).sum()
mse = ((df['salario'] - (a * df['experiencia'] + b))**2).sum()/(n-2)
se_pred = (mse * (1 + 1/n + (x_novo - x_mean)**2 / sxx))**(1/2)

z = 1.96
ic_lower = salario_prev - z * se_pred
ic_upper = salario_prev + z * se_pred

print(f' - O intervalo de confiança (95%) dessa previsão é: R${ic_lower*1000:,.2f} a R${ic_upper*1000:,.2f}')

print(f'\nResultado da análise:')

if ic_lower <= salario_8_dado <= ic_upper:
    print(f'- Salário dado (R${salario_8_dado*1000:,.2f}) está dentro do IC previsto')
elif ic_lower > salario_8_dado:
    print(f'- Salário dado (R${salario_8_dado*1000:,.2f}) é menor que o IC inferior (R${ic_lower*1000:,.2f})')
    print(f'- Diferença absoluta: {(salario_8_dado-ic_lower)*1000:,.2f}')
    print(f'- Diferença relativa: {((salario_8_dado/ic_lower)-1):.2%}')
elif ic_upper < salario_8_dado:
    print(f'- Salário dado (R${salario_8_dado*1000:,.2f}) é maior que o IC superior (R${ic_upper*1000:,.2f})')
    print(f'- Diferença absoluta: R${(salario_8_dado-ic_upper)*1000:,.2f}')
    print(f'- Diferença relativa: {((salario_8_dado/ic_upper)-1):.2%}')
"""

########################################################################
# NÍVEL 7-8: Manipulação
########################################################################

"""
7. Análise de resíduos

# Calcule os resíduos (diferença entre valor real e previsto)
# Crie um gráfico de resíduos (x = experiência, y = resíduo)
# O que você observa? Os resíduos parecem aleatórios?
"""

"""
df = df_exerc.copy()
a, b, r, p, stderr = stats.linregress(df['experiencia'], df['salario'])

df['previsto'] = a * df['experiencia'] + b

df['residuo'] = df['salario'] - df['previsto']

# print(df)

sns.set_style('whitegrid')

sns.scatterplot(data=df, x='experiencia', y='salario', label='exp x salario')
sns.lineplot(data=df, x='experiencia', y='previsto', color='red', linestyle='--', label='exp x prev')
sns.scatterplot(data=df, x='experiencia', y='residuo', label='exp x residuo')

plt.axhline(0, color='black', linestyle='--')

plt.xlim(0)
plt.show()

# Eu pude observar que o plot dos resíduos ficam em torno de y=0, com baixa dispersão. 
# Isso provavelmente é um bom sinal e tbm indica que se eu fizesse uma regressão linear
# dos resíduos relativamente à reta y=0, o r2 seria bem alto.
"""

########################################################################

"""
8. Comparação entre grupos

# Separe os dados em dois grupos:
# - Júnior: experiência < 5 anos
# - Sênior: experiência >= 5 anos
#
# Execute regressão separada para cada grupo
# Compare as inclinações. O que isso sugere?
"""

"""
df = df_exerc.copy()

df_j = df[df['experiencia']<5]
df_s = df[df['experiencia']>=5]

# Grupo júnior

a_j, b_j, r_j, p_j, stderr_j = stats.linregress(df_j['experiencia'], df_j['salario'])
df_j['previsto'] = a_j * df_j['experiencia'] + b_j

print(f'Grupo Júnior:')
print(f' - Inclinação: {a_j:.2f}')
print(f' - Intercepto: {b_j:.2f}')
print(f' - R²: {r_j**2:.4f}')
print(f' - p-valor: {p_j:.4f}')
print(f' - Equação da reta: salario = {a_j:.2f} * experiencia + {b_j:.2f}')


# Grupo sênior

a_s, b_s, r_s, p_s, stderr_s = stats.linregress(df_s['experiencia'], df_s['salario'])
df_s['previsto'] = a_s * df_s['experiencia'] + b_s

print(f'Grupo Sênior:')
print(f' - Inclinação: {a_s:.2f}')
print(f' - Intercepto: {b_s:.2f}')
print(f' - R²: {r_s**2:.4f}')
print(f' - p-valor: {p_s:.4f}')
print(f' - Equação da reta: salario = {a_s:.2f} * experiencia + {b_s:.2f}')


sns.set_style('whitegrid')

sns.scatterplot(data=df_j, x='experiencia', y='salario', label='exp x sal (jr)')
sns.lineplot(data=df_j, x='experiencia', y='previsto', linestyle='--', label='exp x prev (jr)')

sns.scatterplot(data=df_s, x='experiencia', y='salario', label='exp x sal (se)')
sns.lineplot(data=df_s, x='experiencia', y='previsto', linestyle='--', label='exp x prev (se)')

plt.tight_layout()
plt.show()

# O gráfico dos jr tem uma inclinação maior e intercepto menor, enquanto o grafico do senior faz o contrário.
# O que pode indicar que no começo, o crescimento salarial é alto, mas ao longo do tempo ele vai se estabilizando.
# Isso me faz pensar que a melhor regressao nesse caso seja algo como um logaritmo. Cresce rapido e depois estabiliza.
"""

########################################################################
# NÍVEL 9-10: Desafios
########################################################################

"""
9. Dashboard de regressão

# Crie um dashboard com 2 subplots (1 linha, 2 colunas):
# (0) Gráfico de dispersão com reta de regressão
# (1) Gráfico de resíduos
#
# Adicione as estatísticas principais (R², p-valor, equação)
# Salve a figura como 'dashboard_regressao.png'
"""

"""
df = df_exerc.copy()
a, b, r, p, stderr = stats.linregress(df['experiencia'], df['salario'])

df['previsto'] = a * df['experiencia'] + b

df['residuo'] = df['salario'] - df['previsto']

# print(df)

plt.figure(figsize=(14, 6))
sns.set_style('whitegrid')

plt.subplot(1, 2, 1)
sns.scatterplot(data=df, x='experiencia', y='salario', label='exp x salario')
sns.lineplot(data=df, x='experiencia', y='previsto', color='red', linestyle='--', label='exp x prev')
plt.title(f'Gráfico de dispersão - Experiência x Salário')
plt.xlim(0)
plt.ylim(0)

plt.subplot(1, 2, 2)
sns.scatterplot(data=df, x='experiencia', y='residuo', label='exp x residuo', color='orange')
plt.axhline(0, color='black', linestyle='--', label='y=0')
plt.axhline(df['residuo'].min(), color='skyblue', linestyle='--', label='res min')
plt.axhline(df['residuo'].max(), color='skyblue', linestyle='--', label='res max')
plt.title('Gráfico de dispersão Resíduo da Previsão x Salário')
plt.xlim(0 , 10)
plt.ylim(-10, 10)

plt.suptitle(f'Regressão Linear: Salário = {a*1000:.2f} x Experiência + {b*1000:.2f}\nR²: {r**2:.2f} | p-valor: {p:.4f}')
plt.tight_layout()
plt.show()
"""

########################################################################

"""
10. DESAFIO FINAL: Relatório executivo

# Com base na regressão entre experiência e salário:
# 
# A empresa quer saber se deve investir em programas de retenção
# de funcionários seniores (que têm mais experiência).
#
# Escreva um relatório de 2-3 parágrafos para o gerente:
# 
# 1. Qual o impacto real da experiência no salário?
# 2. O modelo é confiável? (R², p-valor)
# 3. Quanto um funcionário com 15 anos de experiência ganha a mais
#    que um com 5 anos?
# 4. Qual sua recomendação sobre investir em retenção?
#
# Use linguagem clara, sem jargões estatísticos.
"""

df = df_exerc.copy()
a, b, r, p, stderr = stats.linregress(df['experiencia'], df['salario'])

print(f'Inclinação: {a:.2f}')
print(f'Intercepto: {b:.2f}')
print(f'R²: {r**2:.4f}')
print(f'p-valor: {p:.4f}')
print(f'Equação da reta: salario = {a:.2f} * experiencia + {b:.2f}')

print(f'\nDe acordo com nosso modelo teórico, os salários iniciam a partir de R${b*1000:,.2f} para um funcionário sem experiência')
print(f'A medida que o funcionário vai ganhando experiência, a cada 1 ano de experiência, é previsto um aumento de R${a*1000:,.2f} em seu salário')
print(f'Nosso modelo teórico é confiável, visto que ele comporta a variância de {r**2:.2%} dos dados')
print(f'E esse resultado não é por acaso, visto que a chance de obtermos esses mesmos resultado caso o modelo estivesse errado é de apenas {p:.11%}')
print(f'Um funcionário com 15 anos de experiência ganha em média: R${(a*15+b)*1000:,.2f} enquanto um funcionário com 5 anos ganha em média R${(a*5+b)*1000:,.2f}')
print(f'Isso representa uma diferença absoluta de R${((a*15+b)-(a*5+b))*1000:,.2f}, que equivale a uma diferença relativa de {((a * 15 + b) / (a * 5 + b)) - 1:.2%}')
print(f'Acredito que nossa empresa oferece um bom plano de carreira para nossos funcionários e não corremos risco de perdê-los para outras empresas')
print(f'Entretanto, recomendo que seja feita uma pesquisa sobre satisfação de cada funcionário, para podermos analisarmos a correlação entre avaliação, experiência e salário')
