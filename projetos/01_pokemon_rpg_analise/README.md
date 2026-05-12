# Projeto de Tratamento da Pokédex para RPG

## 📋 Sobre o Projeto

Pipeline de limpeza e adaptação de dados da Pokédex (gerações 1 a 9) para um sistema de RPG. O projeto padroniza nomes de colunas, trata strings, classifica Pokémon como lendários/míticos/pseudolendários e converte os stats originais para valores balanceados para RPG.

## 🎯 Objetivos

- Padronizar nomes de colunas e valores textuais (minúsculo, sem espaços)
- Classificar Pokémon como lendário, mítico ou pseudolendário
- Ordenar os dados por ID e geração
- Converter stats (HP, Attack, Defense, Sp. Atk, Sp. Def, Speed) para sistema de RPG
- Calcular novo BST (Base Stat Total) adaptado
- Remover colunas desnecessárias após conversão

## 📂 Estrutura do Projeto

- 02_raw/pokedex_raw.csv - Dados brutos da Pokédex
- 02_raw/pokedex_bruno_raw.csv - Dados com classificação de lendários/míticos
- 01_limpeza.py - Script de limpeza e padronização inicial
- 02_adaptacao_pokedex_rpg.py - Script de conversão para RPG
- 03_processed/pokedex.csv - Saída da limpeza (padronizada)
- 03_processed/pokedex_rpg.csv - Saída final (adaptada para RPG)

## 🔧 Etapas do Pipeline

### Script 1: 01_limpeza.py

| Etapa | Descrição |
|-------|-----------|
| Renomear colunas | ID→id, Name→name, Type1→type_1, Total→bst, HP→hp, Attack→atk, Defense→def, Sp. Atk→sp_atk, Sp. Def→sp_def, Speed→spd, Generation→gen |
| Padronização de strings | strip() + lower() em todas as colunas do tipo string |
| Ordenação | Por id e depois por gen |
| Reordenação das colunas | id, gen, name, form, type_1, type_2, hp, atk, def, sp_atk, sp_def, spd, bst |
| Classificação PML | Adiciona coluna 'pml' a partir do segundo arquivo: 'leg' (lendário), 'psd_leg' (pseudolendário), 'myth' (mítico) |

### Script 2: 02_adaptacao_pokedex_rpg.py

| Stat | Multiplicador | Arredondamento |
|------|---------------|----------------|
| HP | x 0.75 | floor(x + 0.5) para inteiro |
| Attack | x 0.05 | floor(x + 0.5) para inteiro |
| Defense | x 0.05 | floor(x + 0.5) para inteiro |
| Sp. Atk | x 0.05 | floor(x + 0.5) para inteiro |
| Sp. Def | x 0.05 | floor(x + 0.5) para inteiro |
| Speed | x 0.10 | floor(x + 0.5) para inteiro |

Após a conversão, o BST original é removido e um novo 'bst_rpg' é calculado como a soma dos seis stats convertidos.

## 📊 Exemplo de Transformação

| Stat | Original (Ex: Charizard) | Convertido (RPG) |
|------|--------------------------|------------------|
| HP | 78 | 59 (78 x 0.75 = 58.5 → 59) |
| Attack | 84 | 4 (84 x 0.05 = 4.2 → 4) |
| Defense | 78 | 4 (78 x 0.05 = 3.9 → 4) |
| Sp. Atk | 109 | 5 (109 x 0.05 = 5.45 → 5) |
| Sp. Def | 85 | 4 (85 x 0.05 = 4.25 → 4) |
| Speed | 100 | 10 (100 x 0.10 = 10) |
| BST original | 534 | - |
| bst_rpg | - | 86 |

## 🚀 Como Executar

Pré-requisitos:
pip install pandas numpy

Organize os arquivos:
Coloque pokedex_raw.csv e pokedex_bruno_raw.csv na pasta 02_raw/

Execute a limpeza:
python 01_limpeza.py

Execute a adaptação para RPG:
python 02_adaptacao_pokedex_rpg.py

Resultados:
- 03_processed/pokedex.csv (dados padronizados)
- 03_processed/pokedex_rpg.csv (dados adaptados para RPG)

## 📌 Observações

- O script trata Pokémon com formas alternativas (ex: Castform, Deoxys, Mega Evoluções)
- A classificação 'pml' pode ficar vazia para Pokémon comuns (sem status especial)
- Os multiplicadores foram definidos para balanceamento de um sistema de RPG específico
- A ordenação por ID e geração garante consistência com a evolução cronológica

## 👤 Autor

vhsouza - 12/05/2026

## 📄 Licença

Uso educacional - Projeto de estudo de limpeza e transformação de dados com pandas.
