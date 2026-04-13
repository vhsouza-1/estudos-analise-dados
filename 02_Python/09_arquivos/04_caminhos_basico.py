"""
Módulo 9: Manipulação de Arquivos
Aula 9.4: Criando e Verificando Caminhos
Data: 13/04/2026
Objetivo: Aprender a criar caminhos e verificar existência de arquivos/pastas
"""

# ==========================================
# 1. EXPLICAÇÃO: O QUE É PATHLIB?
# ==========================================

print("="*50)
print("1. O QUE É PATHLIB?")
print("="*50)

"""
pathlib é uma biblioteca do Python para trabalhar com caminhos de arquivos.
Ela funciona em Windows, Linux e Mac sem precisar se preocupar com as diferenças.

Sem pathlib (problema):
    caminho = "pasta\\subpasta\\arquivo.txt"  # Só funciona no Windows

Com pathlib (solução):
    from pathlib import Path
    caminho = Path("pasta") / "subpasta" / "arquivo.txt"  # Funciona em qualquer SO
"""

from pathlib import Path

# ==========================================
# 2. EXPLICAÇÃO: CRIANDO OBJETOS PATH
# ==========================================

print("\n" + "="*50)
print("2. CRIANDO OBJETOS PATH")
print("="*50)

# Criando um objeto Path para um arquivo
arquivo = Path('pessoas.csv')
print(f'Objeito Path: {arquivo}')
print(f'Tipo: {type(arquivo)}') # <class 'pathlib._local.WindowsPath'>

# Criar um objeto Path para uma pasta
pasta = Path('minha_pasta')
print(f'Pasta: {pasta}')

# ==========================================
# 3. EXPLICAÇÃO: JUNTANDO CAMINHOS COM /
# ==========================================

print("\n" + "="*50)
print("3. JUNTANDO CAMINHOS COM /")
print("="*50)

# O operador / junta partes do caminho
caminho = Path('dados') / 'planilhas' / 'relatorio.xslx'
print(f'Caminho criado: {caminho}')

# Isso funciona em qualquer sistema operacional!
# No Windows vira: dados\planilhas\relatorio.xlsx
# No Linux vira: dados/planilhas/relatorio.xlsx

# ==========================================
# 4. EXPLICAÇÃO: VERIFICANDO SE EXISTE (.exists())
# ==========================================

print("\n" + "="*50)
print("4. VERIFICANDO SE EXISTE (.exists())")
print("="*50)

# Verificar se um arquivo existe
arquivo = Path('pessoas.csv')
print(f'Arquivo "pessoas.csv" existe? {arquivo.exists()}')

# Verificar se um arquivo que não existe... não existe
inexistente = Path("arquivo_que_nao_existe.txt")
print(f"Arquivo inexistente existe? {inexistente.exists()}")

# Verificar se uma pasta existe
pasta = Path("csv_files")
print(f"Pasta 'csv_files' existe? {pasta.exists()}")

# ==========================================
# 5. EXPLICAÇÃO: É ARQUIVO OU PASTA?
# ==========================================

print("\n" + "="*50)
print("5. É ARQUIVO OU PASTA?")
print("="*50)

# .is_file() verifica se é um arquivo
arquivo = Path('pessoas.csv')
print(f'É arquivo? {arquivo.is_file()}')

# .is_dir verifica se é uma pasta
pasta = Path(".")
print(f"'.' é arquivo? {Path('.').is_file()}")
print(f"'.' é pasta? {Path('.').is_dir()}")

# ==========================================
# 6. EXEMPLOS PRÁTICOS
# ==========================================

print("\n" + "="*50)
print("6. EXEMPLOS PRÁTICOS")
print("="*50)

# 6.1 Verificar se um arquivo existe antes de ler
print('\n--- Verificando antes de ler ---')
arquivo = Path('pessoas.csv')

if arquivo.exists():
    with open(arquivo, 'r') as f:
        print(f.read()[:50]) # primeiros 50 caracteres
else:
    print(f'Arquivo {arquivo} não encontrado')

# Criando caminho para um arquivo em uma subpasta
print('\n--- Criando caminho ---')
caminho = Path('dados') / 'processados' / 'final.csv'
print(f'Caminho: {caminho}')
print(f'O arquivo existe? {caminho.exists()}')

# ==========================================
# 7. RESUMO (DE VERDADE)
# ==========================================

print("\n" + "="*50)
print("7. RESUMO")
print("="*50)

"""
Hoje aprendemos 4 coisas sobre pathlib:

1. Path() - cria um objeto de caminho
   from pathlib import Path
   arquivo = Path("meu_arquivo.txt")

2. / - junta partes do caminho
   caminho = Path("pasta") / "subpasta" / "arquivo.txt"

3. .exists() - verifica se arquivo/pasta existe
   if caminho.exists(): ...

4. .is_file() e .is_dir() - verifica se é arquivo ou pasta
   if caminho.is_file(): ...
"""
###########################################################
# EXERCÍCIOS - AULA 9.4
###########################################################
# NÍVEL 1-3: Aquecimento
###########################################################
"""
1. Criando um objeto Path

# Crie um objeto Path para o arquivo "dados.txt"
# Mostre o objeto criado
"""
"""
objeto = Path('dados.txt')
print(f'Objeto criado: {objeto}')
"""
###########################################################
"""
2. Juntando caminhos

# Use o operador / para criar o caminho:
# "projeto" / "src" / "main.py"
# Mostre o resultado
"""
"""
caminho = Path('projeto') / 'src' / 'main.py'
print(f'Resultado: {caminho}')
"""
###########################################################
"""
3. Verificando existência

# Verifique se o arquivo "pessoas.csv" existe
# Mostre "Existe" ou "Não existe"
"""
"""
arquivo = Path('pessoas.csv')

if arquivo.exists():
    print('Existe!')
else:
    print('Não existe!')
"""
###########################################################
# NÍVEL 4-6: Aplicação
###########################################################
"""
4. Verificando antes de ler

# Peça ao usuário o nome de um arquivo
# Verifique se o arquivo existe
# Se existir, mostre "Arquivo encontrado"
# Se não existir, mostre "Arquivo não encontrado"
"""
"""
nome_arquivo = input(f'Informe o nome de um arquivo: ')
arquivo = Path(nome_arquivo)

if arquivo.exists():
    print('Arquivo encontrado')
else:
    print('Arquivo não encontrado')
"""
###########################################################
"""
5. É arquivo ou pasta?

# Peça ao usuário um caminho (ex: ".", "pessoas.csv", "csv_files")
# Verifique se é arquivo ou pasta
# Mostre o resultado
"""
"""
caminho_informado = input('Informe um caminho: ')
caminho = Path(caminho_informado)

if caminho.is_file():
    print('É um arquivo!')
elif caminho.is_dir():
    print('É uma pasta!')
else:
    print('Não é arquivo nem pasta!')
"""
###########################################################
"""
6. Criando caminho seguro

# Crie um caminho para "dados/raw/entrada.csv" usando pathlib
# Mostre o caminho
# Verifique se o arquivo existe (provavelmente não)
"""
"""
caminho = Path('dados/raw/entrada.csv')
print(f'Caminho: {caminho}')
print(f'Arquivo existe? {caminho.exists()}')

caminho = Path('C:\\Users\\code\\Desktop\\estudos-analise-dados\\02_python\\09_arquivos') # teste com o caminho do script
print(f'Caminho: {caminho}')
print(f'Arquivo existe? {caminho.exists()}')
"""
###########################################################
# NÍVEL 7-8: Manipulação
###########################################################
"""
7. Validando entrada do usuário

# Peça ao usuário o nome de um arquivo para ler
# Verifique se o arquivo existe
# Se existir, leia e mostre as primeiras 3 linhas
# Se não existir, mostre uma mensagem de erro
"""
"""
arquivo = Path(input('Informe o nome do arquivo: '))

if arquivo.exists():
    with open('teste.txt', 'r') as file:
        cont = 0
        for linha in file:
            if cont < 3:
                print(linha.strip())
                cont += 1 # só consegui lembrar como fazer isso com contador. Era pra fazer assim mesmo?

else:
    print('Não existe')
"""
###########################################################
"""
8. Criando múltiplos caminhos

# Crie uma lista com os nomes: ["dados.csv", "relatorio.txt", "backup.zip"]
# Para cada nome, crie um objeto Path e verifique se existe
# Mostre: "dados.csv: Existe" ou "dados.csv: Não existe"
"""
"""
lista = ["dados.csv", "relatorio.txt", "backup.zip"]

for nome in lista:
    arquivo = Path(nome)
    if arquivo.exists():
        print(f'{nome}: Existe')
    else:
        print(f'{nome}: Não existe')
"""
###########################################################
# NÍVEL 9-10: Desafios
###########################################################
"""
9. Verificando múltiplos arquivos

# Use glob do módulo pathlib para listar todos os arquivos .csv
# Dica: Path(".").glob("*.csv") retorna um iterador com os caminhos
# Para cada arquivo, mostre o nome e diga se é arquivo (sempre será)
"""
"""
# Como na pasta não tem nenhum arquivo .csv (apaguei todos da aula passada), vou usar para .txt (criei dois nessa aula para testar)

arquivos_txt = Path('.').glob('*.txt')

for arquivo in arquivos_txt:
    print(f'Nome do arquivo: {arquivo}')
    print(f'   É arquivo? {arquivo.is_file()}')
    print()
"""
###########################################################
"""
10. DESAFIO FINAL: Criador de estrutura segura

# Peça ao usuário um nome de projeto
# Crie os seguintes caminhos (sem criar as pastas ainda, apenas os objetos Path):
#   - [projeto]/dados/raw/
#   - [projeto]/dados/processed/
#   - [projeto]/scripts/
#   - [projeto]/output/
# Para cada caminho, verifique se a pasta já existe
# Mostre um relatório: "pasta X: Existe" ou "pasta X: Não existe"
"""
projeto = input('Informe o nome do projeto: ').strip()

projeto_dados_raw = Path(projeto) / 'dados' / 'raw'
projeto_dados_processed = Path(projeto) / 'dados' / 'processed'
projeto_scripts = Path(projeto) / 'scripts'
projeto_output = Path(projeto) / 'output'

projeto_pastas = [projeto_dados_raw, projeto_dados_processed, projeto_scripts, projeto_output] # gostou? hehe

for pasta in projeto_pastas:
    print(f'pasta {pasta}: {'Existe' if pasta.exists() else 'Não existe'}')