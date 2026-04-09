"""
Módulo 9: Manipulação de Arquivos
Aula 9.2: Escrita de Arquivos de Texto
Data: 09/04/2026
Objetivo: Aprender a escrever em arquivos de texto
"""

# ==========================================
# 1. EXPLICAÇÃO: O MODO "w" (WRITE)
# ==========================================

print("="*50)
print("1. O MODO 'w' (WRITE)")
print("="*50)

"""
MODO "w" = WRITE (escrever)

O que faz:
- Cria um novo arquivo (se não existir)
- Se o arquivo já existir, APAGA TODO O CONTEÚDO anterior
- Depois escreve o novo conteúdo

CUIDADO! Se você abrir um arquivo existente com "w", o conteúdo antigo é perdido.
"""

# Exemplo: criando um arquivo novo
print('--- Criando um arquivo novo ---')
with open('novo_arquivo.txt', 'w') as arquivo:
    arquivo.write("Esta é a primeira linha.\n")
    arquivo.write("Esta é a segunda linha.\n")

print("Arquivo 'novo_arquivo.txt' criado com sucesso!")

# Verificando o conteúdo
with open('novo_arquivo.txt', 'r') as arquivo:
    print(f'Conteúdo do arquivo:')
    print(arquivo.read())

# ==========================================
# 2. EXPLICAÇÃO: CUIDADO COM "w" EM ARQUIVO EXISTENTE
# ==========================================

print("\n" + "="*50)
print("2. CUIDADO: 'w' APAGA O CONTEÚDO ANTERIOR")
print("="*50)

# Primeiro, vamos criar um arquivo com algum conteúdo
with open("teste.txt", "w") as arquivo:
    arquivo.write("Este conteúdo será apagado depois.\n")
    arquivo.write("Esta é a segunda linha original.\n")

print("Arquivo 'teste.txt' criado com conteúdo original.")

# Agora, vamos abrir com "w" novamente (isso apaga o conteúdo anterior!)
with open("teste.txt", "w") as arquivo:
    arquivo.write("Novo conteúdo! O antigo foi perdido.\n")

print("\nApós abrir com 'w' novamente:")
with open("teste.txt", "r") as arquivo:
    print(arquivo.read())

# ==========================================
# 3. EXPLICAÇÃO: O MODO "a" (APPEND)
# ==========================================

print("\n" + "="*50)
print("3. O MODO 'a' (APPEND)")
print("="*50)

"""
MODO "a" = APPEND (adicionar)

O que faz:
- Cria um novo arquivo (se não existir)
- Se o arquivo já existir, MANTÉM o conteúdo anterior
- Adiciona o novo conteúdo no FINAL do arquivo

É o modo seguro para adicionar informações sem perder as existentes.
"""

# Exemplo: adicionando linhas sem perder as anteriores
print("--- Adicionando conteúdo com modo 'a' ---")
with open("teste.txt", "a") as arquivo:
    arquivo.write("Esta linha foi adicionada com append!\n")
    arquivo.write("Mais uma linha adicionada.\n")

print("Conteúdo final do arquivo (original + adicionado):")
with open("teste.txt", "r") as arquivo:
    print(arquivo.read())

# ==========================================
# 4. EXPLICAÇÃO: ESCREVENDOS MÚLTIPLAS LINHAS
# ==========================================

print("\n" + "="*50)
print("4. ESCREVENDO MÚLTIPLAS LINHAS")
print("="*50)

# 4.1. write() - uma linha por vez
print("--- Usando write() várias vezes ---")
with open("multiplas1.txt", "w") as arquivo:
    arquivo.write("Linha 1\n")
    arquivo.write("Linha 2\n")
    arquivo.write("Linha 3\n")

# 4.2. writelines() - escreve uma lista de linhas
print("\n--- Usando writelines() ---")
linhas = ["Linha A\n", "Linha B\n", "Linha C\n"]
with open("multiplas2.txt", "w") as arquivo:
    arquivo.writelines(linhas)

# 4.3. Importante: writelines NÃO adiciona quebra de linha automaticamente!
print("\n--- Cuidado: writelines não adiciona \\n ---")
linhas_sem_quebra = ["Linha 1", "Linha 2", "Linha 3"]
with open("multiplas3.txt", "w") as arquivo:
    arquivo.writelines(linhas_sem_quebra)

print("Resultado (tudo na mesma linha):")
with open("multiplas3.txt", "r") as arquivo:
    print(arquivo.read())

# Correto: adicionar \n manualmente
print("\n--- Correto: adicionando \\n ---")
linhas_com_quebra = ["Linha 1\n", "Linha 2\n", "Linha 3\n"]
with open("multiplas4.txt", "w") as arquivo:
    arquivo.writelines(linhas_com_quebra)

# ==========================================
# 5. EXPLICAÇÃO: DIFERENÇA ENTRE OS MODOS
# ==========================================

print("\n" + "="*50)
print("5. RESUMO DOS MODOS DE ABERTURA")
print("="*50)

"""
Tabela de modos:

| Modo | Nome      | O que faz                                      |
|------|-----------|------------------------------------------------|
| "r"  | read      | Lê o arquivo (padrão). Erro se não existir.   |
| "w"  | write     | Escreve. Cria novo ou APAGA o existente.      |
| "a"  | append    | Adiciona ao final. Cria novo se não existir.  |
| "x"  | exclusive | Cria um novo arquivo. Erro se já existir.     |
"""
# Exemplo do modo "x" (exclusive)
print("\n--- Modo 'x' (exclusive) ---")
try:
    with open("arquivo_novo.txt", "x") as arquivo:
        arquivo.write("Criado com modo 'x'\n")
    print("Arquivo criado com sucesso!")

    # Tentar criar novamente com 'x' dá erro
    with open("arquivo_novo.txt", "x") as arquivo:
        arquivo.write("Isso não vai funcionar")
except FileExistsError:
    print("Erro: arquivo já existe! O modo 'x' só funciona para arquivos novos.")

# ==========================================
# 6. EXEMPLOS PRÁTICOS
# ==========================================

print("\n" + "="*50)
print("6. EXEMPLOS PRÁTICOS")
print("="*50)

# 6.1. Salvando resultados de uma análise
print("\n--- Salvando resultados ---")
notas = [7.5, 8.0, 6.5, 9.0, 7.0]

with open("resultado.txt", "w") as arquivo:
    arquivo.write("=== RELATÓRIO DE NOTAS ===\n")
    arquivo.write(f"Quantidade de alunos: {len(notas)}\n")
    arquivo.write(f"Média da turma: {sum(notas)/len(notas):.2f}\n")
    arquivo.write(f"Maior nota: {max(notas)}\n")
    arquivo.write(f"Menor nota: {min(notas)}\n")

print("Relatório salvo em 'resultado.txt'")

# 6.2. Adicionando logs com append
print("\n--- Sistema de log com append ---")
import datetime

def registrar_log(mensagem):
    with open("log.txt", "a") as arquivo:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        arquivo.write(f"[{timestamp}] {mensagem}\n")

registrar_log("Programa iniciado")
registrar_log("Usuário fez login")
registrar_log("Programa encerrado")

print("Logs adicionados em 'log.txt'")

# 6.3. Criando um arquivo CSV simples
print("\n--- Criando arquivo CSV ---")
alunos = [
    ["Ana", 8.5],
    ["Bruno", 6.0],
    ["Carla", 9.0]
]

with open("alunos.csv", "w") as arquivo:
    arquivo.write("nome;nota\n")  # cabeçalho
    for aluno in alunos:
        arquivo.write(f"{aluno[0]};{aluno[1]}\n")

print("Arquivo CSV criado: alunos.csv")

# 6.4. Copiando um arquivo
print("\n--- Copiando arquivo ---")
with open("origem.txt", "w") as arquivo:
    arquivo.write("Conteúdo original\n")
    arquivo.write("Este arquivo será copiado\n")

with open("origem.txt", "r") as origem:
    conteudo = origem.read()

with open("destino.txt", "w") as destino:
    destino.write(conteudo)

print("Arquivo copiado de 'origem.txt' para 'destino.txt'")

# ==========================================
# 7. RESUMO
# ==========================================

print("\n" + "="*50)
print("7. RESUMO")
print("="*50)

"""
✅ "w" (write): cria ou APAGA e escreve. CUIDADO!
✅ "a" (append): adiciona ao final. Mantém o conteúdo existente.
✅ "x" (exclusive): cria apenas se o arquivo NÃO existir.
✅ write(): escreve uma string.
✅ writelines(): escreve uma lista de strings (sem quebra automática).
✅ write() não adiciona quebra de linha. Use "\n" explicitamente.

📌 Regras de ouro:
- Use "w" quando quiser criar/sobrescrever um arquivo
- Use "a" quando quiser adicionar informações (logs, histórico)
- Use "x" quando quiser evitar sobrescrever acidentalmente
- Sempre use with para garantir que o arquivo seja fechado
"""
####################################################
# EXERCÍCIOS - AULA 9.2
####################################################
# NÍVEL 1-3: Aquecimento
####################################################
"""
1. Escrevendo uma linha

# Crie um arquivo "saudacao.txt"
# Escreva a linha "Olá, mundo!" usando write()
# Depois, leia o arquivo para confirmar
"""
"""
print(end='')
with open('saudacao.txt', 'w') as arquivo:
    arquivo.write('Olá, mundo!')

with open('saudacao.txt', 'r') as arquivo:
    print(arquivo.read())
"""
####################################################
"""
2. Escrevendo múltiplas linhas com write()

# Crie um arquivo "frutas.txt"
# Escreva três linhas: "maçã", "banana", "laranja" (cada uma em sua linha)
# Use write() três vezes
"""
"""
print(end='')

with open('frutas.txt', 'w') as arquivo:
    arquivo.write('maçã\n')
    arquivo.write('banana\n')
    arquivo.write('laranja\n')

with open('frutas.txt', 'r') as arquivo:
    print(arquivo.read())
"""
####################################################
"""
3. Usando writelines()

# Crie uma lista: frutas = ["maçã\n", "banana\n", "laranja\n"]
# Use writelines() para escrever todas de uma vez
"""
"""
frutas = ["maçã\n", "banana\n", "laranja\n"]

with open('frutas.txt', 'w') as arquivo:
    arquivo.writelines(frutas)

with open('frutas.txt', 'r') as arquivo:
    print(arquivo.read())
"""
####################################################
# NÍVEL 4-6: Aplicação
####################################################
"""
4. Modo "a" (append)

# Crie um arquivo "log.txt" com a linha "Primeira entrada"
# Depois, use o modo "a" para adicionar "Segunda entrada"
# Mostre o conteúdo final (deve ter duas linhas)
"""
"""
print(end='')

with open('log.txt', 'w') as log:
    log.write('Primeira entrada\n')

with open('log.txt', 'a') as log:
    log.write('Segunda entrada\n')

with open('log.txt', 'r') as log:
    print(log.read())
"""
####################################################
"""
5. Salvando uma lista de números

# Crie uma lista com os números de 1 a 10
# Salve cada número em uma linha do arquivo "numeros.txt"
# Depois, leia o arquivo e mostre a soma dos números
"""
"""
numeros = [n for n in range(1, 11)]

with open('numeros.txt', 'w') as arquivo:
    for n in numeros:
        arquivo.write(f'{n}\n')

with open('numeros.txt', 'r') as arquivo:
    soma = 0
    for linha in arquivo:
        soma += int(linha.strip())
    print(soma)
"""
####################################################
"""
6. Criando um arquivo com cabeçalho

# Crie um arquivo "relatorio.txt"
# Escreva:
# === RELATÓRIO ===
# Data: [data atual]
# Usuário: [seu nome]
# -----------------
# (use o módulo datetime para a data)
"""
"""
import datetime

with open('relatorio.txt', 'w') as arquivo:
    arquivo.write('=== RELATÓRIO ===\n')
    arquivo.write(f'Data: {datetime.datetime.now().strftime('%Y/%m/%d')}\n')
    arquivo.write(f'Usuário: vhsouza')
"""
####################################################
# NÍVEL 7-8: Manipulação
####################################################
"""
7. Criando um arquivo CSV
python

# Dada a lista de alunos:
alunos = [
    ["Ana", 8.5, 7.0],
    ["Bruno", 6.0, 7.5],
    ["Carla", 9.0, 8.5]
]
# Crie um arquivo "alunos.csv" com o formato:
# nome,nota1,nota2
# Ana,8.5,7.0
# Bruno,6.0,7.5
# Carla,9.0,8.5
"""
"""
alunos = [
    ["Ana", 8.5, 7.0],
    ["Bruno", 6.0, 7.5],
    ["Carla", 9.0, 8.5]
]

with open('alunos.csv', 'w') as arquivo:
    arquivo.write('nome;nota1;nota2\n')
    for aluno in alunos:
        arquivo.write(f'{aluno[0]};{aluno[1]};{aluno[2]}\n')
"""
####################################################
"""
8. Registro de operações (log)

# Crie um programa que:
# - Pergunta ao usuário o que ele quer registrar
# - Adiciona a entrada no arquivo "historico.txt" com timestamp
# - O programa continua até o usuário digitar "sair"
# 
# Exemplo de saída no arquivo:
# [2024-01-15 10:30:00] Comprou 10 maçãs
# [2024-01-15 10:31:00] Vendeu 5 bananas
"""
"""
import datetime

while True:
    registro = input(f'Informe o registro: ')
    if registro.strip().lower() == 'sair':
        break
    else:
        with open('historico.txt', 'a') as arquivo:
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            arquivo.write(f'[{timestamp}] {registro}\n')
"""
####################################################
# NÍVEL 9-10: Desafios
####################################################
"""
9. Mesclando arquivos com append

# Crie três arquivos: "parte1.txt", "parte2.txt", "parte3.txt"
# Cada um com algumas linhas de texto
# Crie um quarto arquivo "completo.txt" que contenha todo o conteúdo dos três
# Use o modo "a" para adicionar cada arquivo ao final do completo.txt
"""
"""
_ = 0

with open('parte1.txt', 'w') as arq1:
    arq1.write('Primeiro texto, veio do arquivo 1.\n')

with open('parte2.txt', 'w') as arq2:
    arq2.write('Segundo texto, veio do arquivo 2.\n')

with open('parte3.txt', 'w') as arq3:
    arq3.write('Terceiro texto, veio do arquivo 3.\n')

##

with open('parte1.txt', 'r') as arq1:
    conteudo = arq1.read()

with open('completo.txt', 'a') as arquivo:
    arquivo.write(conteudo)

#

with open('parte2.txt', 'r') as arq2:
    conteudo = arq2.read()

with open('completo.txt', 'a') as arquivo:
    arquivo.write(conteudo)

#

with open('parte3.txt', 'r') as arq3:
    conteudo = arq3.read()

with open('completo.txt', 'a') as arquivo:
    arquivo.write(conteudo)

#

with open('completo.txt', 'r') as arquivo:
    print(arquivo.read())
"""
####################################################
"""
10. DESAFIO FINAL: Processador de texto simples

# Crie um programa que:
# 1. Pergunta ao usuário o nome do arquivo de entrada
# 2. Lê o arquivo
# 3. Aplica as seguintes transformações:
#    - Converte todo o texto para maiúsculas
#    - Remove linhas vazias
#    - Adiciona numeração das linhas (1: TEXTO, 2: TEXTO)
# 4. Pergunta o nome do arquivo de saída
# 5. Salva o resultado no arquivo de saída
# 
# Exemplo:
# Arquivo de entrada:
#   olá mundo
#   
#   python é legal
# 
# Arquivo de saída:
#   1: OLÁ MUNDO
#   2: PYTHON É LEGAL
"""
arq_entrada = input('Informe o nome do arquivo de entrada: ')

with open(arq_entrada, 'r') as arquivo:
    conteudo_entrada = []
    for linha in arquivo:
        if linha.strip() != '':
            conteudo_entrada.append(linha.strip())

conteudo_tratado = []
for i, linha in enumerate(conteudo_entrada):
    conteudo_tratado.append(f'{i+1}. {linha.upper()}\n')

arq_saida = input('Informe o arquivo de saída: ')

with open(arq_saida, 'w') as arquivo:
    arquivo.writelines(conteudo_tratado)