"""
Módulo 8: Funções
Aula 8.2: Parâmetros e Escopo
Data: 06/04/2026
Objetivo: Aprender sobre parâmetros avançados e escopo de variáveis
"""

# ==========================================
# 1. PARÂMETROS OPCIONAIS (REVISÃO)
# ==========================================

print("="*50)
print("1. PARÂMETROS OPCIONAIS")
print("="*50)

# Parâmetros com valor padrão são opicionais
def saudacao(nome, saudacao_padrao='Olá'):
    print(f'{saudacao_padrao}, {nome}!')

# Usando sem o opicional
saudacao('Ana')

# Usando com o opcional
saudacao('Ana', 'Bom dia')

# Ordem importa: parâmetros obrigatórios vêm primeiro!
# def saudacao(saudacao_padrao="Olá", nome):  # ERRADO!
#     print(f"{saudacao_padrao}, {nome}!")

# ==========================================
# 2. ARGUMENTOS NOMEADOS
# ==========================================

print("\n" + "="*50)
print("2. ARGUMENTOS NOMEADOS")
print("="*50)

# Podemos chamar funções nomeando os argumentos
def apresentar(nome, idade, cidade):
    print(f'{nome} tem {idade} anos e mora em {cidade}')

# Jeito tradicional (pela ordem)
apresentar('Ana', 25, 'SP')

# Jeito com argumentos nomeados (ordem não importa)
apresentar(cidade='RJ', nome='Bruno', idade=30)
apresentar(idade=22, cidade='BH', nome='Carla')

# Misturando, argumentos posicionais primeiro, depois nomeados
apresentar('Daniel', cidade='POA', idade=28)
# apresentar(nome="Daniel", 28, "POA") # ERRADO! nomeados depois de posicionais

# ==========================================
# 3. *args - ARGUMENTOS POSICIONAIS VARIÁVEIS
# ==========================================

print("\n" + "="*50)
print("3. *args - ARGUMENTOS POSICIONAIS VARIÁVEIS")
print("="*50)

# *args permite receber qualquer quantidade de argumentos posicionais
def soma_todos(*args):
    print(f'Recebi: {args} (tipo: {type(args)})')
    return sum(args)

print(f"soma_todos(1, 2, 3): {soma_todos(1, 2, 3)}")
print(f"soma_todos(10, 20, 30, 40): {soma_todos(10, 20, 30, 40)}")
print(f"soma_todos(5): {soma_todos(5)}")
print(f"soma_todos(): {soma_todos()}")  # args é uma tupla vazia

# Combinando parâmetros normais com *args
def calcular(operacao, *args):
    if operacao == 'soma':
        return sum(args)
    elif operacao == 'multiplica':
        resultado = 1
        for num in args:
            resultado *= num
        return resultado
    else:
        return None

print(f"\ncalcular('soma', 1, 2, 3, 4): {calcular('soma', 1, 2, 3, 4)}")
print(f"calcular('multiplica', 2, 3, 4): {calcular('multiplica', 2, 3, 4)}")

# ==========================================
# 4. **kwargs - ARGUMENTOS NOMEADOS VARIÁVEIS
# ==========================================

print("\n" + "="*50)
print("4. **kwargs - ARGUMENTOS NOMEADOS VARIÁVEIS")
print("="*50)

# **kwargs permite receber qualquer quantidade de argumentos nomeados
def exibir_dados(**kwargs):
    print(f'Recebi: {kwargs} (tipo: {type(kwargs)})')
    for chave, valor in kwargs.items():
        print(f'   {chave}: {valor}')

exibir_dados(nome="Ana", idade=25, cidade="SP")
exibir_dados(produto="celular", preco=1500, quantidade=10)
exibir_dados()  # kwargs é um dicionário vazio

# combinando *args e **kwargs
def super_funcao(*args, **kwargs):
    print(f'Args (posicionais): {args}')
    print(f'Kwargs (nomeados): {kwargs}')

super_funcao(1, 2, 3, nome='Ana', idade=25)

# ==========================================
# 5. EXEMPLO PRÁTICO COM *args e **kwargs
# ==========================================

print("\n" + "="*50)
print("5. EXEMPLO PRÁTICO")
print("="*50)

def criar_relatorio(titulo, *valores, **metadados):
    """
        Cria um relatório com título, valores e metadados.

        Parâmetros:
            titulo (str): Título do relatório
            *valores: Lista de valores numéricos
            **metadados: Informações adicionais (autor, data, etc.)
    """
    print(f"\n{'=' * 40}")
    print(f"RELATÓRIO: {titulo}")
    print(f"{'=' * 40}")

    if valores:
        print(f'Valores: {valores}')
        print(f'Total: {sum(valores)}')
        print(f'Média: {sum(valores)/len(valores)}')
        print(f'Maior: {max(valores)}')
        print(f'Menor: {min(valores)}')
    else:
        print(f'Nenhum valor fornecido')

    if metadados:
        print(f'\nMetadados:')
        for chave, valor in metadados.items():
            print(f'    {chave}: {valor}')

criar_relatorio("Vendas Janeiro", 150, 200, 180, 300, autor="Ana", data="2024-01-31")
criar_relatorio("Vendas Fevereiro", 250, 180, autor="Bruno", departamento="Vendas")
criar_relatorio("Relatório Vazio")

# ==========================================
# 6. ESCOPO DE VARIÁVEIS (LOCAL vs GLOBAL)
# ==========================================

print("\n" + "="*50)
print("6. ESCOPO LOCAL vs GLOBAL")
print("="*50)

# Variável global (fora de qualquer função)
mensagem = 'Olá, mundo!'
print(f'Global: {mensagem}')

def teste_escopo():
    # Variável local (dentro da função)
    mensagem = 'Dentro da função'
    print(f'Dentro da função: {mensagem}')

teste_escopo()
print(f"Fora da função: {mensagem}")  # continua "Olá, mundo!"

# ==========================================
# 7. ACESSANDO VARIÁVEIS GLOBAIS DENTRO DE FUNÇÕES
# ==========================================

print("\n" + "="*50)
print("7. ACESSANDO VARIÁVEIS GLOBAIS")
print("="*50)

# Podemos ler variáveis globais dentro de funções
contador = 10

def ler_global():
    print(f'Valor do contador: {contador}') # lê a global

ler_global()

# Mas para MODIFICAR precisamos da palavra-chave 'global'
def modificar_global():
    global contador
    contador = 20
    print(f'Dentro da função: {contador}')
modificar_global()
print(f'Fora da função: {contador}') # agora é 20

# CUIDADO! Sem 'global' cria uma variável LOCAL
def tentar_modificar():
    contador = 30 # Isso cria uma variável LOCAL
    print(f'Dentro: {contador}')

tentar_modificar()
print(f'Fora: {contador}')

# ==========================================
# 8. ESCOPO DE PARÂMETROS
# ==========================================

print("\n" + "="*50)
print("8. ESCOPO DE PARÂMETROS")
print("="*50)

# Parâmetros são variáveis LOCAIS da função
def dobrar(numero):
    numero = numero * 2 # modifica a variável local
    print(f'Dentro da função: {numero}')

x = 10
dobrar(x)
print(f'Fora da função: {x}')

# Para modificar precisamos retornar
def dobrar_retornando(numero):
    return numero * 2

x = 10
x = dobrar_retornando(x)
print(f'Após retorno: {x}')

# ==========================================
# 9. EXEMPLOS PRÁTICOS
# ==========================================

print("\n" + "="*50)
print("9. EXEMPLOS PRÁTICOS")
print("="*50)

# 9.1 Função flexível para criar dicionário
print(f'\n--- Criando perfil com **kwargs ---')
def criar_perfil(nome, **dados):
    perfil = {'nome': nome}
    perfil.update(dados)
    return perfil

perfil1 = criar_perfil('Ana', idade=25, cidade='SP')
perfil2 = criar_perfil('Bruno', profissao='engenheiro', empresa='Tech', salario=5000)
print(perfil1)
print(perfil2)

def calculadora(operacao, *numeros):
    if not numeros:
        return 0
    if operacao == 'soma':
        return sum(numeros)
    elif operacao == 'produto':
        resultado = 1
        for num in numeros:
            resultado *= num
        return resultado
    elif operacao == 'media':
        return sum(numeros)/len(numeros)
    else:
        return None

print(f"soma de 1,2,3,4: {calculadora('soma', 1, 2, 3, 4)}")
print(f"produto de 2,3,4: {calculadora('produto', 2, 3, 4)}")
print(f"média de 10,20,30: {calculadora('media', 10, 20, 30)}")

# 9.3 Contador global
print(f'\n--- Contador de chamadas ---')
contador_chamadas = 0

def funcao_contada():
    global contador_chamadas
    contador_chamadas += 1
    if contador_chamadas == 1:
        print(f'Função chamada {contador_chamadas} vez')
    elif contador_chamadas > 1:
        print(f'Função chamada {contador_chamadas} vezes')

funcao_contada()
funcao_contada()
funcao_contada()

# ==========================================
# 10. RESUMO
# ==========================================

print("\n" + "="*50)
print("10. RESUMO")
print("="*50)

"""
✅ Parâmetros opcionais: valor padrão (def funcao(x, y=10))
✅ Argumentos nomeados: chamar função com nome dos parâmetros
✅ *args: lista de argumentos posicionais variáveis (tupla)
✅ **kwargs: dicionário de argumentos nomeados variáveis
✅ Escopo local: variáveis dentro de funções
✅ Escopo global: variáveis fora de funções
✅ global: palavra-chave para modificar variável global

📌 Regras:
- Parâmetros obrigatórios vêm antes de opcionais
- Argumentos posicionais vêm antes de nomeados
- Evite usar 'global' - prefira retornar valores
- *args e **kwargs são convenções (pode usar outros nomes, mas não faça!)
"""
#############################################################
# EXERCÍCIOS - AULA 8.2
#############################################################
# NÍVEL 1-3: Aquecimento
#############################################################
"""
1. Parâmetro opcional

# Crie uma função "apresentar" que recebe nome e um parâmetro opcional "sobrenome" (padrão "")
# Se sobrenome for fornecido, imprime nome completo; senão, só o nome
"""
"""
def apresentar(nome, sobrenome=''):
    print(nome, sobrenome)

apresentar('Ana')
apresentar('Bruno', 'Henrique')
"""
#############################################################
"""
2. *args básico

# Crie uma função "soma_quadrados" que recebe qualquer quantidade de números
# Retorna a soma dos quadrados de cada número
# Exemplo: soma_quadrados(2, 3, 4) = 4 + 9 + 16 = 29
"""
"""
def soma_quadrados(*numeros):
    soma_quadrados = 0
    for num in numeros:
        soma_quadrados += num ** 2
    return soma_quadrados

print(soma_quadrados(2, 3, 4))
"""
#############################################################
"""
3. **kwargs básico

# Crie uma função "mostrar_config" que recebe **kwargs
# Mostra cada chave e valor formatado como "chave = valor"
"""
"""
def mostrar_config(**kwargs):
    for chave, valor in kwargs.items():
        print(f'{chave}: {valor}')

mostrar_config(a=1, b=3, c='a')
"""
#############################################################
# NÍVEL 4-6: Aplicação
#############################################################
"""
4. Função com *args e **kwargs

# Crie uma função "registrar" que recebe:
# - nome (obrigatório)
# - *telefones (vários telefones)
# - **dados (email, idade, cidade, etc.)
# Retorna um dicionário com todas as informações
# Exemplo: registrar("Ana", "119999", "118888", email="ana@email.com", idade=25)
"""
"""
def registrar(nome, *telefones, **dados):
    infos = {'nome': nome, 'telefones': telefones}
    infos.update(dados)
    return infos

print(registrar("Ana", "119999", "118888", email="ana@email.com", idade=25))
"""
#############################################################
"""
5. Contador com escopo global

# Crie uma variável global "contador" inicializada em 0
# Crie uma função "incrementar" que aumenta o contador em 1
# Crie uma função "decrementar" que diminui o contador em 1
# Crie uma função "mostrar" que exibe o valor atual
# Teste as funções
"""
"""
contador = 0

def incrementar():
    global contador
    contador += 1
    print(contador)

def decrementar():
    global contador
    contador -= 1
    print(contador)

print(contador)
decrementar()
incrementar()
incrementar()
incrementar()
incrementar()
incrementar()
"""
#############################################################
"""
6. Função com múltiplos parâmetros opcionais

# Crie uma função "desconto_progressivo" que recebe:
# - valor (obrigatório)
# - desconto1 (padrão 0), desconto2 (padrão 0), desconto3 (padrão 0)
# Aplica os descontos em sequência (valor = valor * (1 - desconto/100))
# Retorna o valor final
# Exemplo: desconto_progressivo(100, desconto1=10, desconto2=5) = 100 * 0.9 * 0.95 = 85.5
"""
"""
def desconto_progressivo(valor, desconto1=0, desconto2=0, desconto3=0):
    valor = valor * (1 - desconto1 / 100)
    valor = valor * (1 - desconto2 / 100)
    valor = valor * (1 - desconto3 / 100)
    return valor

print(desconto_progressivo(100, desconto1=10, desconto2=5))
"""
#############################################################
# NÍVEL 7-8: Manipulação
#############################################################
"""
7. Emulador de print com *args e **kwargs

# Crie uma função "meu_print" que imprime:
# - *args: os valores para imprimir
# - **kwargs: pode receber "sep" (separador, padrão " ") e "end" (final, padrão "\n")
# Use a função print dentro da sua função!
# Teste: meu_print("Olá", "mundo", sep="-", end="!\n")
"""
"""
def meu_print(*valores, **parametros):
    for v in valores:
        print(v, sep=parametros['sep'], end=parametros['end'])

meu_print('Olá', 'Mundo', sep='-', end='!\n')
"""
#############################################################
"""
8. Validador de tipos com *args

# Crie uma função "validar_tipos" que recebe:
# - *valores: valores para validar
# - tipo_esperado: tipo esperado (ex: int, str, float)
# - **kwargs: pode receber "min" e "max" para números
# Retorna True se todos os valores atendem às condições, False caso contrário
# Exemplo: validar_tipos(10, 20, 30, tipo_esperado=int, min=5, max=100) → True
"""
"""
def validar_tipos(*valores, tipo_esperado=int, min=5, max=100):
    for v in valores:
        if type(v) is tipo_esperado:
            tipo = True
        else:
            tipo = False

        if v >= min:
            minimo = True
        else:
            minimo = False

        if v <= max:
            maximo = True
        else:
            maximo = False

    if tipo and minimo and maximo:
        return True
    else:
        return False

print(validar_tipos(10, 20, 30, tipo_esperado=int, min=5, max=100))
"""
#############################################################
# NÍVEL 9-10: Desafios
#############################################################
"""
9. Decorador de log (introdução)

# Um decorador é uma função que modifica outra função
# Crie uma função "log_chamadas" que:
# - Recebe uma função como argumento
# - Retorna uma nova função que:
#   * Imprime "Chamando [nome da função] com args=[...] e kwargs={...}"
#   * Chama a função original
#   * Imprime "Resultado: [resultado]"
#   * Retorna o resultado
# Teste decorando uma função de soma
"""
"""Nem entendi o enunciado, muito confuso... Pra que introduzir um conceito dificil no enunciado de um desafio? Nem explicou o que é..."""
#############################################################
"""
10. DESAFIO FINAL: Sistema de configuração com escopo global

# Crie um sistema de configuração global usando funções:
# 1. config = {} (dicionário global vazio)
# 2. set_config(chave, valor) - define/configura uma chave
# 3. get_config(chave, padrao=None) - retorna o valor ou padrão se não existir
# 4. load_config(**kwargs) - carrega múltiplas configurações de uma vez
# 5. show_config() - mostra todas as configurações formatadas
# 6. reset_config() - limpa todas as configurações
#
# Teste:
# set_config("tema", "escuro")
# set_config("idioma", "pt-BR")
# load_config(notificacoes=True, volume=80)
# show_config()
# print(get_config("tema"))  # "escuro"
# print(get_config("debug", False))  # False
# reset_config()
# show_config()  # {}
"""
config = {}

def set_config(chave, valor):
    global config
    config[chave] = valor

def get_config(chave, padrao=None):
    return config.get(chave, padrao)

def load_config(**kwargs):
    global config
    config.update(kwargs)

def show_config():
    if config == {}:
        print(config)
    else:
        for chave, valor in config.items():
            print(f'{chave}: {valor}')

def reset_config():
    global config
    config = {}

print(f'original: config: {config}')
set_config('tema', 'escuro')
print(f'após set_config("tema", "escuro"): config: {config}')
load_config(notificacoes=True, volume=80)
print(f'após load_config(notificacoes=True, volume=80): config: {config}')
print()
show_config()
print()
print(get_config("tema"))

print(get_config("debug", False))  # False
reset_config()
show_config()  # {}











#############################################################