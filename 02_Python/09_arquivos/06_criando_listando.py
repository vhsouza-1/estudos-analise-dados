"""
Módulo 9: Manipulação de Arquivos
Aula 9.6: Criando Pastas e Listando Arquivos
Data: 14/04/2026
Objetivo: Aprender a criar pastas e listar arquivos
"""
from collections import defaultdict
from pathlib import Path

# ==========================================
# 1. EXPLICAÇÃO: .mkdir() - CRIAR PASTA
# ==========================================

print("="*50)
print("1. .mkdir() - CRIAR PASTA")
print("="*50)

# Criar uma pasta simples
pasta_nova = Path('minha_pasta_nova')

if not pasta_nova.exists():
    pasta_nova.mkdir()
    print(f'Pasta "{pasta_nova}" criada!')
else:
    print(f'Pasta "{pasta_nova}" já existe')

# Criar pastas aninhadas (pasta dentro de pasta)
pastas_aninhadas = Path('pasta1/pasta2/pasta3')

if not pastas_aninhadas.exists():
    pastas_aninhadas.mkdir(parents=True) # parents=True cria todas as pastas do caminho
    print(f"Pastas aninhadas criadas: {pastas_aninhadas}")
else:
    print(f"Pastas já existem")

# exist_ok=True - não dá erro se a pasta já existir
pasta_com_exist_ok = Path('outra_pasta')
pasta_com_exist_ok.mkdir(exist_ok=True) # não dá erro se a pasta já existir
print(f'Pasta "{pasta_com_exist_ok}" criada (ou já existia)')

# Testei para ver o que acontecia
# caminho = Path('pasta1')
# caminho.mkdir()

# ==========================================
# 2. EXPLICAÇÃO: .glob() - LISTAR ARQUIVOS COM PADRÃO
# ==========================================

print("\n" + "="*50)
print("2. .glob() - LISTAR ARQUIVOS COM PADRÃO")
print("="*50)

# Criar alguns arquivos de exemplo para listar
for nome in ["dados.csv", "planilha.csv", "relatorio.txt", "script.py", "backup.zip"]:
    Path(nome).touch()  # cria arquivo vazio (não vamos usar muito, só para exemplo)

print("Arquivos criados para exemplo: dados.csv, planilha.csv, relatorio.txt, script.py, backup.zip")

# Listar todos os arquivos CSV
print("\n--- Arquivos .csv ---")
for arquivo in Path('.').glob('*.csv'):
    print(f'  - {arquivo.name}')

# Listar todos os arquivos CSV
print("\n--- Arquivos .txt ---")
for arquivo in Path('.').glob('*.txt'):
    print(f'  - {arquivo.name}')

# Listar todos os arquivos .py
print("\n--- Arquivos .py ---")
for arquivo in Path(".").glob("*.py"):
    print(f"  - {arquivo.name}")

# Padrão curinga: * significa "qualquer coisa"
print("\n--- Todos os arquivos com a letra 'a' no nome ---") # bom pra selecionar arquivos por ano, cidade, nome, etc ne?
for arquivo in Path(".").glob("*a*"):
    print(f"  {arquivo.name}")


# ==========================================
# 3. EXPLICAÇÃO: .iterdir() - LISTAR TUDO
# ==========================================

print("\n" + "="*50)
print("3. .iterdir() - LISTAR TUDO")
print("="*50)

# .iterdir() lista TUDO (arquivos e pastas) na pasta atual
print('--- Tudo na pasta atual ---')
for item in Path('.').iterdir():
    if item.is_file():
        print(f'  [ARQUIVO] {item.name}')
    elif item.is_dir():
        print(f'  [PASTA]   {item.name}')

print()
for item in Path('.').glob('*'): # mesma coisa né?
    if item.is_file():
        print(f'  [ARQUIVO] {item.name}')
    elif item.is_dir():
        print(f'  [PASTA]   {item.name}')


# ==========================================
# 4. COMPARANDO .glob() E .iterdir()
# ==========================================

print("\n" + "="*50)
print("4. .glob() vs .iterdir()")
print("="*50)

print("'glob' é para filtrar (ex: todos os .csv)")
print("'iterdir' é para listar tudo (sem filtro)")

print('\n--- .glob("*.csv") ---')
csvs = list(Path('.').glob('*.csv'))
print(f'Encontrou {len(csvs)} arquivo(s) .csv')

print('\n--- .iterdir() ---')
todos = list(Path('.').iterdir())
print(f'Encontrou {len(todos)} item(ns) no total')

# ==========================================
# 5. EXEMPLOS PRÁTICOS
# ==========================================

print("\n" + "="*50)
print("5. EXEMPLOS PRÁTICOS")
print("="*50)

# 5.1 Criar estrutura de pastas para um projeto
print('\n--- Criando estrutura de projeto ---')
projeto = Path('meu_projeto')

pastas = ['dados', 'scripts', 'output', 'logs']

for nome_pasta in pastas:
    (projeto / nome_pasta).mkdir(parents=True, exist_ok=True)
    print(f'Pasta criada: {projeto / nome_pasta}')

"""
Ai percebi uma coisa, meio que tudo tem essa estrutura basica ne? Tipo assim, pra fazer algum projeto com dados, 
ou pra fazer um prgrama de computador, eu precio de dados, os scripts que vao fazer algo com esses dados, o output 
que o scripr+dados vai me devolver e os logs pra registro... né?

Minha cabeça ta começando a entender algumas questões sobre computação que tem me deixado bem empolgado haha

Caraca isso é tão lindo, como eu adoro entender as coisas
"""

# 5.2 Contar arquivos por extensão
# 5.2. Contar arquivos por extensão
print("\n--- Contando arquivos por extensão ---")
contagem = {}

for arquivo in Path(".").glob("*"):
    if arquivo.is_file():
        ext = arquivo.suffix if arquivo.suffix else "sem extensão"
        contagem[ext] = contagem.get(ext, 0) + 1 # por quê você não usou defaultdict aqui? Você não me ensinou isso assim...

for ext, qtd in contagem.items():
    print(f'   {ext}: {qtd} arquivo(s)')

# 5.3 Criar subpastas para organizar arquivos (simulação)
print('\n--- Simulação de organização ---')
extensoes = ['.csv', '.txt', '.py']

for ext in extensoes:
    nome_pasta = f'{ext[1:]}_files' # remove o ponto do início
    print(f'Arquivos {ext} iriam para a pasta: {nome_pasta}/')

# ==========================================
# 6. RESUMO (DE VERDADE)
# ==========================================

print("\n" + "="*50)
print("6. RESUMO")
print("="*50)

"""
Hoje aprendemos 3 coisas sobre pathlib:

1. .mkdir() - criar pastas
   - .mkdir() - cria uma pasta (dá erro se já existir)
   - .mkdir(parents=True) - cria pastas aninhadas
   - .mkdir(exist_ok=True) - não dá erro se já existir

2. .glob("padrão") - listar arquivos com padrão
   - "*.csv" - todos os CSV
   - "*.txt" - todos os TXT
   - "*a*" - arquivos com a letra 'a' no nome

3. .iterdir() - listar TUDO (arquivos e pastas)
"""
###################################################################
# EXERCÍCIOS - AULA 9.6
###################################################################
# NÍVEL 1-3: Aquecimento
###################################################################
"""
1. Criando uma pasta simples

# Crie uma pasta chamada "teste_aula"
# Verifique se ela existe depois de criar
"""
"""
nova_pasta = Path('teste_aula')

if not nova_pasta.exists():
    nova_pasta.mkdir()
    print(f'{nova_pasta} criada!')
else:
    print(f'{nova_pasta} já existe!')

# sempre colocar o mkdir dentro da verificação de existência pra não ficar gerando erro no código, né?
"""
###################################################################
"""
2. Criando pastas aninhadas

# Crie as pastas: "projeto/dados/raw" (uma dentro da outra)
# Use parents=True
"""
"""
pastas_aninhadas = Path('projeto/dados/raw')

if not pastas_aninhadas.exists():
    pastas_aninhadas.mkdir(parents=True)
    print(f'{pastas_aninhadas} criadas!')
else:
    print(f'{pastas_aninhadas} já existem!')
"""
###################################################################
"""
3. Listando arquivos .csv

# Use .glob() para listar todos os arquivos .csv na pasta atual
# Mostre o nome de cada um
"""
"""
print(f'Itens na pasta atual: ')
for item in Path('.').glob('*'):
    print(f'  - {item.name}')
"""
###################################################################
# NÍVEL 4-6: Aplicação
###################################################################
"""
4. Listando arquivos .txt

# Use .glob() para listar todos os arquivos .txt
# Para cada arquivo, mostre o nome e o tamanho (use .stat().st_size)
"""
"""
print(f'Arquivos .txt na pasta atual')
for item in Path('.').glob('*.txt'):
    print(f'  - {item.name}: {item.stat().st_size}')
"""
###################################################################
"""
5. Contando arquivos por extensão

# Use .glob("*") para percorrer todos os arquivos
# Conte quantos arquivos têm extensão .csv, .txt, .py
# Mostre o resultado
"""
"""
contagem = defaultdict(int)

for item in Path('.').glob('*'):
    if item.is_file():
        ext = item.suffix if item.suffix != '' else 'no_ext'

    elif item.is_dir():
        ext = 'dir'

    contagem[ext] += 1

for ext, num in contagem.items():
    print(f'{ext:>4}: {num} arquivo(s)')
"""
###################################################################
"""
6. Criador de projetos

# Peça ao usuário um nome de projeto e um ano
# Crie a estrutura:
#   [ano]_[projeto]/
#     inputs/
#     outputs/
#     relatorios/
# Exemplo: "2024_vendas" → pasta "2024_vendas" com as subpastas
"""
"""
nome_projeto = input('Informe o nome do projeto: ')
ano = int(input('Informe o ano do projeto: '))

projeto_ano = Path(f'{ano}_{nome_projeto}')

pastas = ['inputs', 'outputs', 'relatorios']

for pasta in pastas:
    subpasta = projeto_ano / pasta
    subpasta.mkdir(exist_ok=True, parents=True)
"""
###################################################################
# NÍVEL 7-8: Manipulação
###################################################################
"""
7. Scanner de arquivos duplicados (por nome)

# Varra a pasta atual e encontre arquivos com o mesmo nome (ignorando extensão)
# Exemplo: "dados.csv" e "dados.txt" têm o mesmo nome "dados"
# Mostre: "dados: .csv, .txt"
"""
"""
scanner = defaultdict(list)

for item in Path('.').glob('*'):

    if item.is_file():

        scanner[item.stem].append(item.suffix)

repetidos = {nome: ext for nome, ext in scanner.items() if len(ext) > 1}

for nome, exts in repetidos.items():
    print(f'{nome}: {exts}')
"""
###################################################################
"""
8. Criador de pastas por data

# Crie pastas para os últimos 5 anos (2020, 2021, 2022, 2023, 2024)
# Dentro de cada uma, crie as subpastas: "janeiro", "fevereiro", "marco"
# Use um loop para não repetir código
"""
"""
anos = [str(2026 - i) for i in range(1,6)]

meses = ['janeiro', 'fevereiro', 'marco']

for ano in anos:
    pasta_ano = Path(ano)
    for mes in meses:
        pasta_ano_mes = pasta_ano / mes
        pasta_ano_mes.mkdir(exist_ok=True, parents=True)
"""
###################################################################
# NÍVEL 9-10: Desafios
###################################################################
"""
9. Relatório de ocupação

# Crie um relatório da pasta atual mostrando:
# - Quantos arquivos existem (total)
# - Quantas pastas existem
# - Qual o tamanho total de todos os arquivos (soma dos .stat().st_size)
# - Qual o maior arquivo (nome e tamanho)
# - Qual a extensão mais comum
"""
"""
arquivos = []
pastas = []
tamanhos = defaultdict(float)
extensoes = defaultdict(int)

for item in Path('.').glob('*'):

    if item.is_file():
        arquivos.append(item)
        extensoes[item.suffix] += 1

    elif item.is_dir():
        pastas.append(item)

    tamanhos[item.name] = item.stat().st_size

print(f'Quantos arquivos existem: {len(arquivos)}')
print(f'Quantas pastas existem: {len(pastas)}')
print(f'Qual o tamanho total de todos os arquivos: {sum(tamanhos.values())}')
print(f'Qual o maior arquivo: {max(tamanhos.items(), key=lambda x: x[1])}')
print(f'Qual a extensão mais comum: {max(extensoes.items(), key=lambda x: x[1])}')
"""
###################################################################
"""
10. DESAFIO FINAL: Organizador com validação

# Crie um programa que:
# 1. Varre a pasta atual
# 2. Para cada arquivo, identifica a extensão
# 3. Cria uma pasta com o nome da extensão (ex: "csv_files")
# 4. ANTES de mover, verifica se o arquivo de destino já existe
#    - Se existir, adiciona um número: "dados(1).csv"
# 5. Mostra o que seria movido com o nome final
#
# Exemplo de saída:
#   dados.csv → csv_files/dados.csv
#   dados.csv (já existe) → csv_files/dados(1).csv
#   relatorio.txt → txt_files/relatorio.txt
#
# CUIDADO: Não mova os arquivos de verdade. Só simule.
"""
pastas = defaultdict(list)

for item in Path('.').glob('*'):

    if item.is_file():

        pastas[f'{item.suffix[1:]}_files'].append(item.name)

        print(f'{item.name} -> {item.suffix[1:]}_files/{item.name}')