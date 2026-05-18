"""
Bloco 4: Estatística para Dados
Aula 04: Teste A/B - Conceitos Fundamentais
Data: 18/05/2026
Objetivo: Entender o QUE é um teste A/B e os conceitos por trás dele

NESTA AULA:
- Apenas conceitos e analogias
- Sem código novo (apenas prints explicativos)
- Exercícios CONCEITUAIS no final
"""

print("="*50)
print("AULA 04 - TESTE A/B: CONCEITOS FUNDAMENTAIS")
print("="*50)

# ==========================================
# 1. O QUE É UM TESTE A/B?
# ==========================================

print("\n1. O QUE É UM TESTE A/B?")
print("-"*30)

"""
TESTE A/B é um experimento controlado onde comparamos duas versões
para determinar qual tem melhor desempenho.

EXEMPLO SIMPLES:

Você tem uma loja online. O botão "COMPRAR" é AZUL.
Um amigo sugere: "Troca para VERMELHO que vende mais!"

Como saber se ele está certo?

OPÇÃO RUIM: Trocar para vermelho e torcer.
   - Se vender mais: não sabe se foi o vermelho ou sorte
   - Se vender menos: perdeu dinheiro

OPÇÃO BOA: Teste A/B!
   - Metade dos clientes vê o botão AZUL (GRUPO A)
   - Metade vê o botão VERMELHO (GRUPO B)
   - Compara os resultados
   - Decide baseado em DADOS

POR QUE TESTE A/B É TÃO IMPORTANTE?

1. Baseado em DADOS, não em "achismo"
2. Permite provar CAUSALIDADE (não só correlação)
3. Quantifica o impacto real de uma mudança
4. Evita decisões baseadas em sorte ou viés

EXEMPLOS REAIS DE TESTES A/B:

- Netflix: testa capas diferentes para a mesma série
- Google: testa 41 tons de azul para anúncios
- Amazon: testa posição do botão "Comprar"
- Airbnb: testa texto do botão "Reservar"
"""

# ==========================================
# 2. HIPÓTESE NULA (H0) E HIPÓTESE ALTERNATIVA (H1)
# ==========================================

print("\n2. HIPÓTESE NULA (H0) E HIPÓTESE ALTERNATIVA (H1)")
print("-"*50)

"""
Todo teste estatístico começa com duas hipóteses:

HIPÓTESE NULA (H0): "Não há diferença"
   - É a hipótese de que qualquer diferença observada é por ACASO
   - É o que assumimos como verdade até prova contrária
   - Exemplo: "O botão vermelho tem a MESMA taxa de conversão que o azul"

HIPÓTESE ALTERNATIVA (H1): "Há diferença"
   - É o que queremos PROVAR
   - Exemplo: "O botão vermelho tem taxa de conversão DIFERENTE do azul"

TIPOS DE HIPÓTESE ALTERNATIVA:

| Tipo               | Descrição    | Exemplo |
|--------------------|--------------|---------|
| Bilateral          | É diferente  | "Vermelho é DIFERENTE de azul" |
| Unilateral (maior) | É melhor     | "Vermelho é MELHOR que azul" |
| Unilateral (menor) | É pior       | "Vermelho é PIOR que azul" |

ANALOGIA DO JÚRI:

H0: "O réu é INOCENTE" (presunção de inocência)
H1: "O réu é CULPADO" (o que a acusação quer provar)

O júri só decide "culpado" se as evidências forem FORTES o suficiente.
Caso contrário, mantém "inocente" (mesmo que ele possa ser culpado).

NO TESTE A/B:
- Só trocamos para a versão B se a evidência for FORTE o suficiente
- Caso contrário, mantemos a versão A (mesmo que B possa ser melhor)
"""

# ==========================================
# 3. P-VALOR (O NÚMERO MÁGICO)
# ==========================================

print("\n3. P-VALOR - O QUE SIGNIFICA?")
print("-"*40)

"""
P-VALOR é a probabilidade de observar os resultados (ou algo mais extremo)
assumindo que a HIPÓTESE NULA é verdadeira.

TRADUZINDO PARA PORTUGUÊS:

P-valor = "Se não houvesse diferença real entre as versões,
          qual a chance de eu ver essa diferença (ou maior) por ACASO?"

EXEMPLO NUMÉRICO:

Você jogou uma moeda 10 vezes e deu 8 caras e 2 coroas.

Pergunta: Esta moeda é VICIADA?

Se a moeda fosse HONESTA (H0 verdadeira), a chance de dar 8 ou mais caras
em 10 lançamentos é de aproximadamente 5.5% (p-valor ≈ 0.055)

Isso significa: se a moeda fosse honesta, em 5.5% das vezes
você veria 8 caras (ou mais) por ACASO.

REGRA DE DECISÃO (SIMPLIFICADA):

| P-valor | Interpretação |
|---------|---------------|
| < 0.01  | Evidência FORTE contra H0 |
| 0.01-0.05 | Evidência MODERADA contra H0 |
| 0.05-0.10 | Evidência FRACA contra H0 |
| > 0.10  | Evidência INSUFICIENTE |

NÃO CAIA NESSA ARMADILHA:

P-valor NÃO é:
- "Probabilidade da H0 ser verdadeira"
- "Probabilidade da H1 ser falsa"
- "A chance de ter errado"

P-valor É:
- "Probabilidade de ver esses dados SE H0 for verdadeira"
"""

# ==========================================
# 4. NÍVEL DE SIGNIFICÂNCIA (α)
# ==========================================

print("\n4. NÍVEL DE SIGNIFICÂNCIA (α - ALPHA)")
print("-"*35)

"""
α (alpha) é o LIMIAR que usamos para decidir se rejeitamos H0.

VALOR TRADICIONAL: α = 0.05 (5%)

O QUE SIGNIFICA α = 0.05?

"Estou disposto a aceitar 5% de chance de cometer um ERRO
 ao dizer que há diferença quando na verdade não há."

REGRRA DE DECISÃO:

Se p-valor < α → REJEITAMOS H0
   → Concluímos que há diferença estatisticamente significativa

Se p-valor ≥ α → NÃO REJEITAMOS H0
   → Não há evidência suficiente de diferença

EXEMPLO:

α = 0.05
p-valor = 0.03

0.03 < 0.05 → Rejeitamos H0
→ Concluímos que há diferença significativa

POR QUE α = 0.05 É O PADRÃO?

- Convenção histórica (definida por Ronald Fisher em 1925)
- Equilíbrio entre errar demais e errar de menos
- Para negócios, pode ser diferente (ex: áreas médicas usam 0.01)

QUANDO USAR α DIFERENTE:

| Contexto | α sugerido | Motivo |
|----------|------------|--------|
| Teste A/B de marketing       | 0.05 | Equilíbrio padrão |
| Lançamento de medicamento    | 0.01 | Erro custa vidas |
| Teste interno de baixo risco | 0.10 | Erro tem custo baixo |
"""

# ==========================================
# 5. ERRO TIPO I E ERRO TIPO II
# ==========================================

print("\n5. ERRO TIPO I E ERRO TIPO II")
print("-"*35)

"""
DOIS TIPOS DE ERRO QUE PODEMOS COMETER:

ERRO TIPO I (Falso Positivo):
   - Rejeitar H0 quando ela é VERDADEIRA
   - Concluir que há diferença quando NÃO há
   - Probabilidade = α (nível de significância)
   - Exemplo: Trocar o botão (não funciona) e gastar dinheiro à toa

ERRO TIPO II (Falso Negativo):
   - NÃO rejeitar H0 quando ela é FALSA
   - Concluir que não há diferença quando HÁ
   - Probabilidade = β (beta)
   - Exemplo: Deixar de trocar o botão (que funcionaria) e perder vendas

MATRIZ DE DECISÃO:

| Realidade \\ Decisão | Rejeitar H0 (trocar) | Não rejeitar H0 (manter) |
|---------------------|----------------------|--------------------------|
| H0 é verdadeira (não funciona) | ERRO TIPO I (α) | Decisão correta |
| H0 é falsa (funciona) | Decisão correta | ERRO TIPO II (β) |

PODER ESTATÍSTICO = 1 - β
   → Probabilidade de detectar um efeito REAL quando ele existe
   → Quanto maior, melhor (geralmente queremos > 80%)

EXEMPLO NO NEGÓCIO:

Você testa um novo layout que promete aumentar vendas.

ERRO TIPO I (Falso Positivo):
   - Você implementa o layout (gasta dinheiro)
   - Na verdade, ele não funciona
   - Perdeu tempo e recurso

ERRO TIPO II (Falso Negativo):
   - Você NÃO implementa o layout
   - Na verdade, ele funcionaria
   - Deixou de ganhar dinheiro

QUAL ERRO É "PIOR"? DEPENDE:

- Trocar custa caro? → Erro Tipo I é pior (gastou dinheiro à toa)
- Não trocar perde muito? → Erro Tipo II é pior (deixou de ganhar)
- Área médica? → Erro Tipo I é pior (dar remédio que não funciona)
"""

# ==========================================
# 6. TAMANHO DA AMOSTRA
# ==========================================

print("\n6. TAMANHO DA AMOSTRA - POR QUE IMPORTA?")
print("-"*40)

"""
AMOSTRAS PEQUENAS SÃO UM PROBLEMA GRAVE!

POR QUE AMOSTRAS PEQUENAS SÃO RUINS?

1. RESULTADOS INSTÁVEIS
   - Mudar um único cliente pode mudar a conclusão
   - Exemplo: 2 conversões em 100 → 2%; 3 conversões em 100 → 3%

2. NÃO CONSEGUEM DETECTAR DIFERENÇAS PEQUENAS
   - Diferença de 1% pode ser importante no negócio
   - Amostra pequena não consegue ver essa diferença

3. MAIOR CHANCE DE ERRO TIPO I OU II
   - Amostra pequena = resultado menos confiável

REGRAS PRÁTICAS (SIMPLIFICADAS):

| Efeito esperado | Amostra por grupo (sugestão) |
|-----------------|------------------------------|
| Grande (5%+)    | 500-1000 |
| Médio (2-5%)    | 1000-3000 |
| Pequeno (1-2%)  | 3000-5000 |
| Muito pequeno (0.5-1%) | 5000-10000+ |

FÓRMULA NA PRÓXIMA AULA (AULA 05):
- Não vou jogar fórmula mágica agora
- Vamos aprender uma função que calcula para você

📌 REGRA DE OURO:

"Teste A/B com amostra pequena é PIOR que não fazer teste nenhum"

Pode levar a decisões erradas que custam dinheiro.
"""

# ==========================================
# 7. RESUMO DOS CONCEITOS
# ==========================================

print("\n7. RESUMO - TESTE A/B (CONCEITOS)")
print("-"*35)

"""
✅ O QUE É TESTE A/B:
   - Experimento controlado comparando duas versões
   - Baseado em dados, não achismo
   - Permite provar causalidade

✅ HIPÓTESE NULA (H0):
   - "Não há diferença entre as versões"
   - Presunção de inocência

✅ HIPÓTESE ALTERNATIVA (H1):
   - "Há diferença entre as versões"
   - O que queremos provar

✅ P-VALOR:
   - Probabilidade de ver os dados SE H0 for verdadeira
   - NÃO é probabilidade de H0 ser verdadeira

✅ NÍVEL DE SIGNIFICÂNCIA (α):
   - Limiar para rejeitar H0 (tradicionalmente 0.05)
   - Se p-valor < α → rejeitamos H0

✅ ERRO TIPO I:
   - Dizer que há diferença quando não há (falso positivo)
   - Probabilidade = α

✅ ERRO TIPO II:
   - Dizer que não há diferença quando há (falso negativo)
   - Probabilidade = β

✅ PODER ESTATÍSTICO = 1 - β
   - Probabilidade de detectar um efeito real

✅ TAMANHO DA AMOSTRA:
   - Amostras pequenas geram conclusões erradas
   - Quanto menor o efeito esperado, maior a amostra necessária
"""

# ==========================================
# EXERCÍCIOS - AULA 04 (CONCEITUAIS)
# ==========================================

print("\n" + "="*50)
print("EXERCÍCIOS - TESTE A/B (CONCEITOS)")
print("="*50)

"""
Responda as perguntas abaixo. Não precisa escrever código.
Use apenas o que aprendeu nesta aula.

O objetivo é FIXAR OS CONCEITOS antes de partimos para a prática.
"""

########################################################################
# EXERCÍCIO 1
########################################################################

"""
1. Uma loja testou duas versões da página de checkout.
   A versão B teve conversão maior, mas o p-valor foi 0.08 com α=0.05.

   a) A diferença é estatisticamente significativa? Por quê?
   b) O que você recomenda para a loja? Manter A ou mudar para B?
   c) Por quê?
"""

"""
a) a diferença não é estatisticamente significativa, pois, como o p-valor é maior que o alfa posto de antemão,
pode ser que a diferença seja apenas por acaso.

b) Se nenhum outro teste for feito, eu recomendo não mudar a página de checkout, pois a diferença não é estatisticamente
significativa. Entretanto, como a taxa de conversão foi maior, e o p-valor foi próximo de alfa, eu recomendo refazer o teste
com uma amostra maior.

c) vide resposta anterior.
"""

########################################################################
# EXERCÍCIO 2
########################################################################

"""
2. Explique com suas palavras o que significa p-valor = 0.03.

   Não use jargões técnicos. Imagine que você está explicando
   para um gerente que não sabe estatística.
"""

"""
Primeiramente é uma medida de probabilidade. 0.03 é igual a 3%.
O p-valor mede a probabilidade do resultado específico acontecer 
caso a nossa hipotese esteja errada.
Ou seja, pense na loteria. Qual a chance de vc ganhar a loteria duas vezes consecutivas se não tiver nenhum complô por baixo dos panos?
O p-valor responde essa questão.
"""

########################################################################
# EXERCÍCIO 3
########################################################################

"""
3. Uma empresa farmacêutica testa um novo remédio.
   α = 0.01 (mais rigoroso que 0.05).

   a) Por que eles usaram α = 0.01 em vez de 0.05?
   b) Qual erro (Tipo I ou Tipo II) eles querem evitar?
   c) O que aconteceria se usassem α = 0.05?
"""

"""
a) Porque, num contexto farmacêutico, é exigido maior rigor em relação a possibilidade de erro.

b) Eles querem evitar o erro de tipo 1, falso positivo, ou seja, evitar que o resultado diga que o remédio funciona quando ele não funciona.

c) Se usassem alpha=0.05 significa que a tolerância ao erro seria 5 vezes maior. 
"""

########################################################################
# EXERCÍCIO 4
########################################################################

"""
4. Uma startup fez um teste A/B com apenas 100 usuários por grupo.
   O resultado foi inconclusivo (p-valor = 0.12).

   a) O que pode ter causado esse resultado inconclusivo?
   b) O que você sugere para a startup?
   c) A frase "teste A/B com amostra pequena é pior que não fazer teste"
      faz sentido neste caso? Por quê?
"""

"""
a) a amostragem reduzida de usuários pode ter causado esse resultado inconclusivo.

b) Eu recomendo que a startup calcule de antemão o tamanho da amostra necessário para fazer o teste a/b em questão.

c) Depende do número recomendado da amostragem, mas provavelmente sim.
"""

########################################################################
# EXERCÍCIO 5
########################################################################

"""
5. Classifique cada situação como ERRO TIPO I ou ERRO TIPO II:

   a) A campanha de marketing NÃO funciona, mas o teste diz que sim.
   b) O novo layout FUNCIONA, mas o teste diz que não.
   c) O remédio NÃO tem efeito, mas o estudo diz que tem.
   d) O treinamento MELHORA produtividade, mas a empresa decide não adotar.
"""

"""
a) Tipo 1 - Falso Positivo.
b) Tipo 2 - Falso Negativo.
c) Tipo 1 - Falso Positivo.
d) Tipo 2 - Falso Negativo.
"""

########################################################################
# EXERCÍCIO 6
########################################################################

"""
6. Um analista diz: "P-valor de 0.03 significa que há 97% de chance
   da versão B ser melhor que a versão A."

   a) Esta afirmação está correta? Por quê?
   b) Explique o erro na afirmação.
   c) Como você explicaria o resultado corretamente?
"""

"""
a) Essa afirmação está incorreta. p-valor de 0.03 indica que se h0 for verdadeira, o resultado tem 3% de chance de acontecer

b) Apesar de ser uma forma de aproximação do significado correto, o p-valor diz respeito a coincidência e não da probabilidade de sucesso de forma direta. 
Algo que não é possível prever com certeza.

c) P-valor de 0.03 significa que a chance desse resultado ser uma coincidência é de 3%. Ou, a chance de não ser uma coincidência é de 97%.
"""

########################################################################
# EXERCÍCIO 7
########################################################################

"""
7. Você está rodando um teste A/B para decidir se muda ou não o preço de um produto.
   Trocar o preço custa R$ 10.000 de implementação.
   Se funcionar, o ganho esperado é de R$ 50.000.

   a) Qual erro (Tipo I ou Tipo II) seria MAIS CARO para o negócio?
   b) Você usaria α = 0.05 ou α = 0.10? Por quê?
"""

"""
a) Um erro do tipo 2, falso negativo, seria mais "caro" visto que o lucro esperado é 5 vezes maior que o preço de implementação.

b) Em concordância com a resposta anterior, eu quero evitar um falso negativo, mas não me cegar a ponto de pular de ponta em um falso positivo.
Dessa forma, acredito que o alpha=0.05, seja um bom equilibrio, mas se os 10000 for um investimento relativamente baixo, talvez a=0.1 seja justificável.
"""

########################################################################
# EXERCÍCIO 8
########################################################################

"""
8. Uma empresa fez 20 testes A/B diferentes.
   Em 1 deles, o p-valor foi menor que 0.05 por ACASO (não havia efeito real).

   a) Isso é possível? Por quê?
   b) Se α = 0.05, quantos testes se espera que dêem falso positivo?
   c) Como empresas grandes lidam com esse problema?
"""

"""
a) Sim, isso é possível, a chance do acaso é de 5%.
b) Se espera que 5 de 100 teste dêem falso positivo. Em 20, espera-se 1.
c) Fazendo um grande volume de testes.
"""

########################################################################
# EXERCÍCIO 9
########################################################################

"""
9. Um analista rodou um teste com 500 usuários por grupo e obteve p-valor = 0.06.
   Ele diz: "Quase deu significativo. Vou rodar mais 200 usuários para ver se chega em 0.05."

   a) Esta é uma boa prática? Por quê?
   b) O que pode acontecer se ele fizer isso?
   c) O que ele deveria fazer?
"""

"""
a) Essa não é uma boa prática, pois ele está consciente ou inconscientemente tentando cavar um resultado específico

b) Ele pode obter o valor de 0.05 para o p-valor (assim como obter um resultado maior) e manipular o teste, o invalidando-o

c) Ele deveria aceitar e reportar o resultado do teste, ou refazer o teste com uma quantidade maior de usuários. 
"""

########################################################################
# EXERCÍCIO 10
########################################################################

"""
10. DESAFIO: Monte um parágrafo explicando para um gerente não-técnico
    os resultados de um teste A/B com os seguintes números:

    - Versão A (atual): 5% de conversão
    - Versão B (teste): 5.5% de conversão
    - P-valor: 0.03
    - Amostra: 5000 clientes por grupo

    Use linguagem clara, sem jargões estatísticos.
    Inclua: o que foi testado, qual foi o resultado, se é confiável,
    e uma recomendação final.
"""

"""
A equipe de análise de dados realizou um teste entre dois layouts do site de e-commerce de nossa empresa.
O teste consistiu de 2 grupos de clientes com 5000 integrantes cada escolhidos aleatoriamente.
O primeiro grupo teve acesso ao layout atual do site de e-commerce, enquanto o segundo grupo teve acesso ao layout testado.
O primeiro grupo teve uma taxa de conversão de 5%, ou seja, 5% dos 5000 (250 clientes) que visitaram o site acabaram comprando.
Seguindo essa mesma lógica o segundo grupo teve 5.5%, ou seja, 275 clientes.
Apesar da diferença baixa (25 clientes em um total de 5000) os teste mostram que a chance de que esse resultado seja uma coincidência é
de apenas 3%. Tradicionalmente para teste estatísticos usamos um limite de 5%.
Dessa forma, o apesar do baixo resultado, o teste tem uma significância estatística alta.

Caso seja implementado, o aumento na receita prevista é de (calculo)
o custo para implementação é de (calculo)

O equipe de análise de dados recomenda a substituição do layout.
"""
