"""
Módulo 9: arquivos
Exercícios Integradores
Data: 14/04
Objetivo: Resolver problemas que misturam tudo que vimos
"""
import csv
from collections import defaultdict
from pathlib import Path
import datetime

"""
MÓDULO 9: MANIPULAÇÃO DE ARQUIVOS - AULA 9.7

Exercícios Integradores

Objetivo:

Juntar tudo que aprendemos no Módulo 9:

    Leitura e escrita de arquivos

    CSV com DictReader/DictWriter

    Caminhos com pathlib

    Criar pastas e organizar arquivos

"""
####################################################################
"""
Exercício 1: Organizador de Arquivos por Extensão

Tema: pathlib, .mkdir(), .glob(), .rename()

Crie um programa que organiza arquivos da pasta atual por extensão.

Passos:
1. Varre a pasta atual
2. Para cada arquivo, identifica a extensão
3. Cria uma pasta com o nome da extensão (ex: "txt_files")
4. Move o arquivo para a pasta correspondente
5. Mostra um relatório: "Movidos: 5 arquivos"

CUIDADO: Teste primeiro com arquivos que você pode perder!
Sugestão: crie alguns arquivos .txt, .csv, .py de teste primeiro.
"""
"""
# Criar alguns arquivos de exemplo para listar (peguei da aula passada)
for nome in ["dados.csv", "planilha.csv", "relatorio.txt", "documento.txt", "backup.zip"]:
    Path(nome).touch()  # cria arquivo vazio (não vamos usar muito, só para exemplo)

# Vou excluir o .py pq na pasta em questão que eu estou mexendo tem .py de outras aulas

for item in Path('.').glob('*'):
    if item.suffix != '.py':
        ext = item.suffix[1:]
        if ext: # pode usar no lugar de "if ext != '':" né?
            pasta = Path(f'{ext}_files')
            pasta.mkdir(exist_ok=True)
            item.rename(pasta / item.name)
"""
####################################################################
"""
Exercício 2: Gerador de Relatório a partir de CSV

Tema: CSV, pathlib, leitura, escrita

Você tem um arquivo "vendas.csv" com:
produto,quantidade,preco,vendedor
celular,10,1500,Ana
fone,30,200,Bruno
celular,5,1500,Ana
notebook,3,3500,Carla

Tarefas:
1. Leia o arquivo CSV usando DictReader
2. Calcule:
   - Faturamento por produto (quantidade * preco)
   - Faturamento por vendedor
   - Total geral de vendas
3. Crie um arquivo "relatorio.txt" com os resultados
4. Use pathlib para criar uma pasta "relatorios" e salvar o arquivo lá
"""
"""
_=1

with open('vendas.csv', 'w', newline='') as arquivo:
    arquivo.write('produto,quantidade,preco,vendedor\n')
    arquivo.write('celular,10,1500,Ana\n')
    arquivo.write('fone,30,200,Bruno\n')
    arquivo.write('celular,5,1500,Ana\n')
    arquivo.write('notebook,3,3500,Carla\n')

with open('vendas.csv', 'r') as arquivo:

    leitor = csv.DictReader(arquivo)

    faturamento_produto = defaultdict(float)
    faturamento_vendedor = defaultdict(float)
    total_vendas = 0

    for venda in leitor: # isso aqui costuma-se fazer dentro ou fora do with open()? Tipo, eu abro o documento faço esses calculos e fecho ele com os dados que eu quero. Ou eu abro ele, salvo os dados e depois faço as contas?

        produto = venda['produto']
        quantidade = int(venda['quantidade'])
        preco = float(venda['preco'])
        vendedor = venda['vendedor']

        faturamento_produto[produto] = quantidade * preco

        faturamento_vendedor[vendedor] = quantidade * preco

        total_vendas += quantidade

with open('relatorio.txt', 'w', newline='') as arquivo:
    arquivo.write('=== Faturamento por produto ===\n\n')
    for produto, faturamento in faturamento_produto.items():
        arquivo.write(f'    {produto:<9}: R$ {faturamento:.2f}\n')
    arquivo.write('\n')
    arquivo.write('=== Faturamento por vendedor ===\n\n')
    for vendedor, faturamento in faturamento_vendedor.items():
        arquivo.write(f'    {vendedor:<9}: R$ {faturamento:.2f}\n')
    arquivo.write('\n')
    arquivo.write('=== Total geral de vendas ===\n\n')
    arquivo.write(f'{total_vendas}\n')

Path('relatorios').mkdir(exist_ok=True)
Path('relatorio.txt').rename('relatorios/relatorio.txt')
"""
####################################################################
"""
Exercício 3: Dividindo um Arquivo Grande

Tema: Leitura, escrita, pathlib

Crie um programa que divide um arquivo grande em vários menores.

Passos:
1. Peça ao usuário o nome do arquivo de entrada
2. Peça o número de linhas por arquivo de saída (ex: 100)
3. Leia o arquivo linha por linha
4. A cada N linhas, crie um novo arquivo
5. Os arquivos devem se chamar: "nome_original_parte_1.txt", "nome_original_parte_2.txt", etc.
6. Salve os arquivos em uma pasta "partes"

Exemplo: arquivo de 250 linhas, dividir a cada 100 linhas:
- parte_1: linhas 1-100
- parte_2: linhas 101-200
- parte_3: linhas 201-250
"""
"""
arquivo_entrada = Path(input('Informe o nome do arquivo de entrada: '))
N = int(input('Informe o número de linhas por arquivo de saída: '))
num = 1

Path('partes').mkdir(exist_ok=True)

with open(arquivo_entrada, 'r') as arquivo:

    a = len(list(arquivo))
    if a % N == 0:
        num_max = a/N
    else:
        num_max = (a/N)+0.5

with open(arquivo_entrada, 'r') as f:

    while num <= num_max:

        contador = 0

        with open(f'partes/{arquivo_entrada.stem}_parte_{num}.txt', 'w', newline='') as f1:

            for linha in f:

                f1.write(f'{linha.strip()}\n')

                contador += 1

                if contador >= N:
                    break

        num += 1

# Eu não consegui fazer esse desafio de uma forma elegante. Ai precisei fazer aquele primeiro open pra contar quantas 
# linha tem no arquivo original pra calcular de antemão o número de arquivos que iria precisar.
# Quando tentei fazer sem isso, eu caia no problema de gerar arquivos infinitos vazios.
# Como esse desafio poderia ser feito, com as coisas que eu sei, sem precisar fazer esse primeiro open?
"""
####################################################################
"""
Exercício 4: Validador de Arquivos CSV

Tema: CSV, validação, pathlib

Crie um programa que valida a estrutura de arquivos CSV em uma pasta.

Para cada arquivo .csv, verifique:
1. Se o arquivo não está vazio
2. Se tem cabeçalho (primeira linha)
3. Se todas as linhas têm o mesmo número de colunas que o cabeçalho
4. Se não há linhas completamente vazias

Mostre um relatório:
- dados.csv: OK (3 linhas, 2 colunas)
- vendas.csv: ERRO - linha 5 tem 4 colunas (cabeçalho tem 3)
- clientes.csv: ERRO - arquivo vazio

Use pathlib para listar os arquivos .csv
"""
"""
with open('dados.csv', 'w', newline='') as arq:
    arq.write('tipo,quantidade\n')
    arq.write('moto,2\n')
    arq.write('carro,1\n')

with open('vendas.csv', 'w', newline='') as arq:
    arq.write('produto,preco,quantidade\n')
    arq.write('fone,100,20\n')
    arq.write('celular,1000,5\n')
    arq.write('notebook,2000,3\n')
    arq.write('bateria,500,10,teste\n')

with open('clientes.csv', 'w', newline='') as arq:
    arq.write('')

with open('dados_sem_cabecalho.csv', 'w', newline='') as arq:
    arq.write('\n')
    arq.write('moto,2\n')
    arq.write('carro,1\n')

###########################################################

for caminho in Path('.').glob('*.csv'):

    erro = 0

    print(f'{caminho}: ')

    with open(caminho, 'r') as arquivo:
        leitor = csv.DictReader(arquivo)
        validando = list(leitor)

    # validador vazio:
    if not validando:
        print('   ERRO - arquivo vazio')
        erro += 1

    # validador cabeçalho:
    cabecalho = []

    for linha in validando:
        for chave in linha:
            if chave in cabecalho:
                continue
            else:
                cabecalho.append(chave)

    if cabecalho.count(None) == len(cabecalho):
        print('   ERRO - arquivo sem cabeçalho')
        erro += 1

    elif cabecalho.count(None) != 0 and cabecalho.count(None) < len(cabecalho):

        # validador numero de colunas das linhas em relação ao cabeçalho
        linha_contador = 1

        for linha in validando:
            chaves = [chave for chave in linha.keys()]

            if None in chaves:
                print(f'   ERRO - linha {linha_contador} tem {len(chaves)} colunas (cabeçalho tem {len(cabecalho)-cabecalho.count(None)})')
                erro += 1
            linha_contador += 1

    if erro == 0:
        print(f'   OK: {len(validando)} linhas {len(cabecalho)} colunas')

    print()

# aqui eu gastei neurônio viu hahaha
"""
####################################################################
"""
Exercício 5: DESAFIO FINAL - Pipeline de Processamento de Dados

Tema: Todos os conceitos do módulo 9
python


Crie um sistema completo de processamento de dados que:

=== PARTE 1: ESTRUTURA ===
1. Cria a seguinte estrutura de pastas (se não existir):
   dados/raw/
   dados/processed/
   scripts/
   logs/
   output/

=== PARTE 2: PROCESSAMENTO ===
2. Lê todos os arquivos .csv da pasta "dados/raw/"
3. Para cada arquivo:
   - Adiciona uma coluna "data_processamento" com a data atual
   - Filtra linhas onde o campo "valor" > 0 (se existir)
   - Salva o arquivo processado em "dados/processed/" com o mesmo nome
4. Registra no log:
   - Nome do arquivo processado
   - Quantas linhas foram filtradas (removidas)
   - Quantas linhas restaram
   - Timestamp do processamento

=== PARTE 3: RELATÓRIO ===
5. Gera um relatório final "output/resumo.txt" com:
   - Total de arquivos processados
   - Total de linhas processadas (soma de todas)
   - Total de linhas filtradas
   - Lista dos arquivos com problemas (se houver)

=== DADOS DE TESTE ===
Crie alguns arquivos CSV na pasta "dados/raw/" para testar:

dados1.csv:
nome,valor
produto1,100
produto2,-50
produto3,200

dados2.csv:
nome,valor
produto4,300
produto5,0
produto6,150

dados3.csv: (arquivo vazio ou com erro - para testar validação)

"""
############### Criar estrutura do projeto ###############

pastas = [
    'dados/raw/',
    'dados/processed/',
    'scripts/',
    'logs/',
    'output/'
]

for pasta in pastas:
    Path(pasta).mkdir(parents=True, exist_ok=True)

############### Criar dados de teste ###############

with open('dados/raw/dados1.csv', 'w', newline='') as f:
    f.write('nome,valor\n')
    f.write('produto1,100\n')
    f.write('produto2,-50\n')
    f.write('produto3,200\n')

with open('dados/raw/dados2.csv', 'w', newline='') as f:
    f.write('nome,valor\n')
    f.write('produto4,300\n')
    f.write('produto5,0\n')
    f.write('produto6,150\n')

with open('dados/raw/vendas.csv', 'w', newline='') as arq:
    arq.write('produto,preco,quantidade\n')
    arq.write('fone,100,20\n')
    arq.write('celular,1000,5\n')
    arq.write('notebook,2000,3\n')
    arq.write('bateria,500,10,teste\n')

with open('dados/raw/clientes.csv', 'w', newline='') as arq:
    arq.write('')

with open('dados/raw/dados_sem_cabecalho.csv', 'w', newline='') as arq:
    arq.write('\n')
    arq.write('moto,2\n')
    arq.write('carro,1\n')

############### Identificando arquivos com erros ###############

arquivos_erros = defaultdict(list)

for arquivo in Path('dados/raw').glob('*.csv'):

    with open(arquivo, 'r') as f:
        leitor = csv.DictReader(f)
        validando = list(leitor)

    # validador vazio:
    if not validando:
        erro_1 = 'ERRO - arquivo vazio'
        arquivos_erros[arquivo.name].append(erro_1)

    # validador cabeçalho:
    cabecalho = []
    for linha in validando:
        for chave in linha:
            if chave in cabecalho:
                continue
            else:
                cabecalho.append(chave)

    if cabecalho.count(None) == len(cabecalho):
        erro_2 = 'ERRO - arquivo sem cabeçalho'
        if erro_1 not in arquivos_erros[arquivo.name]:
            arquivos_erros[arquivo.name].append(erro_2)

    elif cabecalho.count(None) != 0 and cabecalho.count(None) < len(cabecalho):

        # validador numero de colunas das linhas em relação ao cabeçalho
        linha_contador = 1

        for linha in validando:
            chaves = [chave for chave in linha.keys()]

            if None in chaves:
                erro_3 = f'ERRO - linha {linha_contador} tem {len(chaves)} colunas (cabeçalho tem {len(cabecalho)-cabecalho.count(None)})'
                arquivos_erros[arquivo.name].append(erro_3)
            linha_contador += 1

############### Aplicando pipeline ###############

total_arquivos_processados = 0
total_linhas_processadas = 0
total_linhas_filtradas = 0

for item in Path('dados/raw').glob('*.csv'):

    if item.name not in arquivos_erros.keys():

        with open(f'dados/raw/{item.name}', 'r') as f:

            leitor = csv.DictReader(f)
            arquivo = list(leitor)
            arquivo_processado = [linha for linha in arquivo if float(linha['valor']) > 0]
            linhas_filtradas = len(arquivo)-len(arquivo_processado)
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            arquivo_processado.append({'data_processamento': timestamp})

        with open(f'dados/processed/{item.name}', 'w', newline='') as f:
            campos = ['nome', 'valor', 'data_processamento']
            escritor = csv.DictWriter(f, fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(arquivo_processado)

        with open('logs/log.txt', 'a', newline='') as f:
            f.write(f'[{timestamp}] Arquivo processado: {item.name} | linhas filtradas: {linhas_filtradas} | linhas restantes: {len(arquivo_processado)-1}\n')

        total_arquivos_processados += 1
        total_linhas_processadas += len(arquivo)
        total_linhas_filtradas += linhas_filtradas

with open('output/relatorio.txt', 'w', newline='') as f:
    f.write(f'Total de arquivos processados: {total_arquivos_processados}\n')
    f.write(f'Total de linhas processadas: {total_linhas_processadas}\n')
    f.write(f'Total de linhas filtradas: {total_linhas_filtradas}\n')
    f.write(f'====================================================\n')
    f.write(f'Lista dos arquivos com problemas:\n')
    f.write(f'\n')
    for arquivo, erros in arquivos_erros.items():
        f.write(f'{arquivo}:\n')
        for erro in erros:
            f.write(f'  -{erro}\n')
        f.write('\n')

# Esse último desafio eu realmente fiquei bem orgulhoso. Pode não ter sido o script mais limpo do mundo, mas ele deu conta do recado hehe