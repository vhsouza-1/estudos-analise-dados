"""
Bloco 3: Python para Dados
Módulo 2: Visualização de Dados
Aula 6: Estilos e Paletas
Data: 02/05/2026
Objetivo: Aprender a personalizar estilos e paletas de cores no Seaborn
"""

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Usar dataset Iris

iris = sns.load_dataset('iris')

# ==========================================
# 1. ESTILOS DE FUNDO (set_style)
# ==========================================

print("="*50)
print("1. ESTILOS DE FUNDO (set_style)")
print("="*50)

"""
Estilos disponíveis no Seaborn:
- 'darkgrid'   : fundo escuro com grade (padrão)
- 'whitegrid'  : fundo branco com grade
- 'dark'       : fundo escuro sem grade
- 'white'      : fundo branco sem grade
- 'ticks'      : fundo branco com marcas nos eixos
"""

estilos = ['darkgrid', 'whitegrid', 'dark', 'white', 'ticks']

# plt.figure(figsize=(15, 10))
# for i, estilo in enumerate(estilos):
#     plt.subplot(2, 3, i+1)
#     sns.set_style(estilo)
#     sns.boxplot(data=iris, x='species', y='petal_length', width=0.5)
#     plt.title(f'Estilo: {estilo}')
#
# plt.tight_layout()
# plt.show()

# ==========================================
# 2. RESETAR PARA O PADRÃO
# ==========================================

print("\n" + "="*50)
print("2. RESETAR PARA O PADRÃO")
print("="*50)

# Voltar ao estilo padrão
sns.set_style('darkgrid')
print("Estilo resetado para 'darkgrid'") # resetando para darkgrid percebi que o default do meu era white kkkkkk

# ==========================================
# 3. PALETAS DE CORES (set_palette)
# ==========================================

print("\n" + "="*50)
print("3. PALETAS DE CORES (set_palette)")
print("="*50)

"""
Paletas disponíveis:
- 'deep'       : padrão
- 'muted'      : cores suaves
- 'pastel'     : cores pastel
- 'bright'     : cores vibrantes
- 'dark'       : cores escuras
- 'colorblind' : cores para daltônicos
"""

# Criar boxplot com cada paleta
paletas = ['deep', 'muted', 'pastel', 'bright', 'dark', 'colorblind']

# plt.figure(figsize=(15, 10))
# for i, paleta in enumerate(paletas, 1):
#     plt.subplot(2, 3, i)
#     sns.set_palette(paleta)
#     sns.boxplot(data=iris, x='species', y='petal_length', hue='species') # se n colocar o hue as cores ficam iguais
#     plt.title(f'Paleta: {paleta}')
#
# plt.tight_layout()
# plt.show()

# ==========================================
# 4. COMBINANDO ESTILO E PALETA
# ==========================================

print("\n" + "="*50)
print("4. COMBINANDO ESTILO E PALETA")
print("="*50)

# Configurar estilo e paleta juntos
sns.set_style('whitegrid')
sns.set_palette('viridis')

# plt.figure(figsize=(10, 6))
# sns.histplot(iris['petal_length'], bins=20)
# plt.title('Estilo: whitegrid | Paleta: viridis')
# plt.show()

# ==========================================
# 5. PALETAS PERSONALIZADAS
# ==========================================

print("\n" + "="*50)
print("5. PALETAS PERSONALIZADAS")
print("="*50)

# Criar paleta personalizada com nomes de cores
sns.set_palette(['red', 'blue', 'green'])

# plt.figure(figsize=(10, 6))
# sns.boxplot(data=iris, x='species', y='petal_length', hue='species') # esse tbm precisa do hue
# plt.title('Paleta personalizada: red, blue, green')
# plt.show()

# ==========================================
# 6. VOLTAR AO PADRÃO
# ==========================================

print("\n" + "="*50)
print("6. VOLTAR AO PADRÃO")
print("="*50)

# Resetar tudo para o padrão do Seaborn
sns.set_theme() # que estranho, quando eu resetei agr o darkgrid ficou como padrão, mas antes todos meus plots era no tema white, que estranho
print("Configurações resetadas para o padrão do Seaborn")

# ==========================================
# 7. RESUMO
# ==========================================

print("\n" + "="*50)
print("7. RESUMO")
print("="*50)

"""
✅ ESTILOS (sns.set_style):
   - 'darkgrid' : fundo escuro com grade (padrão)
   - 'whitegrid': fundo branco com grade
   - 'dark'     : fundo escuro sem grade
   - 'white'    : fundo branco sem grade
   - 'ticks'    : fundo branco com marcas nos eixos

✅ PALETAS (sns.set_palette):
   - 'deep', 'muted', 'pastel', 'bright', 'dark', 'colorblind'
   - Lista de cores: ['red', 'blue', 'green']
   - 'viridis', 'coolwarm' (do matplotlib)

✅ RESETAR:
   - sns.set_theme() - volta ao padrão do Seaborn
"""
####################################################################
# EXERCÍCIOS - AULA 2.6
####################################################################

# Dados para todos os exercícios:

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

iris = sns.load_dataset('iris')

####################################################################
# NÍVEL 1-3: Aquecimento
####################################################################
"""
1. Testando estilos

# Crie um boxplot de petal_length por species
# Teste os estilos: 'darkgrid', 'whitegrid', 'dark', 'white', 'ticks'
# Mostre cada um (pode ser em subplots ou separadamente)
"""
"""
estilos = ['darkgrid', 'whitegrid', 'dark', 'white', 'ticks']

plt.figure(figsize=(14, 10))
for i, estilo in enumerate(estilos):
    sns.set_style(estilo)
    plt.subplot(2, 3, i+1)
    sns.boxplot(data=iris, x='species', y='petal_length', hue='species')
    plt.title(f'Estilo: {estilo}')

plt.tight_layout()
plt.show()
"""
####################################################################
"""
2. Testando paletas

# Crie um boxplot de petal_length por species
# Teste as paletas: 'deep', 'muted', 'pastel', 'bright', 'dark', 'colorblind'
# Mostre cada uma
"""
"""
paletas = ['deep', 'muted', 'pastel', 'bright', 'dark', 'colorblind']

plt.figure(figsize=(14, 10))
sns.set_style('whitegrid')
for i, paleta in enumerate(paletas):
    sns.set_palette(paleta)
    plt.subplot(2, 3, i+1)
    sns.boxplot(data=iris, x='species', y='petal_length', hue='species')
    plt.title(f'Paleta: {paleta}')

plt.tight_layout()
plt.show()
"""
####################################################################
"""
3. Estilo + Paleta

# Configure estilo 'whitegrid' e paleta 'viridis'
# Crie um histograma da coluna 'petal_length' com 20 bins
"""
"""
estilo = 'whitegrid'
paleta = 'viridis'

plt.figure(figsize=(10, 6))

sns.set_style(estilo)
sns.set_palette(paleta)

sns.histplot(iris['petal_length'], bins=20)

plt.title(f'Estilo: {estilo} | Paleta: {paleta}')

plt.show()
"""
####################################################################
# NÍVEL 4-6: Aplicação
####################################################################
"""
4. Comparação de estilos (um gráfico por estilo)

# Crie um gráfico de dispersão (sepal_length x sepal_width)
# Faça 5 versões (um para cada estilo)
# Organize em uma figura 1x5
"""
"""
plt.figure(figsize=(19, 4))

estilos = ['darkgrid', 'whitegrid', 'dark', 'white', 'ticks']

sns.set_style('ticks')

for i, estilo in enumerate(estilos):
    sns.set_style(estilo)
    plt.subplot(1, 5, i+1)
    sns.scatterplot(data=iris, x='sepal_length', y='sepal_width', hue='species')
    plt.title(f'Estilo: {estilo}')
    plt.ylabel('sepal_width')
    plt.xlabel('sepal_length')

plt.tight_layout()
plt.show()
"""
####################################################################
"""
5. Gráfico com paleta personalizada

# Crie uma paleta personalizada com 3 cores: 'purple', 'orange', 'cyan'
# Crie um boxplot de petal_length por species com essa paleta
"""
"""
paleta = ['purple', 'orange', 'cyan']

plt.figure(figsize=(10, 6))
sns.set_palette(paleta)
sns.boxplot(data=iris, x='species', y='petal_length', hue='species', width=0.5)
plt.title('Petal Length x Species')

plt.tight_layout()
plt.show()
"""
####################################################################
"""
6. Estilo e paleta em pairplot

# Configure estilo 'whitegrid' e paleta 'Set2'
# Crie um pairplot do iris colorido por 'species'
"""
"""
sns.set_style('whitegrid')
sns.set_palette('Set2')

sns.pairplot(data=iris, hue='species')

plt.show()
"""
####################################################################
# NÍVEL 7-8: Manipulação
####################################################################
"""
7. Dashboard comparativo (estilos)

# Crie uma figura 2x3 com boxplots de petal_length por species
# Cada subplot com um estilo diferente ('darkgrid', 'whitegrid', 'dark', 'white', 'ticks')
# Título de cada subplot deve ser o nome do estilo
"""
"""
Já fiz, literalmente é o exercício 1
"""
####################################################################
"""
8. Dashboard comparativo (paletas)

# Crie uma figura 2x3 com boxplots de petal_length por species
# Cada subplot com uma paleta diferente ('deep', 'muted', 'pastel', 'bright', 'dark', 'colorblind')
# Título de cada subplot deve ser o nome da paleta
"""
"""
Já fiz, literalmente é o exercício 2
"""
####################################################################
# NÍVEL 9-10: Desafios
####################################################################
"""
9. Explorando estilos e paletas

# Crie um dashboard 2x2 com:
# (0,0): boxplot (petal_length por species), estilo 'whitegrid', paleta 'pastel'
# (0,1): histograma (petal_length), estilo 'darkgrid', paleta 'viridis'
# (1,0): dispersão (sepal_length x sepal_length), estilo 'ticks', paleta 'coolwarm'
# (1,1): pairplot (iris, hue='species'), estilo 'whitegrid', paleta 'Set1'
"""
"""
plt.figure(figsize=(14, 8))

sns.set_style('whitegrid')
sns.set_palette('pastel')
plt.subplot(2, 2, 1)
sns.boxplot(data=iris, x='species', y='petal_length', hue='species', width=0.5)
plt.title('Petal Length x Species')

sns.set_style('darkgrid')
sns.set_palette('viridis')
plt.subplot(2, 2, 2)
sns.histplot(data=iris, x='petal_length', hue='species')
plt.title('Distribuição Petal Length x Species')

sns.set_style('ticks')
sns.set_palette('coolwarm')
plt.subplot(2, 2, 3)
sns.scatterplot(data=iris, x='sepal_length', y='sepal_length', hue='species') # pediu errado ne? kkkkkk mas eu fiz...
plt.title('Distribuição Sepal Length x Species')

sns.set_style('whitegrid')
sns.set_palette('Set1')
plt.subplot(2, 2, 4) # ta ficando louco de mandar fazer pairplot no 2, 2 né? kkkkkk abriu dois grafico aqui
sns.pairplot(data=iris, hue='species')
plt.title('Pairplot Iris')

plt.tight_layout()
plt.show()
"""
####################################################################
"""
10. DESAFIO FINAL: Análise Iris com estilo profissional

# Configure um estilo e paleta que você ache mais profissional
# Crie um relatório visual com:
# 1. Boxplot de petal_length por species
# 2. Boxplot de sepal_length por species
# 3. Histograma de petal_length
# 4. Gráfico de dispersão (sepal_length x sepal_width) colorido por species
# 
# Organize em um dashboard 2x2
# Adicione um título geral para o dashboard usando fig.suptitle()
"""
plt.figure(figsize=(14, 8))

sns.set_style('whitegrid')
sns.set_palette('Set1')

plt.subplot(2, 2, 1)
sns.boxplot(data=iris, x='species', y='petal_length', hue='species', width=0.3)
plt.title('Petal Length x Species')

plt.subplot(2, 2, 2)
sns.boxplot(data=iris, x='species', y='sepal_length', hue='species', width=0.3)
plt.title('Sepal Length x Species')

plt.subplot(2, 2, 3)
sns.histplot(data=iris, x='petal_length', hue='species', bins=20)
plt.title('Distribuição Petal Length')

plt.subplot(2, 2, 4)
sns.scatterplot(data=iris, x='sepal_length', y='sepal_width', hue='species')
plt.title('Sepal Length x Sepal Width')

plt.suptitle('Análise de Petal Length, Sepal Length e Width do Dataset Iris')

plt.tight_layout()
plt.show()