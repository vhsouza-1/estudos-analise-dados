"""
Bloco 4: Estatística para Dados
Módulo 2: Distribuições de Probabilidade
Aula 2: Fundamentos de Distribuições de Probabilidade
Data: 14/05/2026
Objetivo: Aprender os principais tipos de distribuições e suas aplicações

CONTEÚDO:
1. O que é uma Distribuição de Probabilidade?
2. Distribuição Normal (a mais importante)
3. Distribuição Binomial (sim/não)
4. Distribuição de Poisson (eventos por tempo/espaço)
5. Distribuição Uniforme
6. Teorema Central do Limite (TCL)
7. Aplicação prática em análise de dados
8. Resumo e Exercícios
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# ==========================================
# 1. O QUE É UMA DISTRIBUIÇÃO DE PROBABILIDADE?
# ==========================================

print("="*50)
print("1. O QUE É UMA DISTRIBUIÇÃO DE PROBABILIDADE?")
print("="*50)

"""
DISTRIBUIÇÃO DE PROBABILIDADE = descreve como os valores de uma variável se distribuem

Perguntas que ela responde:
- Qual a probabilidade de um valor específico ocorrer?
- Qual o intervalo que contém a maioria dos valores?
- Quão provável é um valor extremo?

POR QUE É IMPORTANTE PARA ANÁLISE DE DADOS?

1. ENTENDER O COMPORTAMENTO DOS DADOS
   - Se os dados seguem uma distribuição normal, podemos usar testes paramétricos
   - Se são assimétricos, precisamos de abordagens diferentes

2. FAZER PREVISÕES
   - Sabendo a distribuição, podemos calcular probabilidades
   - Exemplo: probabilidade de vendas superarem uma meta

3. IDENTIFICAR ANOMALIAS
   - Valores muito improváveis segundo a distribuição podem ser outliers
   - Exemplo: um salário 5 desvios acima da média

PRINCIPAIS DISTRIBUIÇÕES PARA ANALISTA DE DADOS:

| Distribuição | Tipo de dado         | Exemplo |
|--------------|----------------------|---------|
| Normal       | Contínuo (simétrico) | Altura, peso, QI |
| Binomial     | Discreto (sim/não)   | Cliques em anúncio, sucesso em teste A/B |
| Poisson      | Discreto (contagem)  | Número de clientes por hora, acidentes por dia |
| Uniforme     | Contínuo (igual)     | Número aleatório entre 0 e 1 |
"""

# ==========================================
# 2. DISTRIBUIÇÃO NORMAL (GAUSSIANA)
# ==========================================

print("\n" + "="*50)
print("2. DISTRIBUIÇÃO NORMAL - A MAIS IMPORTANTE")
print("="*50)

"""
DISTRIBUIÇÃO NORMAL: forma de sino, simétrica em torno da média

CARACTERÍSTICAS:
- Média = Mediana = Moda (todas iguais)
- 68% dos dados estão a 1 desvio padrão da média
- 95% dos dados estão a 2 desvios padrão da média
- 99.7% dos dados estão a 3 desvios padrão da média

PARÂMETROS:
- μ (mu) = média
- σ (sigma) = desvio padrão

NOTAÇÃO: X ~ N(μ, σ²)

ONDE USAR NA PRÁTICA:
- Altura e peso de populações
- Erros de medição
- Resultados de testes padronizados (ENEM, SAT)
- Muitos fenômenos naturais e sociais
"""

# Gerando diferentes normais
np.random.seed(42)

x = np.linspace(-4, 4, 100)
normal_padrao = stats.norm.pdf(x, 0, 1)
normal_media1 = stats.norm.pdf(x, 1, 1)
normal_desvio2 = stats.norm.pdf(x, 0, 2)

print("--- Parâmetros da Distribuição Normal ---")
print(f"N(0,1) - Média 0, Desvio 1 (normal padrão)")
print(f"N(1,1) - Média 1, Desvio 1")
print(f"N(0,2) - Média 0, Desvio 2")

# Regra empírica (68-95-99.7)
print("\n--- REGRA EMPÍRICA (68-95-99.7) ---")
print("Em uma distribuição normal:")
print("  - 68% dos dados estão a 1 desvio padrão da média")
print("  - 95% dos dados estão a 2 desvios padrão da média")
print("  - 99.7% dos dados estão a 3 desvios padrão da média")

# Exemplo prático
print("\n--- EXEMPLO PRÁTICO ---")
print("QI tem distribuição normal com média 100 e desvio 15")
print("  - 68% das pessoas têm QI entre 85 e 115")
print("  - 95% das pessoas têm QI entre 70 e 130")
print("  - 99.7% das pessoas têm QI entre 55 e 145")

# Calculando probabilidades com scipy
print("\n--- CALCULANDO PROBABILIDADES ---")
print("Qual a probabilidade de uma pessoa ter QI > 130?")

prob_maior_130 = 1 - stats.norm.cdf(130, 100, 15)
print(f"P(QI > 130) = {prob_maior_130:.3f} = {prob_maior_130*100:.1f}%")

print("\nQual a probabilidade de uma pessoa ter QI entre 85 e 115?")
prob_entre = stats.norm.cdf(115, 100, 15) - stats.norm.cdf(85, 100, 15)
print(f"P(85 < QI < 115) = {prob_entre:.3f} = {prob_entre*100:.1f}%")

# ==========================================
# 3. DISTRIBUIÇÃO BINOMIAL
# ==========================================

print("\n" + "="*50)
print("3. DISTRIBUIÇÃO BINOMIAL")
print("="*50)

"""
DISTRIBUIÇÃO BINOMIAL: modela o número de sucessos em n tentativas independentes

CARACTERÍSTICAS:
- Cada tentativa tem apenas dois resultados: sucesso ou fracasso
- Probabilidade de sucesso (p) é constante
- Tentativas são independentes

PARÂMETROS:
- n = número de tentativas
- p = probabilidade de sucesso

NOTAÇÃO: X ~ Binomial(n, p)

ONDE USAR NA PRÁTICA:
- Teste A/B (quantos cliques em cada versão)
- Controle de qualidade (quantos produtos defeituosos)
- Pesquisas (quantas pessoas votariam em um candidato)
"""

np.random.seed(42)

# Exemplo: lançamento de moeda 10 vezes
n = 10  # 10 lançamentos
p = 0.5  # probabilidade de cara

x = np.arange(0, n+1)
binomial = stats.binom.pmf(x, n, p)

print("--- EXEMPLO: LANÇAMENTO DE MOEDA ---")
print(f"Lançando uma moeda {n} vezes")
print(f"Probabilidade de cada número de caras:")

for i, prob in enumerate(binomial):
    print(f"  {i} caras: {prob:.3f} ({prob*100:.1f}%)")

print(f"\nProbabilidade de ter exatamente 5 caras: {stats.binom.pmf(5, n, p):.3f}")

# Exemplo prático: taxa de conversão
print("\n--- EXEMPLO PRÁTICO: TAXA DE CONVERSÃO ---")
print("Em um teste A/B, 100 pessoas veem um anúncio")
print("A taxa de conversão histórica é 10% (p=0.1)")
print("Qual a probabilidade de ter exatamente 15 conversões?")

conv_15 = stats.binom.pmf(15, 100, 0.1)
print(f"P(15 conversões) = {conv_15:.3f} = {conv_15*100:.1f}%")

print("\nQual a probabilidade de ter MAIS DE 15 conversões?")
prob_mais_15 = 1 - stats.binom.cdf(15, 100, 0.1)
print(f"P(>15 conversões) = {prob_mais_15:.3f} = {prob_mais_15*100:.1f}%")

# ==========================================
# 4. DISTRIBUIÇÃO DE POISSON
# ==========================================

print("\n" + "="*50)
print("4. DISTRIBUIÇÃO DE POISSON")
print("="*50)

"""
DISTRIBUIÇÃO DE POISSON: modela o número de eventos que ocorrem em um intervalo fixo

CARACTERÍSTICAS:
- Eventos ocorrem independentemente
- Taxa média (λ) é constante
- Dois eventos não podem ocorrer exatamente no mesmo instante

PARÂMETRO:
- λ (lambda) = número médio de eventos por intervalo

NOTAÇÃO: X ~ Poisson(λ)

ONDE USAR NA PRÁTICA:
- Número de clientes por hora em uma loja
- Número de acidentes por dia em uma rodovia
- Número de emails recebidos por dia
- Número de chamadas em um call center
"""

np.random.seed(42)

# Exemplo: clientes por hora
lambdas = [2, 5, 10]
x = np.arange(0, 20)

print("--- EXEMPLO: CLIENTES POR HORA EM UMA LOJA ---")
print(f"Média de clientes por hora: λ = 5")

# Probabilidades para Poisson com λ=5
poisson_5 = stats.poisson.pmf(x, 5)

print("Probabilidade de diferentes números de clientes:")
for i in [0, 5, 10, 15]:
    prob = stats.poisson.pmf(i, 5)
    print(f"  {i} clientes: {prob:.3f} ({prob*100:.1f}%)")

print("\n--- EXEMPLO PRÁTICO: CALL CENTER ---")
print("Um call center recebe em média 3 chamadas por minuto (λ=3)")
print("Qual a probabilidade de receber 5 chamadas em um minuto?")

chamadas_5 = stats.poisson.pmf(5, 3)
print(f"P(5 chamadas) = {chamadas_5:.3f} = {chamadas_5*100:.1f}%")

print("\nQual a probabilidade de receber MAIS DE 5 chamadas?")
prob_mais_5 = 1 - stats.poisson.cdf(5, 3)
print(f"P(>5 chamadas) = {prob_mais_5:.3f} = {prob_mais_5*100:.1f}%")

# ==========================================
# 5. DISTRIBUIÇÃO UNIFORME
# ==========================================

print("\n" + "="*50)
print("5. DISTRIBUIÇÃO UNIFORME")
print("="*50)

"""
DISTRIBUIÇÃO UNIFORME: todos os valores têm a mesma probabilidade

PARÂMETROS:
- a = valor mínimo
- b = valor máximo

NOTAÇÃO: X ~ Uniform(a, b)

ONDE USAR NA PRÁTICA:
- Números aleatórios para simulação
- Sorteios justos
- Quando não há informação sobre a distribuição (princípio da indiferença)
"""

print("--- EXEMPLO: NÚMERO ALEATÓRIO ENTRE 0 E 10 ---")
print("Qualquer número entre 0 e 10 tem a mesma probabilidade")

# Gerar números uniformes
uniformes = np.random.uniform(0, 10, 1000)
print(f"Média teórica: 5.0")
print(f"Média amostral: {uniformes.mean():.2f}")
print(f"Desvio teórico: {10/(12**0.5):.2f}")
print(f"Desvio amostral: {uniformes.std():.2f}")

# ==========================================
# 6. TEOREMA CENTRAL DO LIMITE (TCL)
# ==========================================

print("\n" + "="*50)
print("6. TEOREMA CENTRAL DO LIMITE - O MAIS IMPORTANTE")
print("="*50)

"""
TEOREMA CENTRAL DO LIMITE (TCL):

"Para uma amostra suficientemente grande, a distribuição da MÉDIA amostral se aproxima de uma distribuição normal, independentemente da distribuição original dos dados."

POR QUE ISSO É REVOLUCIONÁRIO?

1. PODEMOS USAR ESTATÍSTICA NORMAL PARA QUASE TUDO
   - Não importa se os dados originais são binomiais, Poisson, etc.
   - A média da amostra será aproximadamente normal

2. PODEMOS CALCULAR INTERVALOS DE CONFIANÇA
   - Sabemos que 95% das médias amostrais estão a 2 desvios da média

3. PODEMOS TESTAR HIPÓTESES
   - Teste t, ANOVA, regressão - todos usam o TCL

QUÃO GRANDE A AMOSTRA PRECISA SER?
- n ≥ 30 é geralmente suficiente
- Para distribuições muito assimétricas, pode precisar de n ≥ 50
"""

print("--- DEMONSTRAÇÃO DO TCL ---")

# Distribuição original: uniforme (não é normal)
original = np.random.uniform(0, 1, 10000)

# Vamos tirar várias amostras e calcular a média de cada uma
n_amostras = 1000
tamanho_amostra = 30
medias = []

for _ in range(n_amostras):
    amostra = np.random.uniform(0, 1, tamanho_amostra)
    medias.append(amostra.mean())

print(f"Distribuição original: Uniforme(0,1) - NÃO é normal")
print(f"Distribuição das médias (n={tamanho_amostra}) - é aproximadamente normal")
print(f"Média das médias: {np.mean(medias):.3f} (deveria ser 0.5)")
print(f"Desvio das médias: {np.std(medias):.3f}")

# ==========================================
# 7. APLICAÇÃO PRÁTICA: ANÁLISE DE VENDAS
# ==========================================

print("\n" + "="*50)
print("7. APLICAÇÃO PRÁTICA - ANÁLISE DE VENDAS")
print("="*50)

np.random.seed(42)

# Simulando vendas diárias de uma loja
dias = 365
vendas_diarias = np.random.poisson(50, dias)  # média 50 vendas/dia

print("Análise de Vendas Diárias (Distribuição de Poisson)")
print(f"Média de vendas por dia: {vendas_diarias.mean():.1f}")
print(f"Desvio padrão: {vendas_diarias.std():.1f}")
print(f"Mínimo: {vendas_diarias.min()}")
print(f"Máximo: {vendas_diarias.max()}")

# Qual a probabilidade de vender mais de 60 unidades em um dia?
prob_mais_60 = 1 - stats.poisson.cdf(60, vendas_diarias.mean())
print(f"\nProbabilidade de vender >60 unidades: {prob_mais_60:.3f} ({prob_mais_60*100:.1f}%)")

# Simulação de Teste A/B usando Binomial
print("\n--- TESTE A/B SIMULADO ---")
print("Versão atual: 5% de conversão (p=0.05)")
print("Nova versão: 6% de conversão (p=0.06)")
print("1000 visitas por versão")

# Gerar resultados
atual = np.random.binomial(1, 0.05, 1000)
nova = np.random.binomial(1, 0.06, 1000)

print(f"Conversão atual: {atual.mean()*100:.1f}%")
print(f"Conversão nova: {nova.mean()*100:.1f}%")

# Calculando significância estatística
from scipy.stats import chi2_contingency

tabela = pd.crosstab(
    ['Atual']*1000 + ['Nova']*1000,
    list(atual) + list(nova)
)
print(f"\nTabela de contingência:\n{tabela}")

# ==========================================
# 8. VISUALIZAÇÃO DAS DISTRIBUIÇÕES
# ==========================================

print("\n" + "="*50)
print("8. VISUALIZAÇÃO DAS DISTRIBUIÇÕES")
print("="*50)

"""
# Criar visualizações
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 1. Normal
x = np.linspace(-4, 4, 100)
axes[0, 0].plot(x, stats.norm.pdf(x, 0, 1))
axes[0, 0].fill_between(x, stats.norm.pdf(x, 0, 1), alpha=0.3)
axes[0, 0].set_title('Distribuição Normal N(0,1)')
axes[0, 0].set_xlabel('Valor')
axes[0, 0].set_ylabel('Densidade')
axes[0, 0].axvline(0, color='red', linestyle='--', alpha=0.5)

# 2. Binomial
n, p = 20, 0.5
x = np.arange(0, n+1)
axes[0, 1].bar(x, stats.binom.pmf(x, n, p))
axes[0, 1].set_title(f'Distribuição Binomial (n={n}, p={p})')
axes[0, 1].set_xlabel('Número de Sucessos')
axes[0, 1].set_ylabel('Probabilidade')

# 3. Poisson
lamb = 5
x = np.arange(0, 15)
axes[1, 0].bar(x, stats.poisson.pmf(x, lamb))
axes[1, 0].set_title(f'Distribuição de Poisson (λ={lamb})')
axes[1, 0].set_xlabel('Número de Eventos')
axes[1, 0].set_ylabel('Probabilidade')

# 4. Uniforme
x = np.linspace(0, 10, 100)
axes[1, 1].plot(x, stats.uniform.pdf(x, 0, 10))
axes[1, 1].fill_between(x, stats.uniform.pdf(x, 0, 10), alpha=0.3)
axes[1, 1].set_title('Distribuição Uniforme U(0,10)')
axes[1, 1].set_xlabel('Valor')
axes[1, 1].set_ylabel('Densidade')

plt.tight_layout()
plt.show()
"""

# ==========================================
# 9. QUANDO USAR CADA DISTRIBUIÇÃO
# ==========================================

print("\n" + "="*50)
print("9. QUANDO USAR CADA DISTRIBUIÇÃO")
print("="*50)

"""
GUIA PRÁTICO PARA ANALISTA DE DADOS

| Situação | Distribuição | Exemplo |
|----------|--------------|---------|
| Dados contínuos e simétricos | NORMAL | Altura, peso, QI, notas de prova |
| Contagem de sucessos em n tentativas | BINOMIAL | Cliques em anúncio, produtos defeituosos |
| Contagem de eventos por tempo/espaço | POISSON | Clientes por hora, acidentes por dia |
| Valor aleatório sem preferência | UNIFORME | Sorteio, simulação inicial |
| Média de uma amostra (n grande) | NORMAL (TCL) | Quase qualquer média amostral |

DICAS RÁPIDAS:

✅ USE NORMAL quando:
   - Os dados são simétricos
   - A média e mediana são próximas
   - Você quer calcular percentis/probabilidades

✅ USE BINOMIAL quando:
   - Cada tentativa tem resultado SIM/NÃO
   - Você quer saber quantos sucessos em n tentativas
   - Exemplo: "Qual a chance de 20 de 100 clientes comprarem?"

✅ USE POISSON quando:
   - Você conta eventos em um intervalo fixo
   - Eventos são raros e independentes
   - Exemplo: "Quantos clientes por hora?"
"""

# ==========================================
# 10. RESUMO DA AULA
# ==========================================

print("\n" + "="*50)
print("10. RESUMO - DISTRIBUIÇÕES DE PROBABILIDADE")
print("="*50)

"""
✅ DISTRIBUIÇÃO NORMAL:
   - stats.norm.pdf(x, media, desvio)  # densidade
   - stats.norm.cdf(x, media, desvio)  # probabilidade acumulada
   - stats.norm.ppf(p, media, desvio)  # valor para dado percentil

✅ DISTRIBUIÇÃO BINOMIAL:
   - stats.binom.pmf(k, n, p)  # prob de exatamente k sucessos
   - stats.binom.cdf(k, n, p)  # prob de até k sucessos

✅ DISTRIBUIÇÃO DE POISSON:
   - stats.poisson.pmf(k, lambda)  # prob de exatamente k eventos
   - stats.poisson.cdf(k, lambda)  # prob de até k eventos

✅ DISTRIBUIÇÃO UNIFORME:
   - np.random.uniform(min, max, size)
   - stats.uniform.pdf(x, min, max-min)

✅ TEOREMA CENTRAL DO LIMITE:
   - A média amostral tende à normal
   - n ≥ 30 é geralmente suficiente

📌 PARA O ANALISTA DE DADOS JR:
   - DOMINE a distribuição normal (é a que mais aparece)
   - ENTENDA Binomial e Poisson (aparecem muito em negócios)
   - SAIBA que o TCL permite usar normal para muitas situações
"""

# ==========================================
# EXERCÍCIOS - AULA 2 (DISTRIBUIÇÕES)
# ==========================================

print("\n" + "="*50)
print("EXERCÍCIOS - DISTRIBUIÇÕES DE PROBABILIDADE")
print("="*50)

# Dados para todos os exercícios
np.random.seed(42)

# Cenário: Loja de e-commerce
"""
Contexto:
Uma loja online tem:
- Média de 50 vendas por dia (distribuição de Poisson)
- Taxa de conversão do site de 3% (Binomial)
- Tempo de carregamento da página segue distribuição normal com média 2s e desvio 0.5s
- O número de visitantes por hora segue distribuição de Poisson com média 30
"""

# Simular dados para os exercícios
vendas_diarias = np.random.poisson(50, 100)
conversoes = np.random.binomial(100, 0.03, 100)
tempo_carregamento = np.random.normal(2, 0.5, 100)
visitantes_hora = np.random.poisson(30, 24)

# print("\nDados simulados para os exercícios:")
# print(f"Vendas diárias (100 dias): média = {vendas_diarias.mean():.1f}")
# print(f"Conversões (amostras de 100 visitas): média = {conversoes.mean():.1f}%")
# print(f"Tempo de carregamento: média = {tempo_carregamento.mean():.2f}s")
# print(f"Visitantes por hora (24h): média = {visitantes_hora.mean():.1f}")

########################################################################
# NÍVEL 1-3: Aquecimento
########################################################################

"""
1. Probabilidades na Normal

# O tempo de carregamento da página segue N(2, 0.5)
# Calcule:
# - Probabilidade de carregar em menos de 1.5 segundos
# - Probabilidade de carregar entre 2 e 3 segundos
# - Probabilidade de carregar em mais de 3.5 segundos
"""

"""
prob_1_5 = stats.norm.cdf(1.5, 2, 0.5)
print(f'Probabilidade de carregar em menos de 1.5 segundos: {prob_1_5*100:.2f}%')

prob_entre = stats.norm.cdf(3, 2, 0.5) - stats.norm.cdf(2, 2, 0.5)
print(f'Probabilidade de carregar entre 2 e 3 segundos: {prob_entre*100:.2f}%')

prob_maior_3 = 1 - stats.norm.cdf(3.5, 2, 0.5)
print(f'Probabilidade de carregar em mais de 3.5 segundos: {prob_maior_3:.4f}%')
"""

########################################################################

"""
2. Probabilidades na Binomial

# A taxa de conversão do site é 3% (p=0.03)
# Para uma amostra de 200 visitantes:
# - Qual a probabilidade de exatamente 5 conversões?
# - Qual a probabilidade de ter MAIS DE 8 conversões?
# - Qual a probabilidade de ter 0 conversões?
"""

"""
p = 0.03  # taxa de conversão
n = 200   # número de visitantes

prob_5 = stats.binom.pmf(5, n, p)
print(f'Qual a probabilidade de exatamente 5 conversões?: {prob_5*100:.2f}%')

prob_mais_8 = 1 - stats.binom.cdf(8, n, p)
print(f'Qual a probabilidade de ter MAIS DE 8 conversões?: {prob_mais_8*100:.2f}%')

prob_0 = stats.binom.pmf(0, n, p)
print(f'Qual a probabilidade de ter 0 conversões?: {prob_0*100:.2f}%')
"""

########################################################################

"""
3. Probabilidades na Poisson

# A loja recebe em média 30 visitantes por hora
# Calcule:
# - Probabilidade de receber exatamente 25 visitantes em uma hora
# - Probabilidade de receber MENOS DE 20 visitantes
# - Probabilidade de receber MAIS DE 40 visitantes
"""

"""
l = 30 # lambda: taxa de visitantes por hora

prob_25 = stats.poisson.pmf(25, l)
print(f'Probabilidade de receber exatamente 25 visitantes: {prob_25*100:.2f}%')

prob_menos_20 = stats.poisson.cdf(19, l) # Se é menos de 20, então 20 n entra, né?
print(f'Probabilidade de receber MENOS DE 20 visitantes: {prob_menos_20:.2f}%')

prob_mais_40 = 1 - stats.poisson.cdf(40, l)
print(f'Probabilidade de receber MAIS DE 40 visitantes: {prob_mais_40*100:.2f}%')
"""

########################################################################
# NÍVEL 4-6: Aplicação
########################################################################

"""
4. Simulação da Regra Empírica

# Gere 10000 amostras de uma distribuição normal N(100, 15)
# Verifique se aproximadamente:
# - 68% estão entre 85 e 115
# - 95% estão entre 70 e 130
# - 99.7% estão entre 55 e 145
#
# Mostre os percentuais reais da sua simulação
"""

"""
dados = np.random.normal(100, 15, 10000)

entre1_mask = (dados >= 85) & (dados <= 115) # entre 85 e 115
entre2_mask = (dados >= 70) & (dados <= 130) # entre 70 e 130
entre3_mask = (dados >= 55) & (dados <= 145) # entre 55 e 145

print(f'Percentual entre 85 e 115: {entre1_mask.sum()/len(dados)*100:.2f}%') # 68.08%
print(f'Percentual entre 70 e 130: {entre2_mask.sum()/len(dados)*100:.2f}%') # 95.33%
print(f'Percentual entre 55 e 145: {entre3_mask.sum()/len(dados)*100:.2f}%') # 99.74%
"""

########################################################################

"""
5. Teorema Central do Limite

# A distribuição de Poisson com λ=5 é assimétrica
# Demonstre o TCL:
# 1. Gere 1000 amostras de Poisson(5) com tamanho 30
# 2. Calcule a média de cada amostra
# 3. Plote o histograma das médias
# 4. Compare com uma normal de mesma média e desvio
"""

"""
l = 5
n = 30
n_amostras = 1000
medias = []

for _ in range(n_amostras):
    amostra = np.random.poisson(l, n)
    media_amostra = np.mean(amostra)
    medias.append(media_amostra)

desvio = np.std(medias)
media = np.mean(medias)

normal = np.random.normal(media, desvio, n_amostras)

df = pd.DataFrame({
    'medias_p': medias
})

df2 = pd.DataFrame({
    'normal': normal
})

sns.histplot(data=df, x='medias_p', bins=30, color='purple', label='Medias Poisson', alpha=0.5) # só sei usar histograma com sns hehe
sns.histplot(data=df2, x='normal', bins=30, color='skyblue', label='Normal', alpha=0.5)

plt.legend()
plt.show()
"""

########################################################################

"""
6. Identificando a distribuição

# Para cada situação abaixo, identifique qual distribuição usar:
# a) Número de clientes que entram em uma loja por hora
# b) Número de funcionários que faltam em um dia (em uma empresa de 500)
# c) Altura dos jogadores de basquete
# d) Número de acidentes por semana em uma rodovia
# e) Resultado de um dado justo
#
# Depois, simule dados para UMA das situações à sua escolha
"""

"""
print('Número de clientes que entram em uma loja por hora: Poisson (evento com limites temporais - distribuição discreta com taxa fixa)')
print('Número de funcionários que faltam em um dia (em uma empresa de 500): Poisson (evento com limites temporais - distribuição discreta com taxa fixa)')
print('Altura dos jogadores de basquete: Normal (distribuição em uma amostragem - distribuição com centro e desvio padrao)')
print('Número de acidentes por semana em uma rodovia: Poisson (evento com limites temporais - distribuição discreta com taxa fixa)')
print('Resultado de um dado justo: Uniforme (distribuição aleatória - distribuição em que controlamos apenas o valor máximo e mínimo)')

# Simular altura de jogadores de basquete

altura_media = 190
desvio_altura = 5

alturas = np.random.normal(altura_media, desvio_altura, 1000)

plt.figure(figsize=(10, 6))
plt.hist(alturas, bins=30, alpha=0.7, edgecolor='black')
plt.title('Histograma das Alturas', fontsize=14)
plt.xlabel('Altura (cm)', fontsize=12)
plt.ylabel('Densidade', fontsize=12)
plt.show()
"""

########################################################################
# NÍVEL 7-8: Manipulação
########################################################################

"""
7. Comparando distribuições teóricas com dados reais

# Use os dados simulados de 'vendas_diarias' (Poisson com λ=50)
# 1. Calcule a média e desvio dos dados reais
# 2. Compare com os valores teóricos (λ e √λ)
# 3. Plote o histograma dos dados reais
# 4. Plote a curva teórica da Poisson por cima
# 5. Os dados parecem seguir a distribuição teórica?
"""

"""
media_vendas = np.mean(vendas_diarias)
desvio_vendas = np.std(vendas_diarias)

print(f'Vendas diárias:\n - Média: {media_vendas:.2f}\n - Desvio: {desvio_vendas:.2f}')

print(f'\nPoisson(50):\n - Média: 50\n - Desvio: {50**(1/2):.2f}')

x = np.arange(30, 70)
y = stats.poisson.pmf(x, 50)

plt.hist(vendas_diarias, color='skyblue', density=True, edgecolor='black', bins=8, alpha=0.5)
plt.plot(x, y, color='red')
plt.show()
"""

########################################################################

"""
8. Intervalos de confiança baseados na Normal

# Usando o TCL, calcule intervalos de confiança para a média das vendas diárias
# Use os 100 dias de dados simulados (vendas_diarias)
# 
# Intervalo de confiança: média ± z * (desvio / √n)
# Para 95% de confiança, z = 1.96
#
# Calcule:
# - Média amostral
# - Intervalo de 95% de confiança
# - O valor teórico (50) está dentro do intervalo?
"""

"""
z = 1.96
n = len(vendas_diarias)
media = np.mean(vendas_diarias)
desvio = np.std(vendas_diarias)

ic_1 = media + (z * desvio / n**(1/2))
ic_2 = media - (z * desvio / n**(1/2))

print(f'Média amostral de vendas_diarias: {np.mean(vendas_diarias):.2f}')
print(f'Intervalo de 95% de confiança: {ic_1:.2f} - {ic_2:.2f}')
print(f'O valor teórico (50) está dentro do intervalo? {ic_1 >= 50 >= ic_2}')
"""

########################################################################
# NÍVEL 9-10: Desafios
########################################################################

"""
9. Simulação de Teste A/B

# Simule um teste A/B com 1000 visitantes para cada versão
# Versão A: taxa de conversão 4%
# Versão B: taxa de conversão 4.5%
#
# 1. Gere os resultados usando Binomial
# 2. Calcule a conversão real de cada versão
# 3. Use o teste qui-quadrado para verificar se a diferença é significativa
# 4. Interprete o resultado (houve diferença significativa?)
"""

"""
n = 1000
p_a = 0.04
p_b = 0.045

result_a = np.random.binomial(1, p_a, n)
result_b = np.random.binomial(1, p_b, n)

conv_a = np.sum(result_a)
conv_b = np.sum(result_b)

tabela = [
    [conv_a, n - conv_a],
    [conv_b, n - conv_b]
]

chi2, p, _, _ = chi2_contingency(tabela)

print(f'Resultado:')
print(f'P-valor: {p:.4f}')
print(f"Taxa A: {conv_a/n:.3f} ({conv_a/n*100:.1f}%)")
print(f"Taxa B: {conv_b/n:.3f} ({conv_b/n*100:.1f}%)")

if p < 0.05:
    print(f'\nDiferença significativa! Versão B é provavelmente melhor')
elif p >= 0.05:
    print(f'\nDiferença não significativa! Versão B pode não ser melhor')
"""

########################################################################

"""
10. DESAFIO FINAL: Previsão de Vendas

# Uma loja quer prever as vendas para os próximos 30 dias
# Baseado nos dados históricos (vendas_diarias), que seguem Poisson(50)
#
# 1. Simule 30 dias de vendas futuras (use Poisson)
# 2. Calcule:
#    - Probabilidade de vender mais de 60 unidades em um dia
#    - Probabilidade de vender menos de 40 unidades em um dia
#    - Probabilidade de ter uma semana (7 dias) com média > 55
# 3. Crie um relatório executivo de 1 parágrafo com as recomendações
#    (ex: "Devemos aumentar o estoque pois há X% de chance de...")
"""
l = 50
n = 30

vendas_futuras = np.random.poisson(l, n)

prob_60 = stats.poisson.pmf(60, l)
print(f'Probabilidade de vender mais de 60 unidades em um dia: {prob_60*100:.2f}%')

prob_menos_40 = stats.poisson.cdf(39, l)
print(f'Probabilidade de vender menos de 40 unidades em um dia: {prob_menos_40*100:.2f}%')

# Eu não tenho nem ideia de por onde começar a fazer: Probabilidade de ter uma semana (7 dias) com média > 55
# Acho que o que você me passou não dá pra fazer esse exercício...
