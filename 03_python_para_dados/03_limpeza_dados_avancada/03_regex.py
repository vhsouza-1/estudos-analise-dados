"""
Bloco 3: Python para Dados
Módulo 3: Limpeza de Dados Avançada
Aula 3: Expressões Regulares (Regex) para Limpeza de Texto
Data: 06/05/2026
Objetivo: Aprender a usar padrões regex para identificar, extrair e limpar dados textuais
"""

import pandas as pd
import numpy as np
import re

# ==========================================
# 1. O QUE SÃO EXPRESSÕES REGULARES?
# ==========================================

print("="*50)
print("1. O QUE SÃO EXPRESSÕES REGULARES?")
print("="*50)

"""
EXPRESSÕES REGULARES (REGEX): são padrões usados para encontrar, extrair ou substituir
partes específicas de texto.

Pense como um "ctrl+F" superpoderoso que entende padrões.

Exemplos de uso em dados:
- Validar emails (tem @ e .com?)
- Extrair números de telefone (11 99999-9999)
- Encontrar todas as datas em um texto
- Limpar caracteres especiais
- Padronizar CEPs, CPFs, placas
"""

# ==========================================
# 2. IMPORTANDO E PRIMEIROS PASSOS
# ==========================================

print("\n" + "="*50)
print("2. IMPORTANDO E PRIMEIROS PASSOS")
print("="*50)

"""
No Pandas, usamos métodos .str que aceitam regex:
- .str.contains()   # verifica se padrão existe
- .str.extract()    # extrai parte do texto
- .str.replace()    # substitui padrão
- .str.findall()    # encontra todas as ocorrências

Também podemos usar o módulo `re` do Python para testes rápidos.
"""

import re

# Teste rápido: encontrar dígitos em um texto
texto = "Pedro tem 25 anos e 3 gatos"
digitos = re.findall(r'\d+', texto)
print(f"Texto: {texto}")
print(f"Dígitos encontrados: {digitos}")

# ==========================================
# 3. PADRÕES BÁSICOS (O ALFABETO DO REGEX)
# ==========================================

print("\n" + "="*50)
print("3. PADRÕES BÁSICOS - O ALFABETO DO REGEX")
print("="*50)

"""
META-CHARACTERES (caracteres especiais):

| Padrão | Significado                        |Exemplo| Combina com |
|--------|------------------------------------|-------|-------------|
| \d     | dígito (0-9)                       | \d{2} | 42, 99      |
| \D     | NÃO dígito                         | \D+   | abc, !@#    |
| \w     | letra/dígito/_                     | \w{3} | aB1, x_y    |
| \W     | NÃO letra/dígito/_                 | \W+   | !@#, espaço |
| \s     | espaço (espaço, tab, quebra)       | \s    | ' ', '\n'   |
| \S     | NÃO espaço                         | \S+   | palavra,123 |
| .      | qualquer caractere (exceto quebra) | .{2}  | ab, 12, !@  |
| \.     | ponto literal                      | \.    | .           |
| \      | escape                             | \\@   | @ literal   |

QUANTIFICADORES (quantas vezes):

| Quantificador | Significado        | Exemplo                                   |
|---------------|--------------------|-------------------------------------------|
| *             | 0 ou mais vezes    | \d* (qualquer quantidade, inclusive zero) |
| +             | 1 ou mais vezes    | \d+ (pelo menos um dígito)                |
| ?             | 0 ou 1 vez         | \d? (zero ou um dígito)                   |
| {n}           | exatamente n vezes | \d{5} (5 dígitos)                         |
| {n,m}         | entre n e m vezes  | \d{2,4} (2 a 4 dígitos)                   |
"""

print("Exemplos práticos:")

padroes = [
    (r'\d', "dígito individual"),
    (r'\d{2}', "dois dígitos seguidos"),
    (r'\d+', "um ou mais dígitos"),
    (r'\w+', "palavra (letras/números/_)"),
    (r'\s', "espaço em branco"),
]

for padrao, descricao in padroes:
    resultado = re.findall(padrao, 'Olá 42, mundo 123!')
    print(f'  {padrao:8} ({descricao:30}) -> {resultado}')

# ==========================================
# 4. PADRÕES COMUNS PARA DADOS
# ==========================================

print("\n" + "="*50)
print("4. PADRÕES COMUNS PARA DADOS")
print("="*50)

"""
Padrões que você vai usar SEMANALMENTE:

| O que procurar                 | Padrão Regex            | Exemplo         |
|--------------------------------|-------------------------|-----------------|
| Números inteiros               | \d+                     | 42, 1000, 7     |
| Números decimais               | \d+\.\d+                | 25.99, 3.14     |
| Telefone (SP)                  | \(\d{2}\) \d{4,5}-\d{4} | (11) 99999-9999 |
| Email                          | \w+@\w+\.\w{2,3}        | ana@email.com   |
| Data DD/MM/AAAA                | \d{2}/\d{2}/\d{4}       | 25/12/2024      |
| CEP (Brasil)                   | \d{5}-\d{3}             | 01234-567       |
| Placa de carro (padrão antigo) | [A-Z]{3}-\d{4}          | ABC-1234        |
| Só letras                      | [A-Za-z]+               | ApenasLetras    |
| Só números                     | ^\d+$                   | 123456          |
"""

# Demonstrando alguns padrões
texto_exemplo = """
Contatos:
- Ana: ana@email.com, (11) 98765-4321
- Bruno: bruno@empresa.com.br, (21) 9876-5432
- Carlos: carlos@site.com, (31) 99999-8888

Datas: 15/01/2024 e 20/02/2024
CEP: 01234-567
Placa: ABC-1234
"""

print("Texto exemplo:")
print(texto_exemplo)

print("\n--- Extraindo emails ---")
emails = re.findall(r'\w+@\w+\.\w{2,3}(?:\.\w{2})?', texto_exemplo)
print(f"Emails encontrados: {emails}")

print("\n--- Extraindo telefones ---")
telefones = re.findall(r'\(\d{2}\) \d{4,5}-\d{4}', texto_exemplo)
print(f"Telefones encontrados: {telefones}")

print("\n--- Extraindo datas ---")
datas = re.findall(r'\d{2}/\d{2}/\d{4}', texto_exemplo)
print(f"Datas encontradas: {datas}")

# ==========================================
# 5. GRUPOS E CAPTURA COM parenteses ()
# ==========================================

print("\n" + "="*50)
print("5. GRUPOS DE CAPTURA - PARENTESES ()")
print("="*50)

"""
Parênteses () servem para:
1. Agrupar partes do padrão
2. Capturar partes específicas (extrair só o que interessa)
"""

# Exemplo: extrair DDD e número separadamente
telefone = "(11) 98765-4321"
padrao_telefone = r'\((\d{2})\) (\d{4,5})-(\d{4})'

match = re.search(padrao_telefone, telefone)

if match:
    print(f"Telefone: {telefone}")
    print(f"  DDD: {match.group(1)}")
    print(f"  Parte1: {match.group(2)}")
    print(f"  Parte2: {match.group(3)}")
    print(f"  Completo: {match.group(0)}")

# No Pandas, .str.extract() usa grupos para criar colunas
df_telefones = pd.DataFrame({
    'telefone': ['(11) 98765-4321', '(21) 9876-5432', '(31) 99999-8888']
})

print("\n--- Usando .str.extract() no Pandas ---")
print(df_telefones)

df_telefones[['ddd', 'numero']] = df_telefones['telefone'].str.extract(r'\((\d{2})\) (\d{4,5}-\d{4})')
print("\nApós extração:")
print(df_telefones)

# ==========================================
# 6. FUNÇÕES DO MÓDULO re (PARA TESTES)
# ==========================================

print("\n" + "="*50)
print("6. FUNÇÕES DO MÓDULO re")
print("="*50)

"""
Principais funções do módulo `re`:

| Função                            | O que faz                           | Retorna        |
|-----------------------------------|-------------------------------------|----------------|
| re.findall(padrao, texto)         | Encontra todas as ocorrências       | Lista          |
| re.search(padrao, texto)          | Encontra a primeira ocorrência      | Match object   |
| re.match(padrao, texto)           | Verifica se texto COMEÇA com padrão | Match object   |
| re.sub(padrao, substituto, texto) | Substitui padrões                   | String         |
| re.compile(padrao)                | Compila padrão para reuso           | Pattern object |
"""

texto_teste = "Valor: R$ 1.234,56"

# re.findall - encontra todos
numeros = re.findall(r'\d+', texto_teste)
print(f"re.findall('\\d+', '{texto_teste}') -> {numeros}")

# re.sub - substitui
texto_limpo = re.sub(r'[^0-9,]', '', texto_teste)  # remove tudo exceto números e vírgula
print(f"re.sub('[^0-9,]', '', '{texto_teste}') -> '{texto_limpo}'")

# ==========================================
# 7. EXEMPLOS PRÁTICOS NO PANDAS
# ==========================================

print("\n" + "="*50)
print("7. EXEMPLOS PRÁTICOS NO PANDAS")
print("="*50)

# Criando DataFrame sujo
df_sujo = pd.DataFrame({
    'produto': ['Camiseta - AZUL - M', 'Calça Jeans - PRETA - G', 'Tênis - BRANCO - 42'],
    'preco': ['R$ 49,90', '129.90', 'R$ 199,00'],
    'codigo': ['PROD-001', 'PROD-002', 'xpto-003'],
    'descricao': [
        'Produto novo, lacrado. Entrega rápida!',
        'Usado, como novo. 6 meses de uso',
        'Produto com defeito na caixa'
    ]
})

print("DataFrame sujo:")
print(df_sujo.to_string())

# 7.1 Extrair cor do produto (palavra após o traço, antes do último traço)
print("\n--- Extraindo cor do produto ---")
df_sujo['cor'] = df_sujo['produto'].str.extract(r'- (\w+) -')
print(df_sujo[['produto', 'cor']])

# 7.2 Extrair tamanho/tamanho
print("\n--- Extraindo tamanho do produto ---")
df_sujo['tamanho'] = df_sujo['produto'].str.extract(r'- (\w+)$')
print(df_sujo[['produto', 'tamanho']])

# 7.3 Limpar preço (extrair apenas números)
print("\n--- Limpando preço (remover R$ e converter) ---")
df_sujo['preco_limpo'] = df_sujo['preco'].str.replace(r'[^0-9,\-\.]', '', regex=True)
df_sujo['preco_limpo'] = df_sujo['preco_limpo'].str.replace(',', '.')
df_sujo['preco_limpo'] = pd.to_numeric(df_sujo['preco_limpo'], errors='coerce')
print(df_sujo[['preco', 'preco_limpo']])

# 7.4 Extrair código numérico (após o hífen)
print("\n--- Extraindo número do código ---")
df_sujo['codigo_num'] = df_sujo['codigo'].str.extract(r'(\d+)$')
print(df_sujo[['codigo', 'codigo_num']])

# 7.5 Verificar se descrição contém palavras-chave
print("\n--- Classificando descrição ---")
df_sujo['tem_lacrado'] = df_sujo['descricao'].str.contains(r'lacrado|novo', case=False, na=False)
df_sujo['tem_defeito'] = df_sujo['descricao'].str.contains(r'defeito|problema', case=False, na=False)
print(df_sujo[['descricao', 'tem_lacrado', 'tem_defeito']])

# ==========================================
# 8. LIMPEZA AVANÇADA COM REGEX
# ==========================================

print("\n" + "="*50)
print("8. LIMPEZA AVANÇADA COM REGEX")
print("="*50)

df_limpeza = pd.DataFrame({
    'texto_sujo': [
        '  Telefone: (11) 99999-8888  ',
        'Email: ana.silva@empresa.com.br',
        'Valor: R$ 1.234,56',
        'Data: 25/12/2024',
        '### PRODUTO XYZ ###'
    ]
})

print("Texto original:")
print(df_limpeza)

# 8.1 Remover espaços extras (início e fim)
df_limpeza['texto'] = df_limpeza['texto_sujo'].str.strip()
print("\n1. Após .strip():")
print(df_limpeza['texto'])

# 8.2 Remover prefixos indesejados
df_limpeza['texto'] = df_limpeza['texto'].str.replace(r'^(Telefone:|Email:|Valor:|Data:|###\s*|\s*###)', '', regex=True)
print("\n2. Após remover prefixos:")
print(df_limpeza['texto'])

# 8.3 Remover caracteres especiais (manter letras, números, espaço e alguns símbolos úteis)
df_limpeza['texto'] = df_limpeza['texto'].str.replace(r'[^a-zA-Z0-9\s\.@/:-]', ' ', regex=True)
print("\n3. Após remover caracteres especiais:")
print(df_limpeza['texto'])

# 8.4 Substituir múltiplos espaços por um único
df_limpeza['texto'] = df_limpeza['texto'].str.replace(r'\s+', ' ', regex=True)
print("\n4. Após normalizar espaços (fim):")
print(df_limpeza['texto'])

# ==========================================
# 9. REFERÊNCIA RÁPIDA DE REGEX
# ==========================================

print("\n" + "="*50)
print("9. REFERÊNCIA RÁPIDA - REGEX")
print("="*50)

"""
REFERÊNCIA COMPLETA:

[CARACTERES]
\d  → dígito (0-9)
\D  → NÃO dígito
\w  → letra, número ou _ (alfanumérico + underscore)
\W  → NÃO alfanumérico
\s  → espaço, tab, quebra de linha
\S  → NÃO espaço
.   → qualquer caractere (exceto quebra de linha)
\   → escape (ex: \. para ponto literal)

[QUANTIFICADORES]
*   → 0 ou mais
+   → 1 ou mais
?   → 0 ou 1
{n} → exatamente n
{n,} → n ou mais
{n,m} → entre n e m

[ÂNCORAS]
^   → início do texto
$   → fim do texto
\b  → borda de palavra

[GRUPOS]
()  → grupo de captura
(?:) → grupo NÃO capturado (agrupa sem extrair)

[EXEMPLOS PRÁTICOS]
- Emails: \w+@\w+\.\w{2,3}(?:\.\w{2})?
- Telefone: \(\d{2}\) \d{4,5}-\d{4}
- CPF: \d{3}\.\d{3}\.\d{3}-\d{2}
- CEP: \d{5}-\d{3}
- Placa (antiga): [A-Z]{3}-\d{4}
- Data (DD/MM/AAAA): \d{2}/\d{2}/\d{4}
- Número decimal: \d+,\d{2} ou \d+\.\d{2}
- Só letras: ^[A-Za-z]+$
- Só números: ^\d+$
- URL: https?://[\w\-\.]+\.\w{2,3}/?\S*
"""

# ==========================================
# 10. RESUMO DA AULA
# ==========================================

print("\n" + "="*50)
print("10. RESUMO DA AULA")
print("="*50)

"""
✅ PADRÕES BÁSICOS:
   - \d, \w, \s, . 
   - +, *, ?, {n}, {n,m}

✅ MÉTODOS NO PANDAS:
   - str.contains(padrao, regex=True)
   - str.extract(padrao)  # precisa de grupos ()
   - str.replace(padrao, substituto, regex=True)

✅ MÓDULO re (para testes):
   - re.findall(padrao, texto)
   - re.search(padrao, texto)
   - re.sub(padrao, substituto, texto)

✅ DICAS IMPORTANTES:
   1. Sempre use r'padrao' (raw string) para evitar escapes duplicados
   2. Teste padrões no regex101.com antes de implementar
   3. Comece simples, depois vá adicionando complexidade
   4. Use grupos () para extrair partes específicas
"""

# ==========================================
# EXERCÍCIOS - AULA 3
# ==========================================

print("\n" + "="*50)
print("EXERCÍCIOS - EXPRESSÕES REGULARES")
print("="*50)

# Dados para todos os exercícios
np.random.seed(42)

df_dados_sujos = pd.DataFrame({
    'id': [101, 102, 103, 104, 105],
    'cliente': [
        'Ana Silva (ana@email.com) - (11) 98765-4321',
        'Bruno Santos - bruno@empresa.com - (21) 9876-5432',
        'Carla Souza - carla@site.com.br - Contato: (31) 99999-8888',
        'Daniel Lima - daniel@email.com | Telefone (11) 1234-5678',
        'Elisa Ferreira (elisa@co.com) - Tel: (11) 91234-5678'
    ],
    'produto': [
        'CAMISETA - AZUL - M',
        'CALÇA - PRETA - G',
        'TENIS - BRANCO - 42',
        'BOLSA - MARROM - ÚNICO',
        'RELÓGIO - PRETO - M'
    ],
    'valor': [
        'R$ 49,90',
        '129.90',
        'R$ 199,00',
        'R$ 89.90',
        'R$ 299,00'
    ],
    'data': [
        '2024-01-15',
        '15/02/2024',
        '2024-03-20',
        '20/04/2024',
        '2024-05-10'
    ]
})

# print("DataFrame para exercícios:")
# print(df_dados_sujos.to_string())

# Adicionar algumas inconsistências
df_dados_sujos.loc[2, 'valor'] = '199,00'  # sem R$
df_dados_sujos.loc[4, 'data'] = '10/05/2024'  # formato diferente

########################################################################
# NÍVEL 1-3: Aquecimento
########################################################################

"""
1. Encontrando padrões básicos

# Usando o módulo re, encontre no texto abaixo:
# - Todos os dígitos
# - Todas as palavras (sequências de letras)
# - Todos os caracteres que NÃO são dígitos
"""

"""
texto_ex1 = "O código PROD-42 custa R$ 199.90. Estoque: 25 unidades."

todos_digitos = re.findall(r'\d+', texto_ex1)
print(f'Todos os dígitos: {todos_digitos}')

todas_palavras = re.findall(r'[a-zA-ZÀ-ÿ]+', texto_ex1)
print(f'Todas as palavras: {todas_palavras}')

todos_caracteres_ndigitos = re.findall(r'\D', texto_ex1)
print(f'Todos os caracteres que NÃO são dígitos: {todos_caracteres_ndigitos}')
"""

########################################################################

"""
2. Extraindo emails

# Do DataFrame df_dados_sujos, extraia o email de cada cliente
# Use .str.extract() com um padrão regex
# Crie uma nova coluna 'email'
"""
"""
df = df_dados_sujos.copy()
print(df.to_string())

padrao_email = r'(\w+@[\w\.]+\.\w+(?:\.\w+)?)' # separar assim é boas práticas?

df['email'] = df['cliente'].str.extract(padrao_email)

print(df[['cliente', 'email']].to_string())
"""

########################################################################

"""
3. Extraindo telefones

# Do DataFrame df_dados_sujos, extraia o telefone de cada cliente
# Considere padrões como (11) 98765-4321 ou (11) 9876-5432
# Crie uma nova coluna 'telefone'
"""

"""
df = df_dados_sujos.copy()

padrao_telefone = r'(\(\d+\) \d{4,5}\-\d{4})'

df['telefone'] = df['cliente'].str.extract(padrao_telefone)

print(df[['cliente', 'telefone']].to_string())
"""

########################################################################
# NÍVEL 4-6: Aplicação
########################################################################

"""
4. Extraindo dados do produto

# A coluna 'produto' está no formato "NOME - COR - TAMANHO"
# Use .str.extract() com grupos para criar três novas colunas:
# - 'nome_produto'
# - 'cor_produto' 
# - 'tamanho_produto'
"""

"""
df = df_dados_sujos.copy()

print(df['produto'])

regex_nome_produto = r'(^\w+)'
df['nome_produto'] = df['produto'].str.strip().str.extract(regex_nome_produto)

regex_cor_produto = r'\- (\w+) \-'
df['cor_produto'] = df['produto'].str.extract(regex_cor_produto)

regex_tamanho_produto = r'(\w+$)'
df['tamanho_produto'] = df['produto'].str.strip().str.extract(regex_tamanho_produto)

print(df.to_string())
"""

########################################################################

"""
5. Limpando valores monetários

# A coluna 'valor' tem formatos inconsistentes:
# - "R$ 49,90"
# - "129.90" 
# - "R$ 199,00"
# - "199,00"
#
# Crie uma função para:
# 1. Remover "R$ " se existir
# 2. Substituir vírgula por ponto
# 3. Converter para float
# 
# Crie uma nova coluna 'valor_limpo' com os valores numéricos
"""

"""
df = df_dados_sujos.copy()

def limpar_valor(df):
    df['valor_limpo'] = pd.to_numeric(df['valor'].replace(r'^R\$ ', '', regex=True).replace(r',', '.', regex=True))
    return df

df_limpo = limpar_valor(df)

print(df_limpo.to_string())
"""

########################################################################

"""
6. Padronizando datas

# A coluna 'data' tem dois formatos:
# - "2024-01-15" (YYYY-MM-DD)
# - "15/02/2024" (DD/MM/YYYY)
#
# Padronize todas para o formato YYYY-MM-DD
# Dica: use .str.extract() com grupos e depois reorganize
"""

"""
df = df_dados_sujos.copy()

print(df['data'])

regex_data = r'(^\d{2})/(\d{2})/(\d{4})'

df[['dia', 'mes', 'ano']] = df['data'].str.extract(regex_data)

df['data_limpa'] = df['ano'] + '-' + df['mes'] + '-' + df['dia']
df['data_limpa'] = df['data_limpa'].fillna(df['data'])

print(df[['data', 'data_limpa']].to_string())
"""

########################################################################
# NÍVEL 7-8: Manipulação
########################################################################

"""
7. Validação de padrões

# Crie um relatório que verifique:
# - Quantos emails são válidos (contêm @ e .)
# - Quantos telefones estão no formato correto (com DDD e hífen)
# - Quantos valores foram convertidos com sucesso (não ficaram NaN)
#
# Mostre os resultados com print()
"""

"""
df = df_dados_sujos.copy()

regex_email = r'(\w+@[\w\.]+\.\w+(?:\.\w+)?)'
df['email'] = df['cliente'].str.extract(regex_email)
email_mask = (df['email'].str.contains('\@')) & (df['email'].str.contains('\.'))
print(f'Quantos email são válidos: {df['email'][email_mask].count()}')

regex_telefone = r'(\(\d+\) \d{4,5}\-\d{4})'
df['telefone'] = df['cliente'].str.extract(regex_telefone)
telefone_mask = (df['telefone'].str.contains('\(')) & (df['telefone'].str.contains('\)')) & (df['telefone'].str.contains('-'))
print(f'Quantos telefones estão no formato correto: {df['telefone'][telefone_mask].count()}')

print(f'Quantos valores foram convertidos com sucesso: {df['telefone'].count()+df['email'].count()}')
"""

########################################################################
# NÍVEL 9-10: Desafios
########################################################################

"""
9. Dashboard de qualidade com regex

# Crie um relatório completo de qualidade textual para o df_dados_sujos
# O relatório deve incluir para CADA coluna:
# - Contagem de valores nulos
# - Contagem de valores que seguem o padrão esperado
# - Sugestão de correção
#
# Colunas e seus padrões:
# - cliente: deve ter nome + email + telefone
# - produto: deve ter "NOME - COR - TAMANHO"
# - valor: deve ser R$ ###,##
# - data: deve ser YYYY-MM-DD ou DD/MM/YYYY
"""

"""
print(f'Coluna "Cliente": ')
print(f'Contagem de valores nulos: {df_dados_sujos['cliente'].isnull().sum().sum()}')

regex_nome = r'^[a-zA-ZÀ-ÿ\s]'
regex_email = r'(\w+@[\w\.]+\.\w+(?:\.\w+)?)'
regex_telefone = r'(\(\d+\) \d{4,5}\-\d{4})'

cliente_mask = (
        df_dados_sujos['cliente'].str.contains(regex_nome) &
        (df_dados_sujos['cliente'].str.contains(regex_email)) &
        (df_dados_sujos['cliente'].str.contains(regex_telefone))
)

print(f'Contagem de valores que seguem o padrão esperado: {df_dados_sujos['cliente'][cliente_mask].count()}')
print()

print(f'Coluna "Produto": ')
print(f'Contagem de valores nulos: {df_dados_sujos['produto'].isnull().sum().sum()}')

regex_nome_produto = r'(^\w+)'
regex_cor_produto = r'\- (\w+) \-'
regex_tamanho_produto = r'(\w+$)'

produto_mask = (
    (df_dados_sujos['produto'].str.contains(regex_nome_produto)) &
    (df_dados_sujos['produto'].str.contains(regex_cor_produto)) &
    (df_dados_sujos['produto'].str.contains(regex_tamanho_produto))
)
print(f'Contagem de valores que seguem o padrão esperado: {df_dados_sujos['produto'][produto_mask].count()}')
print()

print(f'Coluna "Valor": ')
print(f'Contagem de valores nulos: {df_dados_sujos['valor'].isnull().sum().sum()}')
regex_valor = r'(R\$ \d{3},\d{2})' # n entendi pq vc pediu nesse formato, mas fiz exatamente como vc pediu. Poderiamos ter feito com . tbm e fazer um OU na mascara
valor_mask = df_dados_sujos['valor'].str.contains(regex_valor)
print(f'Contagem de valores que seguem o padrão esperado: {df_dados_sujos['valor'][valor_mask].count()}')
print()

print(f'Coluna "Data": ')
print(f'Contagem de valores nulos: {df_dados_sujos['data'].isnull().sum().sum()}')
regex_data1 = r'(\d{4}\-\d{2}\-\d{2})'
regex_data2 = r'(\d{2}/\d{2}/\d{4})'
data_mask = (
    (df_dados_sujos['data'].str.contains(regex_data1)) |
    (df_dados_sujos['data'].str.contains(regex_data2))
)
print(f'Contagem de valores que seguem o padrão esperado: {df_dados_sujos['data'][data_mask].count()}')
print()
"""

########################################################################

"""
10. DESAFIO FINAL: Pipeline completa

# Crie uma função pipeline_regex(df) que:
# 1. Extrai email, telefone da coluna 'cliente'
# 2. Extrai nome, cor, tamanho da coluna 'produto'
# 3. Limpa e converte 'valor' para float
# 4. Padroniza 'data' para datetime
# 5. Remove colunas originais (opcional)
# 6. Retorna DataFrame limpo E dicionário com transformações
#
# Teste no df_dados_sujos
"""


def pipeline_regex(df_sujo):

    df = df_sujo.copy()

    regex_nome = r'(^[a-zA-ZÀ-ÿ\s]+)'
    df['nome'] = df['cliente'].str.extract(regex_nome)

    regex_email = r'(\w+@[\w\.]+\.\w+(?:\.\w+)?)'
    df['email'] = df['cliente'].str.extract(regex_email)

    regex_telefone = r'(\(\d+\) \d{4,5}\-\d{4})'
    df['telefone'] = df['cliente'].str.extract(regex_telefone)

    regex_nome_produto = r'(^\w+)'
    df['nome_produto'] = df['produto'].str.strip().str.extract(regex_nome_produto)

    regex_cor_produto = r'\- (\w+) \-'
    df['cor_produto'] = df['produto'].str.extract(regex_cor_produto)

    regex_tamanho_produto = r'(\w+$)'
    df['tamanho_produto'] = df['produto'].str.strip().str.extract(regex_tamanho_produto)

    df['valor_limpo'] = pd.to_numeric(df['valor'].replace(r'^R\$ ', '', regex=True).replace(r',', '.', regex=True))

    regex_data = r'(^\d{2})/(\d{2})/(\d{4})'
    df[['dia', 'mes', 'ano']] = df['data'].str.extract(regex_data)
    df['data_limpa'] = df['ano'] + '-' + df['mes'] + '-' + df['dia']
    df['data_limpa'] = df['data_limpa'].fillna(df['data'])

    df = df[['nome', 'email', 'telefone', 'nome_produto', 'cor_produto', 'tamanho_produto', 'valor_limpo', 'data_limpa']]

    df = df.rename(columns={
        'nome': 'cliente',
        'valor_limpo': 'valor',
        'data_limpa': 'data'
    })

    return df

df_limpo = pipeline_regex(df_dados_sujos)

print(df_limpo.to_string())

# prontinho! fiquei feliz com o resultado. Não fiz o relatório pq precisei correr pra almoçar!