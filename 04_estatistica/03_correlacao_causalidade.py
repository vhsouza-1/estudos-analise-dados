"""
Bloco 4: Estatística para Dados
Módulo 3: Correlação e Causalidade
Aula 3: Fundamentos de Correlação e Causalidade
Data: 15/05/2026
Objetivo: Aprender a medir correlação entre variáveis e entender a diferença entre correlação e causalidade

CONTEÚDO:
1. O que é Correlação?
2. Coeficiente de Pearson (correlação linear)
3. Coeficiente de Spearman (correlação de ordem)
4. Matriz de Correlação e Heatmap
5. CORRELAÇÃO NÃO IMPLICA CAUSALIDADE (o mais importante!)
6. Exemplos clássicos de correlações espúrias
7. Como identificar causalidade?
8. Aplicação prática em análise de dados
9. Resumo e Exercícios
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# ==========================================
# 1. O QUE É CORRELAÇÃO?
# ==========================================

print("="*50)
print("1. O QUE É CORRELAÇÃO?")
print("="*50)

"""
CORRELAÇÃO = medida de como duas variáveis se relacionam

Perguntas que ela responde:
- Quando uma variável aumenta, a outra também aumenta? (correlação positiva)
- Quando uma variável aumenta, a outra diminui? (correlação negativa)
- As variáveis têm alguma relação? (correlação próxima de zero)

EXEMPLOS:
- Correlação POSITIVA: quanto mais horas de estudo, maior a nota
- Correlação NEGATIVA: quanto mais tempo na esteira, menor o peso
- Correlação PRÓXIMA DE ZERO: tamanho do pé e QI (não têm relação)

TIPOS DE CORRELAÇÃO:

| Tipo           | Valor               | Significado                     |
|----------------|---------------------|---------------------------------|
| Positiva forte | próximo de +1       | Caminham juntas (mesma direção) |
| Negativa forte | próximo de -1       | Caminham em direções opostas    |
| Fraca          | próximo de 0        | Não há relação linear           |
| Perfeita       | exatamente +1 ou -1 | Relação matemática exata        |

IMPORTANTE: Correlação mede relação LINEAR. Duas variáveis podem ter relação não-linear (ex: U) e correlação próxima de zero.
"""

# ==========================================
# 2. COEFICIENTE DE PEARSON
# ==========================================

print("\n" + "="*50)
print("2. COEFICIENTE DE PEARSON - CORRELAÇÃO LINEAR")
print("="*50)

"""
PEARSON (r): mede a correlação LINEAR entre duas variáveis numéricas

INTERPRETAÇÃO:
- r = 1: correlação positiva perfeita
- r = -1: correlação negativa perfeita
- r = 0: nenhuma correlação linear

FÓRMULA: r = cov(X,Y) / (σx * σy)

ONDE USAR:
- Dados contínuos
- Relação linear (não serve para curvas)
- Dados sem outliers significativos
"""

# Criando diferentes tipos de correlação
n = 100

# Correlação positiva forte
x_pos = np.random.normal(50, 10, n)
y_pos = x_pos * 0.8 + np.random.normal(0, 5, n)  # y aumenta com x

# Correlação negativa forte
x_neg = np.random.normal(50, 10, n)
y_neg = -x_neg * 0.8 + np.random.normal(0, 5, n)  # y diminui com x

# Correlação fraca (próxima de zero)
x_fraca = np.random.normal(50, 10, n)
y_fraca = np.random.normal(50, 20, n)  # sem relação

# Sem correlação (relação não-linear)
x_nao_linear = np.linspace(-3, 3, n)
y_nao_linear = x_nao_linear**2 + np.random.normal(0, 0.5, n)  # parábola

print("--- Exemplos de Correlação de Pearson ---")

r_pos, p_pos = stats.pearsonr(x_pos, y_pos)
print(f"Correlação positiva: r = {r_pos:.3f} (forte)")

r_neg, p_neg = stats.pearsonr(x_neg, y_neg)
print(f"Correlação negativa: r = {r_neg:.3f} (forte)")

r_fraca, p_fraca = stats.pearsonr(x_fraca, y_fraca)
print(f"Correlação fraca: r = {r_fraca:.3f}")

r_nao_linear, p_nao_linear = stats.pearsonr(x_nao_linear, y_nao_linear)
print(f"Relação não-linear: r = {r_nao_linear:.3f} (não captura a relação!)")

# ==========================================
# 3. COEFICIENTE DE SPEARMAN
# ==========================================

print("\n" + "="*50)
print("3. COEFICIENTE DE SPEARMAN - CORRELAÇÃO DE ORDEM")
print("="*50)

"""
SPEARMAN (ρ): mede a correlação baseada nos RANKS (ordem) dos valores

VANTAGENS:
- Captura relações monotônicas (não apenas lineares)
- Mais robusto a outliers
- Pode ser usado com dados ordinais

QUANDO USAR:
- Dados com outliers
- Relação não-linear mas monotônica (sempre cresce ou sempre decresce)
- Dados ordinais (ex: classificação de satisfação)
"""

print("--- Comparação: Pearson vs Spearman ---")

# Dados com outlier
x_outlier = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 100])
y_outlier = x_outlier * 2

r_pearson, _ = stats.pearsonr(x_outlier, y_outlier)
r_spearman, _ = stats.spearmanr(x_outlier, y_outlier)

print(f"Dados com outlier extremo:")
print(f"  Pearson: {r_pearson:.3f} (afetado pelo outlier)")
print(f"  Spearman: {r_spearman:.3f} (robusto)")

# Dados com relação monotônica não-linear (exponencial)
x_monotonico = np.linspace(1, 5, 50)
y_monotonico = np.exp(x_monotonico)  # relação exponencial

r_pearson_mono, _ = stats.pearsonr(x_monotonico, y_monotonico)
r_spearman_mono, _ = stats.spearmanr(x_monotonico, y_monotonico)

print(f"\nRelação exponencial (não-linear mas monotônica):")
print(f"  Pearson: {r_pearson_mono:.3f} (não captura bem)")
print(f"  Spearman: {r_spearman_mono:.3f} (captura a monotonicidade)")

# ==========================================
# 4. MATRIZ DE CORRELAÇÃO E HEATMAP
# ==========================================

print("\n" + "="*50)
print("4. MATRIZ DE CORRELAÇÃO E HEATMAP")
print("="*50)

"""
MATRIZ DE CORRELAÇÃO: mostra as correlações entre todas as pares de variáveis

HEATMAP: visualização da matriz de correlação (cores)
"""

# Criando dataset com múltiplas variáveis correlacionadas
np.random.seed(42)
n = 200

df_correlacao = pd.DataFrame({
    'vendas': np.random.normal(1000, 200, n),
    'marketing': np.random.normal(500, 100, n),
    'preco': np.random.normal(100, 20, n),
    'clientes': np.random.normal(50, 10, n),
    'tempo_site': np.random.normal(5, 1, n)
})

# Adicionar correlações artificiais
df_correlacao['vendas'] = (
    df_correlacao['vendas'] +
    df_correlacao['marketing'] * 0.5 -
    df_correlacao['preco'] * 0.3 +
    df_correlacao['clientes'] * 0.8
)

print("Dataset de exemplo:")
print(df_correlacao.head())

# Calcular matriz de correlação
matriz_corr = df_correlacao.corr()
print("\nMatriz de Correlação:")
print(matriz_corr.round(3))

# Heatmap
# plt.figure(figsize=(10, 8))
# sns.heatmap(matriz_corr, annot=True, cmap='coolwarm', center=0, square=True, fmt='.2f', linewidths=0.5, vmin=-1)
# plt.title('Matriz de Correlação - Heatmap')
# plt.tight_layout()
# plt.savefig('matriz_correlacao.png')
# plt.show()

print("\nInterpretação do Heatmap:")
print("- Cores vermelhas: correlação positiva")
print("- Cores azuis: correlação negativa")
print("- Quanto mais intensa a cor, mais forte a correlação")

# ==========================================
# 5. CORRELAÇÃO NÃO IMPLICA CAUSALIDADE
# ==========================================

print("\n" + "="*50)
print("5. CORRELAÇÃO NÃO IMPLICA CAUSALIDADE - O MAIS IMPORTANTE!")
print("="*50)

"""
ESTA É A LIÇÃO MAIS IMPORTANTE DE TODO O CURSO!

CORRELAÇÃO ≠ CAUSALIDADE

Duas variáveis podem ser correlacionadas sem que uma CAUSE a outra.

POSSIBILIDADES QUANDO ENCONTRAMOS CORRELAÇÃO:

1. CAUSALIDADE REAL: A causa B
   Exemplo: Mais horas de estudo → Melhores notas

2. CAUSALIDADE REVERSA: B causa A
   Exemplo: Mais policiais → Mais crimes? (Na verdade, mais crimes → mais policiais)

3. TERCEIRA VARIÁVEL (FATOR DE CONFUSÃO): C causa A e B
   Exemplo: Sorvete e Afogamentos estão correlacionados!
   - Mas é o CALOR que causa ambos (mais sorvete e mais pessoas na piscina)

4. CORRELAÇÃO ESPÚRIA (ACASO): Sem relação real, apenas coincidência
   Exemplo: Nomeações de juízes federais e temperatura nos EUA
"""

print("--- EXEMPLO CLÁSSICO: SORVETE E AFOGAMENTOS ---")
print("""
Dados mostram que:
- Quando as vendas de sorvete aumentam
- O número de afogamentos também aumenta

Correlação: POSITIVA FORTE!

Mas comprar sorvete NÃO causa afogamentos.

O que está acontecendo? 
→ O CALOR (terceira variável) causa ambos:
   - Calor → mais pessoas comem sorvete
   - Calor → mais pessoas vão à praia/piscina → mais afogamentos

LIÇÃO: Sempre pergunte se existe uma TERCEIRA VARIÁVEL explicando a correlação.
""")

# ==========================================
# 6. EXEMPLOS CLÁSSICOS DE CORRELAÇÕES ESPÚRIAS
# ==========================================

print("\n" + "="*50)
print("6. EXEMPLOS CLÁSSICOS DE CORRELAÇÕES ESPÚRIAS")
print("="*50)

"""
EXEMPLOS REAIS DE CORRELAÇÕES SEM CAUSALIDADE:

1. Número de filmes do Nicolas Cage e número de afogamentos em piscinas
   → Correlação: 0.66 (forte!)
   → Realidade: coincidência estatística

2. Consumo de margarina per capita e divórcios no Maine
   → Correlação: 0.99 (quase perfeita!)
   → Realidade: ambas aumentaram com o tempo (tendência temporal)

3. Venda de fraldas e cerveja na sexta-feira à noite
   → Correlação real!
   → Causa: pais jovens compram fraldas e cerveja juntos

4. Número de pessoas que morreram afogadas e número de filmes estrelando o Nicolas Cage
   → Correlação: extremamente alta
   → Realidade: pura coincidência

POR QUE ISSO IMPORTA?
- Empresas podem tirar conclusões erradas
- Políticas públicas baseadas em correlação podem falhar
- Testes A/B e experimentos controlados são melhores para causalidade
"""

print("""
📌 REGRA DE OURO:

Só porque duas coisas andam juntas, não significa que uma CAUSA a outra.

SEMPRE pergunte:
1. Existe uma explicação lógica para a causalidade?
2. Pode ser o contrário (causalidade reversa)?
3. Existe uma terceira variável explicando?
4. É apenas coincidência?
""")

# ==========================================
# 7. COMO IDENTIFICAR CAUSALIDADE?
# ==========================================

print("\n" + "="*50)
print("7. COMO IDENTIFICAR CAUSALIDADE?")
print("="*50)

"""
MÉTODOS PARA ESTABELECER CAUSALIDADE:

1. EXPERIMENTOS CONTROLADOS (Padrão Ouro)
   - Randomização (dividir grupos aleatoriamente)
   - Grupo de controle vs grupo de tratamento
   - Exemplo: Teste A/B

2. ESTUDOS LONGITUDINAIS
   - Acompanhar as mesmas pessoas ao longo do tempo
   - Ver o que acontece ANTES e DEPOIS

3. CRITÉRIOS DE BRADFORD HILL
   - Força da associação
   - Consistência (replicado em diferentes estudos)
   - Especificidade
   - Temporalidade (causa vem antes do efeito)
   - Gradiente biológico (dose-resposta)

4. TESTE A/B (no contexto de negócios)
   - Dividir usuários aleatoriamente
   - Aplicar mudança em um grupo
   - Comparar resultados

NO DIA A DIA DO ANALISTA:
- Você vai encontrar MUITAS correlações
- Você vai ajudar o time a NÃO tirar conclusões erradas
- Você vai sugerir testes A/B para validar causalidade
"""

print("--- EXEMPLO: TESTE A/B PARA CAUSALIDADE ---")
print("""
Pergunta: Mudar a cor do botão de COMPRAR (verde para vermelho) aumenta vendas?

Correlação (dados históricos): 
- Lojas com botão vermelho vendem mais
- Mas pode ser que lojas maiores usem botão vermelho

Para provar CAUSALIDADE:
1. Teste A/B: 50% dos usuários veem verde, 50% veem vermelho
2. Randomização elimina fatores de confusão
3. Se grupo vermelho compra mais → evidência de causalidade
""")

# ==========================================
# 8. APLICAÇÃO PRÁTICA
# ==========================================

print("\n" + "="*50)
print("8. APLICAÇÃO PRÁTICA - ANÁLISE DE CORRELAÇÃO")
print("="*50)

# Dataset de e-commerce
np.random.seed(42)
n = 500

df_loja = pd.DataFrame({
    'preco': np.random.uniform(50, 200, n),
    'marketing': np.random.uniform(500, 2000, n),
    'avaliacao': np.random.uniform(1, 5, n),
    'estoque': np.random.randint(10, 100, n),
    'vendas': np.random.poisson(100, n)
})

# Adicionar relações realistas
df_loja['vendas'] = (
    100 - df_loja['preco'] * 0.3 +
    df_loja['marketing'] * 0.02 +
    df_loja['avaliacao'] * 10 +
    np.random.normal(0, 20, n)
)

print("Análise de Correlação - Loja Online")
print(df_loja.head())

# Matriz de correlação
corr = df_loja.corr()
print("\nMatriz de Correlação:")
print(corr.round(3))

# Heatmap
# plt.figure(figsize=(10, 8))
# sns.heatmap(corr, annot=True, cmap='coolwarm', center=0, fmt='.2f', vmin=-1, vmax=1)
# plt.title('Correlações - Loja Online')
# plt.tight_layout()
# plt.show()

# Análise de correlações específicas
print("\n--- Análise de Correlações ---")

preco_vendas = corr.loc['preco', 'vendas']
print(f"Preço × Vendas: {preco_vendas:.3f}")
print("  Interpretação: quanto maior o preço, menores as vendas (negativo)")

marketing_vendas = corr.loc['marketing', 'vendas']
print(f"Marketing × Vendas: {marketing_vendas:.3f}")
print("  Interpretação: mais marketing → mais vendas (positivo)")

avaliacao_vendas = corr.loc['avaliacao', 'vendas']
print(f"Avaliação × Vendas: {avaliacao_vendas:.3f}")
print("  Interpretação: produtos mais avaliados vendem mais")

# AVISO SOBRE CAUSALIDADE
print("\n⚠️ IMPORTANTE: Correlação não implica causalidade!")
print("As relações acima podem ter causas reversas ou terceiras variáveis.")

# ==========================================
# 9. RESUMO DA AULA
# ==========================================

print("\n" + "="*50)
print("9. RESUMO - CORRELAÇÃO E CAUSALIDADE")
print("="*50)

"""
✅ COEFICIENTE DE PEARSON (r):
   - stats.pearsonr(x, y)
   - Mede relação LINEAR
   - Sensível a outliers

✅ COEFICIENTE DE SPEARMAN (ρ):
   - stats.spearmanr(x, y)
   - Mede relação MONOTÔNICA (baseada em ranks)
   - Robusto a outliers

✅ MATRIZ DE CORRELAÇÃO:
   - df.corr()
   - sns.heatmap(df.corr(), annot=True, cmap='coolwarm')

✅ CORRELAÇÃO NÃO É CAUSALIDADE!
   - Pode ser causalidade reversa
   - Pode ser terceira variável (fator de confusão)
   - Pode ser coincidência (correlação espúria)

✅ COMO ESTABELECER CAUSALIDADE:
   - Teste A/B (padrão ouro para negócios)
   - Experimentos controlados randomizados
   - Estudos longitudinais (antes/depois)

📌 PARA O ANALISTA DE DADOS JR:
   - SEMPRE desconfie de correlações
   - SEMPRE pergunte: "Isso é causal ou apenas coincidência?"
   - Use heatmaps para explorar relações
   - Proponha testes A/B para validar hipóteses
"""

# ==========================================
# EXERCÍCIOS - AULA 3 (CORRELAÇÃO E CAUSALIDADE)
# ==========================================

print("\n" + "="*50)
print("EXERCÍCIOS - CORRELAÇÃO E CAUSALIDADE")
print("="*50)

# Dados para todos os exercícios
np.random.seed(42)

df_empresa = pd.DataFrame({
    'funcionario_id': range(1, 101),
    'horas_trabalhadas': np.random.normal(40, 5, 100),
    'projetos_concluidos': np.random.poisson(5, 100),
    'treinamentos': np.random.poisson(3, 100),
    'tempo_empresa': np.random.exponential(3, 100).astype(int),
    'salario': np.random.normal(5000, 1000, 100),
    'satisfacao': np.random.uniform(1, 5, 100)
})

# Adicionar algumas relações
df_empresa['projetos_concluidos'] = (
    df_empresa['projetos_concluidos'] +
    df_empresa['horas_trabalhadas'] * 0.05 +
    df_empresa['treinamentos'] * 0.3
).astype(int)

df_empresa['salario'] = (
    df_empresa['salario'] +
    df_empresa['tempo_empresa'] * 50 +
    df_empresa['projetos_concluidos'] * 100
)

########################################################################
# NÍVEL 1-3: Aquecimento
########################################################################

"""
1. Calculando correlação de Pearson

# Calcule a correlação de Pearson entre:
# - horas_trabalhadas e projetos_concluidos
# - tempo_empresa e salario
# - treinamentos e satisfacao
#
# Interprete cada resultado (positiva/negativa/fraca/forte)
"""

"""
df = df_empresa.copy()

r_1, p_1 = stats.pearsonr(df['horas_trabalhadas'], df['projetos_concluidos'])
r_2, p_2 = stats.pearsonr(df['tempo_empresa'], df['salario'])
r_3, p_3 = stats.pearsonr(df['treinamentos'], df['satisfacao'])

print(f'Correlação de Pearson entre:')
print(f' - horas_trabalhadas e projetos_concluidos: {r_1:.3f} (positiva fraca)')
print(f' - tempo_empresa e salario: {r_2:.3f} (positiva fraca)')
print(f' - treinamentos e satisfacao: {r_3:.3f} (positiva fraca)')
"""

########################################################################

"""
2. Correlação de Spearman

# Calcule a correlação de Spearman entre as mesmas variáveis do exercício 1
# Compare os resultados com Pearson
# Em qual caso há maior diferença? Por quê?
"""

"""
df = df_empresa.copy()

r_1, _ = stats.pearsonr(df['horas_trabalhadas'], df['projetos_concluidos'])
r_2, _ = stats.pearsonr(df['tempo_empresa'], df['salario'])
r_3, _ = stats.pearsonr(df['treinamentos'], df['satisfacao'])

s_1, _ = stats.spearmanr(df['horas_trabalhadas'], df['projetos_concluidos'])
s_2, _ = stats.spearmanr(df['tempo_empresa'], df['salario'])
s_3, _ = stats.spearmanr(df['treinamentos'], df['satisfacao'])

print(f'Correlação de Spearman entre:')
print(f' - horas_trabalhadas e projetos_concluidos: {s_1:.3f} (positiva fraca)')
print(f' - tempo_empresa e salario: {s_2:.3f} (positiva fraca)')
print(f' - treinamentos e satisfacao: {s_3:.3f} (positiva fraca)')

print(f'\nComparação entre Pearson e Spearman:')
print(f' - horas_trabalhadas e projetos_concluidos: {r_1:.3f}, {s_1:.3f}')
print(f' - tempo_empresa e salario: {r_2:.3f}, {s_2:.3f} ')
print(f' - treinamentos e satisfacao: {r_3:.3f}, {s_3:.3f} ')

"""

########################################################################

"""
3. Matriz de correlação

# Calcule a matriz de correlação completa do DataFrame
# Mostre a matriz (use .round(2))
# Quais são as 3 correlações mais fortes (ignorando a diagonal)?
"""

"""
df = df_empresa.copy()

df = df.drop('funcionario_id', axis=1)

df_corr = df.corr()

print(f'Matriz de correlação:\n{df_corr.round(2).to_string()}')

print(f'3 Correlações mais fortes:')
print(f' - Projetos e Salário: 0.35')
print(f' - Treinamento e Salário: 0.21')
print(f' - Projetos e Satisfação: -0.20')
"""

########################################################################
# NÍVEL 4-6: Aplicação
########################################################################

"""
4. Heatmap de correlação

# Crie um heatmap da matriz de correlação usando seaborn
# Use cmap='coolwarm', annot=True, fmt='.2f'
# Título: "Matriz de Correlação - Funcionários"
# Salve a figura como 'heatmap_funcionarios.png'
"""

"""
df = df_empresa.copy()

df = df.drop('funcionario_id', axis=1)

df_corr = df.corr()

plt.figure(figsize=(10, 8))
sns.heatmap(df_corr, cmap='coolwarm', annot=True, fmt='.2f', vmin=-1, vmax=1)
plt.title('Matriz de Correlação - Funcionários')
plt.tight_layout()
plt.savefig('heatmap_funcionarios.png')
plt.show()
"""

########################################################################

"""
5. Identificando correlações espúrias

# No DataFrame abaixo (dados aleatórios), calcule as correlações
# Você deve encontrar correlações significativas por ACASO
# Qual é a maior correlação que você encontrou?
"""

"""
np.random.seed(42)
df_aleatorio = pd.DataFrame({
    'vendas_sorvete': np.random.normal(100, 20, 50),
    'afogamentos': np.random.normal(10, 3, 50),
    'temperatura': np.random.normal(25, 5, 50)
})

df_corr = df_aleatorio.corr()

sns.heatmap(df_corr, cmap='coolwarm', annot=True, fmt='.2f', vmin=-1, vmax=1)
plt.show()

print(f'Afogamento e Temperatura: -0.23 (n faz muito sentido hehe)')
"""

########################################################################

"""
6. Correlação vs Causalidade - Análise de Casos

# Para cada situação abaixo, responda:
# a) Provavelmente correlação real? Por quê?
# b) Existe causalidade? Se sim, qual direção?
# c) Pode haver terceira variável?

# Caso 1: Número de bombeiros no incêndio vs Dano causado
# Provavelmente correlação real negativa, quanto mais bombeiros no incendio, menor deve ser o dano.

# Caso 2: Horas de estudo vs Notas na prova
# Provavelmente correlação real positiva, quanto mais horas de estudo, melhor deve ser o desempenho na prova.

# Caso 3: Número de hospitais em uma cidade vs Expectativa de vida
# Provavelmente correlação real positiva, quanto maior o número de hospitais, maior o acesso a saúde (pensando no contexto do Brasil em que o SUS é público)

# Caso 4: Consumo de café vs Qualidade do sono
# Provavelmente correção real negativa, quanto maior o consumo de cafeína, pior é a qualidade do sono. Claro que depende da forma de consumo do café.
"""

########################################################################
# NÍVEL 7-8: Manipulação
########################################################################

"""
7. Correlações parciais (conceito)

# O conjunto de dados tem correlação entre 'horas_trabalhadas' e 'salario'
# Mas será que essa correlação é explicada por 'tempo_empresa'?
# 
# Calcule a correlação entre horas_trabalhadas e salario APENAS para:
# - Funcionários com tempo_empresa < 3 anos
# - Funcionários com tempo_empresa >= 3 anos
# 
# As correlações são diferentes? O que isso sugere?
"""

"""
df = df_empresa.drop('funcionario_id', axis=1).copy()

df_corr = df.corr()

print(f'Correlação entre horas_trabalhadas e salario: {df_corr.loc['horas_trabalhadas', 'salario']:.3f} (correlação praticamente nula)')

funcionario_mask1 = df['tempo_empresa'] < 3  # Apenas funcionários com menos de 3 anos de empresa
funcionario_mask2 = df['tempo_empresa'] >= 3 # Apenas funcionários com pelo menor 3 anos de empresa

df1 = df[funcionario_mask1]
df2 = df[funcionario_mask2]

df1_corr = df1.corr()
df2_corr = df2.corr()

print(f'Correlação entre horas_trabalhadas e salario (tempo_empresa < 3 anos): {df1_corr.loc['horas_trabalhadas', 'salario']:.3f} (correção negativa fraca)')
print(f'Correlação entre horas_trabalhadas e salario (tempo_empresa >= 3 anos): {df2_corr.loc['horas_trabalhadas', 'salario']:.3f} (correção positiva fraca)')
"""

########################################################################

"""
8. Criando um relatório de correlação

# Crie uma função relatorio_correlacao(df) que:
# 1. Calcula a matriz de correlação
# 2. Identifica as 5 correlações mais fortes (positivas e negativas)
# 3. Para cada uma, faz uma análise de possíveis interpretações
# 4. Retorna um dicionário com os resultados
#
# Aplique no df_empresa
"""

"""
def relatorio_correlacao(df):

    df = df.drop('funcionario_id', axis=1).copy()

    df_corr = df.corr()

    labels = []
    corrs = []

    for label1 in df.columns:
        for label2 in df.columns:
            if label1 != label2 and (label2, label1) not in labels:
                tupla_labels = (label1, label2)
                corr_labels = df_corr.loc[label1, label2]

                labels.append(tupla_labels)
                corrs.append(corr_labels)

    df_new = pd.DataFrame({
        'colunas': labels,
        'corrs': corrs
    })

    df_new['coluna1'] = df_new['colunas'].str[0]
    df_new['coluna2'] = df_new['colunas'].str[1]
    df_new['corrs_abs'] = df_new['corrs'].abs()

    df_new = df_new.sort_values('corrs_abs', ascending=False)

    df_new = df_new[['coluna1', 'coluna2', 'corrs']].reset_index(drop=True)

    return df_new

df = relatorio_correlacao(df_empresa)

# eu preferi fazer uma função que rankeia todas as correlações :) para mostrar as 5 primeiras é só fazer .head()

print(df.head())
"""

########################################################################
# NÍVEL 9-10: Desafios
########################################################################

"""
9. Correlação em séries temporais (cuidado!)

# Séries temporais frequentemente mostram correlações espúrias
# Duas variáveis podem crescer juntas pelo tempo, não por relação real
#
# Crie duas séries temporais independentes com tendência de crescimento
# Calcule a correlação entre elas
# O resultado é significativo? Deveria ser? Por quê?
"""

"""
serie1 = np.arange(0, 50, 1)
serie2 = np.arange(5, 89, 3)

r, p = stats.pearsonr(serie1[:len(serie2)], serie2)

print(r, p)

print(f'O resultado não é significativo, pois as séries são desrelacionadas totalmente, apenas do r ser praticamente 1 o p ser praticamente 0')
"""

########################################################################

"""
10. DESAFIO FINAL: Tomada de decisão

# A empresa quer decidir se oferece mais treinamentos para funcionários
# Baseado nos dados do df_empresa:
# - Calcule a correlação entre 'treinamentos' e 'projetos_concluidos'
# - Calcule a correlação entre 'treinamentos' e 'satisfacao'
#
# Imagine que você precisa apresentar para um gerente não-técnico:
# 1. Os dados sugerem que treinamentos melhoram produtividade?
# 2. Os dados sugerem que treinamentos melhoram satisfação?
# 3. Você recomendaria investir em mais treinamentos? Por quê?
# 4. Que tipo de estudo adicional você sugeriria para provar causalidade?
#
# Escreva um PARÁGRAFO respondendo em português claro
"""
df = df_empresa.copy()

r1, p1 = stats.pearsonr(df['treinamentos'], df['projetos_concluidos'])
r2, p2 = stats.pearsonr(df['treinamentos'], df['satisfacao'])

print(f'Correlação entre Treinamento e Projetos concluidos: r={r1:.3f}, p={p1:.3f}')
print(f'Correlação entre Treinamento e Satisfação: r={r2:.3f}, p={p2:.3f}')

# Os dados não sugerem que existe correlação direta entre o treinamento recebido pelos funcionários e a sua satisfação/conclusão de projetos.
# Pois o coeficiente de pearson é praticamente 0 e o p-valor é praticamente 50% para os dois.
# Dessa forma, eu não recomendo investir em mais treinamentos, pelo menos não de forma isolada.
# Algo que poderiamos ver é a relação entre o salario e a satisfação/conclusão de projetos
# Ou até mesmo podemos ver como o treinamento influencia essas duas variaveis em diferentes faixas salariais.
# Por exemplo, pode ser que o treinamento seja mais efetivo em faixas salariais maiores
# O que indicaria que o treinamento tem influencia relevante nesses parametros, mas que ele não compensaria, sozinho, um salario baixo.
# Também pode ser importante investigar a relação entre horas_trabalhadas com satisfação/conclusão de projetos.
# Visto que horas_trabalhadas e salario são grandes influencias na satisfação do funcionario.
# Em conjunto a isso, acredito que a relação entre tempo de empresa e projetos concluidos tbm deva ser analisada,
# Visto que é provavel que quanto mais tempo de empresa, mais habil o funcionario se torna.
# Enfim, existem diversas relações entre variaveis que devem ser analisadas.