"""
Módulo 1: Fundamentos (Primeiros Passos)
Aula 1.1: O comando print()
Data: 17/03/2026
"""

# EXEMPLOS BÁSICOS

# Meu primeiro programa
print("Olá, mundo!")
print('Olá, mundo!') # funciona com aspas simples também

# Impressão de números
print(42)

# Impressão de contas diretamente
print(10 + 5)

#EXPERIMENTAÇÕES

# Modifique o código e execute novamente:

# 1. Troque o texto do primeiro print para algo pessoal
print("Meu nome é Vinícius!")

# 2. Imprima o seu ano de nascimento
print(1999)

# 3. Faça uma conta diferente (multiplicação, divisão, subtração)
print(3 * 7)
print(25 / 5)
print(25 // 5) # divisão inteira
print(9 - 4)


# 4. Tente imprimir duas coisas no mesmo print() separadas por vírgula:
print("Meu ano de nascimento é:", 1999)
print("Minha idade é: ", 26) # aqui é normal dar esse espaço entre as duas coisas? Percebi que o Python meio que já dá esse espaço.
print("Minha idade é:" + " " + "26") #Também dá para fazer assim. Mas o 26 tem que ser string

## Perguntas para você refletir:

# 1. O que acontece se você tirar as aspas do "Olá, mundo!"?
# print(Olá, mundo!) # o Python não a entende enquanto uma string de texto e retorna erro

# 2. E se você colocar aspas no número 42?
print("42")
print("42 + 5") # o Python entende que o 42 é um texto e não um número, tanto que não dá para realizar operações com ele
print("42" + "5")
print(42 + 5) #casos para não confundir...

# 3. O Python obedece à ordem das operações matemáticas? Teste print(10 + 5 * 2)
print(10 + 5 * 2) #obedece sim!
print((10 + 5) * 2)

######################
# EXPERIMENTAÇÕES 2
######################

#1. Experimento 1.1: O parâmetro sep(separador)
print('Olá', 'mundo', '!', sep='-')
print('Olá', 'mundo', '!', sep='')
print('Olá', 'mundo', '!', sep='*')

#2. Experimento 1.2: O paramêtro end
print('Isso', end=' ')
print('continua', end=' ')
print('Na mesma linha')

print('Primeira linha', end='\n\n')
print('Depois do espaço')

#3. Experimento 1.3: Caracteres especiais
print('Linha 1\nLinha 2') # nova linha
print('Coluna1\tColuna2') # tabulação
print('Coluna1\tColuna2\nColuna3\tColuna4') # Combinação nova linha e tabulação
print('Caminho; C:\\User\\Vinícius') #precisa de barra dupla para mostrar uma barra
print("Aspas \"duplas\" dentro de aspas duplas")
# print("Aspas "duplas" dentro de aspas duplas") assim dá erro

#4. Experimento 1.4: Multiplicando strings
print('=' * 20) # linha de ======
print('PYTHON' * 3) #PYTHON 3 vezes, sem espaço
print('=-' * 15) #linha de =-=-=-

#5. Experimento 5: Formatando números

#5.1. Experimento 5.1 Controlando casas decimais
pi = 3.1415926
print("pi como definido:", pi)
print(f'pi com 2 casas: {pi:.2f}') # Esse f indica formatação? esse colchete é pra puxar uma variável de fora?
print(f'pi com 4 casas: {pi:.4f}')
print(f'pi com notação científica: {pi:.2e}')
print(f'pi com notação científica (teste): {pi:.5e}')

#5.2. Experimento 5.2 Alinhamento
print(f'|{'esquerda':<10}|') # alinhou o texto 'esquerda' à esquerda. O colchete então indica o que será formatado?
print(f'|{'direita':>8}|') # esse número indica o tamanho do espaço entre as duas ||
print(f'|{'centro':^10}|')

# 6. Experimento 6: Print com texto longo

# 6.1 Três aspas para texto longo

print("""Isso é um texto
que pode ter
múltiplas linhas
sem precisar de vários prints!""") # interessante, não precisa de \n para formatar...

# 6.2 Combinando com variáveis

nome = 'Vinícius'

print(f"""
=== CARTÃO DE VISITA ===
Nome: {nome}
Data: 17/03/2026
Estudando: Python
========================
""") # quando esqueci o primeiro f, o meu nome não apareceu...

# 7.1 Caracteres invisíveis

print('Olá\rmundo!') # oxi, esse foi estranho haha
print('Olá\b\b\bmundo!') # estranho tbm, provavelmente os dois são utilizados para editar strings específicas né

# 8.1 Tabela simples

print('=' * 33)
print(f'| {'Produto':^10}| {'Preço':^10}|{'Qtd':>5}  |')
print('=' * 33)
print(f'| {'Arroz':^10}| {23.50:^10.2f}|{3:>5}  |') # os colchetes realmente significam "algo a ser editado" então e depois do ":" vem os detalhes
print('=' * 33)
print(f'| {'Feijão':^10}| {8.75:^10.2f}|{5:>5}  |') # no nosso caso é numero:alinhamento, "tamanho da célula" e.casas decimais
print('=' * 33)



