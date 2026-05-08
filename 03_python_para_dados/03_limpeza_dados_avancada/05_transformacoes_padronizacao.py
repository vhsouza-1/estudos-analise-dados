"""
Bloco 3: Python para Dados
Módulo 3: Limpeza de Dados Avançada
Aula 5: Transformações e Padronização
Data: 08/05/2026
Objetivo: Aprender a transformar, criar e padronizar colunas em DataFrames
"""

import pandas as pd
import numpy as np

# ==========================================
# 1. O QUE SÃO TRANSFORMAÇÕES?
# ==========================================

print("="*50)
print("1. O QUE SÃO TRANSFORMAÇÕES?")
print("="*50)

"""
TRANSFORMAÇÕES são operações que criam novas colunas ou modificam as existentes.

Exemplos comuns:
1. Criar 'valor_total' a partir de 'quantidade' * 'preco'
2. Categorizar idades (jovem, adulto, idoso)
3. Normalizar valores (colocar na escala 0-1)
4. Aplicar uma função a cada elemento
5. Mapear códigos para nomes (1 → 'Masculino')
6. Substituir valores com base em condições

Nesta aula vamos aprender TODAS essas técnicas.
"""

# Dados de exemplo
df_vendas = pd.DataFrame({
    'produto': ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C'],
    'quantidade': [10, 5, 8, 12, 6, 7, 9, 4, 11],
    'preco': [100, 200, 150, 105, 198, 155, 97, 202, 148],
    'categoria': ['eletro', 'moveis', 'eletro', 'eletro', 'moveis', 'eletro', 'eletro', 'moveis', 'eletro'],
    'status': ['APROVADO', 'pendente', 'APROVADO', 'reprovado', 'APROVADO', 'PENDENTE', 'aprovado', 'Reprovado', 'APROVADO']
})

print("DataFrame de exemplo:")
print(df_vendas)

# ==========================================
# 2. OPERAÇÕES ARITMÉTICAS ENTRE COLUNAS
# ==========================================

print("\n" + "="*50)
print("2. OPERAÇÕES ARITMÉTICAS ENTRE COLUNAS")
print("="*50)

# 2.1 Criando coluna a partir de operação simples
print("--- Criando 'valor_total' (quantidade * preco) ---")
df_vendas['valor_total'] = df_vendas['quantidade'] * df_vendas['preco']
print(df_vendas[['produto', 'quantidade', 'preco', 'valor_total']])

# 2.2 Múltiplas operações
print("\n--- Criando 'lucro_estimado' (valor_total * 0.3) e 'com_imposto' (valor_total * 1.1) ---")
df_vendas['lucro_estimado'] = df_vendas['valor_total'] * 0.3
df_vendas['com_imposto'] = df_vendas['valor_total'] * 1.1
print(df_vendas[['produto', 'valor_total', 'lucro_estimado', 'com_imposto']])

# ==========================================
# 3. TRANSFORMAÇÕES COM .apply()
# ==========================================

print("\n" + "="*50)
print("3. TRANSFORMAÇÕES COM .apply()")
print("="*50)

"""
.apply() aplica uma função a cada elemento (ou linha/coluna) do DataFrame.

Quando usar:
- Quando a transformação é complexa (não dá para fazer com operação simples)
- Quando você precisa de lógica condicional
- Quando você quer usar funções Python puras
"""

# 3.1 apply em uma coluna (elemento a elemento)
print("--- .apply() em uma coluna (deixando status padronizado) ---")

def padronizar_status(status):
    status = str(status).lower().strip()
    if status in ['aprovado', 'aprovada']:
        return 'Aprovado'
    elif status in ['reprovado', 'reprovada']:
        return 'Reprovado'
    elif status in ['pendente', 'pendent']:
        return 'Pendente'
    else:
        return 'Desconhecido'

df_vendas['status_pad'] = df_vendas['status'].apply(padronizar_status)
print(df_vendas[['status', 'status_pad']])

# 3.2 apply com lambda (função de uma linha)
print("\n--- Usando lambda para criar coluna de desconto ---")
df_vendas['desconto'] = df_vendas['valor_total'].apply(lambda x: x * 0.1 if x > 1000 else x * 0.05)
print(df_vendas[['valor_total', 'desconto']])

# 3.3 apply com múltiplas colunas (axis=1)
print("\n--- .apply() em múltiplas colunas (criando categoria de preço) ---")

def classificar_produto(row):
    if row['quantidade'] > 10 and row['preco'] > 150:
        return 'Premium'
    elif row['quantidade'] > 10 or row['preco'] > 150:
        return 'Destaque'
    else:
        return 'Regular'

df_vendas['classificacao'] = df_vendas.apply(classificar_produto, axis=1)
print(df_vendas[['quantidade', 'preco', 'classificacao']])

# ==========================================
# 4. TRANSFORMAÇÕES COM .map()
# ==========================================

print("\n" + "="*50)
print("4. TRANSFORMAÇÕES COM .map()")
print("="*50)

"""
.map() é usado para:
- Mapear valores de um dicionário (código → significado)
- É mais RÁPIDO que .apply() para mapeamentos simples
- Ideal para substituir valores categóricos
"""

# 4.1 Mapeamento de categorias
print("--- Mapeando categorias abreviadas para nomes completos ---")
categoria_map = {
    'eletro': 'Eletrônicos',
    'moveis': 'Móveis'
}
df_vendas['categoria_completa'] = df_vendas['categoria'].map(categoria_map)
print(df_vendas[['categoria', 'categoria_completa']])

# 4.2 Mapeamento com fallback (valores não encontrados viram NaN)
print("\n--- Mapeamento com fallback (preenchendo NaN depois) ---")
df_vendas['categoria_completa'] = df_vendas['categoria'].map(categoria_map).fillna('Outros')
print(df_vendas[['categoria', 'categoria_completa']])

# 4.3 Mapeamento para códigos numéricos
print("\n--- Mapeando status para códigos numéricos ---")
status_codigo = {
    'Aprovado': 1,
    'Pendente': 2,
    'Reprovado': 3
}
df_vendas['status_codigo'] = df_vendas['status_pad'].map(status_codigo)
print(df_vendas[['status_pad', 'status_codigo']])

# ==========================================
# 5. TRANSFORMAÇÕES COM .replace()
# ==========================================

print("\n" + "="*50)
print("5. TRANSFORMAÇÕES COM .replace()")
print("="*50)

"""
.replace() é ideal para:
- Substituir valores específicos
- Corrigir erros pontuais
- Funciona em DataFrames inteiros ou colunas específicas
"""

df_replace_exemplo = pd.DataFrame({
    'produto': ['A', 'B', 'C', 'A', 'B', 'C'],
    'status': ['aprovado', 'pendente', 'reprovado', 'APROVADO', 'PENDENTE', 'REPROVADO'],
    'valor': [100, -999, 200, 150, -1, 250]
})

print("DataFrame para replace:")
print(df_replace_exemplo)

# 5.1 Replace simples em uma coluna
print("\n--- Substituindo valores negativos por NaN ---")
df_replace_exemplo['valor_limpo'] = df_replace_exemplo['valor'].replace([-999, -1], np.nan)
print(df_replace_exemplo[['valor', 'valor_limpo']])

# 5.2 Replace com dicionário (múltiplos valores)
print("\n--- Padronizando status com replace ---")
status_map = {
    'aprovado': 'Aprovado',
    'APROVADO': 'Aprovado',
    'pendente': 'Pendente',
    'PENDENTE': 'Pendente',
    'reprovado': 'Reprovado',
    'REPROVADO': 'Reprovado'
}
df_replace_exemplo['status_pad'] = df_replace_exemplo['status'].replace(status_map)
print(df_replace_exemplo[['status', 'status_pad']])

# 5.3 Replace em todo o DataFrame
print("\n--- Replace em todo DataFrame (removendo caracteres especiais) ---")
df_caracteres = pd.DataFrame({
    'nome': ['João!', 'Maria@', 'Pedro#'],
    'cidade': ['São Paulo$', 'Rio%', 'Belo&']
})

print("Antes:")
print(df_caracteres)

print("\nDepois (removendo !@#$%&):")
df_caracteres_limpo = df_caracteres.replace(r'[!@#$%&]', '', regex=True)
print(df_caracteres_limpo)

# ==========================================
# 6. CRIAÇÃO DE CATEGORIAS (BINNING)
# ==========================================

print("\n" + "="*50)
print("6. CRIAÇÃO DE CATEGORIAS - pd.cut() e pd.qcut()")
print("="*50)

"""
Binning = agrupar valores contínuos em categorias.

- pd.cut(): divide com BASE NOS VALORES (ex: 0-10, 11-20, 21-30)
- pd.qcut(): divide com BASE NA FREQUÊNCIA (mesmo número de elementos por categoria)
"""

df_idades = pd.DataFrame({
    'nome': ['Ana', 'Bruno', 'Carlos', 'Daniela', 'Eduardo', 'Fernanda', 'Gabriel', 'Helena'],
    'idade': [15, 22, 35, 42, 18, 55, 28, 65],
    'salario': [1200, 2500, 4800, 5200, 1900, 6800, 3200, 8500]
})

print("Dados para categorização:")
print(df_idades)

# 6.1 pd.cut() - categorias baseadas em valores
print("\n--- pd.cut() - Faixas etárias (baseado nos valores) ---")
faixas_etarias = [0, 18, 30, 50, 100]
rotulos = ['Menor', 'Jovem Adulto', 'Adulto', 'Idoso']

df_idades['faixa_etaria'] = pd.cut(df_idades['idade'], bins=faixas_etarias, labels=rotulos)
print(df_idades[['idade', 'faixa_etaria']])

# 6.2 pd.cut() com número de bins automático
print("\n--- pd.cut() com 4 bins automáticos ---")
df_idades['faixa_salario_auto'] = pd.cut(df_idades['salario'], bins=4)
print(df_idades[['salario', 'faixa_salario_auto']])

# 6.3 pd.qcut() - categorias baseadas em quantis (mesmo número por categoria)
print("\n--- pd.qcut() - Quartis de salário (mesmo número de pessoas por categoria) ---")
df_idades['quartil_salario'] = pd.qcut(df_idades['salario'], q=4, labels=['1º Quartil', '2º Quartil', '3º Quartil', '4º Quartil'])
print(df_idades[['salario', 'quartil_salario']])
print(f"\nContagem por quartil:\n{df_idades['quartil_salario'].value_counts()}")

# ==========================================
# 7. NORMALIZAÇÃO E PADRONIZAÇÃO
# ==========================================

print("\n" + "="*50)
print("7. NORMALIZAÇÃO E PADRONIZAÇÃO")
print("="*50)

"""
NORMALIZAÇÃO: colocar dados em escala 0-1 (ou -1 a 1)
Fórmula: (x - min) / (max - min)

PADRONIZAÇÃO: transformar para média 0 e desvio 1 (escala Z)
Fórmula: (x - média) / desvio

Quando usar cada?
- Normalização: quando você precisa de limites fixos (ex: 0-1)
- Padronização: quando dados têm outliers e você quer distribuição normal
"""

df_numeros = pd.DataFrame({
    'produto': ['A', 'B', 'C', 'D', 'E'],
    'vendas': [100, 200, 300, 400, 500],
    'preco': [10, 20, 30, 40, 50]
})

print("Dados originais:")
print(df_numeros)

# 7.1 Normalização (min-max)
print("\n--- Normalização (escala 0-1) ---")
df_numeros['vendas_norm'] = (df_numeros['vendas'] - df_numeros['vendas'].min()) / (df_numeros['vendas'].max() - df_numeros['vendas'].min())
df_numeros['preco_norm'] = (df_numeros['preco'] - df_numeros['preco'].min()) / (df_numeros['preco'].max() - df_numeros['preco'].min())
print(df_numeros[['vendas', 'vendas_norm', 'preco', 'preco_norm']])

# 7.2 Padronização (Z-score)
print("\n--- Padronização (Z-score - média 0, desvio 1) ---")
df_numeros['vendas_z'] = (df_numeros['vendas'] - df_numeros['vendas'].mean()) / df_numeros['vendas'].std()
df_numeros['preco_z'] = (df_numeros['preco'] - df_numeros['preco'].mean()) / df_numeros['preco'].std()
print(df_numeros[['vendas', 'vendas_z', 'preco', 'preco_z']])
print(f"\nMédia do Z-score (deveria ser ~0): {df_numeros['vendas_z'].mean():.10f}")
print(f"Desvio do Z-score (deveria ser 1): {df_numeros['vendas_z'].std():.2f}")

# 7.3 Normalização com .apply() (alternativa)
print("\n--- Normalização com .apply() (mais elegante) ---")

def normalizar(serie):
    return (serie - serie.min()) / (serie.max() - serie.min())

df_numeros['vendas_norm2'] = normalizar(df_numeros['vendas'])
df_numeros['preco_norm2'] = normalizar(df_numeros['preco'])
print(df_numeros[['vendas', 'vendas_norm2', 'preco', 'preco_norm2']])

# ==========================================
# 8. TRANSFORMAÇÕES CONDICIONAIS COM np.where()
# ==========================================

print("\n" + "="*50)
print("8. TRANSFORMAÇÕES CONDICIONAIS COM np.where()")
print("="*50)

"""
np.where() é como um IF-ELSE vetorizado.
Sintaxe: np.where(condicao, valor_se_true, valor_se_false)

É MAIS RÁPIDO que .apply() para condições simples.
"""

df_condicional = pd.DataFrame({
    'produto': ['A', 'B', 'C', 'D', 'E'],
    'vendas': [50, 150, 250, 350, 450],
    'estoque': [100, 80, 120, 40, 200]
})

print("Dados originais:")
print(df_condicional)

# 8.1 Condição simples
print("\n--- np.where() - Classificando por desempenho ---")
df_condicional['desempenho'] = np.where(df_condicional['vendas'] > 200, 'Alto', 'Baixo')
print(df_condicional[['vendas', 'desempenho']])

# 8.2 Condição com múltiplas opções (aninhada)
print("\n--- np.where() aninhado - Múltiplas classificações ---")
df_condicional['classificacao'] = np.where(
    df_condicional['vendas'] > 300,
    'Excelente',
    np.where(df_condicional['vendas'] > 200, 'Bom', 'Regular')
)
print(df_condicional[['vendas', 'classificacao']])

# 8.3 Condição combinando múltiplas colunas
print("\n--- np.where() com múltiplas condições ---")
df_condicional['repor_estoque'] = np.where(
    (df_condicional['estoque'] < 50) | (df_condicional['vendas'] > 300),
    'Repor',
    'OK'
)
print(df_condicional[['vendas', 'estoque', 'repor_estoque']])

# ==========================================
# 9. TRANSFORMAÇÕES COM .applymap() (DataFrame inteiro) # .applymap() caiu em desuso nas versões recentes. Só usar .map() mesmo
# ==========================================

print("\n" + "="*50)
print("9. TRANSFORMAÇÕES COM .applymap()")
print("="*50)

"""
.applymap() aplica uma função a CADA ELEMENTO do DataFrame inteiro.

Quando usar:
- Quando você quer transformar TODAS as células
- Exemplo: formatar todos os números para 2 casas decimais
- Exemplo: aplicar uma função de limpeza em todas as células de texto
"""

df_applymap = pd.DataFrame({
    'nome': ['  Ana  ', '  Bruno  ', '  Carlos  '],
    'cidade': ['  SP  ', '  RJ  ', '  BH  '],
    'valor': [100.567, 200.123, 300.789]
})

print("DataFrame original:")
print(df_applymap)

# 9.1 Limpando strings em todas as colunas de texto
print("\n--- .applymap() para limpar espaços em todas as strings ---")
df_limpo = df_applymap.map(lambda x: x.strip() if isinstance(x, str) else x)
print(df_limpo)

# 9.2 Formatando números
print("\n--- .applymap() para formatar números (2 casas decimais) ---")
df_formatado = df_applymap.map(lambda x: f"{x:.2f}" if isinstance(x, float) else x)
print(df_formatado)

# ==========================================
# 10. EXEMPLO PRÁTICO: PIPELINE COMPLETA
# ==========================================

print("\n" + "="*50)
print("10. EXEMPLO PRÁTICO - PIPELINE DE TRANSFORMAÇÕES")
print("="*50)

# Dataset realista com dados de clientes
df_clientes_transform = pd.DataFrame({
    'id_cliente': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'nome': ['  João Silva  ', 'MARIA SANTOS', 'Pedro  ', '  Ana Paula  ', 'JOSÉ', 'Carla', '  Roberto  ', 'Fernanda', 'Rafael', 'TATIANE'],
    'idade': [25, 32, 45, 28, 35, -5, 52, 38, 150, 29],
    'renda': [3000, 4000, 7000, 5000, 6000, -1000, 8000, 4500, 12000, 5500],
    'categoria': ['basic', 'premium', 'basic', 'gold', 'PREMIUM', 'gold', 'BASIC', 'platinum', 'Gold', 'basic'],
    'compras': [5, 12, 8, 15, 10, 0, 20, 7, 25, 9]
})

print("Dados brutos:")
print(df_clientes_transform)


def pipeline_transformacoes(df):
    df_limpo = df.copy()
    transformacoes = []

    # Passo 1: Limpar nomes (strip e title)
    df_limpo['nome'] = df_limpo['nome'].str.strip().str.title()
    transformacoes.append("Nomes padronizados (strip + title)")

    # Passo 2: Corrigir idades inconsistentes (negativas ou > 100)
    idade_invalida = (df_limpo['idade'] < 0) | (df_limpo['idade'] > 100)
    df_limpo.loc[idade_invalida, 'idade'] = df_limpo['idade'].median().round() # esqueceu de arredondar ou transofmrar em int
    transformacoes.append(f"Idades inválidas substituídas pela mediana ({df_limpo['idade'].median():.0f})")

    # Passo 3: Corrigir rendas negativas
    renda_negativa = df_limpo['renda'] < 0
    df_limpo.loc[renda_negativa, 'renda'] = df_limpo['renda'].median()
    transformacoes.append("Rendas negativas substituídas pela mediana")

    # Passo 4: Padronizar categorias (minúsculas + mapeamento)
    df_limpo['categoria'] = df_limpo['categoria'].str.lower()
    categoria_map = {
        'basic': 'Básico',
        'premium': 'Premium',
        'gold': 'Gold',
        'platinum': 'Platinum'
    }
    df_limpo['categoria'] = df_limpo['categoria'].map(categoria_map).fillna('Outro')
    transformacoes.append("Categorias padronizadas e mapeadas")

    # Passo 5: Criar nova coluna (estrato baseado em compras)
    def definir_estrato(compras):
        if compras >= 20:
            return 'VIP'
        elif compras >= 10:
            return 'Frequente'
        else:
            return 'Ocasional'

    df_limpo['estrato'] = df_limpo['compras'].apply(definir_estrato)
    transformacoes.append("Estrato de cliente criado (COM base em compras)")

    # Passo 6: Criar score combinado (renda + compras normalizados)
    renda_norm = (df_limpo['renda'] - df_limpo['renda'].min()) / (df_limpo['renda'].max() - df_limpo['renda'].min())
    compras_norm = (df_limpo['compras'] - df_limpo['compras'].min()) / (
                df_limpo['compras'].max() - df_limpo['compras'].min())
    df_limpo['score'] = (renda_norm + compras_norm) / 2
    transformacoes.append("Score combinado de renda e compras criado (0-1)")

    # Passo 7: np.where para classificação final
    df_limpo['priority'] = np.where(
        (df_limpo['categoria'] == 'Platinum') | (df_limpo['score'] > 0.8),
        'Alta Prioridade',
        np.where(df_limpo['score'] > 0.5, 'Média Prioridade', 'Baixa Prioridade')
    )
    transformacoes.append("Prioridade de atendimento definida")

    return df_limpo, transformacoes


# Aplicar pipeline
df_final, log_transformacoes = pipeline_transformacoes(df_clientes_transform)

print("\n" + "=" * 50)
print("RESULTADO APÓS TRANSFORMAÇÕES")
print("=" * 50)
print(df_final.to_string())

print("\n" + "=" * 50)
print("LOG DE TRANSFORMAÇÕES")
print("=" * 50)
for i, log in enumerate(log_transformacoes, 1):
    print(f"{i}. ✓ {log}")

# ==========================================
# 11. RESUMO DA AULA
# ==========================================

print("\n" + "="*50)
print("11. RESUMO DA AULA")
print("="*50)

"""
✅ OPERAÇÕES ARITMÉTICAS:
   - df['nova'] = df['col1'] + df['col2']
   - df['nova'] = df['col1'] * fator

✅ .apply() (funções complexas):
   - df['col'] = df['col'].apply(funcao)
   - df['nova'] = df.apply(funcao_linha, axis=1)

✅ .map() (mapeamento dicionário):
   - df['col'] = df['col'].map(dicionario)
   - df['col'] = df['col'].map(dicionario).fillna('Outros')

✅ .replace() (substituição de valores):
   - df['col'] = df['col'].replace(valor_antigo, valor_novo)
   - df['col'] = df['col'].replace(dicionario)

✅ CATEGORIZAÇÃO:
   - pd.cut(df['col'], bins=..., labels=...)  # baseado em valores
   - pd.qcut(df['col'], q=..., labels=...)    # baseado em frequência

✅ NORMALIZAÇÃO:
   - (df['col'] - df['col'].min()) / (df['col'].max() - df['col'].min())

✅ PADRONIZAÇÃO (Z-score):
   - (df['col'] - df['col'].mean()) / df['col'].std()

✅ np.where() (IF-ELSE vetorizado):
   - np.where(condicao, valor_true, valor_false)

✅ .applymap() (DataFrame inteiro):
   - df.applymap(funcao)  # aplica a cada elemento

📌 BOAS PRÁTICAS:
   1. Prefira operações vetorizadas (+, -, *, /) ao invés de .apply()
   2. Use .map() para mapeamentos simples (mais rápido)
   3. Use np.where() para condições simples (mais rápido que .apply())
   4. Sempre documente transformações complexas
"""

# ==========================================
# EXERCÍCIOS - AULA 5
# ==========================================

print("\n" + "="*50)
print("EXERCÍCIOS - TRANSFORMAÇÕES E PADRONIZAÇÃO")
print("="*50)

# Dados para todos os exercícios
np.random.seed(42)

df_funcionarios = pd.DataFrame({
    'funcionario_id': range(1, 21),
    'nome': ['ana', 'BRUNO', 'carla', 'DANIEL', '  elisa  ', 'FABIO', 'gabriela', 'HUGO', '  isabela  ', 'JOAO',
             'KARINA', 'LUCAS', 'mariana', 'NATALIA', '  otavio  ', 'PAULA', 'Rafael', 'SILVIA', 'TATIANA', 'ULISSES'],
    'departamento': ['vendas', 'TI', 'vendas', 'RH', 'TI', 'VENDAS', 'rh', 'ti', 'RH', 'VENDAS',
                     'financeiro', 'financeiro', 'vendas', 'TI', 'financeiro', 'rh', 'vendas', 'TI', 'financeiro', 'vendas'],
    'salario': [3000, 4500, 3200, 4000, 4800, 3100, 3500, 5000, 4200, 3300,
                5500, 6000, 3800, 5200, 4800, 3700, 4100, 5300, 5800, 3400],
    'anos_empresa': [2, 5, 3, 8, 4, 1, 6, 10, 3, 2,
                     7, 9, 4, 6, 5, 2, 3, 8, 7, 1],
    'avaliacao': [3, 4, 3, 5, 4, 2, 4, 5, 3, 2,
                  5, 5, 4, 4, 4, 3, 3, 5, 5, 2],
    'bonus': [500, 800, 600, 1000, 900, 400, 750, 1200, 650, 450,
              1100, 1300, 700, 950, 850, 550, 600, 1000, 1250, 500]
})



########################################################################
# NÍVEL 1-3: Aquecimento
########################################################################

"""
1. Criando coluna derivada (salário total)

# Crie uma coluna 'salario_total' que é a soma de 'salario' + 'bonus'
"""

"""
df = df_funcionarios.copy()

df['salario_total'] = df['salario'] + df['bonus']

print(df[['salario', 'bonus', 'salario_total']])
"""

########################################################################

"""
2. Aplicando função simples (.apply)

# Crie uma coluna 'faixa_salario' que classifica o salário em:
# - 'Baixo' se salario < 4000
# - 'Médio' se 4000 <= salario < 5000
# - 'Alto' se salario >= 5000
#
# Use .apply() com uma função lambda ou função definida
"""

"""
df = df_funcionarios.copy()

def faixa_salario(salario):

    salario = float(salario)

    if salario < 4000:
        return 'Baixo'
    elif 4000 <= salario < 5000:
        return 'Médio'
    elif salario >= 5000:
        return 'Alto'
    return None

df['faixa_salario'] = df['salario'].apply(faixa_salario)

print(df[['salario', 'faixa_salario']].sort_values('salario'))
"""

########################################################################

"""
3. Mapeamento de departamentos (.map)

# A coluna 'departamento' tem inconsistências (maiúsculas/minúsculas)
# Padronize para o formato: primeira letra maiúscula, resto minúscula
# Exemplo: 'vendas' → 'Vendas', 'TI' → 'Ti' (depois corrigimos)
#
# Depois crie um mapeamento para nomes completos:
# - 'Vendas' → 'Vendas'
# - 'Ti' → 'Tecnologia da Informação'
# - 'Rh' → 'Recursos Humanos'
# - 'Financeiro' → 'Financeiro'
"""

"""
df = df_funcionarios.copy()

df['departamento'] = df['departamento'].str.strip().str.capitalize()

dict_departamento = {
    'Vendas': 'Vendas',
    'Ti': 'Tecnologia da Informação',
    'Rh': 'Recursos Humanos',
    'Financeiro': 'Financeiro'
}

df['departamento'] = df['departamento'].map(dict_departamento)

print(df['departamento'])
"""

########################################################################
# NÍVEL 4-6: Aplicação
########################################################################

"""
4. Categorização com pd.cut()

# Use pd.cut() para criar categorias de 'anos_empresa':
# - 'Novato': 0-3 anos
# - 'Experiente': 3-7 anos
# - 'Sênior': 7+ anos
#
# Crie uma coluna 'tempo_casa'
"""

"""
df = df_funcionarios.copy()

faixas_etarias = [0, 3, 7, 100]
rotulos = ['Novato', 'Experimente', 'Sênior']

df['tempo_casa'] = pd.cut(df['anos_empresa'], bins=faixas_etarias, labels=rotulos)

print(df[['anos_empresa', 'tempo_casa']].sort_values('anos_empresa'))
"""

########################################################################

"""
5. Categorização com pd.qcut()

# Use pd.qcut() para dividir os funcionários em 4 grupos iguais
# com base no salário (quartis)
# Crie uma coluna 'quartil_salario' com os rótulos:
# 'Q1', 'Q2', 'Q3', 'Q4'
"""

"""
df = df_funcionarios.copy()

rotulos = ['Q1', 'Q2', 'Q3', 'Q4']
quantis = len(rotulos)

df['quartil_salario'] = pd.qcut(df['salario'], q=quantis, labels=rotulos)

print(df[['salario', 'quartil_salario']].sort_values('salario'))

"""

########################################################################

"""
6. Normalização e padronização

# Usando a coluna 'salario':
# - Crie 'salario_norm' (normalização min-max, escala 0-1)
# - Crie 'salario_z' (padronização Z-score)
# - Mostre as estatísticas básicas de cada uma
"""

"""
df = df_funcionarios.copy()

def normalizar(coluna):
    return (coluna - coluna.min()) / (coluna.max() - coluna.min())

def padronizar(coluna):
    return (coluna - coluna.mean()) / coluna.std()

def porcentagem(coluna):
    return coluna / coluna.max()

df['salario_norm'] = normalizar(df['salario']).round(2)
df['salario_z'] = padronizar(df['salario']).round(2)
df['salario_pct'] = porcentagem(df['salario']).round(2)

print(df[['salario', 'salario_norm', 'salario_pct','salario_z']].sort_values('salario'))

# Fiz a pct só pra ver como fica a distribuição
"""

########################################################################
# NÍVEL 7-8: Manipulação
########################################################################

"""
7. Transformações condicionais (np.where)

# Crie uma coluna 'aumento_salarial' com base nas regras:
# - Se anos_empresa >= 5: aumento de 10% sobre o salário
# - Se anos_empresa >= 3: aumento de 5% sobre o salário
# - Senão: sem aumento
#
# Dica: use np.where() aninhado ou múltiplas condições
"""

"""
df = df_funcionarios.copy()

def aumento_salarial(row):
    
    if row['anos_empresa'] >= 5:
        return row['salario'] * 1.1
    elif row['anos_empresa'] >= 3:
        return row['salario'] * 1.05
    else:
        return row['salario']

df['aumento_salarial'] = df.apply(aumento_salarial, axis=1)

print(df[['anos_empresa', 'salario', 'aumento_salarial']].sort_values('anos_empresa'))

# achei essa forma mais legível que um .where() aninhado
"""

########################################################################

"""
8. Criando score composto

# Crie um 'score_funcionario' que combina:
# - avaliação (peso 0.4)
# - anos_empresa (peso 0.3, normalizado)
# - bonus (peso 0.3, normalizado)
#
# 1. Normalize 'anos_empresa' e 'bonus' para escala 0-1
# 2. Calcule o score com os pesos
# 3. Crie uma coluna 'classificacao' baseada no score:
#    - > 0.8: 'Excelente'
#    - > 0.6: 'Bom'
#    - > 0.4: 'Regular'
#    - <= 0.4: 'Necessita Melhoria'
"""

"""
df = df_funcionarios.copy()

colunas_originais = [coluna for coluna in df.columns]

def normalizar(coluna):
    return (coluna - coluna.min())/(coluna.max() - coluna.min())

colunas = ['avaliacao', 'anos_empresa', 'bonus']

for coluna in df.columns:
    if coluna in colunas:
        df[f'{coluna}_norm'] = normalizar(df[coluna])

df['score_funcionario'] = (df['avaliacao_norm'] * 0.4  + df['anos_empresa_norm'] * 0.3 + df['bonus_norm'] * 0.3).round(2)

def classificar(score_funcionario):

    if score_funcionario > 0.8:
        return 'Excelente'
    elif score_funcionario > 0.6:
        return 'Bom'
    elif score_funcionario > 0.4:
        return 'Regular'
    elif score_funcionario <= 0.4:
        return 'Necessita Melhoria'
    else:
        return None

df['classificacao'] = df['score_funcionario'].apply(classificar)

colunas_analise = ['score_funcionario', 'classificacao']
colunas_finais = colunas_originais + colunas_analise
df = df[colunas_finais] # ideia que eu tive pra limpar o df final

print(df.to_string())
"""

########################################################################
# NÍVEL 9-10: Desafios
########################################################################

"""
9. Pipeline de transformações completa

# Crie uma função pipeline_transformacoes_funcionarios(df) que:
# 1. Padroniza nomes (strip + title)
# 2. Padroniza departamentos (minúsculas → Capitular)
# 3. Cria coluna 'salario_total' (salario + bonus)
# 4. Cria coluna 'tempo_casa' usando pd.cut
# 5. Cria coluna 'faixa_salario' usando np.where
# 6. Cria 'score_funcionario' como no exercício 8
# 7. Retorna DataFrame limpo e dicionário com log
#
# Teste no df_funcionarios
"""

"""
def pipeline_transformacoes_funcionarios(df_sujo):

    df = df_sujo.copy()
    relatorio = []

    df['nome'] = df['nome'].str.strip().str.title()
    relatorio.append(f'Nomes padronizados (strip + title)')

    dict_departamento = {
        'Vendas': 'Vendas',
        'Ti': 'Tecnologia da Informação',
        'Rh': 'Recursos Humanos',
        'Financeiro': 'Financeiro'
    }

    df['departamento'] = df['departamento'].str.strip().str.title()
    df['departamento'] = df['departamento'].map(dict_departamento)
    relatorio.append(f'Departamentos padronizados (strip + map(dict_departamento))')

    df['salario_total'] = df['salario'] + df['bonus']
    relatorio.append('Coluna "salario_total" criada (salario + bonus)')

    faixas_etarias = [0, 3, 7, 100]
    rotulos = ['Novato', 'Experimente', 'Sênior']
    df['tempo_casa'] = pd.cut(df['anos_empresa'], bins=faixas_etarias, labels=rotulos)
    relatorio.append('Coluna "tempo_casa" criada (baseada em "anos_empresa")')

    def faixa_salario(salario):
        salario = float(salario)
        if salario < 4000:
            return 'Baixo'
        elif 4000 <= salario < 5000:
            return 'Médio'
        elif salario >= 5000:
            return 'Alto'
        return None
    df['faixa_salario'] = df['salario'].apply(faixa_salario)
    relatorio.append('Coluna "faixa_salario criada (baseada no "salario")"')

    def normalizar(coluna):
        return (coluna - coluna.min()) / (coluna.max() - coluna.min())

    colunas = ['avaliacao', 'anos_empresa', 'bonus']

    for coluna in df.columns:
        if coluna in colunas:
            df[f'{coluna}_norm'] = normalizar(df[coluna])

    df['score_funcionario'] = (df['avaliacao_norm'] * 0.4 + df['anos_empresa_norm'] * 0.3 + df['bonus_norm'] * 0.3).round(2)
    relatorio.append('Coluna "score_funcionario" criada (com base nas colunas "avaliacao", "anos_empresa", "bonus", após normalização)')

    def classificar(score_funcionario):

        if score_funcionario > 0.8:
            return 'Excelente'
        elif score_funcionario > 0.6:
            return 'Bom'
        elif score_funcionario > 0.4:
            return 'Regular'
        elif score_funcionario <= 0.4:
            return 'Necessita Melhoria'
        else:
            return None

    df['classificacao'] = df['score_funcionario'].apply(classificar)
    relatorio.append('Coluna "classificacao" criada (com base em "score_funcionario")')

    df = df.drop(['anos_empresa_norm', 'avaliacao_norm', 'bonus_norm'], axis=1)

    return df, relatorio

df_limpo, log = pipeline_transformacoes_funcionarios(df_funcionarios)

print(df_limpo.head().to_string())
print()

for i, linha in enumerate(log, 1):
    print(f'{i}: {linha}')

"""

# O relatorio desse pipeline ficou mais clean, me inspirei bastante no exemplo que vc deu na aula, obrigado!

########################################################################

"""
10. DESAFIO FINAL: Crivo de funcionários

# Crie um sistema de crivo que classifica funcionários em categorias
# de prioridade para promoção baseado em MÚLTIPLOS critérios:
#
# Critérios:
# - Salário total: > 5000 é 'Alto', entre 4000-5000 é 'Médio', < 4000 é 'Baixo'
# - Avaliação: 5 é 'Excelente', 4 é 'Bom', <=3 é 'Regular'
# - Anos de empresa: > 7 é 'Sênior', 3-7 é 'Pleno', < 3 é 'Junior'
# - Score do exercício 8: > 0.7 é 'Alto', 0.5-0.7 é 'Médio', < 0.5 é 'Baixo'
#
# Regras de prioridade (implemente como achar melhor):
# - Prioridade 1: Avaliação Excelente + Score Alto
# - Prioridade 2: Salário Alto + Anos Sênior
# - Prioridade 3: Score Médio ou Bom
# - Prioridade 4: Demais casos
#
# Crie uma coluna 'prioridade_promocao' com valores 1, 2, 3, 4
# e outra coluna 'justificativa' explicando o motivo
#
# Depois crie um resumo mostrando quantos funcionários em cada prioridade
"""


import pandas as pd
import numpy as np

# Dados para o exercício:
np.random.seed(42)

df_funcionarios = pd.DataFrame({
    'funcionario_id': range(1, 21),
    'nome': ['ana', 'BRUNO', 'carla', 'DANIEL', '  elisa  ', 'FABIO', 'gabriela', 'HUGO', '  isabela  ', 'JOAO',
             'KARINA', 'LUCAS', 'mariana', 'NATALIA', '  otavio  ', 'PAULA', 'Rafael', 'SILVIA', 'TATIANA', 'ULISSES'],
    'departamento': ['vendas', 'TI', 'vendas', 'RH', 'TI', 'VENDAS', 'rh', 'ti', 'RH', 'VENDAS',
                     'financeiro', 'financeiro', 'vendas', 'TI', 'financeiro', 'rh', 'vendas', 'TI', 'financeiro', 'vendas'],
    'salario': [3000, 4500, 3200, 4000, 4800, 3100, 3500, 5000, 4200, 3300,
                5500, 6000, 3800, 5200, 4800, 3700, 4100, 5300, 5800, 3400],
    'anos_empresa': [2, 5, 3, 8, 4, 1, 6, 10, 3, 2,
                     7, 9, 4, 6, 5, 2, 3, 8, 7, 1],
    'avaliacao': [3, 4, 3, 5, 4, 2, 4, 5, 3, 2,
                  5, 5, 4, 4, 4, 3, 3, 5, 5, 2],
    'bonus': [500, 800, 600, 1000, 900, 400, 750, 1200, 650, 450,
              1100, 1300, 700, 950, 850, 550, 600, 1000, 1250, 500]
})

df = df_funcionarios.copy()

df['nome'] = df['nome'].str.strip().str.title()
df['departamento'] = df['departamento'].str.strip().str.upper()

df['salario_total'] = df['salario'] + df['bonus']

def classificacar_salario_total(salario_total):
    if salario_total > 5000:
        return 'Alto'
    elif 4000 <= salario_total <= 5000:
        return 'Médio'
    elif salario_total < 4000:
        return 'Baixo'
    else:
        return None

df['salario_class'] = df['salario_total'].apply(classificacar_salario_total)

def classificar_avaliacao(avaliacao):
    if avaliacao >= 5:
        return 'Excelente'
    elif 3 < avaliacao < 5:
        return 'Bom'
    elif avaliacao <= 3:
        return 'Regular'
    else:
        return None

df['avaliacao_class'] = df['avaliacao'].apply(classificar_avaliacao)

def classificar_anos_empresa(anos_empresa):
    if anos_empresa > 7:
        return 'Sênior'
    elif 3 <= anos_empresa <= 7:
        return 'Pleno'
    elif anos_empresa < 3:
        return 'Júnior'
    else:
        return None

df['anos_empresa_class'] = df['anos_empresa'].apply(classificar_anos_empresa)

def normalizar(coluna):
    return (coluna - coluna.min()) / (coluna.max() - coluna.min())

colunas = ['avaliacao', 'anos_empresa', 'bonus']

for coluna in df.columns:
    if coluna in colunas:
        df[f'{coluna}_norm'] = normalizar(df[coluna])

df['score_funcionario'] = (df['avaliacao_norm'] * 0.4 + df['anos_empresa_norm'] * 0.3 + df['bonus_norm'] * 0.3).round(2)

def classificar(score_funcionario):

    if score_funcionario > 0.8:
        return 'Excelente'
    elif score_funcionario > 0.6:
        return 'Bom'
    elif score_funcionario > 0.4:
        return 'Regular'
    elif score_funcionario <= 0.4:
        return 'Necessita Melhoria'
    else:
        return None

df['classificacao'] = df['score_funcionario'].apply(classificar)

df = df.drop(['anos_empresa_norm', 'avaliacao_norm', 'bonus_norm'], axis=1)

def classificar_score_funcionario(score_funcionario):
    if score_funcionario > 0.7:
        return 'Alto'
    elif 0.5 <= score_funcionario <= 0.7:
        return 'Médio'
    elif score_funcionario < 0.5:
        return 'Baixo'
    else:
        return None

df['score_funcionario_class'] = df['score_funcionario'].apply(classificar_score_funcionario)

def definir_prioridade_promocao(row):
    if (row['avaliacao_class'] == 'Excelente') and (row['score_funcionario_class'] == 'Alto'):
        return 1, 'Avaliação Excelente + Score Alto'
    elif (row['salario_class'] == 'Alto') and (row['anos_empresa_class'] == 'Sênior'):
        return 2, 'Salário Alto + Sênior'
    elif (row['score_funcionario_class'] == 'Médio') or (row['classificacao'] == 'Bom'):
        if row['score_funcionario_class'] == 'Médio':
            return 3, 'Score Médio'
        elif row['classificacao'] == 'Bom':
            return 3, 'Classificação Bom'
        else:
            return None, None
    else:
        return 4, 'Demais casos'

df[['prioridade_promocao', 'justificativa']] = df.apply(definir_prioridade_promocao, axis=1, result_type='expand')

print(df.to_string())