"""
Módulo 1: Fundamentos (Primeiros Passos)
Aula 1.2: Comentários
Data: 17/03/2026
"""

# =========================================
# 1. Comentário de linha única:
# =========================================

    # Isso é um comentário de linha única
    print('Olá!') # Comentário de linha única depois do código
    #print('Olá!') # Código comentado é desativado

# =========================================
# 2. Comentário de múltiplas linhas (docstring)
# =========================================
    """
    Isso é uma string multilinha que NÃO é atribuída a nenhuma variável.
    O Python ignora, então funciona como comentário.
    Muito usado no INÍCIO de arquivos e funções
    """
    print('Código normal')

# =========================================
# 3. Docstring (utilização profissional)
# =========================================

    # Quando usado no início de funções/classes/arquivos, vira DOCUMENTAÇÃO:
    """
    Módulo 1: Fundamentos (Primeiros Passos)
    Aula 1.2: Comentários
    Data: 17/03/2026
    """
# =========================================
# 4. Boas práticas
# =========================================

# 4.1 Comentários bons (explicam o PORQUÊ):

    # Ruim (explica o óbvio)
    x = x + 1  # incrementa 1 em X

    # Bom (explica o não óbvio)
    tempo_segundos = tempo_ms / 1000 # Ajuste necessário porque a API retorna valores em milissegundos

# 4.2 Comentários para "TODOs" (tarefas pendentes). Ex:

    #TODO: Implementar validação de entrada do usuário
    #FIXME: Esta função falha com números negativos
    #NOTE: Esta parte será otimizada depois

    #Muito legal a identificação diferente para os TODO/FIXME

# 4.3 Comentários para debug (temporários)

    print(f'DEBUG: valor de x é {x}') # Linha temporária
    # print(f'DEBUG: valor de x é {x}') # comentado = debug desligado

# =========================================
# 5. O que você pode não saber:
# =========================================

# 5.1 Docstring vs Comentários comuns. Exemplo:

def calcular_media(notas):
    """
    Calcula a média de uma lista de notas.
    Usa divisão por zero? Não! Retorna 0 se lista vazia.
    """
    if not notas:
        return 0
    return sum(notas) / len(notas)

# A diferença: isso aparece com help(calcular_media)
# Comentários comuns (#) não aparecem na ajuda oficial

# 5.2 Shebang (primeira linha do arquivo - em sistemas Unix)

    #!/usr/bin/env python3
    # Acima é uma linha especial para sistemas Linux/Mac
    # Diz ao sistema: "use Python pra executar este arquivo"

# =========================================
# VERIFICAÇÃO RÁPIDA
# =========================================

# Perguntas para você responder (só para garantir):

    # 1. Como fazer um comentário de UMA linha em Python?

        #R: Utilizando "#" antes do comentário

    # 2. Como fazer um comentário de MÚLTIPLAS linhas?

        #R: Utilizando aspas triplas """ comentário """

    # 3. Qual a diferença entre # e """ no início de um arquivo?

        #R: # no começo de um documento é um shebang usado em sistemas Unix para informações especificas. Já """ indica documentação/cabeçalho/informações daquele documento

    # 4. Por que isso é ruim? x = 10 # x recebe 10

        #R: Porque é um comentário óbvio que descreve o que o código faz, mas não o PORQUÊ isso está sendo feito.