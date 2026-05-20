"""
Bloco 4: Estatística para Dados
Aula 06: Regressão Linear - Conceitos Fundamentais
Data: 20/05/2026
Objetivo: Entender o QUE é regressão linear e para que serve

NESTA AULA:
- Apenas conceitos, analogias e interpretações
- Código apenas para demonstrar os conceitos (sem funções novas complexas)
- Exercícios CONCEITUAIS no final
"""

import numpy as np
import matplotlib.pyplot as plt

print("="*50)
print("AULA 06 - REGRESSÃO LINEAR: CONCEITOS FUNDAMENTAIS")
print("="*50)

# ==========================================
# 1. O QUE É REGRESSÃO LINEAR?
# ==========================================

print("\n1. O QUE É REGRESSÃO LINEAR?")
print("-"*40)

"""
REGRESSÃO LINEAR é uma técnica para entender a RELAÇÃO entre duas variáveis
e fazer PREVISÕES.

PENSE NUMA RETA: y = a + b*x

- x: variável independente (o que você USA para prever)
- y: variável dependente (o que você quer PREVER)
- b: inclinação (quanto y muda quando x aumenta 1 unidade)
- a: intercepto (valor de y quando x = 0)

EXEMPLO SIMPLES:

Você quer prever o preço de um imóvel (y) com base na área (x).

Se a relação for: preço = 50000 + 2000 * área

- Intercepto (a) = 50000 → um imóvel de área 0 custaria R$ 50.000
- Inclinação (b) = 2000 → cada metro quadrado a mais aumenta R$ 2.000 no preço

POR QUE "LINEAR"?

Porque a relação é uma LINHA RETA. Se a relação é curva, precisamos de outros métodos.

PARA QUE SERVE NO DIA A DIA DO ANALISTA?

1. PREVISÃO: Quanto vou vender se aumentar o investimento em marketing?
2. ENTENDIMENTO: Qual o impacto de cada hora de treinamento na produtividade?
3. IDENTIFICAR TENDÊNCIAS: As vendas estão aumentando ao longo do tempo?
"""

# ==========================================
# 2. A EQUAÇÃO DA RETA (y = a + bx)
# ==========================================

print("\n2. A EQUAÇÃO DA RETA - y = a + b*x")
print("-"*40)

"""
DECOMPONDO A EQUAÇÃO:

y = a + b*x

| Símbolo | Nome                     | O que significa                  | Exemplo (preço do imóvel) |
|---------|--------------------------|----------------------------------|---------------------------|
| y       | Variável dependente      | O que queremos PREVER            | Preço do imóvel           |
| x       | Variável independente    | O que USAMOS para prever         | Área do imóvel            |
| a       | Intercepto               | Valor de y quando x=0            | Preço base (R$ 50.000)    |
| b       | Inclinação (coeficiente) | Quanto y muda quando x aumenta 1 | Cada m² aumenta R$ 2.000  |

EXEMPLOS NUMÉRICOS:

Se preço = 50000 + 2000 * área

- Área = 50m² → preço = 50000 + 2000*50 = R$ 150.000
- Área = 80m² → preço = 50000 + 2000*80 = R$ 210.000
- Área = 100m² → preço = 50000 + 2000*100 = R$ 250.000

INTERPRETAÇÃO DA INCLINAÇÃO (b):

- b > 0 → relação POSITIVA (x aumenta, y aumenta)
- b < 0 → relação NEGATIVA (x aumenta, y diminui)
- b = 0 → SEM relação (y não muda com x)

INTERPRETAÇÃO DO INTERCEPTO (a):

- É o valor "base" quando x = 0
- Às vezes não faz sentido prático (ex: imóvel com área 0)
- Mas é matematicamente necessário para a equação
"""

# ==========================================
# 3. EXEMPLOS DO DIA A DIA
# ==========================================

print("\n3. EXEMPLOS DO DIA A DIA DO ANALISTA")
print("-"*45)

"""
EXEMPLO 1: MARKETING E VENDAS

Pergunta: Quanto cada real investido em marketing gera em vendas?

Dados históricos:
- Investimento em marketing (x)
- Vendas geradas (y)

Regressão: vendas = 10000 + 5 * marketing

Interpretação:
- A cada R$ 1 em marketing, as vendas aumentam R$ 5
- Mesmo sem marketing, a empresa vende R$ 10.000 (base)

EXEMPLO 2: TREINAMENTO E PRODUTIVIDADE

Pergunta: Cada hora de treinamento aumenta quantas unidades produzidas?

Regressão: produtividade = 50 + 2 * horas_treinamento

Interpretação:
- Cada hora de treinamento aumenta 2 unidades produzidas
- Um funcionário sem treinamento produz 50 unidades

EXEMPLO 3: TEMPO E VENDAS (TENDÊNCIA)

Pergunta: As vendas estão crescendo ao longo do tempo?

Regressão: vendas = 1000 + 50 * mes

Interpretação:
- A cada mês, as vendas aumentam R$ 50 (tendência de crescimento)
- No mês 0 (início), as vendas eram R$ 1.000

EXEMPLO 4: PREÇO E DEMANDA

Pergunta: Como o preço afeta a quantidade vendida?

Regressão: unidades_vendidas = 500 - 2 * preco

Interpretação:
- A cada R$ 1 de aumento no preço, vendemos 2 unidades a menos
- A preço zero, venderíamos 500 unidades (teórico)
"""

# ==========================================
# 4. O QUE É R² (COEFICIENTE DE DETERMINAÇÃO)
# ==========================================

print("\n4. O QUE É R²?")
print("-"*20)

"""
R² (lê-se "R ao quadrado") mede o quanto o modelo explica os dados.

INTERPRETAÇÃO:

- R² = 1 → modelo PERFEITO (todos os pontos na reta)
- R² = 0.8 → 80% da variação em y é explicada por x
- R² = 0.3 → apenas 30% é explicada (relação fraca)
- R² = 0 → nenhuma relação linear

PENSE ASSIM:

Se você tem uma nota de prova (y) e quer prever com base nas horas de estudo (x):

- R² = 0.9 → horas de estudo EXPLICA 90% da nota
- R² = 0.2 → horas de estudo explica APENAS 20% (outros fatores importam mais)

EXEMPLOS DE R² NO MUNDO REAL:

| Situação                        | R² típico | Interpretação |
|---------------------------------|-----------|---------------|
| Preço do imóvel x área          | 0.6 - 0.8 | Área explica bem, mas localização também importa |
| Vendas x marketing              | 0.4 - 0.6 | Marketing ajuda, mas outros fatores influenciam |
| Nota da prova x horas de estudo | 0.2 - 0.4 | Estudo ajuda, mas inteligência/sono também contam |
| Altura x peso                   | 0.7 - 0.8 | Altamente correlacionado |

REGRAS PRÁTICAS:

| R²        | Interpretação para o negócio |
|-----------|------------------------------|
| > 0.7     | Forte - modelo confiável para previsões |
| 0.4 - 0.7 | Moderado - útil, mas com cautela |
| < 0.4     | Fraco - outras variáveis são mais importantes |

NÃO CAIA NESSA ARMADILHA:

R² ALTO NÃO SIGNIFICA CAUSALIDADE!

Exemplo: Vendas de sorvete e afogamentos podem ter R² alto, mas um não causa o outro.
"""

# ==========================================
# 5. DEMONSTRAÇÃO VISUAL
# ==========================================

print("\n5. DEMONSTRAÇÃO VISUAL - COMO A RETA É AJUSTADA")
print("-"*45)

# Criando dados de exemplo
np.random.seed(42)

# Horas de estudo (x) e nota (y)
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = 5 + 0.8 * x + np.random.normal(0, 0.5, 10)  # nota = 5 + 0.8*horas + erro

# Calculando a reta de regressão (manualmente para demonstração)
# Em produção usaremos funções prontas
coefs = np.polyfit(x, y, 1)  # [inclinação, intercepto]
b = coefs[0]  # inclinação
a = coefs[1]  # intercepto

print(f"Dados: horas de estudo (x) e nota (y)")
print(f"Reta encontrada: nota = {a:.2f} + {b:.2f} * horas")
print(f"Interpretação: cada hora de estudo aumenta a nota em {b:.2f} pontos")

# Visualização
# plt.figure(figsize=(10, 6))
# plt.scatter(x, y, color='blue', alpha=0.7, label='Dados reais')
# plt.plot(x, a + b*x, color='red', linewidth=2, label='Reta de regressão')
# plt.xlabel('Horas de estudo')
# plt.ylabel('Nota')
# plt.title('Regressão Linear: Nota vs Horas de Estudo')
# plt.legend()
# plt.grid(True, alpha=0.3)
# plt.tight_layout()
# plt.savefig('regressao_demo.png')
# plt.show()

print("\n✅ Gráfico salvo como 'regressao_demo.png'")

# ==========================================
# 6. COMO INTERPRETAR OS RESULTADOS (PARA O NEGÓCIO)
# ==========================================

print("\n6. COMO INTERPRETAR RESULTADOS - LINGUAGEM DE NEGÓCIO")
print("-"*50)

"""
RELATÓRIO PARA UM GERENTE (exemplo com dados de marketing):

"Rodamos uma análise para entender o impacto do investimento em marketing nas vendas.

RESULTADOS:
- A cada R$ 1.000 investido em marketing, as vendas aumentam R$ 5.000
- O modelo explica 75% da variação nas vendas (R² = 0.75)
- A relação é estatisticamente significativa (p-valor < 0.001)

RECOMENDAÇÃO:
- Aumentar o investimento em marketing tem impacto positivo e previsível
- Para cada R$ 10.000 adicionais, esperamos R$ 50.000 em vendas extras
- Recomendamos aumentar o orçamento em 20% no próximo trimestre"

O QUE VOCÊ PRECISA SABER PARA RESPONDER:

1. "Qual o impacto de x em y?" → Olhe a inclinação (b)
2. "O modelo é confiável?" → Olhe o R² e o p-valor
3. "Quanto devo investir para atingir uma meta?" → Use a equação
"""

# ==========================================
# 7. LIMITAÇÕES DA REGRESSÃO LINEAR
# ==========================================

print("\n7. LIMITAÇÕES - QUANDO NÃO USAR")
print("-"*35)

"""
REGRESSÃO LINEAR NÃO É BOM QUANDO:

1. A RELAÇÃO NÃO É LINEAR
   - Exemplo: produtividade aumenta até um ponto, depois cai
   - Gráfico teria formato de U ou sino

2. HÁ OUTLIERS EXTREMOS
   - Um ponto muito distante pode distorcer toda a reta
   - Sempre visualize os dados antes!

3. AS VARIÁVEIS NÃO SÃO INDEPENDENTES
   - Exemplo: preço e quantidade têm relação de mercado

4. VOCÊ QUER PROVAR CAUSALIDADE
   - Regressão mostra ASSOCIAÇÃO, não CAUSALIDADE
   - Assim como correlação, regressão não prova causa

O QUE FAZER NESSES CASOS?

| Problema                | Alternativa |
|-------------------------|-------------|
| Relação não-linear      | Regressão polinomial |
| Muitos outliers         | Regressão robusta |
| Quer provar causalidade | Teste A/B, experimento controlado |
| Múltiplas variáveis     | Regressão múltipla (Aula 07) |
"""

# ==========================================
# 8. RESUMO - REGRESSÃO LINEAR (CONCEITOS)
# ==========================================

print("\n8. RESUMO - REGRESSÃO LINEAR (CONCEITOS)")
print("-"*45)

"""
✅ O QUE É:
   - Técnica para entender relação entre variáveis
   - Faz previsões baseadas em dados históricos

✅ EQUAÇÃO: y = a + b*x
   - y: o que queremos PREVER (dependente)
   - x: o que USAMOS para prever (independente)
   - b: INCLINAÇÃO (impacto de x em y)
   - a: INTERCEPTO (valor base)

✅ R² (COEFICIENTE DE DETERMINAÇÃO)
   - Mede quanto o modelo explica os dados
   - 0 a 1 (quanto maior, melhor)
   - 0.7+ = forte, 0.4-0.7 = moderado, <0.4 = fraco

✅ QUANDO USAR:
   - Relação linear entre variáveis
   - Quer prever y a partir de x
   - Quer quantificar o impacto de x em y

✅ LIMITAÇÕES:
   - Não prova causalidade
   - Sensível a outliers
   - Só funciona para relações lineares

📌 PARA O ANALISTA DE DADOS JR:
   1. SEMPRE visualize os dados antes (gráfico de dispersão)
   2. R² ajuda, mas não é a única métrica
   3. Relatório deve ter: inclinação, R², interpretação prática
   4. Lembre: correlação não é causalidade (regressão também não!)
"""

# ==========================================
# EXERCÍCIOS - AULA 06 (CONCEITUAIS)
# ==========================================

print("\n" + "="*50)
print("EXERCÍCIOS - REGRESSÃO LINEAR (CONCEITOS)")
print("="*50)

########################################################################
# EXERCÍCIO 1
########################################################################

"""
1. Uma empresa fez uma regressão entre investimento em marketing (x) e vendas (y).
   O resultado foi: vendas = 10000 + 8 * marketing

   a) O que significa o número 8?
   b) O que significa o número 10000?
   c) Se a empresa investir R$ 5.000 em marketing, qual a venda prevista?
   d) Se a empresa quer vender R$ 100.000, quanto deve investir?
"""

"""
a) O número 8 é a inclinação do gráfico, ele indica que 1 unidade de investimento em marketing gera 8 unidades de vendas

b) O número 10000 é o intercepto (onde o gráfico corta o eixo y), ele indica que se o investimento em marketing for de 0 unidades
a base das vendas é de 10000 unidades.

c) Se a empresa investir 50000 em marketing a venda prevista é de:
x = 5000
venda_prevista = y

y = 8*5000 + 10000
y = 40000 + 10000
y = 50000

d) Se a empresa quer vender 100.000 ela deve investir:
y = 100000
x = investimento

y = 8*x + 10000
100000 = 8*x+10000
x = (100000 - 10000)/8
x = 11250

"""

########################################################################
# EXERCÍCIO 2
########################################################################

"""
2. Uma análise de imóveis encontrou: preço = 80000 + 1500 * area

   a) Qual o preço previsto para um imóvel de 100m²?
   b) Qual o preço previsto para um imóvel de 200m²?
   c) O intercepto (80000) faz sentido prático? Por quê?
"""

"""
a) O preço previsto para um imóvel de 100m2:

preço = 80000 + (1500 * 100)
preço = 230000

b) O preço previsto para um imóvel de 200m²:

preço = 80000 + (1500 * 200)
preço = 380000

c) O intercepto (80000) faz sentido prático? Por quê?

Não, pois não existem casas com 0m2, é apenas uma funcionalidade matemática que expressa o fato de que
existem outros fatores que influenciam no preço de uma casa e que a casa tem um "valor intrinseco"

"""

########################################################################
# EXERCÍCIO 3
########################################################################

"""
3. Duas regressões diferentes:

   Modelo A: R² = 0.85
   Modelo B: R² = 0.45

   a) Qual modelo explica melhor os dados?
   b) O que isso significa na prática?
   c) O modelo com R² maior é sempre melhor? Por quê?
"""

"""
a) O modelo A explica melhor os dados pois 0.85 é um número alto e consideravelmente maior que 0.45

b) Isso significa que a curva é bem ajustada aos pontos do gráfico de dispersão

c) Não necessariamente, pois apesar de ter R2 grande, acredito que isso n impede dele ter um p-valor pequeno.

Outra questão também é a seguinte, quando eu fazia regressões para encontrar gráficos que encaixam com os dados
de experimentos (da minha época de graduação em Física) as vezes encontravamos graficos que "fitavam" melhor
aos dados, mas que não tinham "sentido físico", por exemplo, algum grafico que necessitava que o ponto (0, 0)
fizesse parte do grafico, mas o que fitava melhor aos dados tinha um ponto (0, 1) por exemplo.
"""

########################################################################
# EXERCÍCIO 4
########################################################################

"""
4. Uma regressão de vendas mostrou: unidades = 100 - 3 * preco

   a) A relação é positiva ou negativa? O que isso significa?
   b) Se o preço aumenta R$ 10, o que acontece com as vendas?
   c) A preço zero, quantas unidades seriam vendidas (teoricamente)?
"""

"""
a) A relação é negativa, isso significa que preço e unidades são inversamente proporcionais.
Ou seja, quando uma variável aumenta, a outra diminui.

b) Se o preço aumenta em 10, as vendas passam de 100 (intercepto) para 70 (100 - 3*10)

c) Seriam vendidas 100 unidades.

"""

########################################################################
# EXERCÍCIO 5
########################################################################

"""
5. Você está analisando a relação entre horas de estudo e nota na prova.
   O R² foi 0.32. O que você diz para um colega que acredita que 
   "estudar é a única coisa que importa para a nota"?
"""

"""
Eu diria para o meu colega que, apesar da relação entre horas de estudo e nota da prova
realmente existir, o R2 ser baixo indica que esse não é o fator mais determinante.

Ou seja, duas pessoas que estudaram a mesma quantidade de horas, podem ter desempenhos muito diferentes.
O que indica que outros fatores são mais determinantes. Ou pelo menos, igualmente determinantes.
"""

########################################################################
# EXERCÍCIO 6
########################################################################

"""
6. Um analista disse: "R² = 0.9 significa que 90% das previsões estão corretas."

   a) Esta afirmação está correta? Por quê?
   b) Explique o que R² realmente significa.
"""

"""
a) Essa afirmação não está correta. R2 = 0.9 pode significar que a curva fita 90% dos pontos.
O que mostra que a curva é uma boa aproximação teórica para os dados. O que não quer dizer
que 90% das previsões estão corretas, pois com R2 = 0.9 as previsões podem ser até melhores que 90%.
"""

########################################################################
# EXERCÍCIO 7
########################################################################

"""
7. Para cada situação, responda se REGRESSÃO LINEAR é adequada ou não:

   a) Prever o preço de um carro baseado na idade
   b) Prever o número de clientes baseado no horário do dia (horário de pico)
   c) Prever a satisfação do cliente (1 a 5) baseado no tempo de espera
   d) Prever vendas baseado no mês do ano (janeiro, fevereiro...)
"""

"""
a) Os preços de carros que tem a mesma idade podem variar muito dependendo do modelo.
Provavelmente se pegassemos carros da mesma faixa de preço, o fit seria bom. Mas para diversos modelos, não.

b) Não, a regressão linear é melhor para dados que são crescentes ou decrescentes. n. de clientes por hora do dia
vão ter diferentes picos. Uma distribuição de poisson é mais adequada.

c) Sim, clientes que espeream mais tem maior tendência a apresentar baixa satisfação.

d) Não, pois, assim como o caso b) os dados podem apresentar diferentes picos. 

"""

########################################################################
# EXERCÍCIO 8
########################################################################

"""
8. Uma empresa fez uma regressão entre preço e vendas: vendas = 500 - 2 * preco
   R² = 0.15, p-valor = 0.40

   a) A relação preço-vendas é significativa? (use α=0.05)
   b) O modelo é útil para fazer previsões? Por quê?
   c) O que você recomendaria para a empresa?
"""

"""
a) Não, pois p-valor (40%) é muito maior que alfa (5%)

b) O modelo não é útil para fazer previsões pois R2 é muito baixo (0.15)

c) Realizar outras análises para determinar um modelo melhor que correlacione vendas e preço. 
"""

########################################################################
# EXERCÍCIO 9
########################################################################

"""
9. Monte um parágrafo (para um gerente não-técnico) explicando os resultados:

   Situação: Uma empresa quer entender o impacto do treinamento na produtividade.
   Resultados: produtividade = 50 + 1.5 * horas_treinamento; R² = 0.72; p-valor = 0.001

   Responda:
   - Qual o impacto de cada hora de treinamento?
   - O modelo é confiável?
   - Recomendaria investir em treinamento?
"""

"""
O resultado do modelo mostra que um funcionário sem treinamento produz em média 50 unidades.
E que a cada 2h de treinamento que esse funcionário recebe, ele aumenta sua produção em 3 unidades.

Esse modelo teórico tem uma alta taxa de equiparação com os dados reais (vou deixar assim pq n sei exatamente ainda o que o R2 é)
E se o modelo estiver errado, veriamos esse resultado em apenas 0.1% dos casos. O que sugere que o modelo não deu certo por acaso.

Dessa forma, recomendamos fortemente o investimento em treinamento.
"""

########################################################################
# EXERCÍCIO 10
########################################################################

"""
10. DESAFIO FINAL (Reflexão)

    Você é analista de dados em uma empresa. O gerente de produto quer saber:
    "Se aumentarmos o preço do produto em 10%, quantas vendas vamos perder?"

    Você tem dados históricos de preço e quantidade vendida.

    a) Como você usaria regressão linear para responder?
    b) Que suposições você precisa verificar antes de confiar na resposta?
    c) O que você diria ao gerente sobre a diferença entre "prever" e "causar"?
"""

"""
Primeiramente eu faria um modelo teórico com base em um regressão linear, baseado nos dados históricos.
Depois eu veria se esse modelo se encaixa bem aos dados (R2) e analisaria o p-valor.
Caso R2 e p-valor sejam suficientes bons. Eu faria as contas para responder o gerente.
Na minha resposta à ele, eu deixaria claro que podemos fazer previsões com o modelo teórico, mas que 
temos diversas margens de erro, ou seja, é melhor tomar decisões com base nessa análise, mas análise não preve o futuro com exatidão.
"""




