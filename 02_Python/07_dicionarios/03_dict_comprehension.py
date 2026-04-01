"""
Módulo 7: Dicionários
Aula 7.3: Dict Comprehension
Data: 01/04/2026
Objetivo: Aprender a criar dicionários de forma concisa
"""

# ==========================================
# 1. O QUE É DICT COMPREHENSION?
# ==========================================

print("="*50)
print("1. O QUE É DICT COMPREHENSION?")
print("="*50)

# Dict comprehension é uma forma concisa de criar dicionários
# É similar à list comprehension, mas com chave: valor

# Jeito tradicional (sem dict comprehension)
quadrados = {}
for i in range(1,6):
    quadrados[i] = i ** 2
print(f'Tradicional: {quadrados}')

# Jeito com dict comprehension (uma linha!)
quadrados_lc = {i: i ** 2 for i in range(1, 6)}
print(f'Dict comprehension: {quadrados_lc}')

# ==========================================
# 2. SINTAXE BÁSICA
# ==========================================

print("\n" + "="*50)
print("2. SINTAXE BÁSICA")
print("="*50)

# Estrutura: {chave: valor for item in iterável}

# Exemplo 1: números e seus cubos
cubos = {i: i**3 for i in range(1, 6)}
print(f'Cubos: {cubos}')

# Exemplo 2: letras maiúsculas como chave, minúsculas como valor
maiusculas = {chr(i): chr(i).lower() for i in range(65, 75)} # o que é essa função chr()?
print(f"Maiúsculas -> minúsculas: {maiusculas}")

# Exemplo 3: a partir de uma lista de nomes (nome: tamanho)
nomes = ["Ana", "Bruno", "Carla", "Daniel"]
tamanhos = {nome: len(nome) for nome in nomes}
print(f'Nomes e tamanhos: {tamanhos}')

# ==========================================
# 3. COM CONDICIONAL (FILTRO)
# ==========================================

print("\n" + "="*50)
print("3. COM CONDICIONAL - FILTRANDO")
print("="*50)

# Sintaxe: {chave: valor for item in iterável if condição}
# O if vai no FINAL (filtra os itens)

# Exemplo 1: apenas números pares e seus quadrados
pares_quadrados = {i: i ** 2 for i in range(1, 11) if i % 2 == 0}
print(f'Pares e quadrados: {pares_quadrados}')

# Exemplo 2: apenas palavras com mais de 4 letras
palavras = ["casa", "carro", "sol", "computador", "gato", "python"]
longas = {palavra: len(palavra) for palavra in palavras if len(palavra) > 4}
print(f'Palavras longas: {longas}')

# Exemplo 3: apenas alunos com nota >= 7
notas = {"Ana": 8.5, "Bruno": 6.0, "Carla": 9.0, "Daniel": 7.5, "Eduarda": 4.5}
aprovados = {nome: nota for nome, nota in notas.items() if nota >= 7}
print(f'Aprovados: `{aprovados}')

# ==========================================
# 4. COM IF-ELSE (TRANSFORMAÇÃO)
# ==========================================

print("\n" + "="*50)
print("4. COM IF-ELSE - TRANSFORMANDO VALORES")
print("="*50)

# Sintaxe: {chave: valor_if_true if condição else valor_if_false for item in iterável}
# O if-else vai na EXPRESSÃO (transforma os valores)

# Exemplo 1: classificar números como par ou ímpar
classificacao = {i: 'par' if i % 2 == 0 else 'ímpar' for i in range(1, 11)} # onde está escrito 'ímpar' eu achei que teria que colocar i: 'ímpar'
print(f'Classificação: {classificacao}')

# Exemplo 2: notas com status
notas = {"Ana": 8.5, "Bruno": 6.0, "Carla": 9.0, "Daniel": 4.5}
status = {nome: 'Aprovado' if nota >= 7 else 'Reprovado' for nome, nota in notas.items()}
print(f'Status: {status}')

# Exemplo 3: mapeando notas para conceitos
conceitos = {nome: 'A' if nota >= 9 else 'B' if nota >= 7 else 'C' if nota >= 5 else 'D' for nome, nota in notas.items()}
print(f'Conceitos: {conceitos}')

# ==========================================
# 5. DIFERENÇA ENTRE IF (FILTRO) E IF-ELSE (TRANSFORMAÇÃO)
# ==========================================

print("\n" + "="*50)
print("5. IF (FILTRO) vs IF-ELSE (TRANSFORMAÇÃO)")
print("="*50)

numeros = range(1, 11)

# IF no final (filtra) - alguns itens são excluídos
pares = {i: i**2 for i in numeros if i % 2 == 0}
print(f"Filtro (só pares): {pares}")

# IF-ELSE na expressão (transforma) - TODOS os itens ficam, mas valores mudam
par_ou_impar = {i: ("par" if i % 2 == 0 else "ímpar") for i in numeros}
print(f"Transforma (todos): {par_ou_impar}")

# ==========================================
# 6. DICT COMPREHENSION A PARTIR DE LISTAS
# ==========================================

print("\n" + "="*50)
print("6. A PARTIR DE LISTAS")
print("="*50)

# 6.1 Duas listas (com zip)
nomes = ["Ana", "Bruno", "Carla"]
idades = [25, 30, 22]
pessoas = {nome: idade for nome, idade in zip(nomes, idades)}
print(f'Pessoas (zip): {pessoas}') # Tenho a impressão de que isso deve ser muito usado para dados...

# 6.2. Lista de tuplas
tuplas = [("Ana", 25), ("Bruno", 30), ("Carla", 22)]
pessoas2 = {nome: idade for nome, idade in tuplas}
print(f'Pessoas (tupla): {pessoas2}')

# 6.3. Lista de dicionários
alunos = [
    {"nome": "Ana", "nota": 8.5},
    {"nome": "Bruno", "nota": 6.0},
    {"nome": "Carla", "nota": 9.0}
]

notas_dict = {aluno['nome']: aluno['nota'] for aluno in alunos}
print(f'Notas (dict list): {notas_dict}')

# ==========================================
# 7. DICT COMPREHENSION A PARTIR DE OUTRO DICIONÁRIO
# ==========================================

print("\n" + "="*50)
print("7. A PARTIR DE OUTRO DICIONÁRIO")
print("="*50)

# Transformar um dicionário em outro

# 7.1 Mapeando valores (ex: aumentas notas em 0.5)
notas = {"Ana": 8.5, "Bruno": 6.0, "Carla": 9.0}
notas_ajustadas = {nome: nota + 0.5 for nome, nota in notas.items()}
print(f'Notas ajustadas: {notas_ajustadas}')

# 7.2 Inverter chave e valor:
invertido = {nota: nome for nome, nota in notas.items()}
print(f'Dicionário invertido: {invertido}')

# 7.3 Filtrar dicionário (manter apenas os que tem nota >= 7)
aprovados = {nome: nota for nome, nota in notas.items() if nota >= 7}
print(f'Aprovados: {aprovados}')

# ==========================================
# 8. EXEMPLOS PRÁTICOS
# ==========================================

print("\n" + "="*50)
print("8. EXEMPLOS PRÁTICOS")
print("="*50)

# 8.1 Contador de letras de uma palavra
print("\n--- Contador de letras ---")
palavra = 'banana'
contador = {letra: palavra.count(letra) for letra in set(palavra)}
print(f'Contagem de letras em "banana": {contador}')

# 8.2 Mapeamento de preços com desconto
print(f'\n--- Desconto em produtos ---')
precos = {"celular": 1500, "notebook": 3500, "fone": 200}
desconto_10 = {nome: preco * 0.9 for nome, preco in precos.items()}
print(f'Preços com 10% de desconto: {desconto_10}')

# 8.3. Agrupamento por primeira letra (com dict comprehension)
print("\n--- Agrupamento por primeira letra ---")
palavras = ["casa", "carro", "banana", "cachorro", "bicicleta", "aviao"]
agrupado = {letra: [p for p in palavras if p[0] == letra] for letra in set(p[0] for p in palavras)} # tava confuso em relação a esse set aqui, descobri que a expressão entre parentese é um gerador, bem interessante.
for letra, lista in agrupado.items():
    print(f"{letra}: {lista}")

# 8.4. Conversão de temperatura
print("\n--- Temperaturas ---")
celsius = {"segunda": 25, "terça": 28, "quarta": 22, "quinta": 30, "sexta": 27}
fahrenheit = {dia: (temp * 9/5) + 32 for dia, temp in celsius.items()}
for dia, temp in fahrenheit.items():
    print(f"{dia}: {temp:.1f}°F")

# Nos exercicios e exemplos que vimos, no dict comprehension eu sempre modifico os valores, mas nunca a chave. É assim mesmo?

# ==========================================
# 9. RESUMO
# ==========================================

print("\n" + "="*50)
print("9. RESUMO")
print("="*50)

"""
✅ Dict comprehension: {chave: valor for item in iterável}
✅ Com filtro (if no final): {chave: valor for item in iterável if condição}
✅ Com transformação (if-else na expressão): 
   {chave: valor_if_true if cond else valor_if_false for item in iterável}
✅ A partir de listas: com zip() ou lista de tuplas
✅ A partir de dicionários: percorrendo .items()

📌 Dict comprehension vs List comprehension:
- List: [expressão for item in iterável]
- Dict: {chave: valor for item in iterável}

📌 Quando usar:
- Para criar dicionários de forma concisa
- Para transformar/filtrar dicionários existentes
- Quando a lógica é simples e legível
"""
# ==========================================
# 10. EXERCÍCIOS
# ==========================================

print("\n" + "="*50)
print("10. EXERCÍCIOS")
print("="*50)
###########################################
# EXERCÍCIOS - AULA 7.3
###########################################
# NÍVEL 1-3: Aquecimento
###########################################
"""
1. Mapeamento de meses

# Crie um dicionário onde as chaves são os números de 1 a 12 e os valores são os nomes dos meses
# Use dict comprehension e uma lista com os meses: ["Janeiro", "Fevereiro", ...]
# Dica: você pode usar zip() ou enumerate()
"""
"""
numeros = [i for i in range(1, 13)]
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

meses_numeros = {i: mes for i, mes in zip(numeros, meses)}

print(meses_numeros)
"""
#############################################
"""
2. De string para dicionário

# Dada a string: "a=1,b=2,c=3,d=4,e=5"
# Use dict comprehension para transformar em um dicionário
# Dica: use .split(',') primeiro, depois .split('=')
"""
"""
string = "a=1,b=2,c=3,d=4,e=5"
igualdades = string.split(',')

dict_lc = {igualdade.split('=') for igualdade in igualdades} # se usar .split assim ja forma a dupla de chave e valor...

print(dict_lc)
"""
##############################################
"""
3. Inverter relação

# Dado o dicionário: notas = {"Ana": 8.5, "Bruno": 6.0, "Carla": 9.0}
# Crie um novo dicionário onde a chave é a nota e o valor é uma lista de alunos com aquela nota
# Dica: pode ser que várias notas se repitam (nesse caso, não repetem, mas vamos praticar)
"""
"""
notas = {"Ana": 8.5, "Bruno": 6.0, "Carla": 9.0, 'João': 6.0} # João para testar

alunos = {}

for nome, nota in notas.items(): # só pra comprar com a outra estrutura
    if nota in alunos:
        alunos[nota].append(nome)
    else:
        alunos[nota] = [nome]

print(alunos)

# alunos_dc = {chave: [item for item in itens if nota=chave] for chave in notas} # só pra raciocinar

alunos_dc = {nota1: [nome for nome, nota2 in notas.items() if nota2 == nota1] for nome, nota1 in notas.items()} # tive essa ideia...

print(alunos_dc)
"""
###########################################
# NÍVEL 4-6: Aplicação
###########################################
"""
4. Código de produtos

# Dada a lista de produtos: ["Arroz", "Feijão", "Macarrão", "Leite", "Café"]
# Crie um dicionário onde a chave é o código do produto (AR001, FE002, MA003, LE004, CA005)
# e o valor é o nome do produto
# Use dict comprehension e enumerate()
"""
"""
produtos = ["Arroz", "Feijão", "Macarrão", "Leite", "Café"]

codigos = {(produto[:2].upper()+f'{i:03d}'): produto for i, produto in enumerate(produtos)}

print(codigos)
"""
##########################################
"""
5. Filtro de faixa etária

# Dado o dicionário de idades: 
idades = {"Ana": 12, "Bruno": 25, "Carla": 8, "Daniel": 30, "Eduarda": 17, "Felipe": 45}
# Crie 3 novos dicionários:
# - crianças: idade < 13
# - adolescentes: 13 <= idade < 20
# - adultos: idade >= 20
# Use dict comprehension com condicional (cada um separado)
"""
"""
idades = {"Ana": 12, "Bruno": 25, "Carla": 8, "Daniel": 30, "Eduarda": 17, "Felipe": 45}

criancas = {nome: idade for nome, idade in idades.items() if idade < 13}
adolescentes = {nome: idade for nome, idade in idades.items() if 13 <= idade < 20}
adultos = {nome: idade for nome, idade in idades.items() if idade >= 20}

print(f'crianças: {criancas}')
print(f'adolescentes: {adolescentes}')
print(f'adultos: {adultos}')
"""
############################################################
"""
6. Conversor de moedas com taxa variável

# Dado o dicionário de preços em reais: preços = {"celular": 1500, "notebook": 3500, "fone": 200}
# Crie um novo dicionário com os preços convertidos para dólar
# A taxa de câmbio é: 5.20 para produtos acima de 2000, 5.00 para produtos abaixo
# Use dict comprehension com if-else na expressão
"""
"""
precos = {"celular": 1500, "notebook": 3500, "fone": 200}

precos_convertidos = {nome: preco / 5.2 if preco > 2000 else preco / 5 for nome, preco in precos.items()}

print(precos_convertidos)
"""
###########################################
# NÍVEL 7-8: Manipulação
###########################################
"""
7. Agrupamento de dados (dicionário de dicionários)

# Dada a lista de pessoas com seus dados:
pessoas = [
    {"nome": "Ana", "cidade": "SP", "idade": 25},
    {"nome": "Bruno", "cidade": "RJ", "idade": 30},
    {"nome": "Carla", "cidade": "SP", "idade": 22},
    {"nome": "Daniel", "cidade": "BH", "idade": 28},
    {"nome": "Eduarda", "cidade": "RJ", "idade": 35}
]
# Use dict comprehension para criar um dicionário onde:
# - A chave é a cidade
# - O valor é uma lista de nomes de pessoas que moram nessa cidade
"""
"""
pessoas = [
    {"nome": "Ana", "cidade": "SP", "idade": 25},
    {"nome": "Bruno", "cidade": "RJ", "idade": 30},
    {"nome": "Carla", "cidade": "SP", "idade": 22},
    {"nome": "Daniel", "cidade": "BH", "idade": 28},
    {"nome": "Eduarda", "cidade": "RJ", "idade": 35}
]

habitantes = {pessoa['cidade']: [pessoa1['nome'] for pessoa1 in pessoas if pessoa1['cidade'] == pessoa['cidade']] for pessoa in pessoas}

print(habitantes)

# Aqui eu usei pessoa e pessoa1 pra diferenciar o de dentro com o de fora e conseguir compará-los.
# Uma coisa que eu não entendi bem o pq aconteceu, é pq na estrutura mais externa a chave que eu usei pessoa['cidade'] não veio repetida... Foi coincidência?
# Achei que eu teria que usar algum tipo de set() pra não fazer a cidade vir repetidida, mas ela não veio...
"""
#####################################################################
"""
8. Média móvel (simulada)

# Dado o dicionário de vendas por dia:
vendas = {"segunda": 120, "terça": 150, "quarta": 90, "quinta": 200, "sexta": 180}
# Crie um novo dicionário onde cada valor é a média de 3 dias (dia anterior, dia, dia seguinte)
# Como não há dia anterior para segunda e dia seguinte para sexta, ignore esses casos
# Dica: use .items() e converta para lista para acessar por índice
"""
"""
vendas = {"segunda": 120, "terça": 150, "quarta": 90, "quinta": 200, "sexta": 180}

dias = [chave for chave in vendas.keys()]
qtds = [valor for valor in vendas.values()]

# vendas_dc = {dia: (qtds[i-1]+qtds[i]+qtds[i+1])/3 for dia in dias for i in range(1, len(qtds)+1)}

vendas_dc = {dias[i]: (qtds[i-1]+qtds[i]+qtds[i+1])/3 for i in range(1, len(dias)-1)}

print(vendas_dc)
"""
###########################################
# NÍVEL 9-10: Desafios
###########################################
"""
9. Matriz de distâncias (versão dicionário)

# Dada a lista de cidades: cidades = ["SP", "RJ", "BH", "BR"]
# Crie um dicionário de dicionários onde:
# - A chave principal é a cidade de origem
# - O valor é outro dicionário onde a chave é a cidade de destino e o valor é a distância
# Use dict comprehension aninhada com a seguinte regra:
# - Distância entre cidades diferentes = (ordem_cidade1 + 1) * 100 + (ordem_cidade2 + 1) * 10
# - Distância de uma cidade para ela mesma = 0
# Exemplo: SP (índice 0) para RJ (índice 1): (0+1)*100 + (1+1)*10 = 100 + 20 = 120 km
"""
"""
cidades = ["SP", "RJ", "BH", "BR"]

distancias = {cidades[i]: {cidades[j]: (i+1) * 100 + (j+1) * 10 if cidades[i] != cidades[j] else 0 for j in range(len(cidades))} for i in range(len(cidades))}

print(distancias)

# Achei esse bem tranquilo! É pq eu tenho facilidade com matemática? Na verdade acho que é pq o exercício 7 me deixou treinado haha
"""
#####################################################################
"""
10. DESAFIO FINAL: Contador de palavras com ordem de ocorrência

# Peça ao usuário para digitar uma frase
# Use dict comprehension (e outras ferramentas) para criar um dicionário onde:
# - A chave é a palavra
# - O valor é uma tupla com: (contagem, primeira_posição)
# Exemplo: frase = "casa casa carro casa"
# Resultado: {"casa": (3, 0), "carro": (1, 2)}
# 
# Depois, mostre as palavras na ordem em que apareceram pela primeira vez
# (ou seja, pela primeira_posição)
"""
"""
frase = input('Informe uma frase: ')
palavras = frase.lower().split() # descobri que a ordem importa, se eu colocar .lower() por ultimo, não funciona haha

teste = {palavras[i]: (palavras.count(palavras[i]), palavras.index(palavras[i])) for i in range(len(palavras))}

print(teste)

# tranquilo tbm! só tive que procurar o .index() n lembrava se era .locate(), .find() ou algo do tipo haha
"""