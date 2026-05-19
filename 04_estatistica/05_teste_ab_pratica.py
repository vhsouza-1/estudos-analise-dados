"""
Bloco 4: Estatística para Dados
Aula 05: Teste A/B - Aplicação Prática
Data: 19/05/2026
Objetivo: Aprender a CALCULAR e INTERPRETAR testes A/B na prática

CONTEÚDO:
1. Cálculo do tamanho da amostra (antes do teste)
2. Teste para proporções (conversão, cliques, etc.)
3. Teste para médias (tempo, valor, etc.)
4. Intervalos de confiança
5. Interpretação dos resultados
6. Exercícios práticos
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from statsmodels.stats.proportion import proportions_ztest, proportion_effectsize, confint_proportions_2indep
from statsmodels.stats.power import NormalIndPower

print("="*50)
print("AULA 05 - TESTE A/B: APLICAÇÃO PRÁTICA")
print("="*50)

# ==========================================
# 1. CÁLCULO DO TAMANHO DA AMOSTRA (ANTES DO TESTE!)
# ==========================================

print("\n1. CÁLCULO DO TAMANHO DA AMOSTRA")
print("-"*40)

"""
ANTES DE RODAR QUALQUER TESTE A/B, você precisa saber:
"Quantos usuários preciso em cada grupo?"

Se a amostra for PEQUENA DEMAIS:
- Você pode perder uma diferença REAL (Erro Tipo II)
- Seu resultado será inconclusivo

Se a amostra for GRANDE DEMAIS:
- Você gasta tempo e recurso desnecessariamente

FÓRMULA SIMPLIFICADA (para proporções):

n = (z_alpha/2 + z_power)² * [p0*(1-p0) + p1*(1-p1)] / (p1 - p0)²

Onde:
- p0 = conversão atual (baseline)
- p1 = conversão que queremos detectar
- z_alpha/2 = 1.96 para α=0.05 (bilateral)
- z_power = 0.84 para poder=80%

NA PRÁTICA: Vamos usar a função do statsmodels que faz essa conta para nós.
"""

print("--- EXEMPLO: TAMANHO DA AMOSTRA PARA TESTE DE CONVERSÃO ---")

# Parâmetros
baseline = 0.05      # conversão atual: 5%
efeito_minimo = 0.01 # queremos detectar aumento para 6% (1 ponto percentual)
alpha = 0.05         # nível de significância
power = 0.80         # poder desejado (80%)

print(f"Conversão atual (p0): {baseline*100:.1f}%")
print(f"Conversão desejada (p1): {(baseline + efeito_minimo)*100:.1f}%")
print(f"Nível de significância (α): {alpha}")
print(f"Poder desejado (1-β): {power}")

# Método 1: Usando função do statsmodels
effect_size = proportion_effectsize(baseline, baseline + efeito_minimo)
n = NormalIndPower().solve_power(
    effect_size=effect_size,
    alpha=alpha,
    power=power,
    alternative='two-sided'
)

print(f"\n📊 Tamanho da amostra necessário POR GRUPO: {n:.0f} usuários")
print(f"📊 Total de usuários necessários: {n*2:.0f}")

print("\n💡 INTERPRETAÇÃO:")
print(f"Com {n:.0f} usuários por grupo, conseguimos detectar")
print(f"um aumento de {efeito_minimo*100:.1f}% na conversão")
print(f"com {power*100:.0f}% de confiança (poder) e {alpha*100:.0f}% de chance de erro Tipo I.")

# ==========================================
# 2. TESTE PARA PROPORÇÕES (EX: CONVERSÃO, CLIQUE, COMPRA)
# ==========================================

print("\n" + "="*50)
print("2. TESTE PARA PROPORÇÕES")
print("="*50)

"""
TESTE Z DE PROPORÇÕES: compara duas taxas (ex: % de conversão)

QUANDO USAR:
- Resultado é SIM/NÃO (comprou/não comprou, clicou/não clicou)
- Amostra grande (geralmente n > 30 por grupo)

O QUE PRECISAMOS:
- Número de sucessos no grupo A (ex: quantas compras)
- Número de sucessos no grupo B
- Tamanho do grupo A
- Tamanho do grupo B

A FUNÇÃO proportions_ztest:
proportions_ztest(count, nobs, alternative='two-sided')

Parâmetros:
- count: lista [sucessos_A, sucessos_B]
- nobs: lista [n_A, n_B]
- alternative: 'two-sided' (diferente), 'larger' (maior), 'smaller' (menor)
"""

print("--- EXEMPLO 1: TESTE DE CONVERSÃO DE COMPRA ---")

# Cenário: nova página de checkout
n_A = 2000
conversoes_A = 100  # 5% de conversão

n_B = 2000
conversoes_B = 130  # 6.5% de conversão

print(f"Versão A (atual): {conversoes_A}/{n_A} = {conversoes_A/n_A*100:.2f}%")
print(f"Versão B (nova): {conversoes_B}/{n_B} = {conversoes_B/n_B*100:.2f}%")

# Teste bilateral (queremos saber se é DIFERENTE)
count = np.array([conversoes_A, conversoes_B])
nobs = np.array([n_A, n_B])

z_stat, p_valor = proportions_ztest(count, nobs, alternative='two-sided')

print(f"\n--- RESULTADO DO TESTE ---")
print(f"Estatística Z: {z_stat:.3f}")
print(f"P-valor: {p_valor:.4f}")

alpha = 0.05
print(f"Nível de significância: α = {alpha}")

if p_valor < alpha:
    print("\n✅ REJEITAMOS H0")
    print("   A diferença é ESTATISTICAMENTE SIGNIFICATIVA")
    print(f"   Aumento absoluto: {(conversoes_B/n_B - conversoes_A/n_A)*100:.2f} pontos percentuais")
    print(f"   Aumento relativo: {((conversoes_B/n_B)/(conversoes_A/n_A)-1)*100:.1f}%")
else:
    print("\n❌ NÃO REJEITAMOS H0")
    print("   Não há evidência suficiente de diferença")
    print("   A diferença observada pode ser devida ao acaso")

# Teste unilateral (queremos saber se B é MELHOR que A)
z_stat_one, p_valor_one = proportions_ztest(count, nobs, alternative='larger')

print(f"\n--- TESTE UNILATERAL (B é melhor que A?) ---")
print(f"P-valor unilateral: {p_valor_one:.4f}")

if p_valor_one < alpha:
    print("✅ B é ESTATISTICAMENTE MELHOR que A")
else:
    print("❌ Não podemos afirmar que B é melhor que A")

# ==========================================
# 3. INTERVALO DE CONFIANÇA PARA DIFERENÇA DE PROPORÇÕES
# ==========================================

print("\n" + "="*50)
print("3. INTERVALO DE CONFIANÇA PARA DIFERENÇA DE PROPORÇÕES")
print("="*50)

"""
INTERVALO DE CONFIANÇA (IC): mostra a MAGNITUDE do efeito

- IC de 95%: se repetíssemos o teste muitas vezes, 95% dos intervalos
  conteriam o valor real da diferença

- É MAIS INFORMATIVO que o p-valor sozinho!

INTERPRETAÇÃO:

Se IC = [0.005, 0.025] (0.5% a 2.5%):
   - O efeito é POSITIVO (intervalo todo acima de zero)
   - Aumento real está entre 0.5% e 2.5%

Se IC = [-0.005, 0.015] (-0.5% a 1.5%):
   - O intervalo CONTÉM ZERO
   - O efeito pode ser nulo (não conclusivo)
   - Consistente com p-valor > 0.05
"""

print("--- INTERVALO DE CONFIANÇA (MÉTODO MANUAL SIMPLIFICADO) ---")

# Cálculo manual do IC (aproximado)
pA = conversoes_A / n_A
pB = conversoes_B / n_B
diff = pB - pA

# Erro padrão
se = np.sqrt(pA*(1-pA)/n_A + pB*(1-pB)/n_B)

# IC de 95% (z = 1.96)
z = 1.96
ic_lower = diff - z * se
ic_upper = diff + z * se

print(f"Diferença observada (B - A): {diff*100:.2f} pontos percentuais")
print(f"Intervalo de Confiança (95%): [{ic_lower*100:.2f}%, {ic_upper*100:.2f}%]")

if ic_lower > 0:
    print("✅ Intervalo TODO acima de zero → efeito POSITIVO confirmado")
elif ic_upper < 0:
    print("✅ Intervalo TODO abaixo de zero → efeito NEGATIVO confirmado")
else:
    print("⚠️ Intervalo contém zero → resultado NÃO CONCLUSIVO")

# ==========================================
# 4. TESTE PARA MÉDIAS (EX: TEMPO NA PÁGINA, VALOR DO PEDIDO)
# ==========================================

print("\n" + "="*50)
print("4. TESTE PARA MÉDIAS - TESTE T")
print("="*50)

"""
TESTE T DE STUDENT: compara duas médias

QUANDO USAR:
- Dados contínuos (tempo, valor, idade)
- Distribuição aproximadamente normal (ou amostra grande)

A FUNÇÃO ttest_ind:
stats.ttest_ind(grupoA, grupoB, equal_var=False)

Parâmetros:
- grupoA: array com os valores do grupo A
- grupoB: array com os valores do grupo B
- equal_var=False: assume variâncias diferentes (mais seguro)
"""

np.random.seed(42)

# Simulando dados
n = 100

# Grupo A (atual): média 120s, desvio 30s
tempo_A = np.random.normal(120, 30, n)

# Grupo B (nova): média 130s, desvio 32s
tempo_B = np.random.normal(130, 32, n)

print("--- EXEMPLO: TESTE DE TEMPO NA PÁGINA ---")
print(f"Versão A: média = {tempo_A.mean():.1f}s, desvio = {tempo_A.std():.1f}s")
print(f"Versão B: média = {tempo_B.mean():.1f}s, desvio = {tempo_B.std():.1f}s")

# Teste t (bilateral - queremos saber se é DIFERENTE)
t_stat, p_valor = stats.ttest_ind(tempo_A, tempo_B, equal_var=False)

print(f"\n--- RESULTADO DO TESTE ---")
print(f"Estatística t: {t_stat:.3f}")
print(f"P-valor: {p_valor:.4f}")

if p_valor < 0.05:
    print("\n✅ Diferença ESTATISTICAMENTE SIGNIFICATIVA")
    print(f"   Diferença: {(tempo_B.mean() - tempo_A.mean()):.1f} segundos")
else:
    print("\n❌ Diferença NÃO SIGNIFICATIVA estatisticamente")

# ==========================================
# 5. INTERVALO DE CONFIANÇA PARA DIFERENÇA DE MÉDIAS
# ==========================================

print("\n" + "="*50)
print("5. INTERVALO DE CONFIANÇA PARA DIFERENÇA DE MÉDIAS")
print("="*50)

"""
Intervalo de confiança para diferença de médias.
"""

diff_mean = tempo_B.mean() - tempo_A.mean()
se_mean = np.sqrt(tempo_A.var()/n + tempo_B.var()/n)

ic_mean_lower = diff_mean - z * se_mean
ic_mean_upper = diff_mean + z * se_mean

print(f"Diferença observada (B - A): {diff_mean:.1f} segundos")
print(f"Intervalo de Confiança (95%): [{ic_mean_lower:.1f}, {ic_mean_upper:.1f}] segundos")

if ic_mean_lower > 0:
    print("✅ Intervalo TODO acima de zero → aumento de tempo confirmado")
elif ic_mean_upper < 0:
    print("✅ Intervalo TODO abaixo de zero → redução de tempo confirmada")
else:
    print("⚠️ Intervalo contém zero → resultado NÃO CONCLUSIVO")

# ==========================================
# 6. GUIA RÁPIDO: QUAL TESTE USAR?
# ==========================================

print("\n" + "="*50)
print("6. GUIA RÁPIDO - QUAL TESTE USAR?")
print("="*50)

"""
| Situação                           | Tipo de dado | Teste        | Função               |
|------------------------------------|--------------|--------------|----------------------|
| Comparar taxas (conversão, clique) | Proporções   | Z-test       | proportions_ztest()  |
| Comparar médias (tempo, valor)     | Contínuo     | T-test       | stats.ttest_ind()    |
| Amostra pequena (<30)              | Contínuo     | T-test       | stats.ttest_ind()    |
| Dados não-normais                  | Contínuo     | Mann-Whitney | stats.mannwhitneyu() |

PASSO A PASSO PARA UM TESTE A/B COMPLETO:

1. ANTES DE RODAR:
   - Defina p0 (baseline) e efeito mínimo desejado
   - Calcule o tamanho da amostra necessário

2. DURANTE O TESTE:
   - Colete os dados até atingir o tamanho planejado
   - NÃO OLHE os resultados antes (evita viés)

3. DEPOIS DO TESTE:
   - Calcule p-valor
   - Calcule intervalo de confiança
   - Interprete a MAGNITUDE do efeito (não só o p-valor)
   - Decida com base no impacto para o negócio
"""

# ==========================================
# 7. EXEMPLO COMPLETO - RELATÓRIO EXECUTIVO
# ==========================================

print("\n" + "="*50)
print("7. EXEMPLO COMPLETO - RELATÓRIO EXECUTIVO")
print("="*50)

print("""
--- CASO: NOVA PÁGINA DE CHECKOUT ---

RESULTADOS DO TESTE A/B:

- Versão A (atual): 2000 visitas, 100 conversões (5.00%)
- Versão B (nova): 2000 visitas, 130 conversões (6.50%)
- P-valor: 0.026 (estatisticamente significativo com α=0.05)
- Intervalo de Confiança (95%): [0.2%, 2.8%]

INTERPRETAÇÃO PARA O NEGÓCIO:

1. O que aconteceu?
   A nova página de checkout teve uma taxa de conversão 1.5 ponto percentual maior 
   que a versão atual (6.5% vs 5.0%).

2. Isso é confiável?
   Sim. A probabilidade dessa diferença ser apenas coincidência é de apenas 2.6%,
   abaixo do limite tradicional de 5%.

3. Qual o impacto esperado?
   Com 95% de confiança, o aumento real está entre 0.2% e 2.8%.
   O ponto médio é 1.5%.

4. Quanto isso representa em receita?
   Para cada 10.000 visitantes:
   - Versão atual: 500 conversões
   - Versão nova: 650 conversões (estimado)
   - Ganho: 150 conversões adicionais

5. Recomendação:
   Implementar a nova página de checkout. O ganho estimado compensa 
   o custo de desenvolvimento (avaliar com time de produto).
""")

# ==========================================
# RESUMO DA AULA
# ==========================================

print("\n" + "="*50)
print("8. RESUMO - TESTE A/B (APLICAÇÃO PRÁTICA)")
print("="*50)

"""
✅ TAMANHO DA AMOSTRA (antes do teste):
   - proportion_effectsize(p0, p1)
   - NormalIndPower().solve_power()

✅ TESTE PARA PROPORÇÕES:
   - proportions_ztest(count, nobs, alternative='two-sided')
   - Retorna: estatística z, p-valor

✅ TESTE PARA MÉDIAS:
   - stats.ttest_ind(grupoA, grupoB, equal_var=False)
   - Retorna: estatística t, p-valor

✅ INTERVALO DE CONFIANÇA:
   - Mostra a MAGNITUDE do efeito
   - Se contém zero → não conclusivo
   - Se todo acima/abaixo de zero → efeito confirmado

✅ REGRA DE DECISÃO (α=0.05):
   - p-valor < 0.05 → rejeitamos H0
   - p-valor ≥ 0.05 → não rejeitamos H0

📌 PARA O ANALISTA DE DADOS JR:
   1. CALCULE o tamanho da amostra ANTES do teste
   2. RELATÓRIO deve ter p-valor E intervalo de confiança
   3. TRADUZA para linguagem de negócio
   4. LEMBRE: significância estatística ≠ relevância prática
"""
# ==========================================
# EXERCÍCIOS - AULA 05 (PRÁTICOS)
# ==========================================

print("\n" + "="*50)
print("EXERCÍCIOS - TESTE A/B (APLICAÇÃO PRÁTICA)")
print("="*50)

# Dados para os exercícios
np.random.seed(42)

"""
Cenário para exercícios:

Uma plataforma de e-learning quer testar duas versões da página inicial:
- Versão A (atual): layout padrão
- Versão B (nova): layout com recomendações personalizadas

Métricas coletadas:
- taxa de clique (CTR): cliques / visualizações
- tempo na página (segundos)
- taxa de conversão (usuários que compraram o curso)
"""

# Simular dados (você vai usar estes dados nos exercícios)
n_usuarios = 1000

# Taxa de clique (CTR)
ctr_A = np.random.binomial(1, 0.10, n_usuarios)  # 10% de clique
ctr_B = np.random.binomial(1, 0.12, n_usuarios)  # 12% de clique

# Tempo na página (segundos)
tempo_A = np.random.normal(120, 40, n_usuarios)
tempo_B = np.random.normal(135, 45, n_usuarios)

# Conversão (compra de curso)
conv_A = np.random.binomial(1, 0.05, n_usuarios)  # 5% conversão
conv_B = np.random.binomial(1, 0.06, n_usuarios)  # 6% conversão

# print("\nDados simulados para os exercícios:")
# print(f"CTR - A: {ctr_A.mean()*100:.1f}% | B: {ctr_B.mean()*100:.1f}%")
# print(f"Tempo - A: {tempo_A.mean():.1f}s | B: {tempo_B.mean():.1f}s")
# print(f"Conversão - A: {conv_A.mean()*100:.1f}% | B: {conv_B.mean()*100:.1f}%")

########################################################################
# NÍVEL 1-3: Aquecimento
########################################################################

"""
1. Tamanho da amostra

# Uma empresa tem conversão atual de 8% (p0=0.08)
# Quer detectar um aumento para 10% (p1=0.10)
# Calcule quantos usuários precisa por grupo
# Use α=0.05 e poder=80%
"""

"""
p0 = 0.08
p1 = 0.1
aumento = p1 - p0

alpha = 0.05
power = 0.8

effect_size = proportion_effectsize(p0, p1)

n = NormalIndPower().solve_power(
    alpha=alpha,
    power=power,
    effect_size=effect_size,
    alternative='two-sided'
)

print(f'A empresa precisa de {np.ceil(n):.0f} usuários por grupo')
"""

########################################################################

"""
2. Teste de proporções (CTR)

# Use os dados de CTR (ctr_A e ctr_B)
# Calcule:
# - Quantos cliques em cada grupo
# - Execute o teste de proporções
# - Mostre p-valor e conclusão
"""


"""
print(f'Quantos cliques em cada grupo:')
print(f'Grupo A: {ctr_A.sum()} | Grupo B: {ctr_B.sum()}')

n_A = len(ctr_A)
n_B = len(ctr_B)

conv_A = ctr_A.sum()
conv_B = ctr_B.sum()

count = np.array([conv_A, conv_B])
nobs = np.array([n_A, n_B])

z_stat, p = proportions_ztest(count, nobs, alternative='two-sided')

print(f'O p-valor do teste foi: {p:.4f}')

alpha = 0.05

print(f'Para alpha: {alpha*100}%')
if p < alpha:
    print(f'O resultado tem relevância estatística!')
else:
    print(f'Não houve relevância estatística.')
    print(f'O resultado pode ter sido por acaso.')
"""



########################################################################

"""
3. Teste de médias (tempo na página)

# Use os dados de tempo (tempo_A e tempo_B)
# Execute o teste t para comparar as médias
# Mostre:
# - Médias dos dois grupos
# - Estatística t e p-valor
# - Conclusão (houve diferença significativa?)
"""

"""
t_stat, p_valor = stats.ttest_ind(tempo_A, tempo_B)

print(f'A média dos dois grupos foram:')
print(f'Grupo A: {tempo_A.mean():.2f}s | Grupo B: {tempo_B.mean():.2f}s')

print(f'\nA estatística t do teste foi: {t_stat:.2f}')
print(f'O p-valor do teste foi: {p_valor}')

alpha = 0.05

print(f'\nPara alpha = {alpha*100}%:')
if p_valor < alpha:
    print(f'Houve diferença significativa!')
    print(f'Diferença absoluta entre as médias: {np.abs(tempo_A.mean()-tempo_B.mean()):.2f}s')
    print(f'Diferença relativa entre as médias: {np.abs(tempo_A.mean()-tempo_B.mean())/tempo_A.mean()*100:.2f}%')
else:
    print(f'A diferença pode ser apenas por acaso.')
"""

########################################################################
# NÍVEL 4-6: Aplicação
########################################################################

"""
4. Intervalo de confiança para proporções

# Com base no teste de conversão (conv_A e conv_B):
# - Calcule a diferença observada
# - Calcule o intervalo de confiança de 95%
# - O intervalo contém zero? O que isso significa?
"""

"""
pA = conv_A.mean()
pB = conv_B.mean()

diff = pB-pA

print(f'A diferença observada é de {diff*100:.2f}%')

ic_diff = confint_proportions_2indep(conv_A.sum(), len(conv_A), conv_B.sum(), len(conv_B), alpha=0.05)

print(f'\nIntervalo de Confiança (95%): {ic_diff[0]*100:.2f}% a {ic_diff[1]*100:.2f}%\n')

if ic_diff[0] > 0 and ic_diff[1] > 0:
    print(f'Todo IC (95%) é positivo')
    print(f'Aumento confirmado')
elif ic_diff[0] < 0 and ic_diff[1] < 0:
    print(f'Todo IC (95%) é negativo')
    print(f'Redução confirmada')
else:
    print(f'IC (95%) contém zero')
    print(f'Resultado inconclusivo')
"""

########################################################################

"""
5. Teste unilateral

# Execute um teste UNILATERAL para a conversão
# Queremos saber se a versão B é MELHOR que a A
# Use alternative='larger' no proportions_ztest
# Compare com o resultado bilateral
"""

"""
count = np.array([conv_A.sum(), conv_B.sum()])
nobs = np.array([len(conv_A), len(conv_B)])

z_stat_uni, p_valor_uni = proportions_ztest(count, nobs, alternative='larger')

print(f'p-valor unilateral: {p_valor_uni:.4f}')

z_stat_bi, p_valor_bi = proportions_ztest(count, nobs, alternative='two-sided')

print(f'p-valor bilateral: {p_valor_bi:.4f}')

print(f'Os dois valores de p são altos, entretanto, o unilateral é ainda maior')
print(f'Acredito que isso indique que a chance dos dois ser diferentes é baixa')
print(f'Mas a chance de B ser melhor é ainda menor')
"""

########################################################################

"""
6. Interpretação de resultados

# Com base nos resultados dos exercícios 2, 3 e 4:
# Escreva um relatório de 1 parágrafo para o gerente:
# - O layout novo melhorou o CTR?
# - O layout novo melhorou o tempo na página?
# - O layout novo melhorou a conversão?
# - Qual sua recomendação final?
"""

"""
alpha = 0.05
print(f'Para alpha: {alpha:.2%}')

count_ctr = np.array([ctr_A.sum(), ctr_B.sum()])
nobs_ctr = np.array([len(ctr_A), len(ctr_B)])

_, p_ctr = proportions_ztest(count_ctr, nobs_ctr, alternative='two-sided')

print(f'- p-valor para CTR: {p_ctr:.4f}')

_, p_tempo = stats.ttest_ind(tempo_A, tempo_B)

print(f'- p-valor para tempo página: {p_tempo}')

diff = conv_B.mean()-conv_A.mean()

print(f'\nA diferença observada de conversões é {diff*100:.2f}%')

ic_diff = confint_proportions_2indep(conv_A.sum(), len(conv_A), conv_B.sum(), len(conv_B), alpha=0.05)

print(f'Intervalo de Confiança (95%): {ic_diff[0]:.2%} a {ic_diff[1]*100:.2f}%')

# Nós do time de análise de dados, mediante análise dos dados de CTR, tempo de página e conversão coletados,
# Percebemos que o resultado para o tempo de página aumentou de forma significativa, indicando que o layout do site
# realmente influenciou na retenção do tempo.
# Entretanto, as medidas para CTR e conversão não são estatisticamente relevantes e os cálculos indicam que 
# os resultados podem ter sido por acaso.
# Dessa forma, recomendamos que o novo layout seja implementado para aumentarmos o tempo médio da página
# E que novas pesquisas sejam feitas em cima desse novo layout para descobrirmos como podemos aumentar
# o numero de conversões e de cliques com base num tempo de retenção aumentado.
"""

########################################################################
# NÍVEL 7-8: Manipulação
########################################################################

"""
7. Teste t manual (sem função pronta)

# Calcule o teste t MANUALMENTE para os dados de tempo:
# 1. Calcule a diferença das médias
# 2. Calcule o erro padrão
# 3. Calcule a estatística t
# 4. Compare com o resultado do stats.ttest_ind
"""

"""
mean_diff = tempo_B.mean() - tempo_A.mean()

var_A, var_B = np.var(tempo_A), np.var(tempo_B)

n_A, n_B = len(tempo_A), len(tempo_B)

erro_padrao = np.sqrt(var_A/n_A + var_B/n_B)

t_stat_manual = mean_diff / erro_padrao

t_stat_auto, p_valor = stats.ttest_ind(tempo_B, tempo_A)

print(f't-stat manual: {t_stat_manual}')
print(f't_stat com função: {t_stat_auto}')

print(f'Diferença: {t_stat_auto-t_stat_manual}')
"""

########################################################################

"""
8. Poder do teste (simulação)

# Simule 100 testes A/B onde H0 é FALSA (há diferença real)
# Use:
# - n = 100 por grupo
# - pA = 0.05, pB = 0.07
# 
# Conte em quantos testes o p-valor < 0.05
# Essa proporção é o PODER do teste
# O resultado está próximo do esperado (80%+)?
"""

"""
n = 3000
pA = 0.05
pB = 0.07

contador = 0
n_teste = 100
for i in range(n_teste):
    grupo_A = np.random.binomial(1, pA, n)
    grupo_B = np.random.binomial(1, pB, n)

    count = np.array([grupo_A.sum(), grupo_B.sum()])
    nobs = np.array([len(grupo_A), len(grupo_B)])

    _, p_valor = proportions_ztest(count, nobs, alternative='two-sided')

    if p_valor < 0.05:
        contador += 1

print(f'Quantidade de testes em que p-valor < 0.05: {contador}')
print(f'Proporção em relação à quantidade de testes: {contador/n_teste:.2%}')

# Para 100 testes com n = 100 o poder foi de 7%
# Para n = 1000 o poder foi de 44%
# Para n = 3000 o poder foi de 90%
"""

########################################################################
# NÍVEL 9-10: Desafios
########################################################################

"""
9. Análise completa (todas as métricas)

# Analise TODAS as métricas do teste A/B:
# 1. CTR (taxa de clique)
# 2. Tempo na página
# 3. Conversão
#
# Para cada métrica:
# - Teste estatístico apropriado
# - P-valor
# - Intervalo de confiança
# - Interpretação em português claro
#
# Crie uma tabela resumo com os resultados
"""

# 1. CTR (taxa de clique)

## 1.1 Z-test CTR

count_ctr = np.array([ctr_B.sum(), ctr_A.sum()])
nobs_ctr = np.array([len(ctr_B), len(ctr_A)])

_, p_valor_ctr = proportions_ztest(count_ctr, nobs_ctr, alternative='two-sided')

## 1.2 IC CTR

ic_ctr_lower, ic_ctr_upper = confint_proportions_2indep(ctr_B.sum(), len(ctr_B), ctr_A.sum(), len(ctr_A))

## Explicação

print(f'1. Análise CTR (taxa de clique)')
print(f' - Grupo A: Taxa de conversão: {ctr_A.sum()/len(ctr_A):.2%}')
print(f' - Grupo B: Taxa de conversão: {ctr_B.sum()/len(ctr_B):.2%}')
print(f' - Diferença Absoluta: {ctr_B.sum()/len(ctr_B) - ctr_A.sum()/len(ctr_A):.2%}')
print(f' - Diferença Relativa: {(ctr_B.sum()/ctr_A.sum())-1:.2%}')
print(f' - P-valor: {p_valor_ctr:.2%}')
print(f' - Intervalo de confiança (IC 95%): {ic_ctr_lower:.2%}, {ic_ctr_upper:.2%}')
print(f'Apesar da diferença relativa entre os grupos ser considerável ({(ctr_B.sum()/ctr_A.sum())-1:.2%})')
print(f'A chance de que esse resultado ser por acaso é grande')
print(f'Visto que, se a versão B não fosse melhor, a chance de vermos essa diferença seria de {p_valor_ctr:.2%}')
print(f'Temos 95% de confiança de que a diferença verdadeira está entre {ic_ctr_lower:.2%} e {ic_ctr_upper:.2%}')
print(f'Dessa forma, é possível perceber que os dados sugerem que o novo layout não favorece significativamente o aumento do CTR')

# 2. Tempo na página

## 2.1 T-test tempo na pagina

_, p_valor_tempo = stats.ttest_ind(tempo_B, tempo_A)

## 2.2 IC tempo

n = len(tempo_A)
z = 1.96

diff_tempo = tempo_B.mean() - tempo_A.mean()
se_tempo = np.sqrt(tempo_A.var()/n + tempo_B.var()/n)

ic_tempo_lower = diff_tempo - z * se_tempo
ic_tempo_upper = diff_tempo + z * se_tempo

## 2.3 Explicação

print(f'\n2. Análise do tempo de página')
print(f' - Grupo A: Média de tempo na página: {tempo_A.mean():.2f}s')
print(f' - Grupo B: Média de tempo na página: {tempo_B.mean():.2f}s')
print(f' - Diferença Absoluta: {tempo_B.mean() - tempo_A.mean():.2f}s')
print(f' - Diferença Relativa: {(tempo_B.mean()/tempo_A.mean())-1:.2%}')
print(f' - P-valor: {p_valor_tempo:.14%}')
print(f' - Intervalo de confiança (IC 95%): {ic_tempo_lower:.2f}s, {ic_tempo_upper:.2f}s')

print(f'A diferença relativa entre os dois grupos é considerável {(tempo_B.mean()/tempo_A.mean())-1:.2%}')
print(f'A chance desse resultado ser por acaso é ínfima, visto que:')
print(f'Se a versão B não fosse melhor, a chance de vermos essa diferença seria de {p_valor_tempo:.14%}')
print(f'Além do mais, temos 95% de confiança de que a diferença verdadeira está entre: {ic_tempo_lower:.2f}s e {ic_tempo_upper:.2f}s')
print(f'Dessa forma, é possível perceber que os dados sugerem fortemente que o novo layout favorece significativamente o tempo de página')

# 3. Conversão

## 3.1 Z-test conversão

count_conv = np.array([conv_B.sum(), conv_A.sum()])
nobs_conv = np.array([len(conv_B), len(conv_A)])

_, p_valor_conv = proportions_ztest(count_conv, nobs_conv, alternative='two-sided')

## 3.2 IC conversão

ic_conv_lower, ic_conv_upper = confint_proportions_2indep(conv_B.sum(), len(conv_B), conv_A.sum(), len(conv_A))

## 3.3 Explicação

print(f'\n3. Análise da conversão')
print(f' - Grupo A: Taxa de conversão: {conv_A.mean():.2%}')
print(f' - Grupo B: Taxa de conversão: {conv_B.mean():.2%}')
print(f' - Diferença Absoluta: {conv_B.mean() - conv_A.mean():.2%}')
print(f' - Diferença Relativa: {(conv_B.mean()/conv_A.mean())-1:.2%}')
print(f' - P-valor: {p_valor_conv:.2%}')
print(f' - Intervalo de confiança (IC 95%): {ic_conv_lower:.2%}, {ic_conv_upper:.2%}')
print(f'Apesar da diferença relativa entre os grupos ser considerável ({(conv_B.mean()/conv_A.mean())-1:.2%})')
print(f'A chance de que esse resultado ser por acaso é grande')
print(f'Visto que, se a versão B não fosse melhor, a chance de vermos essa diferença seria de {p_valor_conv:.2%}')
print(f'Temos 95% de confiança de que a diferença verdadeira está entre {ic_conv_lower:.2%} e {ic_conv_upper:.2%}')
print(f'Dessa forma, é possível perceber que os dados sugerem que o novo layout não favorece significativamente o aumento da taxa de conv')

########################################################################

"""
10. DESAFIO FINAL: Decisão de negócio

# A empresa tem recursos para implementar APENAS UMA mudança.
# Qual métrica você priorizaria? Por quê?
# 
# Considere:
# - CTR: aumento de 10% para 12% (relativo de 20%)
# - Conversão: aumento de 5% para 6% (relativo de 20% também)
# - Tempo na página: aumento de 120s para 135s (15s a mais)
#
# Cada cliente que compra gera R$ 100 de receita.
# Cada clique em anúncio gera R$ 0.50 de receita (indireta).
# Tempo na página NÃO gera receita direta, mas indica engajamento.
#
# Escreva uma recomendação final com justificativa financeira.
"""

# Num primeiro momento, eu recomendaria a implementação que favorece a conversão direta.
# Pois, sem analisar profundamente os números, o seguro é sempre prezar pela implementação
# Que gera receita mais direta e mais sobre controle.
# O aumento do CTR favorece a receita de forma indireta
# E o aumento do engajamento pode favorecer o aumento das demais variáveis de forma indireta,
# Mas seria necessário um estudo mais aprofundado para ver a relação entre "engajamento" e as demais variáveis.
# Claro que, apesar da média da receita proveniente da compra do cliente ser muito maior que a média da receita de um único clique
# Dependendo dos valores absolutos dos clique e das compras pode ser que a conversão por meio do CTR compense ou até sobrepuje a receita por compra
# Dessa forma é necessário analisar mais a fundo esses valores
# De forma geral, por uma perspectiva mais conservadora e segura de investimento sugiro a implementação da mudança que prioriza a conversão direta.