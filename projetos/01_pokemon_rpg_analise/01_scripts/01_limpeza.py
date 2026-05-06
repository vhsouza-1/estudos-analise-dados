import pandas as pd
from pathlib import Path

entrada1 = Path('../02_raw/pokedex_raw.csv')

df1 = pd.read_csv(entrada1)

df1 = df1.rename(columns={
    'ID': 'id',
    'Name': 'name',
    'Form': 'form',
    'Type1': 'type_1',
    'Type2': 'type_2',
    'Total': 'bst',
    'HP': 'hp',
    'Attack': 'atk',
    'Defense': 'def',
    'Sp. Atk': 'sp_atk',
    'Sp. Def': 'sp_def',
    'Speed': 'spd',
    'Generation': 'gen'
})

for coluna in df1.columns:
    if df1[coluna].dtype == 'str':
        df1[coluna] = df1[coluna].str.lower().str.strip()

df1 = df1.sort_values(['id', 'gen']).reset_index(drop=True)

df1 = df1[['id', 'gen', 'name', 'form', 'type_1', 'type_2', 'hp', 'atk', 'def', 'sp_atk', 'sp_def', 'spd', 'bst']]

entrada2 = Path('../02_raw/pokedex_bruno_raw.csv')
df2 = pd.read_csv(entrada2)

df1['pml'] = df2['Pseudo/Mítico/ Lendário']
df1['pml'] = df1['pml'].str.lower().str.strip()

dict_pml = {
    'lendário': 'leg',
    'pseudoendário': 'psd_leg',
    'mítico': 'myth'
}

df1['pml'] = df1['pml'].replace(dict_pml)
df1['pml'] = df1['pml'].fillna('')

saida = Path('../03_processed/pokedex.csv')
df1.to_csv(saida, index=False)

input("\nPressione ENTER para sair...")








































































































