"""
Bloco 3: Python para Dados
Módulo 2: Visualização de Dados
Aula 3: Múltiplos Gráficos (Subplots)
Data: 30/04/2026
Objetivo: Aprender a criar múltiplos gráficos na mesma figura
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# ==========================================
# 1. O QUE SÃO SUBPLOTS?
# ==========================================

print("="*50)
print("1. O QUE SÃO SUBPLOTS?")
print("="*50)

"""
Subplots permitem colocar vários gráficos na MESMA figura.
Útil para:
- Comparar diferentes métricas lado a lado
- Criar dashboards
- Economizar espaço (vários gráficos em uma imagem)

Tipos:
- plt.subplot() - um gráfico por vez, posicionamento manual
- plt.subplots() - cria todos os eixos de uma vez (mais moderno)
"""

# ==========================================
# 2. plt.subplot() - BÁSICO (1 gráfico de cada vez)
# ==========================================

print("\n" + "="*50)
print("2. plt.subplot() - UM POR VEZ")
print("="*50)

"""
plt.subplot(linhas, colunas, índice)
- linhas: número de linhas na grade
- colunas: número de colunas na grade
- índice: posição do gráfico atual (começa em 1)
"""

# Dados
meses = ['Jan', 'Fev', 'Mar', 'Abr']
vendas = [100, 150, 120, 180]
custos = [80, 100, 70, 120]
lucros = [20, 50, 50, 60]

# Criar figure
plt.figure(figsize=(12,4))

# Gráfico 1: Vendas (posição 1)
plt.subplot(1, 3, 1) # 1 linha, 3 colunas, posição 1
plt.plot(meses, vendas, 'bo-')
plt.title('Vendas')
plt.xlabel('Meses')
plt.ylabel('Valor (R$)')

# Gráfico 2: Custos (posição 2)
plt.subplot(1, 3, 2)
plt.plot(meses, custos, 'rs--')
plt.title('Custos')
plt.xlabel('Mês')

# Gráfico 3: Lucro (posição 3)
plt.subplot(1, 3, 3)
plt.plot(meses, lucros, 'g^:')
plt.title('Lucros')
plt.xlabel('Mês')

plt.tight_layout()

plt.close()

# plt.show()

# ==========================================
# 3. plt.subplot() - GRADE 2x2
# ==========================================

print("\n" + "="*50)
print("3. plt.subplot() - GRADE 2x2")
print("="*50)

# Criar figura
plt.figure(figsize=(10, 8))

# Gráfico 1 (linha 1, coluna 1)
plt.subplot(2, 2, 1)
plt.plot(meses, vendas, 'bo-')
plt.title('Vendas')
plt.grid(True, linestyle='--')

# Gráfico 2 (linha 1, coluna 2)
plt.subplot(2, 2, 2)
plt.bar(meses, vendas, color='blue')
plt.title('Vendas (Barras)')
plt.grid(True)

# Gráfico 3 (linha 2, coluna 1)
plt.subplot(2, 2, 3)
plt.plot(meses, custos, 'rs--')
plt.title('Custos')
plt.grid(True)

# Gráfico 4 (linha 2, coluna 2)
plt.subplot(2, 2, 4)
plt.bar(meses, custos, color='red')
plt.title('Custos (Barras)')
plt.grid(True)

plt.tight_layout()
plt.close()
# plt.show()

# ==========================================
# 4. plt.subplots() - MÉTODO MODERNO (RECOMENDADO)
# ==========================================

print("\n" + "="*50)
print("4. plt.subplots() - MÉTODO MODERNO")
print("="*50)

# plt.subplots() crua a figura E todos os eixos de uma vez
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
# fig: a figura inteira
# axes: matriz 2x2 de eixos (cada eixo é um gráfico)

# axes[0,0] - gráfico na linha 0, coluna 0
axes[0,0].plot(meses, vendas, 'bo-')
axes[0,0].set_title('Vendas (linha)')
axes[0,0].grid(True)

# axes[0, 1] - gráfico na linha 0, coluna 1
axes[0, 1].bar(meses, vendas, color='blue')
axes[0, 1].set_title('Vendas (Barras)')
axes[0, 1].grid(True)

# axes[1, 0] - gráfico na linha 1, coluna 0
axes[1, 0].plot(meses, custos, 'rs--')
axes[1, 0].set_title('Custos (Linha)')
axes[1, 0].grid(True)

# axes[1, 1] - gráfico na linha 1, coluna 1
axes[1, 1].bar(meses, custos, color='red')
axes[1, 1].set_title('Custos (Barras)')
axes[1, 1].grid(True)

plt.tight_layout()
plt.close()
# plt.show()

# ==========================================
# 5. GRÁFICOS EM LINHA (1 linha, 3 colunas)
# ==========================================

print("\n" + "="*50)
print("5. plt.subplots() - 1 LINHA, 3 COLUNAS")
print("="*50)

# Criar figura com 1 linha, 3 colunas
fig, axes = plt.subplots(1, 3, figsize=(12, 4))

# Gráfico 1 (coluna 0)
axes[0].plot(meses, vendas, 'bo-')
axes[0].set_title('Vendas')
axes[0].set_xlabel('Mês')
axes[0].set_ylabel('Valor')
axes[0].grid(True)

# Gráfico 2 (coluna 1)
axes[1].plot(meses, custos, 'rs--')
axes[1].set_title('Custos')
axes[1].set_xlabel('Mês')
axes[1].grid(True)

# Gráfico 3 (coluna 2)
axes[2].plot(meses, lucros, 'g^:')
axes[2].set_title('Lucros')
axes[2].set_xlabel('Mês')
axes[2].grid(True)

plt.tight_layout()
plt.close()
# plt.show()

# ==========================================
# 6. EIXOS COMPARTILHADOS (sharex, sharey)
# ==========================================

print("\n" + "="*50)
print("6. EIXOS COMPARTILHADOS")
print("="*50)

# Compartilhar eixo x (mesmo x para todos)
fig, axes = plt.subplots(2, 2, figsize=(10, 8), sharex=True, sharey=True)

# Dados
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x) * 2
y4 = np.cos(x) * 2

axes[0,0].plot(x, y1)
axes[0,0].set_title('Seno')

axes[0,1].plot(x, y2)
axes[0,1].set_title('Cosseno')

axes[1,0].plot(x, y3)
axes[1,0].set_title('Seno x2')

axes[1,1].plot(x,y4)
axes[1,1].set_title('Cosseno x2')

plt.tight_layout()
plt.close()
# plt.show()

print("Com sharex=True e sharey=True, todos os gráficos usam os mesmos limites de eixos")

# ==========================================
# 7. EXEMPLO PRÁTICO COM PANDAS
# ==========================================

print("\n" + "="*50)
print("7. EXEMPLO PRÁTICO COM PANDAS")
print("="*50)

# Dados
df = pd.DataFrame({
    'ano': [2019, 2020, 2021, 2022, 2023, 2024],
    'receita': [50000, 55000, 60000, 75000, 90000, 110000],
    'custo': [40000, 42000, 45000, 50000, 60000, 70000],
    'lucro': [10000, 13000, 15000, 25000, 30000, 40000]
})

# Criar gráficos
fig, axes = plt.subplots(1, 3, figsize=(15, 5), sharey=True)

# Gráfico 1: Receita
axes[0].plot(df['ano'], df['receita'], 'go-', linewidth=2)
axes[0].set_title('Receita por ano')
axes[0].set_xlabel('Ano')
axes[0].set_ylabel('Receita (R$)')
axes[0].grid(True)

# Gráfico 2: Custo
axes[1].plot(df['ano'], df['custo'], 'rs--', linewidth=2)
axes[1].set_title('Custo por ano')
axes[1].set_xlabel('Ano')
axes[1].set_ylabel('Custo (R$)')
axes[1].grid(True)

# Gráfico 3: Lucro
axes[2].plot(df['ano'], df['lucro'], 'b^:', linewidth=2)
axes[2].set_title('Lucro por ano')
axes[2].set_xlabel('Ano')
axes[2].set_ylabel('Lucro (R$)')
axes[2].grid(True)

plt.tight_layout()
plt.close()
# plt.show()

# ==========================================
# 8. SALVANDO FIGURAS COM MÚLTIPLOS GRÁFICOS
# ==========================================

print("\n" + "="*50)
print("8. SALVANDO SUBPLOTS")
print("="*50)

fig, axes = plt.subplots(2, 2, figsize=(10, 8))


axes[0, 0].plot(meses, vendas, 'bo-')
axes[0, 0].set_title('Vendas')

axes[0, 1].bar(meses, vendas, color='blue')
axes[0, 1].set_title('Vendas (Barras)')

axes[1, 0].plot(meses, custos, 'rs--')
axes[1, 0].set_title('Custos')

axes[1, 1].bar(meses, custos, color='red')
axes[1, 1].set_title('Custos (Barras)')

plt.tight_layout()
plt.savefig('dashboard_vendas.png')
plt.close()
# plt.show()

# ==========================================
# 9. DICAS IMPORTANTES
# ==========================================

print("\n" + "="*50)
print("9. DICAS IMPORTANTES")
print("="*50)

"""
📌 plt.subplot() vs plt.subplots()

plt.subplot():
- Adiciona um gráfico por vez
- Bom para criar gráficos gradualmente
- Sintaxe: plt.subplot(linhas, colunas, indice)

plt.subplots():
- Cria todos os eixos de uma vez
- Melhor para programação estruturada
- Sintaxe: fig, axes = plt.subplots(linhas, colunas, figsize=(w, h))

📌 Acesso aos eixos:
- 1 linha, 3 colunas: axes[0], axes[1], axes[2]
- 2 linhas, 2 colunas: axes[0,0], axes[0,1], axes[1,0], axes[1,1]
- 3 linhas, 1 coluna: axes[0], axes[1], axes[2]

📌 Sempre use plt.tight_layout() para evitar sobreposição
"""

# ==========================================
# 10. RESUMO
# ==========================================

print("\n" + "="*50)
print("10. RESUMO")
print("="*50)

"""
✅ plt.subplot(linhas, colunas, indice): adiciona gráfico na posição
✅ plt.subplots(linhas, colunas, figsize): cria figura e eixos de uma vez
✅ axes[linha, coluna]: acessa cada eixo (quando 2D)
✅ axes[indice]: acessa cada eixo (quando 1D)
✅ .set_title(), .set_xlabel(), .set_ylabel(): personalizar cada eixo
✅ plt.tight_layout(): ajusta espaçamento automaticamente
✅ sharex=True, sharey=True: compartilhar limites de eixos

📌 Estruturas comuns:
- 1x2: fig, axes = plt.subplots(1, 2, figsize=(12, 6))
- 2x2: fig, axes = plt.subplots(2, 2, figsize=(10, 10))
- 3x1: fig, axes = plt.subplots(3, 1, figsize=(8, 12))
"""
####################################################################
# EXERCÍCIOS - AULA 2.3
####################################################################
# NÍVEL 1-3: Aquecimento
####################################################################
"""
1. Subplot básico (1x2)


# Dados: meses = ['Jan', 'Fev', 'Mar', 'Abr']
# vendas = [100, 150, 120, 180]
# lucros = [20, 50, 50, 60]
#
# Use plt.subplot() para criar uma figura com 1 linha e 2 colunas
# Gráfico 1: linha - vendas
# Gráfico 2: linha - lucros
# Adicione títulos e grade
"""
"""
meses = ['Jan', 'Fev', 'Mar', 'Abr']
vendas = [100, 150, 120, 180]
lucros = [20, 50, 50, 60]

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(meses, vendas, 'bo-')
plt.title('Vendas por mes')
plt.ylabel('Vendas (R$)')
plt.xlabel('Mês')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(meses, lucros, 'gs--')
plt.title('Lucro por mes')
plt.ylabel('Lucro (R$)')
plt.xlabel('Mês')
plt.grid(True)

plt.tight_layout()
plt.show()
"""
####################################################################
"""
2. Subplot com barras (2x1)

# Use os mesmos dados do exercício 1
# Crie uma figura com 2 linhas e 1 coluna
# Gráfico 1: barras - vendas
# Gráfico 2: barras - lucros
"""
"""
meses = ['Jan', 'Fev', 'Mar', 'Abr']
vendas = [100, 150, 120, 180]
lucros = [20, 50, 50, 60]

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.bar(meses, vendas, color='blue')
plt.title('Vendas por mês (barras)')
plt.ylabel('Vendas (R$)')
plt.xlabel('Mês')

plt.subplot(1, 2, 2)
plt.bar(meses, lucros, color='green')
plt.title('Lucro por mês (barras)')
plt.ylabel('Lucro (R$)')
plt.xlabel('Mês')

plt.tight_layout()
plt.show()
"""
####################################################################
"""
3. plt.subplots() básico (1x3)

# Use plt.subplots(1, 3) para criar:
# Gráfico 1: linha - vendas (azul)
# Gráfico 2: linha - custos (vermelho)
# Gráfico 3: linha - lucros (verde)
"""
"""
meses = ['Jan', 'Fev', 'Mar', 'Abr']
vendas = [100, 150, 120, 180]
lucros = [20, 50, 50, 60]

fig, axes = plt.subplots(1, 3, figsize=(12, 4), sharey=True)

axes[0].plot(meses, vendas, 'b')
axes[0].set_title('Vendas por mês')
axes[0].set_ylabel('Vendas (R$)')
axes[0].set_xlabel('Mês')
axes[0].grid(True, linestyle='--')

axes[1].plot(meses, custos, 'r')
axes[1].set_title('Custos por mês')
axes[1].set_ylabel('Custos (R$)')
axes[1].set_xlabel('Mês')
axes[1].grid(True, linestyle='--')

axes[2].plot(meses, lucros, 'g')
axes[2].set_title('Lucro por mês')
axes[2].set_ylabel('Lucro (R$)')
axes[2].set_xlabel('Mês')
axes[2].grid(True, linestyle='--')

plt.tight_layout()
plt.show()
"""
####################################################################
# NÍVEL 4-6: Aplicação
####################################################################
"""
4. Grade 2x2 com plt.subplots()

# Use plt.subplots(2, 2) para criar:
# (0,0): linha - vendas
# (0,1): barras - vendas
# (1,0): linha - custos
# (1,1): barras - custos
# Adicione títulos apropriados
"""
"""
meses = ['Jan', 'Fev', 'Mar', 'Abr']
vendas = [100, 150, 120, 180]
lucros = [20, 50, 50, 60]

fig, axes = plt.subplots(2, 2, figsize=(12, 8), sharey=True)

axes[0,0].plot(meses, vendas, 'b')
axes[0,0].set_title('Vendas por mes')
axes[0,0].set_ylabel('Vendas (R$)')
axes[0,0].set_xlabel('Mês')
axes[0,0].grid(True)


axes[0,1].bar(meses, vendas, color='blue')
axes[0,1].set_title('Vendas por mes')
axes[0,1].set_ylabel('Vendas (R$)')
axes[0,1].set_xlabel('Mês')


axes[1,0].plot(meses, custos, 'r')
axes[1,0].set_title('Custos por mes')
axes[1,0].set_ylabel('Custos (R$)')
axes[1,0].set_xlabel('Mês')
axes[1,0].grid(True)


axes[1,1].bar(meses, custos, color='red')
axes[1,1].set_title('Custos por mes')
axes[1,1].set_ylabel('Custos (R$)')
axes[1,1].set_xlabel('Mês')

plt.tight_layout()
plt.show()
"""
####################################################################
"""
5. Dashboard de vendas (1x3 com personalização)

# Crie um dashboard 1x3 com:
# Gráfico 1: linha - vendas (azul, círculo, sólida)
# Gráfico 2: linha - custos (vermelho, quadrado, tracejada)
# Gráfico 3: linha - lucros (verde, triângulo, pontilhada)
# Cada gráfico: título, grade, rótulos dos eixos
"""
"""
meses = ['Jan', 'Fev', 'Mar', 'Abr']
vendas = [100, 150, 120, 180]
lucros = [20, 50, 50, 60]

fig, axes = plt.subplots(1, 3, figsize=(14, 4), sharey=True)

axes[0].plot(meses, vendas, 'bo-')
axes[0].set_title('Vendas por Mês')
axes[0].set_ylabel('Valor (R$)')
axes[0].set_xlabel('Mês')
axes[0].grid(True, linestyle='--')

axes[1].plot(meses, custos, 'rs--')
axes[1].set_title('Custos por Mês')
axes[1].set_xlabel('Mês')
axes[1].grid(True, linestyle='--')

axes[2].plot(meses, lucros, 'g^:')
axes[2].set_title('Lucro por Mês')
axes[2].set_xlabel('Mês')
axes[2].grid(True, linestyle='--')

plt.tight_layout()
plt.show()
"""
####################################################################
"""
6. Salvando subplots

# Repita o exercício 5
# Salve a figura como 'dashboard_empresa.png'
"""
"""
meses = ['Jan', 'Fev', 'Mar', 'Abr']
vendas = [100, 150, 120, 180]
lucros = [20, 50, 50, 60]

fig, axes = plt.subplots(1, 3, figsize=(14, 4), sharey=True)

axes[0].plot(meses, vendas, 'bo-')
axes[0].set_title('Vendas por Mês')
axes[0].set_ylabel('Valor (R$)')
axes[0].set_xlabel('Mês')
axes[0].grid(True, linestyle='--')

axes[1].plot(meses, custos, 'rs--')
axes[1].set_title('Custos por Mês')
axes[1].set_xlabel('Mês')
axes[1].grid(True, linestyle='--')

axes[2].plot(meses, lucros, 'g^:')
axes[2].set_title('Lucro por Mês')
axes[2].set_xlabel('Mês')
axes[2].grid(True, linestyle='--')

plt.tight_layout()
plt.savefig('dashboard_empresa.png')
plt.show()
"""
####################################################################
# NÍVEL 7-8: Manipulação
####################################################################
"""
7. Eixos compartilhados

# Use plt.subplots(2, 1, sharex=True, sharey=True)
# Gráfico 1: linha - vendas (meses no eixo X)
# Gráfico 2: linha - custos (meses no eixo X)
# Mostre como os eixos ficam sincronizados
"""
"""
meses = ['Jan', 'Fev', 'Mar', 'Abr']
vendas = [100, 150, 120, 180]
lucros = [20, 50, 50, 60]

fig, axes = plt.subplots(2, 1, figsize=(4, 6), sharex=True, sharey=True)

axes[0].plot(meses, vendas, 'bo-')
axes[0].set_title('Vendas por Mês')
axes[0].set_ylabel('Valor (R$)')
axes[0].set_xlabel('Mês')
axes[0].grid(True, linestyle='--')

axes[1].plot(meses, custos, 'rs--')
axes[1].set_title('Custos por Mês')
axes[1].set_xlabel('Mês')
axes[1].grid(True, linestyle='--')

plt.tight_layout()
plt.show()
"""
####################################################################
"""
8. Gráficos com dados diferentes

# Dados: 
# vendas_mensais = [100, 150, 120, 180, 200, 210] (6 meses)
# vendas_anuais = [50000, 55000, 60000] (3 anos)
# 
# Crie um subplot 1x2 com:
# Gráfico 1: vendas mensais (12 meses - crie dados fictícios)
# Gráfico 2: vendas anuais (barras)
# Os gráficos têm escalas diferentes - isso é normal.
"""
"""
# Dados completos (12 meses)
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
vendas_mensais = [100, 150, 120, 180, 200, 210, 230, 250, 240, 220, 190, 170]

# Dados anuais (3 anos)
anos = ['2022', '2023', '2024']
vendas_anuais = [50000, 55000, 60000]

fig, axes = plt.subplots(1, 2, figsize=(15, 6))

axes[0].plot(meses, vendas_mensais, 'bo-')
axes[0].set_title('Vendas mensais x Mês')
axes[0].set_ylabel('Vendas mensais (qtd.)')
axes[0].grid(True, linestyle='--')

axes[1].plot(anos, vendas_anuais, 'go-')
axes[1].set_title('Vendas anuais x Mês')
axes[1].set_ylabel('Vendas anuais (qtd.)')
axes[1].grid(True, linestyle='--')

plt.tight_layout()
plt.show()
"""
####################################################################
# NÍVEL 9-10: Desafios
####################################################################
"""
9. Dashboard de indicadores (2x2)

# Dados:
anos = [2019, 2020, 2021, 2022, 2023, 2024]
receita = [50000, 55000, 60000, 75000, 90000, 110000]
custo = [40000, 42000, 45000, 50000, 60000, 70000]
lucro = [10000, 13000, 15000, 25000, 30000, 40000]
funcionarios = [10, 11, 12, 14, 16, 18]

# Crie um dashboard 2x2 com:
# (0,0): linha - Receita (verde)
# (0,1): linha - Custo (vermelho)
# (1,0): linha - Lucro (azul)
# (1,1): barras - Funcionários (roxo)
#
# Cada gráfico: título, grade, rótulos
# Salve como 'dashboard_empresa_completo.png'
"""
"""
anos = [2019, 2020, 2021, 2022, 2023, 2024]
receita = [50000, 55000, 60000, 75000, 90000, 110000]
custo = [40000, 42000, 45000, 50000, 60000, 70000]
lucro = [10000, 13000, 15000, 25000, 30000, 40000]
funcionarios = [10, 11, 12, 14, 16, 18]

fig, axes = plt.subplots(2, 2, figsize=(10, 8))

axes[0,0].plot(anos, receita, 'go-')
axes[0,0].set_title('Receita x Ano')
axes[0,0].set_ylabel('Receita (R$)')
axes[0,0].set_xlabel('Ano')
axes[0,0].grid(True, linestyle='--')
axes[0,0].set_ylim(0, 120000)

axes[0,1].plot(anos, custo, 'ro--')
axes[0,1].set_title('Custos x Ano')
axes[0,1].set_ylabel('Custo (R$)')
axes[0,1].set_xlabel('Ano')
axes[0,1].grid(True, linestyle='--')
axes[0,1].set_ylim(0, 120000)

axes[1,0].plot(anos, lucro, 'b^:')
axes[1,0].set_title('Lucro x Ano')
axes[1,0].set_ylabel('Lucro (R$)')
axes[1,0].set_xlabel('Ano')
axes[1,0].grid(True, linestyle='--')
axes[1,0].set_ylim(0, 120000)

axes[1,1].bar(anos, funcionarios, color='purple')
axes[1,1].set_title('Funcionários x Ano')
axes[1,1].set_ylabel('Funcionários (qtd.)')
axes[1,1].set_xlabel('Ano')

plt.tight_layout()
plt.savefig('dashboard_empresa_completo.png')
plt.show()
"""
####################################################################
"""
10. DESAFIO FINAL: Pipeline de dados + Dashboard

# 1. Crie um DataFrame com dados de vendas de 3 produtos ao longo de 6 meses
#    - Produto A: vendas aleatórias entre 100-200
#    - Produto B: vendas aleatórias entre 50-150
#    - Produto C: vendas aleatórias entre 200-300
#    (use np.random.randint ou crie manualmente)
#
# 2. Calcule para cada produto:
#    - Vendas totais (soma de 6 meses)
#    - Média mensal
#    - Mês de maior venda
#
# 3. Crie um dashboard 2x2 com:
#    (0,0): linha - vendas do Produto A (azul)
#    (0,1): linha - vendas do Produto B (vermelho)
#    (1,0): linha - vendas do Produto C (verde)
#    (1,1): barras - vendas totais por produto
#
# 4. Salve o dashboard
# 5. Mostre no console as estatísticas (totais, médias, meses de pico)
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'mes': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun'],
    'Produto A': np.random.randint(100, 201, 6),
    'Produto B': np.random.randint(50, 151, 6),
    'Produto C': np.random.randint(200, 301, 6)
})

for column in df.columns:
    if column != 'mes':
        print(f'- {column}:')
        print(f'  - Vendas totais: {df[column].sum()}')
        print(f'  - Média mensal: {df[column].mean():.2f}')
        print(f'  - Mês de maior venda: { df[['mes', column]].loc[df[column].idxmax(), 'mes']}')
        print()

fig, axes = plt.subplots(2, 2, figsize=(10, 8))

axes[0,0].plot(df['mes'], df['Produto A'], 'bo-')
axes[0,0].set_title('Vendas Produto A x Mês')
axes[0,0].set_ylabel('Vendas Produto A (qtd.)')
axes[0,0].set_xlabel('Mês')
axes[0,0].grid(True)
axes[0,0].set_ylim(0, 400)

axes[0,1].plot(df['mes'], df['Produto B'], 'ro-')
axes[0,1].set_title('Vendas Produto B x Mês')
axes[0,1].set_ylabel('Vendas Produto B (qtd.)')
axes[0,1].set_xlabel('Mês')
axes[0,1].grid(True)
axes[0,1].set_ylim(0, 400)

axes[1,0].plot(df['mes'], df['Produto C'], 'go-')
axes[1,0].set_title('Vendas Produto C x Mês')
axes[1,0].set_ylabel('Vendas Produto C (qtd.)')
axes[1,0].set_xlabel('Mês')
axes[1,0].grid(True)
axes[1,0].set_ylim(0, 400)

produtos = [column for column in df.columns if column != 'mes']
vendas_totais = [df[produto].sum() for produto in produtos]

axes[1,1].bar(produtos, vendas_totais, color='purple')
axes[1,1].set_title('Quantidade de Vendas x Produto')
axes[1,1].set_ylabel('Quantidade de Vendas')
axes[1,1].set_xlabel('Produto')

plt.tight_layout()
plt.savefig('dashboard_basico_simulado.png')
plt.show()
