"""
Módulo 1: Fundamentos (Primeiros Passos)
Aula 1.3: Entendendo erros
Data: 17/03/2026

INSTRUÇÃO: Execute cada seção separadamente.
O objetivo é PROVOCAR erros e aprender com eles.
"""

# ========================================================
# ERRO 1: SyntaxError - O mais básico
# ========================================================

# print('Olá, mundo!' # Falta fechar o parêntese

print('Olá, mundo!') # Corrigido

# ========================================================
# ERRO 2: NameError - Variável não existe
# ========================================================

# print(nome) # nome não foi definido

nome = 'Vinícius'; print(nome) # Corrigido (tentei colocar na mesma linha e não deu certo, mas com o ';' deu certo hehe)

# ========================================================
# ERRO 3: TypeError - Operação com tipos errados
# ========================================================

# idade = 25; print('Minha idade é: ' + idade)

idade = 25
print('Minha idade é:', idade)
print('Minha idade é: ' + str(idade))
print(f'Minha idade é: {idade}') # 3 soluções possíveis

# ========================================================
# ERRO 4: ZeroDivisionError - Matemática Impossível
# ========================================================

# resultado = 10 / 0; print(resultado)

resultado = 10 / 2; print(resultado) # corrigido

# ========================================================
# ERRO 5: IdentationError - O terror dos iniciantes
# ========================================================

# def dizer_oi():
# print("Olá!")

def dizer_oi():
    print('Olá!') # corrigido


# ========================================================
# Desafio - Decifrando os erros
# Abaixo, código ERRADO. Sua missão: identificar o erro e corrigir.
# ========================================================

# DESAFIO 1
# numero = "10"
# resultado = numero + 5
# print(resultado)

# "10" é uma string, não um número, o erro aparece quando tentamos somar o texto "10" com o número 5.
#Correção:

numero = 10
resultado = numero + 5
print(resultado)

# DESAFIO 2
# lista = [1, 2, 3]
# print(lista[3])

"""
Apesar de não termos visto isso na parte teórica, percebi fazendo teste que o número dos itens de lista começa do 0.
Quando eu faço o print e substituo o 3 por 0, 1 e 2, ele me mostra respectivamente 1, 2 e 3. 
Desta forma, para corrigir o erro, se eu quero ver o "terceiro" item da lista, eu tenho que print(lista[2]):
"""
lista = [1, 2, 3]
print(lista[2])

# DESAFIO 3
#def saudacao:
#    print("Olá!")

"""
Erro de syntax normal, o Python espera "()" depois do nome da função que defini.
Estou supondo que isso seja uma função, por semelhança à coisas que já vi em outros locais.
"""
def saudacao():
    print('Olá!')

# DESAFIO 4
"""
x = 10
y = 0
media = x / y
print(media)
"""

# Erro simples, divisão por zero. Correção:

x = 10
y = 1
media = x / y
print(media)

# DESAFIO 5
#print("Olá mundo!)

#Erro simples de syntax, faltou fechar as aspas duplas. Correção:

print("Olá mundo!")

# ========================================================
# Bônus - Usando erros para testar limites
# ========================================================

# Teste 1: Até onde strings vão?
print("5" * 3)    # Funciona? O que acontece? R: Printa o "5" 3 vezes (555), multiplica a string
# print("5" + 3)    # Erro? Por quê? R: Concatenação de variáveis diferentes.

# Teste 2: Divisões interessantes
print(10 / 3)     # Resultado? R: 3.333...
print(10 // 3)    # E agora? R: Achei que daria erro, mas ele apenas pega a parte inteira da divisão

# Teste 3: Limites do Python
print(10 ** 1000)  # Número gigante funciona? R: Sim, funciona e parece que funciona bem até... haha

















