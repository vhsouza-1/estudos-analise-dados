"""
Bloco 2: Python para Dados # aqui é bloco 3, não 2 (bloco 1 SQl e bloco 2 foi python)
Módulo 1: Introdução ao Pandas
Aula 2: Series - Uma coluna de dados
Data: 20/04/2026
Objetivo: Aprender a criar e manipular Series do Pandas
"""
import pandas as pd

# ==========================================
# 1. O QUE É UMA SERIES?
# ==========================================

print("="*50)
print("1. O QUE É UMA SERIES?")
print("="*50)

"""
Uma Series é como uma coluna de dados:
- É um array unidimensional (uma dimensão)
- Cada elemento tem um índice (rótulo)
- Pode guardar qualquer tipo de dado (int, float, str, etc.)

Comparação:
- Lista Python: [10, 20, 30] (só valores)
- Series Pandas: índice 0→10, índice 1→20, índice 2→30 (valores + rótulos)
"""

print("\n" + "="*50)
print("2. CRIANDO SERIES A PARTIR DE LISTAS")
print("="*50)

# Jeito 1: passando uma lista (índice padrão 0, 1, 2...)
print("--- Series com índice padrão ---")
numeros = pd.Series([10, 20, 30, 40, 50])
print(numeros)
print(f"Tipo: {type(numeros)}")
print(f"Valores: {numeros.values}")
print(f"Índice: {numeros.index}")

# Jeito 2: com índice personalizado
print("\n--- Series com índice personalizado ---")
vendas = pd.Series([1500, 200, 3500], index=["celular", "fone", "notebook"])
print(vendas)

# ==========================================
# 3. CRIANDO SERIES A PARTIR DE DICIONÁRIOS
# ==========================================

print("\n" + "="*50)
print("3. CRIANDO SERIES A PARTIR DE DICIONÁRIOS")
print("="*50)

print("--- Series a partir de dicionário ---")
estoque = pd.Series({
    'celular': 10,
    'fone': 30,
    'notebook': 5
})
print(estoque)

# Isso é equivalente a:
# pd.Series([10, 30, 5], index=["celular", "fone", "notebook"])

# ==========================================
# 4. ACESSANDO ELEMENTOS DA SERIES
# ==========================================

print("\n" + "="*50)
print("4. ACESSANDO ELEMENTOS")
print("="*50)

vendas = pd.Series([1500, 200, 3500], index=["celular", "fone", "notebook"])

# Acesso por posição (índice numérico)
print(f"vendas[0] (primeiro): {vendas.iloc[0]}") # quando rodei deu erro, fui pesqusiar e descobri que vc errou. como os indices são personalizados, nao da pra fazer vendas[0] etc.
print(f"vendas[1] (segundo): {vendas.iloc[1]}")
print(f"vendas[2] (terceiro): {vendas.iloc[2]}")

# Acesso por rótulo (índice personalizado)
print(f"\nvendas['celular']: {vendas['celular']}")
print(f"vendas['fone']: {vendas['fone']}")
print(f"vendas['notebook']: {vendas['notebook']}")

# ==========================================
# 5. OPERAÇÕES MATEMÁTICAS COM SERIES
# ==========================================

print("\n" + "="*50)
print("5. OPERAÇÕES MATEMÁTICAS")
print("="*50)

# Series suportam operações matemáticas elemento a elemento
print("--- Operações básicas ---")
vendas = pd.Series([1500, 200, 3500], index=["celular", "fone", "notebook"])

print(f'Original: \n{vendas}')
print(f'\nDobro: \n{vendas * 2}')
print(f'\nMetade: \n{vendas / 2}')
print(f'\nMais 100: \n{vendas + 100}')

# Útil pra projeções e descontos ne?

# Operações entre Series (quando têm os mesmos índices)
print("\n--- Operações entre Series ---")

precos = pd.Series([1500, 200, 3500], index=["celular", "fone", "notebook"])
quantidades = pd.Series([10, 30, 5], index=["celular", "fone", "notebook"])

"""
# era mais facil fazer uma lista chamdada produtos né? Tipo assim:

produtos = ["celular", "fone", "notebook"]
precos = pd.Series([1500, 200, 3500], index=produtos) 
quantidades = pd.Series([10, 30, 5], index=produtos)

tipo igual fazemos para fieldnames no DictWriter
"""

total = precos * quantidades
print(f'Preços:\n{precos}')
print(f'\nQuantidades:\n{quantidades}')
print(f'\nTotal (preco * quantidade):\n{total}')

# ==========================================
# 6. MÉTODOS ÚTEIS DA SERIES
# ==========================================

print("\n" + "="*50)
print("6. MÉTODOS ÚTEIS")
print("="*50)

notas = pd.Series([8.5, 7.0, 9.0, 6.5, 5.5, 8.0])

print(f'Notas:\n{notas}')
print(f'\nSoma: {notas.sum()}') # legal que "inverte a ordem", no python original a gente usa sum() como função e aqui com método
print(f'Média: {notas.mean():.2f}') # esse jeito de calcular media tbm, muito melhor
print(f'Maior nota: {notas.max()}')
print(f"Menor nota: {notas.min()}")
print(f"Quantidade: {notas.count()}")
print(f"Desvio padrão: {notas.std():.2f}") # incrivel, la no MySQL tem uma função parecida, n me lembro a sintax exatamente

# describe() - resumo estatístico completo
print(f"\nResumo estatístico:\n{notas.describe()}") # o que o 25%, 50% e 75% significa?

# ==========================================
# 7. EXEMPLOS PRÁTICOS
# ==========================================

print("\n" + "="*50)
print("7. EXEMPLOS PRÁTICOS")
print("="*50)

# 7.1. Calculando média de vendas por dia
print("\n--- Média de vendas ---")
vendas_semana = pd.Series([120, 150, 90, 200, 180, 210, 160], index=["seg", "ter", "qua", "qui", "sex", "sab", "dom"])
print(f"Vendas da semana:\n{vendas_semana}")
print(f"Média diária: R${vendas_semana.mean():.2f}")
print(f"Dia com maior venda: {vendas_semana.idxmax()} (R${vendas_semana.max()})") # o que é esse idx? eu entendi que é pra acessar o indice, quase como um max com key né?
print(f"Dia com menor venda: {vendas_semana.idxmin()} (R${vendas_semana.min()})")

# 7.2. Aplicando desconto
print("\n--- Aplicando desconto ---")
precos = pd.Series([1500, 200, 3500, 50, 120], index=["celular", "fone", "notebook", "mouse", "teclado"])
desconto_10 = precos * 0.9
print(f"Preços originais:\n{precos}")
print(f"\nPreços com 10% de desconto:\n{desconto_10}")

# 7.3. Filtrando valores (introdução)
print("\n--- Filtrando valores ---")
notas = pd.Series([8.5, 7.0, 9.0, 6.5, 5.5, 8.0, 4.0])

aprovados = notas[notas >= 7]
reprovados = notas[notas < 5]
recuperacao = notas[(notas >= 5) & (notas < 7)] # se colocar o and no lugar do & funciona? n gostei desse &

print(f"Notas originais:\n{notas}")
print(f"\nAprovados (>=7):\n{aprovados}")
print(f"Recuperação (5-7):\n{recuperacao}")
print(f"Reprovados (<5):\n{reprovados}")

# ==========================================
# 8. RESUMO
# ==========================================

print("\n" + "="*50)
print("8. RESUMO")
print("="*50)

"""
✅ Series: uma coluna de dados (array unidimensional com rótulos)
✅ Criar: pd.Series(lista) ou pd.Series(dicionario)
✅ Índice padrão: 0, 1, 2... (posições)
✅ Índice personalizado: index=["a", "b", "c"]
✅ Acessar: series[posicao] ou series["rotulo"]
✅ Operações: +, -, *, / funcionam elemento a elemento
✅ Métodos: .sum(), .mean(), .max(), .min(), .count(), .describe()
✅ Filtrar: series[condicao] (ex: series[series > 10])
"""
#############################################################
# EXERCÍCIOS - AULA 2
#############################################################
# NÍVEL 1-3: Aquecimento
#############################################################
"""
1. Criando Series a partir de lista

# Crie uma Series com as notas [8.5, 7.0, 9.0, 6.5]
# Mostre a Series
"""
"""
notas = pd.Series([8.5, 7.0, 9.0, 6.5])
print(notas) # tem como fazer com que n apareça o dtype: float64 no final?
"""
#############################################################
"""
2. Criando Series com índice personalizado

# Crie uma Series com os preços: celular=1500, fone=200, notebook=3500
# Use o parâmetro index para nomear os produtos
# Mostre a Series
"""
"""
produtos = ['celular', 'fone', 'notebook']
precos = pd.Series([1500, 200, 3500], index=produtos)
print(precos)
"""
#############################################################
"""
3. Acessando elementos

# Use a Series do exercício 2
# Mostre o preço do celular (por rótulo)
# Mostre o segundo produto (por posição)
"""
"""
produtos = ['celular', 'fone', 'notebook']
precos = pd.Series([1500, 200, 3500], index=produtos)

print(f'Preço celular por rótulo: {precos['celular']}')
print(f'Segundo produto por posição: {precos.iloc[1]}')
"""
#############################################################
# NÍVEL 4-6: Aplicação
#############################################################
"""
4. Operações matemáticas

# Crie uma Series com os números [10, 20, 30, 40, 50]
# Calcule e mostre:
# - O dobro de cada número
# - Cada número mais 5
# - Cada número dividido por 2
"""
"""
numeros = pd.Series([10, 20, 30, 40, 50], index=[n for n in range(1,6)])

print(f'Dobro:\n{numeros * 2}')
print(f'\nMais 5:\n{numeros + 5}')
print(f'\nDividido por 2:\n{numeros / 2}')
"""
#############################################################
"""
5. Média, máximo e mínimo

# Crie uma Series com as idades [25, 30, 22, 28, 35, 27, 31]
# Calcule e mostre:
# - Média das idades
# - Maior idade
# - Menor idade
# - Quantidade de idades
"""
"""
idades = pd.Series([25, 30, 22, 28, 35, 27, 31])

print(f'Média das idades: {idades.mean():.2f}')
print(f'Maior idade: {idades.max()}')
print(f'Menor idade: {idades.min()}')
print(f'Quantidade de idades: {idades.count()}')

"""
#############################################################
"""
6. Resumo estatístico

# Use a Series do exercício 5
# Use o método .describe() para mostrar o resumo
# Explique (em comentário) o que significa cada linha do resumo
"""
"""
idades = pd.Series([25, 30, 22, 28, 35, 27, 31])
print(idades.describe())

# count     7.000000 quantidade de itens
# mean     28.285714 media dos valores
# std       4.231402 desvio padrao
# min      22.000000 menor valor
# 25%      26.000000 valor que marca o primeiro (menor) quartil
# 50%      28.000000 valor que marca a mediana (segundo quartil)
# 75%      30.500000 valor que marca o terceiro quartil (top 25%)
# max      35.000000 valor máximo
# dtype: float64 tipo dos dados, float, apenas de que o 64 n sei o que significa
"""
#############################################################
# NÍVEL 7-8: Manipulação
#############################################################
"""
7. Filtrando valores

# Crie uma Series com as notas [8.5, 7.0, 9.0, 6.5, 5.5, 8.0, 4.0, 7.5]
# Mostre apenas as notas maiores ou iguais a 7
# Mostre apenas as notas menores que 6
"""
"""
notas = pd.Series([8.5, 7.0, 9.0, 6.5, 5.5, 8.0, 4.0, 7.5])
notas_maiores = notas[notas >= 7]
notas_menores = notas[notas < 6]

print(f'Notas >= 7: \n{notas_maiores}')
print(f'\nNotas < 6:\n{notas_menores}')
"""
#############################################################
"""
8. Calculando total de vendas

# Crie duas Series:
# - precos: celular=1500, fone=200, notebook=3500, mouse=50
# - quantidades: celular=10, fone=30, notebook=5, mouse=100
# Calcule o total (preco * quantidade) para cada produto
# Calcule o valor total do estoque (soma de todos os totais)
"""
"""
produtos = ['celular', 'fone', 'notebook', 'mouse']

precos = pd.Series([1500, 200, 3500, 50], index=produtos)
quantidade = pd.Series([10, 30, 5, 100], index=produtos)

total_produto = precos * quantidade
print(f'Total por produto:\n{total_produto}')

total_estoque = total_produto.sum()
print(f'\nTotal em estoque: {total_estoque}')
"""
#############################################################
# NÍVEL 9-10: Desafios
#############################################################
"""
9. Analisador de temperaturas

# Crie uma Series com temperaturas de uma semana:
# seg=25, ter=28, qua=22, qui=30, sex=27, sab=26, dom=24
# Calcule e mostre:
# - Temperatura média
# - Dia mais quente (use .idxmax())
# - Dia mais frio (use .idxmin())
# - Quantos dias tiveram temperatura acima da média
"""
"""
dias_semana = ['seg', 'ter', 'qua', 'qui', 'sex', 'sab', 'dom']

temperaturas = pd.Series([25, 28, 22, 30, 27, 26, 24], index=dias_semana)

print(f'Temperatura média: {temperaturas.mean()}')
print(f'Dia mais quente: {temperaturas.idxmax()}')
print(f'Dia mais frio: {temperaturas.idxmin()}')

temperaturas_acima = temperaturas[temperaturas > temperaturas.mean()]
print(f'Quantos dias tiveram temperatura acima da média: {temperaturas_acima.count()}')
"""
#############################################################
"""
10. DESAFIO FINAL: Relatório de vendas

# Crie uma Series com vendas de produtos:
# "celular": 1500, "fone": 200, "notebook": 3500, "mouse": 50, "teclado": 120
# 
# Calcule e mostre um relatório com:
# - Produto mais caro
# - Produto mais barato
# - Média de preços
# - Produtos com preço acima da média
# - Produtos com preço abaixo de R$100
# - Quantidade de produtos com preço entre R$100 e R$1000
"""
"""
produtos = ['celular', 'fone', 'notebook', 'mouse', 'teclado']
precos = pd.Series([1500, 200, 3500, 50, 120], index=produtos)


print(f'Produto mais caro: {precos.idxmax()}')
print(f'Produto mais barato: {precos.idxmin()}')
print(f'Média de preços: {precos.mean():.2f}')

precos_acima = precos[precos > precos.mean()]
print(f'\nProdutos com preço acima da média:\n{precos_acima}')

precos_abaixo100 = precos[precos < 100]
print(f'\nProdutos com preco abaixo da média:\n{precos_abaixo100}')

precos_intervalo = precos[(precos >= 100) & (precos <= 1000)]
print(f'\nQuantidade de produtos com preço entre 100 e 1000: {precos_intervalo.count()}')
"""
