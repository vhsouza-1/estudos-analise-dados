"""
Bloco 3: Python para Dados
Módulo 2: Visualização de Dados
Aula 1: Introdução ao Matplotlib
Data: 28/04/2026
Objetivo: Aprender a criar gráficos básicos com Matplotlib
"""
import matplotlib.pyplot as plt
import pandas as pd

# ==========================================
# 1. O QUE É MATPLOTLIB?
# ==========================================

print("="*50)
print("1. O QUE É MATPLOTLIB?")
print("="*50)

"""
Matplotlib é a biblioteca mais básica para gráficos em Python.
- Criada em 2003
- Base para muitas outras (Seaborn, Plotly)
- Permite criar gráficos de linha, barra, dispersão, pizza, etc.

Vantagens:
- Muito flexível
- Documentação extensa
- Integração com Pandas

Desvantagens:
- Sintaxe verbosa (muita linha para um gráfico simples)
- Estilo "antigo" (mas podemos melhorar)
"""

# ==========================================
# 2. IMPORTANDO O MATPLOTLIB
# ==========================================

print("\n" + "="*50)
print("2. IMPORTANDO O MATPLOTLIB")
print("="*50)

# A convenção padrão da comunidade é:
import matplotlib.pyplot as plt

# Agora podemos usar plt.algo() para criar gráficos

# ==========================================
# 3. GRÁFICO DE LINHA (PLOT)
# ==========================================

print("\n" + "="*50)
print("3. GRÁFICO DE LINHA (plt.plot())")
print("="*50)

# Dados de exemplo
dias = ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab', 'Dom']
vendas = [120, 150, 90, 200, 180, 210, 160]

# Criar o gráfico
# plt.plot(dias, vendas)

# Exibir o gráfico
# plt.show()

print("Gráfico de linha criado! Feche a janela para continuar.")

# ==========================================
# 4. GRÁFICO DE BARRAS (BAR)
# ==========================================

print("\n" + "="*50)
print("4. GRÁFICO DE BARRAS (plt.bar())")
print("="*50)

# Dados de exemplo
produtos = ['Celular', 'Fone', 'Notebook', 'Mouse', 'Teclado']
quantidades = [10, 30, 5, 100, 50]

# Os gráficos estavam bugando um pouco fui pesquisar e descobri esses comandos. Sei que vamos ver em seguida.
# plt.clf()

# Criar o gráfico
# plt.bar(produtos, quantidades)

# Exibir
# plt.show()

print("Gráfico de barras criado!")

# ==========================================
# 5. GRÁFICO DE DISPERSÃO (SCATTER)
# ==========================================

print("\n" + "="*50)
print("5. GRÁFICO DE DISPERSÃO (plt.scatter())")
print("="*50)

# Dados de exemplo: relação entre preço e quantidade vendida
precos = [1500, 200, 3500, 50, 120, 1500, 200, 50]
quantidades_vendidas = [10, 30, 5, 100, 50, 8, 20, 80]

# Criar o gráfico
# plt.clf()
# plt.scatter(precos, quantidades_vendidas)

# Exibir
# plt.show()
# plt.close()

print("Gráfico de dispersão criado!")

# ==========================================
# 6. SALVANDO GRÁFICOS (savefig)
# ==========================================

print("\n" + "="*50)
print("6. SALVANDO GRÁFICOS (plt.savefig())")
print("="*50)

# Criar um gráfico
dias = ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab', 'Dom']
vendas = [120, 150, 90, 200, 180, 210, 160]


# plt.plot(dias, vendas)

# Salvar antes de mostrar (ou depois, mas antes é mais seguro)
# plt.savefig('grafico_linha.png')  # Salva como PNG
# plt.savefig('grafico_linha.pdf')  # Salva como PDF

print("Gráfico salvo como 'grafico_linha.png' e 'grafico_linha.pdf'")

# Exibir (opcional - já salvamos)
# plt.show()
# plt.close()

# ==========================================
# 7. TAMANHO DA FIGURA (figsize)
# ==========================================

print("\n" + "="*50)
print("7. TAMANHO DA FIGURA (figsize)")
print("="*50)

# Criar uma figura maior (10 polegada de largura, 6 de altura)
# plt.figure(figsize=(10, 6))

dias = ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab', 'Dom']
vendas = [120, 150, 90, 200, 180, 210, 160]

# plt.plot(dias, vendas)

# plt.savefig('teste.png')

# plt.show()
# plt.close()

print("Gráfico com tamanho personalizado!")

# ==========================================
# 8. EXEMPLO PRÁTICO COM PANDAS
# ==========================================

print("\n" + "="*50)
print("8. EXEMPLO PRÁTICO COM PANDAS")
print("="*50)

# Dados de vendas (DataFrame)
df_vendas = pd.DataFrame({
    'mes': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun'],
    'vendas': [12000, 15000, 9000, 20000, 18000, 21000],
    'custo': [8000, 10000, 7000, 12000, 11000, 13000]
})

print(f'\nDados vendas:\n{df_vendas}\n')

# Gráfico de linha das vendas
# plt.plot(df_vendas['mes'], df_vendas['vendas'])
#
# plt.show()
# plt.close()
#
# # Gráfico de barras das vendas
# plt.bar(df_vendas['mes'], df_vendas['vendas'])
#
# plt.show()
# plt.close()

# ==========================================
# 9. RESUMO
# ==========================================

print("\n" + "="*50)
print("9. RESUMO")
print("="*50)

"""
✅ import matplotlib.pyplot as plt: importação padrão

✅ plt.plot(x, y): gráfico de linha
✅ plt.bar(x, y): gráfico de barras
✅ plt.scatter(x, y): gráfico de dispersão

✅ plt.show(): exibir o gráfico
✅ plt.savefig('nome.png'): salvar como imagem
✅ plt.figure(figsize=(largura, altura)): tamanho da figura

📌 Regras importantes:
- Sempre importe como 'plt' (convenção)
- plt.show() trava o código até fechar a janela
- plt.savefig() pode ser antes ou depois do show()
"""
#################################################################################
# EXERCÍCIOS - AULA 2.1
#################################################################################
# NÍVEL 1-3: Aquecimento
#################################################################################
"""
1. Gráfico de linha simples

# Dados: meses = ['Jan', 'Fev', 'Mar', 'Abr']
# vendas = [100, 150, 120, 180]
# Crie um gráfico de linha com plt.plot()
"""
"""
meses = ['Jan', 'Fev', 'Mar', 'Abr']
vendas = [100, 150, 120, 180]

plt.plot(meses, vendas)
plt.show()
"""
#################################################################################
"""
2. Gráfico de barras simples

# Use os mesmos dados do exercício 1
# Crie um gráfico de barras com plt.bar()

"""
"""
meses = ['Jan', 'Fev', 'Mar', 'Abr']
vendas = [100, 150, 120, 180]

plt.bar(meses, vendas)
plt.show()
"""
#################################################################################
"""
3. Gráfico de dispersão simples

# Dados: idades = [25, 30, 22, 28, 35]
# salarios = [3000, 4500, 2500, 4000, 5000]
# Crie um gráfico de dispersão com plt.scatter()
"""
"""
idades = [25, 30, 22, 28, 35]
salarios = [3000, 4500, 2500, 4000, 5000]

plt.scatter(idades, salarios)
plt.show()
"""
#################################################################################
# NÍVEL 4-6: Aplicação
#################################################################################
"""
4. Salvando gráfico

# Crie um gráfico de linha com os dados do exercício 1
# Salve o gráfico como 'vendas_mensais.png'
# Salve também como 'vendas_mensais.pdf'
"""
"""
meses = ['Jan', 'Fev', 'Mar', 'Abr']
vendas = [100, 150, 120, 180]

plt.plot(meses, vendas)
plt.savefig('vendas_mensais.png')
plt.savefig('vendas_mensais.pdf')
plt.show()
"""
#################################################################################
"""
5. Tamanho da figura

# Crie um gráfico de barras com os dados do exercício 1
# Use figsize=(8, 4) para o tamanho
# Salve como 'vendas_barras.png'
"""
"""
meses = ['Jan', 'Fev', 'Mar', 'Abr']
vendas = [100, 150, 120, 180]

plt.figure(figsize=(8, 4))
plt.bar(meses, vendas)
plt.savefig('vendas_barras.png')
plt.close()
"""
#################################################################################
"""
6. Gráfico a partir de DataFrame

# Crie um DataFrame com:
# produto = ['A', 'B', 'C', 'D']
# quantidade = [50, 80, 30, 60]
#
# Faça um gráfico de barras com produto no eixo X e quantidade no eixo Y
"""
"""
produto = ['A', 'B', 'C', 'D']
quantidade = [50, 80, 30, 60]

df = pd.DataFrame({
    'produto': produto,
    'quantidade': quantidade
})

plt.bar(df['produto'], df['quantidade'])
plt.show()
"""
#################################################################################
# NÍVEL 7-8: Manipulação
#################################################################################
"""
7. Múltiplas séries em um gráfico

# Crie um DataFrame com:
# mes = ['Jan', 'Fev', 'Mar', 'Abr']
# vendas_produto1 = [100, 120, 90, 110]
# vendas_produto2 = [80, 100, 110, 95]
#
# Faça um gráfico de linha com as duas séries em cores diferentes
# Dica: chame plt.plot() duas vezes antes do plt.show()
"""
"""
mes = ['Jan', 'Fev', 'Mar', 'Abr']
vendas_produto1 = [100, 120, 90, 110]
vendas_produto2 = [80, 100, 110, 95]

df = pd.DataFrame({
    'mes': mes,
    'vendas_produto1': vendas_produto1,
    'vendas_produto2': vendas_produto2
})

plt.plot(df['mes'], df['vendas_produto1'])

plt.plot(df['mes'], df['vendas_produto2'])

plt.show()
"""
#################################################################################
"""
8. Comparação de gráficos

# Use os dados do exercício 7
# Crie dois gráficos separados:
# - Um gráfico de linha com as vendas do produto 1
# - Um gráfico de linha com as vendas do produto 2
# Salve cada um com um nome diferente
"""
"""
mes = ['Jan', 'Fev', 'Mar', 'Abr']
vendas_produto1 = [100, 120, 90, 110]
vendas_produto2 = [80, 100, 110, 95]

df = pd.DataFrame({
    'mes': mes,
    'vendas_produto1': vendas_produto1,
    'vendas_produto2': vendas_produto2
})

plt.plot(df['mes'], df['vendas_produto1'])
plt.savefig('vendas_produto1.png')
plt.close()

plt.plot(df['mes'], df['vendas_produto2'])
plt.savefig('vendas_produto2.png')
"""
#################################################################################
# NÍVEL 9-10: Desafios
#################################################################################
"""
9. Análise de dados reais (simulado)

# Dados de uma loja (2019-2024):
anos = [2019, 2020, 2021, 2022, 2023, 2024]
faturamento = [50000, 55000, 60000, 75000, 90000, 110000]
custos = [40000, 42000, 45000, 50000, 60000, 70000]

# Tarefas:
# 1. Gráfico de linha do faturamento ao longo dos anos
# 2. Gráfico de linha dos custos ao longo dos anos
# 3. Salve os dois gráficos
# 4. Calcule o lucro (faturamento - custo) para cada ano
# 5. Gráfico de barras do lucro por ano
"""
"""
anos = [2019, 2020, 2021, 2022, 2023, 2024]
faturamento = [50000, 55000, 60000, 75000, 90000, 110000]
custos = [40000, 42000, 45000, 50000, 60000, 70000]

df = pd.DataFrame({
    'ano': anos,
    'faturamento': faturamento,
    'custo': custos
})

plt.plot(df['ano'], df['faturamento'])
plt.savefig('faturamento_ano.png')
plt.close()

plt.plot(df['ano'], df['custo'])
plt.savefig('custo_ano.png')
plt.close()

df['lucro'] = df['faturamento'] - df['custo']
plt.bar(df['ano'], df['lucro'])
plt.savefig('lucro_ano.png')
"""
#################################################################################
"""
10. DESAFIO FINAL: Pipeline de vendas

# Leia o arquivo CSV que vamos criar abaixo
# Depois, crie os gráficos solicitados

import pandas as pd
from pathlib import Path

# Criar dados de exemplo
df = pd.DataFrame({
    'produto': ['Celular', 'Fone', 'Notebook', 'Mouse', 'Teclado', 'Monitor', 'Tablet'],
    'quantidade': [150, 300, 45, 500, 120, 30, 80],
    'preco_unitario': [1500, 200, 3500, 50, 120, 800, 1200]
})

# Salvar como CSV
Path('dados_vendas').mkdir(exist_ok=True)
df.to_csv('dados_vendas/produtos.csv', index=False)

# Tarefas:
# 1. Leia o arquivo 'dados_vendas/produtos.csv'
# 2. Calcule o faturamento total por produto (quantidade * preco_unitario)
# 3. Faça um gráfico de barras com produto e faturamento
# 4. Salve o gráfico como 'faturamento_produtos.png'
# 5. Faça um gráfico de dispersão (preco_unitario x quantidade)
# 6. Salve como 'relacao_preco_quantidade.png'
# 7. Encontre o produto com maior faturamento
# 8. Encontre o produto com maior quantidade vendida
# 9. Mostre os resultados no console
"""
import pandas as pd
from pathlib import Path

# Criar dados de exemplo
df = pd.DataFrame({
    'produto': ['Celular', 'Fone', 'Notebook', 'Mouse', 'Teclado', 'Monitor', 'Tablet'],
    'quantidade': [150, 300, 45, 500, 120, 30, 80],
    'preco_unitario': [1500, 200, 3500, 50, 120, 800, 1200]
})

# Salvar como CSV
Path('dados_vendas').mkdir(exist_ok=True)
df.to_csv('dados_vendas/produtos.csv', index=False)

###

caminho = Path('dados_vendas/produtos.csv')
df = pd.read_csv(caminho)

df['faturamento'] = df['quantidade'] * df['preco_unitario']

plt.bar(df['produto'], df['faturamento'])
plt.savefig('faturamento_produtos.png')
plt.close()

plt.scatter(df['preco_unitario'], df['quantidade'])
plt.savefig('relacao_preco_quantidade.png')
plt.close()

produto_maior_faturamento = df.loc[df['faturamento'].idxmax(), 'produto']
print(f'Produto com maior faturamento: {produto_maior_faturamento}')

produto_mais_vendido = df.loc[df['quantidade'].idxmax(), 'produto']
print(f'Produto com maior quantidade vendida: {produto_mais_vendido}')