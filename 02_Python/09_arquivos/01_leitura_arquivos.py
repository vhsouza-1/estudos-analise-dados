"""
Módulo 9: Manipulação de Arquivos
Aula 9.1: Leitura de Arquivos de Texto
Data: 09/04/2026
Objetivo: Aprender a ler arquivos de texto em Python
"""

# ==========================================
# 1. POR QUE PRECISAMOS LER ARQUIVOS?
# ==========================================

print("="*50)
print("1. POR QUE LER ARQUIVOS?")
print("="*50)

# Até agora, todos os dados que usamos estavam dentro do código:
dados = [1, 2, 3, 4, 5] # dados fixos no código

# Problemas:
# 1. Se os dados mudam, precisa mudar o código
# 2. Não dá para ler arquivos grandes (milhares de linhas)
# 3. Dados reais vêm em arquivos (CSV, JSON, logs, etc.)

# Solução: ler dados de arquivos externos!

# ==========================================
# 2. ABRINDO UM ARQUIVO (JEITO SIMPLES)
# ==========================================

print("\n" + "="*50)
print("2. ABRINDO UM ARQUIVO")
print("="*50)

# O arquivo "dados.txt" deve estar na mesma pasta que este script
# (Se não existir, vamos criar um no próximo passo)

# Jeito 1: abrir e fechar manualmente
arquivo = open('dados.txt', 'r') # r = modo leitura (read)
conteudo = arquivo.read()
print(f'Conteúdo do arquivo:\n{conteudo}')
arquivo.close()
print('\nArquivo fechado')

# ==========================================
# 3. O GERENCIADOR DE CONTEXTO (JEITO CERTO)
# ==========================================

print("\n" + "="*50)
print("3. GERENCIADOR DE CONTEXTO (WITH)")
print("="*50)

# O jeito recomendado: usar "with" - fecha automaticamente
print('--- Usando with ---')
with open('dados.txt', 'r') as arquivo: # Não sabia o que é with, precisei pesquisar, evite fazer isso, a aula é justamente pra aprender isso
    conteudo = arquivo.read()
    print(f'Conteúdo:\n{conteudo}')

# O arquivo é fechado AUTOMATICAMENTE ao sair do bloco with

print(f'\nNão precisa fechar manualmente!')

# ==========================================
# 4. LENDO LINHA POR LINHA
# ==========================================

print("\n" + "="*50)
print("4. LENDO LINHA POR LINHA")
print("="*50)

# 4.1. readline() - lê uma linha por vez
print('--- readline() ---')
with open('dados.txt', 'r') as arquivo:
    linha1 = arquivo.readline()
    linha2 = arquivo.readline()
    linha3 = arquivo.readline()
    print(f'Linha 1: {linha1.strip()}')
    print(f'Linha 2: {linha2.strip()}')
    print(f'Linha 3: {linha3, type(linha3)}')

# 4.2. readlines() - lê todas as linhas para uma lista
print('\n--- readlines() ---')
with open('dados.txt', 'r') as arquivo:
    linhas = arquivo.readlines()
    print(f'Linha de linhas: {type(linhas), linhas}')

# 4.3. Iterando diretamente (mais eficiente para arquivos grandes)
print(f'\n--- Iterando diretamente ---')
with open('dados.txt', 'r') as arquivo:
    for i, linha in enumerate(arquivo):
        print(f'Linha {i+1}: {linha.strip()}')

# ==========================================
# 5. CRIANDO UM ARQUIVO PARA TESTAR (SE NÃO EXISTIR)
# ==========================================

print("\n" + "="*50)
print("5. CRIANDO ARQUIVO DE TESTE")
print("="*50)

# Vamos criar um arquivo chamado "teste.txt" para os exercícios:
with open('teste.txt', 'w') as arquivo: # repara que eu tive que inferir que o w é write...
    arquivo.write('Linha 1: Python é incrível!\n')
    arquivo.write('Linha 2: Estou aprendendo a ler arquivos.\n')
    arquivo.write('Linha 3: Isso vai ser muito útil!\n')

print('Arquivo "teste.txt" criado com sucesso!')

# Agora vamos ler o arquivo que acabamos de criar
print('\n--- Lendo o arquivo criado ---')
with open('teste.txt', 'r') as arquivo:
    for linha in arquivo:
        print(linha.strip())

# ==========================================
# 6. TRATANDO ERROS (ARQUIVO NÃO EXISTE)
# ==========================================

print("\n" + "="*50)
print("6. TRATANDO ERROS")
print("="*50)

# Tentar ler um arquivo que não existe causa erro
try: # Não sabia o que é try/except, precisei pesquisar, evite fazer isso, a aula é justamente pra aprender isso
    with open("arquivo_inexistente.txt", "r") as arquivo:
        conteudo = arquivo.read()
except FileNotFoundError:
    print("Erro: Arquivo não encontrado!")
except Exception as e:
    print(f"Erro inesperado: {e}")

# ==========================================
# 7. EXEMPLOS PRÁTICOS
# ==========================================

print("\n" + "="*50)
print("7. EXEMPLOS PRÁTICOS")
print("="*50)

# 7.1 Contando linhas de um arquivo
print('\n--- Contando linhas ---')
with open('dados.txt', 'r') as arquivo:
    numero_linhas = sum(1 for _ in arquivo) # Não sabia o que era esse sum(...), precisei pesquisar, em especial esse "_" evite fazer isso, a aula é justamente pra aprender isso
print(f'O arquivo tem {numero_linhas} linhas')

# 7.2 Procurando uma palavra específica
print(f'\n--- Procurando palavra ---')
palavra_busca = 'Python'
with open('dados.txt', 'r') as arquivo:
    for num, linha in enumerate(arquivo):
        if palavra_busca in linha:
            print(f'"{palavra_busca}" encontrada na linha {num}: {linha.strip()}')

# 7.3 Lendo apenas as primeiras N linhas
print('\n--- Primeiras 2 linhas ---')
with open('dados.txt', 'r') as arquivo:
    primeiras_linhas = [next(arquivo).strip() for _ in range(2)]
print(primeiras_linhas)

# 7.4 Lendo números de um arquivo
print('\n--- Lendo números ---')
# Vamos criar um arquivo com números
with open('numeros.txt', 'w') as arquivo:
    for i in range(11):
        arquivo.write(f'{i}\n')

# Lendo e somando
soma = 0
with open('numeros.txt', 'r') as arquivo:
    for linha in arquivo:
        soma += int(linha.strip())
print(f'Soma dos números de 1 a 10: {soma}')

# ==========================================
# 8. RESUMO
# ==========================================

print("\n" + "="*50)
print("8. RESUMO")
print("="*50)

"""
✅ open(arquivo, modo): abre um arquivo
   - "r": leitura (read) - padrão
   - "w": escrita (write) - apaga e escreve novo
   - "a": append - adiciona ao final

✅ with open(...) as arquivo: gerencia o arquivo (fecha automaticamente)

✅ read(): lê todo o conteúdo como string
✅ readline(): lê uma linha por vez
✅ readlines(): lê todas as linhas como lista
✅ for linha in arquivo: itera sobre as linhas (mais eficiente)

✅ strip(): remove espaços e quebras de linha

📌 Regras de ouro:
- SEMPRE use 'with' para abrir arquivos
- NUNCA confie que o arquivo existe - trate os erros
- Use strip() para limpar as linhas lidas
"""
#################################################################
# EXERCÍCIOS REFORMULADOS - AULA 9.1
#################################################################
# Antes de começar: Crie um arquivo meu_arquivo.txt com algumas linhas de texto.
#################################################################
# NÍVEL 1-3: Aquecimento
#################################################################
"""
1. Lendo um arquivo inteiro

# Abra o arquivo "meu_arquivo.txt" usando with e modo "r"
# Leia todo o conteúdo com read()
# Mostre o conteúdo
"""
# with open('meu_arquivo.txt', 'r', encoding='utf-8') as arquivo:
#     conteudo = arquivo.read()
#     print(conteudo)

#################################################################
"""
2. Lendo linha por linha com readline()

# Use readline() para ler a primeira linha e mostre-a
# Use readline() novamente para ler a segunda linha e mostre-a
"""
"""
print()
with open('meu_arquivo.txt', 'r', encoding='utf-8') as arquivo:
    primeira = arquivo.readline()
    print(primeira.strip())

    segunda = arquivo.readline()
    print(segunda.strip())
    # Isso aqui dá certo pq o with meio que é um iterador?
"""

#################################################################
"""
3. Usando readlines()

# Leia todas as linhas do arquivo com readlines()
# Mostre quantas linhas o arquivo tem (use len())
# Mostre a primeira linha (índice 0)
"""
"""
print()
with open('meu_arquivo.txt', 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.readlines()
    print(f'Nùmero de linhas do arquivo: {len(conteudo)}')
    print(f'Conteúdo da primeira linha: {conteudo[0]}')
"""
#################################################################
# NÍVEL 4-6: Aplicação
#################################################################
"""
4. Iterando sobre linhas com for
python

# Use um loop for para percorrer o arquivo linha por linha
# Para cada linha, mostre: f"Linha {i+1}: {linha.strip()}"
# Dica: use enumerate(arquivo, 1) para ter o número da linha
"""
"""
print(end='')

with open('meu_arquivo.txt', 'r', encoding='utf-8') as arquivo:
    for i, linha in enumerate(arquivo):
        print(f'Linha {i+1}: {linha.strip()}')
"""
#################################################################
"""
5. Contando palavras

# Leia um arquivo de texto
# Conte quantas palavras existem no arquivo
# Dica: linha.split() divide a linha em palavras, len() conta
"""
"""
print(end='')

with open('meu_arquivo.txt', 'r', encoding='utf-8') as arquivo:
    soma_palavras = 0
    for linha in arquivo:
        palavras = linha.split()
        soma_palavras += len(palavras)
    print(f'A quantidade de palavras é: {soma_palavras}')
"""
#################################################################
"""
6. Procurando por uma palavra

# Peça ao usuário uma palavra para buscar
# Leia o arquivo e mostre todas as linhas que contêm essa palavra
# Dica: use "if palavra in linha:"
"""
"""
palavra = input(f'Informe uma palavra para buscar: ')

with open('meu_arquivo.txt', 'r', encoding='utf-8') as arquivo:
    for i, linha in enumerate(arquivo):
        if palavra in linha:
            print(f'"{palavra}" encontrada na linha {i+1}')
"""
#################################################################
# NÍVEL 7-8: Manipulação
#################################################################
"""
7. Estatísticas do arquivo

# Crie um programa que leia um arquivo de texto e mostre:
# - Número total de linhas
# - Número total de palavras
# - Número total de caracteres (incluindo espaços)
# - Linha mais longa (use len() e compare)
"""
"""
print(end='')

with open('meu_arquivo.txt', 'r', encoding='utf-8') as arquivo:

    linhas = []
    palavras = []
    caracteres = []

    for linha in arquivo:
        linhas.append(linha)
        palavras += linha.split()

    for palavra in palavras:
        for caracter in palavra:
            caracteres.append(caracter)

    ind = float('-inf')
    for i, linha in enumerate(linhas):
        if len(linha) > ind:
            ind = len(linha)
            maior_linha = i


    print(f'Número total de linhas: {len(linhas)}')
    print(f'Número total de palavras: {len(palavras)}')
    print(f'Número total de caracteres: {len(caracteres)}')
    print(f'Linha mais longa: {i+1}°, conteúdo: "{linhas[i]}"')
"""
#################################################################
"""
8. Processando notas de um arquivo

# Crie um arquivo "notas.txt" com notas (uma por linha):
# 7.5
# 8.0
# 6.5
# 9.0
# 5.5
#
# Leia o arquivo e calcule:
# - Maior nota
# - Menor nota
# - Média das notas
# - Quantas notas são >= 7
"""
"""
print(end='')

with open('notas.txt', 'w') as arquivo:
    arquivo.write('7.5\n')
    arquivo.write('8.0\n')
    arquivo.write('6.5\n')
    arquivo.write('9.0\n')
    arquivo.write('5.5\n')

with open('notas.txt', 'r') as arquivo:
    notas = []
    for linha in arquivo:
        notas.append(float(linha.strip()))

    notas_m7 = [nota for nota in notas if nota >= 7]

    print(f'Maior nota: {max(notas)}')
    print(f'Menor nota: {min(notas)}')
    print(f'Média das notas: {sum(notas)/len(notas)}')
    print(f'Quantidade de notas >= 7: {len(notas_m7)}')
"""
#################################################################
# NÍVEL 9-10: Desafios
#################################################################
"""
9. Mesclando dois arquivos

# Crie dois arquivos: "alunos.txt" (nomes) e "notas.txt" (notas)
# Cada linha do primeiro corresponde à mesma linha do segundo
# Exemplo:
# alunos.txt:           notas.txt:
# Ana                   8.5
# Bruno                 6.0
# Carla                 9.0
#
# Leia os dois arquivos e crie um relatório:
# "Ana tirou 8.5"
# "Bruno tirou 6.0"
# "Carla tirou 9.0"
# 
# Depois, calcule a média da turma
"""
"""
print(end='')

with open('alunos.txt', 'w') as arquivo:
    arquivo.write('Ana\n')
    arquivo.write('Bruno\n')
    arquivo.write('Carla\n')

with open('notas.txt', 'w') as arquivo:
    arquivo.write('8.5\n')
    arquivo.write('6.0\n')
    arquivo.write('9.0\n')

with open('notas.txt', 'r') as arquivo:
    notas = []
    for nota in arquivo:
        notas.append(float(nota.strip()))

with open('alunos.txt', 'r') as arquivo:
    for aluno, nota in zip(arquivo, notas):
        print(f'{aluno.strip()} tirou {nota}')
    print(f'A média da turma foi: {sum(notas)/len(notas):.2f}')
"""
#################################################################
"""
10. DESAFIO FINAL: Filtrando e salvando em memória

# Crie um arquivo "dados.txt" com várias linhas de texto
# 
# Leia o arquivo e crie UMA lista (em memória) apenas com as linhas que:
# - Têm mais de 20 caracteres
# - Contêm a letra "a" (minúscula ou maiúscula)
#
# Depois, mostre:
# - Quantas linhas foram selecionadas
# - As primeiras 3 linhas selecionadas
# - A linha selecionada mais longa
#
# Não precisa escrever em um novo arquivo, apenas guardar na lista
"""
print(end='')

with open('dados.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write('Esta linha tem mais de vinte caracteres e tem a letra a.\n')
    arquivo.write('Linha curta.\n')
    arquivo.write('Python é incrível e tem letra a.\n')
    arquivo.write('abcde\n')
    arquivo.write('Uma linha longa que passa dos vinte caracteres facilmente.\n')
    arquivo.write('Sem letra aqui não.\n')
    arquivo.write('Abacaxi é uma fruta.\n')
    arquivo.write('x\n')
    arquivo.write('Esta linha também é bem longa e contém a letra a no meio.\n')
    arquivo.write('Casa bonita.\n')

with open('dados.txt', 'r', encoding='utf-8') as arquivo:

    linhas = [linha.strip() for linha in arquivo if len(linha.strip()) > 20 and 'a' in linha]

    print(f'Foram selecionadas {len(linhas)} linhas')

    print(f'\nAs 3 primeiras linhas selecionadas:')
    for i in range(3):
        print(f'   {linhas[i]}')

    print(f'\nLinha selecionada mais longa:')
    print(f'   {max(linhas, key=lambda x: len(x))}')
