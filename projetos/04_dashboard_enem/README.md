# Dashboard ENEM 2019 – Análise de Participação e Desempenho

![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=flat&logo=power-bi&logoColor=black)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen.svg)

## Sobre o Projeto

Dashboard interativo no Power BI para explorar o perfil dos participantes do ENEM 2019 e analisar como o desempenho varia entre diferentes grupos sociais e demográficos.

**Fonte dos dados:** Dataset tratado no projeto [Análise Estatística do ENEM 2019](https://github.com/vhsouza/estudo-analise-dados/tree/main/projetos/03_analise_dados_enem_2019)

## Estrutura do Projeto

- 01_data/enem2019_basico.csv - Dataset tratado e pronto para o dashboard
- 02_dashboard/dashboard_enem_2019.pbix - Arquivo do Power BI
- 03_documentacao/medidas.txt - Lista completa das medidas DAX
- 03_documentacao/print_pagina1.png - Print da página Visão Geral
- 03_documentacao/print_pagina2.png - Print da página Participação
- 03_documentacao/print_pagina3.png - Print da página Desempenho
- 03_documentacao/dashboard_enem_2019.pdf - Exportação em PDF do dashboard
- setup.py - Script para criar estrutura de pastas
- README.md - Este arquivo

## Tecnologias Utilizadas

- Power BI Desktop
- DAX (Data Analysis Expressions)
- Python (pandas) - para limpeza inicial dos dados

## Páginas do Dashboard

### Página 1 – Visão Geral
Panorama geral da base de dados: total de participantes, notas médias, distribuição por UF e idade.

### Página 2 – Participação
Perfil demográfico dos participantes: gênero, cor/raça, faixa etária.

### Página 3 – Desempenho
Comparação de desempenho entre diferentes grupos demográficos.

## Medidas DAX

Lista completa disponível em [03_documentacao/medidas.txt](03_documentacao/medidas.txt)

**Medidas da página 1 - Visão Geral (mais simples)**

- `Total Participantes = COUNTROWS(enem2019_basico)`

- `Média da Nota Final = MEDIAN(enem2019_basico[nota_media])`

- `Média da Redação = MEDIAN(enem2019_basico[nota_redacao])`

- `Média de Acertos = MEDIAN(enem2019_basico[total_acertos])`

## Como Visualizar

1. Baixe o arquivo `02_dashboard/dashboard_enem_2019.pbix`
2. Abra com o Power BI Desktop (versão gratuita disponível no site da Microsoft)
3. Explore os filtros interativos nas três páginas

## Prévia do Dashboard

| Página | Visualização |
|--------|--------------|
| Visão Geral | [`03_documentacao/print_pagina1.png`](03_documentacao/print_pagina1.png) |
| Participação | [`03_documentacao/print_pagina2.png`](03_documentacao/print_pagina2.png) |
| Desempenho | [`03_documentacao/print_pagina3.png`](03_documentacao/print_pagina3.png) |


## Contato
- Nome: Vinícius Henrique Souza
- Físico | Mestre em Educação em Ciências | Estudante de Análise de Dados
- email: vinicius.h.zlc@gmail.com
- linkedin: [https://www.linkedin.com/in/vinícius-henrique-souza-17a077218/](https://www.linkedin.com/in/vin%C3%ADcius-henrique-souza-17a077218/)
