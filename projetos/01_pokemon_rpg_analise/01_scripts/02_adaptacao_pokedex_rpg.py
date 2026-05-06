import pandas as pd
from pathlib import Path
import numpy as np

# Ler arquivo pokedex processada
entrada = Path('../03_processed/pokedex.csv')
df = pd.read_csv(entrada)

# Converter hp da Pokedex (taxa x0.75)
df['hp'] = df['hp'] * 0.75

# Converter atk, def, sp_atk, sp_def da Pokedex (taxa * 0.05)
df['atk'] = df['atk'] * 0.05
df['sp_atk'] = df['sp_atk'] * 0.05
df['def'] = df['def'] * 0.05
df['sp_def'] = df['sp_def'] * 0.05

# Converter spd da Pokedex (taxa * 0.10)
df['spd'] = df['spd'] * 0.10

# Arredondar para cima e transformar em inteiro
for stats in df[['hp', 'atk', 'def', 'sp_atk', 'sp_def', 'spd']]:
    df[stats] = np.floor(df[stats] + 0.5).astype(int)

# dropar BST antigo
df = df.drop('bst', axis=1)

# Calcular novo BST
df['bst_rpg'] = df[['hp', 'atk', 'def', 'sp_atk', 'sp_def', 'spd']].sum(axis=1)

# Salvar pokedex adapatada para rpg
saida = Path('../03_processed/pokedex_rpg.csv')

df.to_csv(saida, index=False)

