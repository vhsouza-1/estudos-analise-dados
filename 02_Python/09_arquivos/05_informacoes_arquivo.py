"""
Módulo 9: Manipulação de Arquivos
Aula 9.5: Informações do Arquivo
Data: 13/04/2026
Objetivo: Aprender a extrair informações de caminhos de arquivos
"""
from collections import defaultdict
from email.policy import default
from pathlib import Path

# ==========================================
# 1. EXPLICAÇÃO: .name - NOME DO ARQUIVO
# ==========================================

print("="*50)
print("1. .name - NOME DO ARQUIVO")
print("="*50)

# .name retorna o nome completo do arquivo (incluindo extensão)
caminho = Path('relatorio_final.pdf')
print(f'Caminho: {caminho}')
print(f'.name: {caminho.name}')

# Com caminho mais longo
caminho = Path("dados/planilhas/vendas_2024.xlsx")
print(f"\nCaminho: {caminho}")
print(f".name: {caminho.name}")  # só o nome do arquivo, não a pasta

# ==========================================
# 2. EXPLICAÇÃO: .stem - NOME SEM EXTENSÃO
# ==========================================

print("\n" + "="*50)
print("2. .stem - NOME SEM EXTENSÃO")
print("="*50)

# .stem retorna o nome do arquivo sem a extensão
caminho = Path("relatorio_final.pdf")
print(f"Caminho: {caminho}")
print(f".stem: {caminho.stem}")  # relatorio_final (sem .pdf)

# Com caminho mais longo
caminho = Path("dados/planilhas/vendas_2024.xlsx")
print(f"\nCaminho: {caminho}")
print(f".stem: {caminho.stem}")  # vendas_2024

# ==========================================
# 3. EXPLICAÇÃO: .suffix - EXTENSÃO
# ==========================================

print("\n" + "="*50)
print("3. .suffix - EXTENSÃO")
print("="*50)

# .suffix retorna a extensão do arquivo (incluindo o ponto)
caminho = Path("relatorio_final.pdf")
print(f"Caminho: {caminho}")
print(f".suffix: {caminho.suffix}")  # .pdf

# Outros exemplos
exemplos = ["dados.csv", "script.py", "imagem.jpg", "backup.zip", "sem_extensao"]
print('\nExemplos')
for arquivo in exemplos:
    caminho = Path(arquivo)
    print(f'Nome do arquivo: {caminho.name} -- Extensão: {caminho.suffix}')

# Arquivo sem extensão retorna string vazia
caminho = Path("arquivo_sem_extensao")
print(f"\nArquivo sem extensão: '{caminho.suffix}'")  # ''

# ==========================================
# 4. EXPLICAÇÃO: .parent - PASTA PAI
# ==========================================

print("\n" + "="*50)
print("4. .parent - PASTA PAI")
print("="*50)

# .parent retorna a pasta onde o arquivo está
caminho = Path("dados/planilhas/vendas_2024.xlsx")
print(f'Caminho: {caminho}')
print(f'.parent: {caminho.parent}')

# Vários níveis de parent
print(f"\n.parent.parent: {caminho.parent.parent}")  # dados
print(f".parent.parent.parent: {caminho.parent.parent.parent}")  # . (pasta atual)

# ==========================================
# 5. COMBINANDO AS INFORMAÇÕES
# ==========================================

print("\n" + "="*50)
print("5. COMBINANDO AS INFORMAÇÕES")
print("="*50)

caminho = Path("projeto/scripts/processador_dados.py")
print(f"Caminho completo: {caminho}")
print(f"  .name:   {caminho.name}")
print(f"  .stem:   {caminho.stem}")
print(f"  .suffix: {caminho.suffix}")
print(f"  .parent: {caminho.parent}")

# ==========================================
# 6. EXEMPLOS PRÁTICOS
# ==========================================

print("\n" + "="*50)
print("6. EXEMPLOS PRÁTICOS")
print("="*50)

# 6.1. Verificar extensão antes de processar
print("\n--- Verificando extensão ---")
arquivo = Path("dados.csv")

if arquivo.suffix == ".csv":
    print(f"{arquivo.name} é um CSV. Pode processar!")
elif arquivo.suffix == ".txt":
    print(f"{arquivo.name} é um TXT. Outro processamento.")
else:
    print(f"{arquivo.name} tem extensão {arquivo.suffix}. Não sei processar.")

# 6.2. Criar nome de arquivo de saída baseado no original
print("\n--- Criando arquivo de saída ---")
entrada = Path("relatorio_original.csv")
saida = Path(entrada.stem + "_processado" + entrada.suffix)
print(f"Entrada: {entrada}")
print(f"Saída:   {saida}")

# 6.3. Listar arquivos e mostrar informações
print("\n--- Listando arquivos .py ---")
for arquivo in Path(".").glob("*.py"):
    print(f"Arquivo: {arquivo.name}")
    print(f"  Nome sem extensão: {arquivo.stem}")
    print(f"  Pasta: {arquivo.parent}")
    print()

# 6.4. Organizar arquivos por extensão (simulação)
print("\n--- Agrupando por extensão ---")
extensoes = defaultdict(list)

for arquivo in Path(".").glob("*"):
    if arquivo.is_file():
        ext = arquivo.suffix if arquivo.suffix else "sem extensão"

        extensoes[ext].append(arquivo.name)

    print(extensoes)

for ext, lista in extensoes.items():
    print(f"{ext}: {len(lista)} arquivo(s)")
    for nome in lista[:3]:  # mostra só os 3 primeiros
        print(f"    - {nome}")

# ==========================================
# 7. RESUMO (DE VERDADE)
# ==========================================

print("\n" + "="*50)
print("7. RESUMO")
print("="*50)

"""
Hoje aprendemos 4 coisas sobre pathlib:

1. .name - nome completo do arquivo (com extensão)
   Path("dados.csv").name → "dados.csv"

2. .stem - nome do arquivo sem extensão
   Path("dados.csv").stem → "dados"

3. .suffix - extensão do arquivo (com o ponto)
   Path("dados.csv").suffix → ".csv"

4. .parent - pasta pai (onde o arquivo está)
   Path("pasta/arquivo.txt").parent → "pasta"
"""
###############################################################
# EXERCÍCIOS - AULA 9.5
###############################################################
# NÍVEL 1-3: Aquecimento
###############################################################
"""
1. Obtendo o nome do arquivo

# Crie um objeto Path para "documentos/relatorio.txt"
# Mostre o .name (nome completo do arquivo)
"""
"""
caminho = Path('documento/relatorio.txt')
print(f'Nome completo do arquivo: {caminho.name}')
"""
###############################################################
"""
2. Obtendo o nome sem extensão

# Use o mesmo caminho do exercício 1
# Mostre o .stem (nome sem extensão)
"""
"""
caminho = Path('documento/relatorio.txt')
print(f'Nome sem extensão: {caminho.stem}')
"""
###############################################################
"""
3. Obtendo a extensão

# Use o mesmo caminho do exercício 1
# Mostre o .suffix (extensão)
"""
"""
caminho = Path('documento/relatorio.txt')
print(f'Extensão: {caminho.suffix}')
"""
###############################################################
# NÍVEL 4-6: Aplicação
###############################################################
"""
4. Obtendo a pasta pai

# Use o caminho "projeto/scripts/processador.py"
# Mostre o .parent (pasta onde o arquivo está)
# Mostre o .parent.parent (pasta da pasta)
"""
"""
caminho = Path('projeto/scripts/processador.py')
print(f'Pasta onde o arquivo está: {caminho.parent}')
print(f'Pasta da pasta: {caminho.parent.parent}')
"""
###############################################################
"""
5. Verificando extensão

# Peça ao usuário o nome de um arquivo
# Verifique a extensão e mostre:
# - Se for .csv: "É um arquivo CSV"
# - Se for .txt: "É um arquivo TXT"
# - Se for .py: "É um script Python"
# - Senão: "Extensão desconhecida"
"""
"""
nome = input('Informe o nome de um arquivo: ')
arquivo = Path(nome)

if arquivo.suffix == '':
    print(f'Arquivo sem extensão ou extensão não informada')
elif arquivo.suffix == '.csv':
    print(f'É um arquivo CSV')
elif arquivo.suffix == '.txt':
    print(f'É um arquivo TXT')
elif arquivo.suffix == '.py':
    print(f'É um scrip Python')
else:
    print(f'Extensão "{arquivo.suffix}" desconhecida')
"""
###############################################################
"""
6. Criando arquivo de saída

# Dado o arquivo "dados_original.csv"
# Crie um nome de arquivo de saída: "dados_original_processado.csv"
# Use .stem e .suffix para construir o novo nome
"""
"""
arquivo = Path('dados_original.csv')
print(f'{arquivo.stem}_processado{arquivo.suffix}')
# pra não ficar igual o seu exemplo, eu usei f-string
"""
###############################################################
# NÍVEL 7-8: Manipulation
###############################################################
"""
7. Listando informações de todos os arquivos .txt

# Liste todos os arquivos .txt na pasta atual
# Para cada um, mostre:
#   - Nome completo (.name)
#   - Nome sem extensão (.stem)
#   - Extensão (.suffix)
"""
"""
for arquivo in Path('.').glob('*.txt'):
    print(arquivo)
    print(f'  - Nome completo: {arquivo.name}')
    print(f'  - Nome sem extensão: {arquivo.stem}')
    print(f'  - Extensão: {arquivo.suffix}')
"""
###############################################################
"""
8. Agrupando por extensão (com dicionário)

# Varra a pasta atual e agrupe os arquivos por extensão
# Use um dicionário onde a chave é a extensão e o valor é uma lista de nomes
# Mostre o resultado
"""
"""
extensoes = defaultdict(list)

for arquivo in Path('.').glob('*'):
    ext = arquivo.suffix

    if ext == '':
        ext = 'Sem extensão'

    extensoes[ext].append(arquivo.name)

for ext, lista in extensoes.items():
    print(ext)
    for arquivo in lista:
        print(f'  - {arquivo}')
"""
###############################################################
# NÍVEL 9-10: Desafios
###############################################################
"""
9. Renomeador de arquivos (simulação)

# Liste todos os arquivos .txt na pasta atual
# Para cada um, crie um novo nome: "backup_" + nome_original
# Exemplo: "dados.txt" → "backup_dados.txt"
# Mostre: "Renomearia: dados.txt → backup_dados.txt"
# (Não precisa renomear de verdade, só mostrar)
"""
"""
print(f'Arquivos .txt na pasta atual:')
for arquivo in Path('.').glob('*.txt'):
    print(f'  - {arquivo.name}')
    print(f'  Renomearia: {arquivo.name} para backup_{arquivo.name}')
    print()
"""
###############################################################
"""
10. DESAFIO FINAL: Organizador por extensão (com movimento)

# Crie pastas para cada extensão encontrada (ex: "txt_files", "csv_files")
# Mova cada arquivo para a pasta correspondente
# 
# Passos:
# 1. Varra a pasta atual
# 2. Para cada arquivo, identifique a extensão
# 3. Crie uma pasta com o nome da extensão (ex: "txt_files")
# 4. Crie o caminho de destino: pasta_extensao / arquivo.name
# 5. Mostre o que seria movido (use .rename() para mover de verdade - opcional)
#
# CUIDADO: Teste primeiro com arquivos que você pode perder!
"""
extensoes = []
pastas = []

for arquivo in Path('.').glob('*'):
    if arquivo.suffix not in extensoes:
        extensoes.append(arquivo.suffix)

for ext in extensoes:
    ext = ext.strip('.')
    pasta = f'{ext}_files'
    pastas.append(pasta)

destinos = []
for ext, pasta in zip(extensoes, pastas):
    for arquivo in Path('.').glob('*'):
        if arquivo.suffix == ext:
            destino = Path(pasta) / arquivo
            destinos.append(destino)

for destino in destinos:
    print(destino)

# Isso que era pra fazer caso eu não fosse mudar de fato?
