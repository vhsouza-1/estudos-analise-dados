# Projeto de Limpeza de Dados - Clientes

## Sobre o Projeto

Pipeline completo de limpeza e padronização de dados de clientes. O projeto trata dados inconsistentes, normaliza formatos e gera métricas como score do cliente e faixa de renda.

## Objetivos

- Padronizar formatos de texto (nomes, categorias, emails)
- Limpar e validar dados de contato (email, telefone)
- Tratar valores nulos e duplicados
- Normalizar dados numéricos (renda, compras)
- Criar métricas de análise (score do cliente, faixa de renda)

## Estrutura do Projeto

- 01_data/01_raw/ - Dados brutos (clientes_raw.csv)
- 01_data/02_processed/ - Dados limpos (cliente_limpo.csv)
- 02_scripts/01_pipeline_limpeza.py - Script de processamento
- 03_reports/01_imagens/ - Visualizações (opcional)
- 04_docs/ - Documentação

## 🔧 Etapas do Pipeline

### 1. Padronização de Formatos

| Coluna | Tratamentos aplicados |
|--------|----------------------|
| nome | Strip de espaços + Title Case |
| categoria | Lowercase + mapeamento de sinônimos (ouro→Gold, básico→Basic, etc.) |
| email | Strip + lowercase + correção de emails sem @ e sem .com |
| telefone | Remoção de caracteres especiais + validação de tamanho (10-11 dígitos) + formatação padrão |
| datas | Conversão para datetime + remoção de datas inválidas (futuras e <1900) |
| renda | Substituição de valores <=0 por nulo + imputação por mediana |
| compras | Substituição de valores negativos por nulo + imputação por mediana |

### 2. Tratamento de Nulos e Duplicatas

| Estratégia | Colunas aplicadas |
|------------|-------------------|
| Remoção de linhas duplicadas | Todas as colunas |
| Preenchimento com valor padrão | email (desconhecido@email.com), telefone ((00) 00000-0000), categoria (Não informado) |
| Imputação por mediana | data_nascimento, data_cadastro |

### 3. Transformações e Métricas

| Métrica | Cálculo |
|---------|---------|
| renda_anual | renda * 12 |
| idade | (data_atual - data_nascimento).days // 365 |
| renda_norm | Normalização min-max: (x - min) / (max - min) |
| compras_norm | Normalização min-max |
| idade_norm | Normalização min-max |
| score_cliente | (compras_norm * 0.4) + (renda_norm * 0.4) + (idade_norm * 0.2) |
| faixa_renda | pd.cut(): Baixa (≤3k), Média (3k-8k), Alta (>8k) |
| categoria_cliente | Score > 0.7: Premium, 0.4-0.7: Regular, ≤ 0.4: Bronze |

## Resultados

- Shape inicial: (conforme seus dados)
- Shape final: (conforme seus dados)
- Duplicatas removidas: 5
- Nulos tratados: (valores do seu output)

## Como Executar

Pré-requisitos:
pip install pandas numpy

Organize os arquivos:
Coloque o arquivo bruto em 01_data/01_raw/clientes_raw.csv

Execute o script:
python 02_scripts/01_pipeline_limpeza.py

Resultado: 01_data/02_processed/cliente_limpo.csv

## Observações

- Datas futuras e anteriores a 1900 foram convertidas para NaT
- Emails e telefones nulos receberam valores padrão (não são descartados)
- Telefones com menos de 10 ou mais de 11 dígitos foram tratados como nulos
- Colunas _norm foram retiradas do arquivo final

## Autor

vhsouza - 11/05/2026

## Licença

Uso educacional - Projeto de estudo de limpeza de dados com pandas.
