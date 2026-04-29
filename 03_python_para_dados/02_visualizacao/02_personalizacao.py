"""
Bloco 3: Python para Dados
Módulo 2: Visualização de Dados
Aula 2: Personalização de Gráficos
Data: 29/04/2026
Objetivo: Aprender a personalizar gráficos (títulos, legendas, cores, etc.)
"""
import matplotlib.pyplot as plt
import pandas as pd
from pkg_resources import find_eggs_in_zip

# ==========================================
# 1. TÍTULO E RÓTULOS DOS EIXOS
# ==========================================

print("="*50)
print("1. TÍTULO E RÓTULOS DOS EIXOS")
print("="*50)

# Dados de exemplo
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun']
vendas = [120, 150, 90, 200, 180, 210]

# # criar o gráfico
# plt.plot(meses, vendas)
#
# # Adicionar título
# plt.title('Vendas por Mês')
#
# # Adicionar rótulos ao eixo x
# plt.xlabel('Mês')
#
# # Adicionar rótulos ao eixo y
# plt.ylabel('Vendas (R$)')
#
# # Exibir
# plt.show()

# ==========================================
# 2. CORES
# ==========================================

print("\n" + "="*50)
print("2. CORES (color=)")
print("="*50)

# Cores disponíveis:
# 'red', 'blue', 'green', 'yellow', 'black', 'purple', 'orange', 'gray', etc.

# plt.plot(meses, vendas, color='blue')
# plt.title('Vendas por Mês')
# plt.xlabel('Mês')
# plt.ylabel('Vendas (R$)')
# plt.show()

# Cores diferentes para cada série
vendas_produto2 = [80, 100, 110, 95, 120, 130]

# plt.plot(meses, vendas, color='blue', label='Produto A')
# plt.plot(meses, vendas_produto2, color='red', label='Produto B')
# plt.title('Vendas por Produto')
# plt.xlabel('Mês')
# plt.ylabel('Vendas (R$)')
# plt.show()

# ==========================================
# 3. LEGENDA
# ==========================================

print("\n" + "="*50)
print("3. LEGENDA (plt.legend())")
print("="*50)

# plt.plot(meses, vendas, color='blue', label='Produto A')
# plt.plot(meses, vendas_produto2, color='red', label='Produto B')
# plt.title('Vendas por Produto')
# plt.xlabel('Mês')
# plt.ylabel('Vendas (R$)')
# plt.legend()  # Adiciona a legenda (usa os labels definidos)
# plt.show()

# Legendas com localização personalizada
# plt.plot(meses, vendas, color='blue', label='Produto A')
# plt.plot(meses, vendas_produto2, color='red', label='Produto B')
# plt.title('Vendas por Produto')
# plt.xlabel('Mês')
# plt.ylabel('Vendas (R$)')
# plt.legend(loc='lower right')  # localização: 'upper left', 'upper right', 'lower left', 'lower right'
# plt.show()

# ==========================================
# 4. ESTILOS DE LINHA (linestyle)
# ==========================================

print("\n" + "="*50)
print("4. ESTILOS DE LINHA (linestyle)")
print("="*50)

# Estilos disponíveis:
# '-' : linha sólida (padrão)
# '--' : linha tracejada
# ':' : linha pontilhada
# '-.' : linha traço-ponto

# plt.plot(meses, vendas, color='blue', linestyle='-', label='Sólida')
# plt.plot(meses, vendas_produto2, color='red', linestyle='--', label='Tracejada')
# plt.title('Comparação de Estilos')
# plt.xlabel('Mês')
# plt.ylabel('Vendas (R$)')
# plt.legend()
# plt.show()

# ==========================================
# 5. MARCADORES (marker)
# ==========================================

print("\n" + "="*50)
print("5. MARCADORES (marker)")
print("="*50)

# Marcadores disponíveis:
# 'o' : círculo
# 's' : quadrado
# '^' : triângulo
# 'D' : diamante
# 'x' : x
# '+' : +

# plt.plot(meses, vendas, color='blue', marker='o', label='Círculo')
# plt.plot(meses, vendas_produto2, color='red', marker='s', label='Quadrado')
# plt.title('Comparação de Marcadores')
# plt.xlabel('Mês')
# plt.ylabel('Vendas (R$)')
# plt.legend()
# plt.show()

# # Combinando estilo de linha + marcador + cor
# plt.plot(meses, vendas, 'o-', color='blue', label='Produto A')  # 'o-' = círculo + linha
# plt.plot(meses, vendas_produto2, 's--', color='red', label='Produto B')  # 's--' = quadrado + tracejada
# plt.title('Combinando Estilos')
# plt.xlabel('Mês')
# plt.ylabel('Vendas (R$)')
# plt.legend()
# plt.show()

# ==========================================
# 6. ESPESSURA DA LINHA (linewidth)
# ==========================================

print("\n" + "="*50)
print("6. ESPESSURA DA LINHA (linewidth)")
print("="*50)

# plt.plot(meses, vendas, color='blue', linewidth=1, label='Fina (1)')
# plt.plot(meses, vendas_produto2, color='red', linewidth=3, label='Grossa (3)')
# plt.title('Comparação de Espessura')
# plt.xlabel('Mês')
# plt.ylabel('Vendas (R$)')
# plt.legend()
# plt.show()

# ==========================================
# 7. GRADE (plt.grid())
# ==========================================

print("\n" + "="*50)
print("7. GRADE (plt.grid())")
print("="*50)

# plt.plot(meses, vendas, color='blue', marker='o')
# plt.title('Vendas por Mês com Grade')
# plt.xlabel('Mês')
# plt.ylabel('Vendas (R$)')
# plt.grid(True)  # Adiciona grade
# plt.show()

# Grade personalizada
# plt.plot(meses, vendas, color='blue', marker='o')
# plt.title('Vendas por Mês - Grade com Estilo')
# plt.xlabel('Mês')
# plt.ylabel('Vendas (R$)')
# plt.grid(True, linestyle='--', alpha=0.7)  # alpha = transparência (0 a 1)
# plt.show()

# ==========================================
# 8. LIMITES DOS EIXOS (xlim, ylim)
# ==========================================

print("\n" + "="*50)
print("8. LIMITES DOS EIXOS (xlim, ylim)")
print("="*50)

# plt.plot(meses, vendas, color='blue', marker='o')
# plt.title('Vendas por Mês - Eixos Ajustados')
# plt.xlabel('Mês')
# plt.ylabel('Vendas (R$)')
# plt.ylim(0, 300)  # Eixo Y vai de 0 a 300
# plt.show()

# ==========================================
# 9. EXEMPLO COMPLETO (tudo junto)
# ==========================================

print("\n" + "="*50)
print("9. EXEMPLO COMPLETO")
print("="*50)

# Dados
anos = [2019, 2020, 2021, 2022, 2023, 2024]
receita = [50000, 55000, 60000, 75000, 90000, 110000]
custo = [40000, 42000, 45000, 50000, 60000, 70000]

# # Criar figura
# plt.figure(figsize=(10, 6))
#
# # Plot duas séries
# plt.plot(anos, receita, color='green', marker='o', linestyle='-', linewidth=2, label='Receita')
# plt.plot(anos, custo, color='red', marker='s', linestyle='--', linewidth=2, label='Custo')
#
# # Personalizações
# plt.title('Evolução de Receita e Custo (2019-2024)', fontsize=16)
# plt.xlabel('Ano', fontsize=12)
# plt.ylabel('Valor', fontsize=12)
# plt.legend(loc='upper left')
# plt.grid(True, linestyle='--', alpha=0.5)
# plt.ylim(30000, 120000)
#
# # Mostrar
# plt.show()

# ==========================================
# 10. EXEMPLO COM PANDAS
# ==========================================

print("\n" + "="*50)
print("10. EXEMPLO COM PANDAS")
print("="*50)

# DataFrame
df = pd.DataFrame({
    'mês': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun'],
    'vendas': [120, 150, 90, 200, 180, 210],
    'custos': [80, 100, 70, 120, 110, 130]
})

# Gráfico direto do DataFrame (com personalização)
# plt.figure(figsize=(10, 6))
# plt.plot(df['mês'], df['vendas'], color='blue', marker='o', linewidth=2, label='Vendas')
# plt.plot(df['mês'], df['custos'], color='red', marker='s', linewidth=2, label='Custos')
# plt.title('Vendas vs Custos', fontsize=16)
# plt.xlabel('Mês', fontsize=12)
# plt.ylabel('Valor (R$)', fontsize=12)
# plt.legend()
# plt.grid(True, linestyle='--')
# plt.show()

# ==========================================
# 11. RESUMO
# ==========================================

print("\n" + "="*50)
print("11. RESUMO")
print("="*50)

"""
✅ plt.title('Título'): título do gráfico
✅ plt.xlabel('Eixo X'): rótulo do eixo X
✅ plt.ylabel('Eixo Y'): rótulo do eixo Y
✅ plt.legend(): legenda (usa label= nos plots)
✅ plt.legend(loc='upper left'): posição da legenda

✅ color='red': cor da linha/marcador
✅ linestyle='--': estilo da linha ( -, --, :, -. )
✅ marker='o': marcador (o, s, ^, D, x, +)
✅ linewidth=2: espessura da linha

✅ plt.grid(True): adiciona grade
✅ plt.grid(True, linestyle='--', alpha=0.7): grade personalizada

✅ plt.xlim(min, max): limites do eixo X
✅ plt.ylim(min, max): limites do eixo Y

📌 Atalhos para combinar estilo:
   'ro-' → círculo vermelho com linha
   'gs--' → quadrado verde com linha tracejada
   'b^:' → triângulo azul com linha pontilhada
"""
##################################################################
# EXERCÍCIOS - AULA 2.2
##################################################################
# NÍVEL 1-3: Aquecimento
##################################################################
"""
1. Título e rótulos

# Dados: meses = ['Jan', 'Fev', 'Mar', 'Abr']
# vendas = [100, 150, 120, 180]
# Crie um gráfico de linha com:
# - Título: "Vendas Mensais"
# - Eixo X: "Mês"
# - Eixo Y: "Vendas (R$)"
"""
"""
meses = ['Jan', 'Fev', 'Mar', 'Abr']
vendas = [100, 150, 120, 180]

plt.plot(meses, vendas)
plt.title('Vendas Mensais')
plt.xlabel('Mês')
plt.ylabel('Vendas (R$)')

plt.show()
"""
##################################################################
"""
2. Cores e legendas

# Use os dados do exercício 1
# Adicione uma segunda série: custos = [80, 100, 70, 120]
# Faça vendas em azul, custos em vermelho
# Adicione legenda ("Vendas", "Custos")
"""
"""
meses = ['Jan', 'Fev', 'Mar', 'Abr']
vendas = [100, 150, 120, 180]
custos = [80, 100, 70, 120]

plt.plot(meses, vendas, color='blue', label='Vendas')
plt.plot(meses, custos, color='red', label='Custos')

plt.title('Vendas Mensais')
plt.xlabel('Mês')
plt.ylabel('Vendas (R$)')

plt.legend()

plt.show()
"""
##################################################################
"""
3. Estilos de linha

# Use os dados do exercício 2
# Vendas: linha sólida (padrão)
# Custos: linha tracejada ('--')
# Adicione grade
"""
"""
meses = ['Jan', 'Fev', 'Mar', 'Abr']
vendas = [100, 150, 120, 180]
custos = [80, 100, 70, 120]

plt.plot(meses, vendas, color='blue', label='Vendas', linestyle='-') # pra testar a ordem
plt.plot(meses, custos, color='red', linestyle='--', label='Custos')

plt.title('Vendas Mensais')
plt.xlabel('Mês')
plt.ylabel('Vendas (R$)')

plt.legend()

plt.grid(True)

plt.show()
"""
##################################################################
# NÍVEL 4-6: Aplicação
##################################################################
"""
4. Marcadores

# Use os dados do exercício 2
# Vendas: círculo como marcador ('o')
# Custos: quadrado como marcador ('s')
# Espessura da linha: 2 para ambas
"""
"""
meses = ['Jan', 'Fev', 'Mar', 'Abr']
vendas = [100, 150, 120, 180]
custos = [80, 100, 70, 120]

plt.plot(meses, vendas, color='blue', label='Vendas', linestyle='-', marker='o', linewidth=2)
plt.plot(meses, custos, color='red', linestyle='--', label='Custos', marker='s', linewidth=2)

plt.title('Vendas Mensais')
plt.xlabel('Mês')
plt.ylabel('Vendas (R$)')

plt.legend()

plt.grid(True)

plt.show()
"""
##################################################################
"""
5. Gráfico de barras personalizado

# Dados: produtos = ['A', 'B', 'C', 'D']
# vendas = [50, 80, 30, 60]
# Crie um gráfico de barras com:
# - Barras na cor 'green'
# - Título: "Vendas por Produto"
# - Eixo Y: "Quantidade"
# - Grade
"""
"""
produtos = ['A', 'B', 'C', 'D']
vendas = [50, 80, 30, 60]

plt.bar(produtos, vendas, color='green')
plt.title('Vendas por Produto')
plt.ylabel('Quantidade')
plt.grid(True)


plt.show()
"""
##################################################################
"""
6. Gráfico de dispersão personalizado

# Dados: idades = [25, 30, 22, 28, 35, 27, 31, 29]
# salarios = [3000, 4500, 2500, 4000, 5000, 3500, 4200, 3800]
# Crie um gráfico de dispersão com:
# - Pontos em azul ('blue')
# - Marcador circular ('o')
# - Título: "Relação Idade vs Salário"
# - Eixo X: "Idade"
# - Eixo Y: "Salário (R$)"
# - Grade
# - Limite do eixo Y: 2000 a 6000
"""
"""
idades = [25, 30, 22, 28, 35, 27, 31, 29]
salarios = [3000, 4500, 2500, 4000, 5000, 3500, 4200, 3800]

plt.scatter(idades, salarios, color='blue', marker='o')
plt.title('Relação Idade vs Salário')
plt.xlabel('Idade')
plt.ylabel('Salário (R$)')
plt.grid(True)
plt.ylim(2000, 6000)

plt.show()
"""
##################################################################
# NÍVEL 7-8: Manipulação
##################################################################
"""
7. Combinando cores, marcadores e estilos

# Dados: anos = [2019, 2020, 2021, 2022, 2023, 2024]
# receita = [50000, 55000, 60000, 75000, 90000, 110000]
# custo = [40000, 42000, 45000, 50000, 60000, 70000]
# lucro = [10000, 13000, 15000, 25000, 30000, 40000]
#
# Crie UM gráfico com as três séries:
# - Receita: linha verde, círculo, sólida
# - Custo: linha vermelha, quadrado, tracejada
# - Lucro: linha azul, triângulo, pontilhada
# Adicione título, legendas, grade, e ajuste o eixo Y
"""
"""
anos = [2019, 2020, 2021, 2022, 2023, 2024]
receita = [50000, 55000, 60000, 75000, 90000, 110000]
custo = [40000, 42000, 45000, 50000, 60000, 70000]
lucro = [10000, 13000, 15000, 25000, 30000, 40000]

plt.plot(anos, receita, color='green', marker='o', linestyle='-', label='Receita')
plt.plot(anos, custo, 'rs--', label='Custo')
plt.plot(anos, lucro, 'b^:', label='Lucro')

plt.title('Receita, Custo e Lucro por Ano')
plt.ylabel('Valor (R$)')
plt.xlabel('Ano')
plt.legend()

plt.grid(True,linestyle='--')

plt.ylim(0, 130000)

plt.show()
"""
##################################################################
"""
8. Gráfico de barras com múltiplas séries

# Dados: empresas = ['Empresa A', 'Empresa B', 'Empresa C']
# receita_2023 = [100000, 80000, 120000]
# receita_2024 = [120000, 90000, 140000]
#
# Crie um gráfico de barras lado a lado:
# - Barras da Empresa A lado a lado
# - Cor azul para 2023, cor laranja para 2024
# - Legenda, título, rótulos
# Dica: use plt.bar() duas vezes, ajustando a posição
"""
"""
# Dados
empresas = ['Empresa A', 'Empresa B', 'Empresa C']
receita_2023 = [100000, 80000, 120000]
receita_2024 = [120000, 90000, 140000]

# Configurações das barras
largura = 0.3  # largura de cada barra
posicoes = range(len(empresas))  # posições base: 0, 1, 2

# Deslocar as barras para os lados
posicoes_2023 = [p - largura/2 for p in posicoes]  # 0.175, 0.825, ...
posicoes_2024 = [p + largura/2 for p in posicoes]  # 0.175, 0.825, ...

# Criar o gráfico
plt.bar(posicoes_2023, receita_2023, width=largura, color='blue', label='2023')
plt.bar(posicoes_2024, receita_2024, width=largura, color='orange', label='2024')

# Personalizar o eixo X (posições originais no centro das duas barras)
plt.xticks(posicoes, empresas)

# Rótulos
plt.title('Receita por Empresa (2023 vs 2024)')
plt.xlabel('Empresa')
plt.ylabel('Receita (R$)')
plt.legend()
plt.show()

# Precisei de muita ajuda pra fazer isso, vc não passou quase nada disso na aula...
# quando é assim nunca sei se vc quer que eu copie o exercicio que vc me passou e jogue em outro chat do DS
# e pergunta "como que faz? o outro chat não me ensinou nada disso". É isso que vc quer? Tipo assim, olha que trabalho
# vc faz eu copiar o trem em outro chat, atoa, sendo que vc poderia me explicar.
# ou vc quer que eu deduza que existe esses parametros? Que na minha cabeça é uma alucinação completa...
# uma coisa é quando vc me fala "pesquise sobre tal coisa" ai eu "opa, então existe um parametro que faz isso legal" ou modulo, ou qqr coisa
# agr a "dica" que vc me deu: "Dica: use plt.bar() duas vezes, ajustando a posição" ce quer que eu faça o que com isso?
# "ajustando a posição" que dica é essa!?
# Se for algum problema de memória desse chat, eu preciso que vc me avise, vc não pode compremeter meu aprendizado pq vc ta com vergonha de falar
# "ah então estamos com um problema de memória, voce pode ou trocar de chat, ou a gente faz um salvamente das coisas importantas ou sla oq"
"""
##################################################################
# NÍVEL 9-10: Desafios
##################################################################
"""
9. Dashboard simples (múltiplos gráficos customizados)

# Use os dados de vendas do exercício 7
# Crie 3 gráficos separados (em arquivos diferentes):
# 1. Gráfico de linha: Receita (verde, círculo, sólida)
# 2. Gráfico de linha: Custo (vermelho, quadrado, tracejada)
# 3. Gráfico de linha: Lucro (azul, triângulo, pontilhada)
#
# Cada gráfico deve ter:
# - Título apropriado
# - Rótulos nos eixos
# - Grade
# - Legenda (quando aplicável)
# - Salve cada um com um nome diferente
"""
"""
anos = [2019, 2020, 2021, 2022, 2023, 2024]
receita = [50000, 55000, 60000, 75000, 90000, 110000]
custo = [40000, 42000, 45000, 50000, 60000, 70000]
lucro = [10000, 13000, 15000, 25000, 30000, 40000]

plt.figure(figsize=(10, 6))
plt.plot(anos, receita, color='green', marker='o', linestyle='-')
plt.title('Receita por ano', fontsize=16)
plt.xlabel('Ano', fontsize=12)
plt.ylabel('Receita (R$)', fontsize=12)
plt.grid(True, linestyle='--')
plt.savefig('receita_ano.png')
plt.close()

plt.figure(figsize=(10, 6))
plt.plot(anos, custo, color='red', marker='s', linestyle='--')
plt.title('Custo por ano', fontsize=16)
plt.xlabel('Ano', fontsize=12)
plt.ylabel('Custo (R$)', fontsize=12)
plt.grid(True, linestyle='--')
plt.savefig('custo_ano.png')
plt.close()

plt.figure(figsize=(10, 6))
plt.plot(anos, lucro, color='blue', marker='^', linestyle=':')
plt.title('Lucro por ano', fontsize=16)
plt.xlabel('Ano', fontsize=12)
plt.ylabel('Lucro (R$)', fontsize=12)
plt.grid(True, linestyle='--')
plt.savefig('lucro_ano.png')
plt.close()
"""
##################################################################
"""
10. DESAFIO FINAL: Relatório executivo

# Dados de uma empresa (2019-2024):
dados = pd.DataFrame({
    'ano': [2019, 2020, 2021, 2022, 2023, 2024],
    'receita': [50000, 55000, 60000, 75000, 90000, 110000],
    'custo': [40000, 42000, 45000, 50000, 60000, 70000],
    'despesas': [5000, 6000, 7000, 8000, 10000, 12000],
    'funcionarios': [10, 11, 12, 14, 16, 18]
})

# Tarefas:
# 1. Calcule o lucro (receita - custo - despesas)
# 2. Crie um gráfico de linha com RECEITA, CUSTO e LUCRO em cores diferentes
#    - Use marcadores diferentes para cada
#    - Use estilos de linha diferentes
#    - Adicione grade, título, legendas
#    - Ajuste o eixo Y para começar em 0
# 3. Crie um gráfico de barras com o número de funcionários por ano
#    - Barras na cor 'purple'
#    - Título: "Evolução do Quadro de Funcionários"
# 4. Calcule o lucro por funcionário (lucro / funcionários)
# 5. Crie um gráfico de linha do lucro por funcionário ao longo dos anos
# 6. Salve os três gráficos
# 7. Mostre no console:
#    - Ano com maior lucro
#    - Ano com maior lucro por funcionário
#    - Média de lucro dos últimos 3 anos
"""
dados = pd.DataFrame({
    'ano': [2019, 2020, 2021, 2022, 2023, 2024],
    'receita': [50000, 55000, 60000, 75000, 90000, 110000],
    'custo': [40000, 42000, 45000, 50000, 60000, 70000],
    'despesas': [5000, 6000, 7000, 8000, 10000, 12000],
    'funcionarios': [10, 11, 12, 14, 16, 18]
})

dados['lucro'] = dados['receita'] - dados['custo'] - dados['despesas']

plt.figure(figsize=(10, 6))
plt.plot(dados['ano'], dados['receita'], 'bs--', label='Receita', linewidth=2)
plt.plot(dados['ano'], dados['custo'], 'r^:', label='Custo', linewidth=2)
plt.plot(dados['ano'], dados['lucro'], 'go-', label='Lucro', linewidth=2)
plt.legend()

plt.title('Receita x Custo x Lucro (por Ano)', fontsize=16)
plt.xlabel('Ano', fontsize=12)
plt.ylabel('Valor (R$)', fontsize=12)

plt.grid(True, linestyle='--')
plt.ylim(0, 120000)

plt.savefig('receita_custo_lucro_p_ano.png')
plt.close()

plt.figure(figsize=(10, 6))
plt.bar(dados['ano'], dados['funcionarios'], color='purple')

plt.title('Evolução do Quadro de Funcionários', fontsize=16)
plt.ylabel('Quantidade', fontsize=12)
plt.xlabel('Ano', fontsize=12)

plt.savefig('evolucao_quadro_funcionarios.png')
plt.close()

dados['lucro_funcionario'] = (dados['lucro'] / dados['funcionarios']).round(2)

plt.figure(figsize=(10, 6))
plt.plot(dados['ano'], dados['lucro_funcionario'], color='purple', linewidth=2, marker='o')
plt.title('Lucro por funcionário x Ano', fontsize=16)
plt.ylabel('Lucro por funcionário (R$)', fontsize=12)
plt.xlabel('Ano', fontsize=12)

plt.grid(True, linestyle='--')
plt.ylim(0)

plt.savefig('lucro_funcionario_p_ano.png')
plt.close()

ano_maior_lucro = dados.loc[dados['lucro'].idxmax(), 'ano']
print(f'Ano com maior lucro: {ano_maior_lucro}')

ano_maior_lucro_funcionario = dados.loc[dados['lucro_funcionario'].idxmax(), 'ano']
print(f'Ano com maior lucro por funcionário: {ano_maior_lucro_funcionario}')

media_lucro_3anos = (dados.sort_values('ano'))['lucro'].tail(3).mean().round(2)
print(f'Média de lucro dos últimos 3 anos: R$ {media_lucro_3anos:,.2f}')