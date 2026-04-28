import pandas as pd
from pathlib import Path

entrada = Path('../02_raw/pokedex_raw.csv')

df = pd.read_csv(entrada)

df = df.rename(columns={
    'Geração': 'gen',
    'ID': 'id',
    'Nome': 'nome',
    'Forma': 'forma',
    'Estágio': 'estagio',
    'Tipo 1': 'tipo_1',
    'Tipo 2': 'tipo_2',
    'HP': 'hp',
    'Ataque': 'atk',
    'Ataque Especial': 'sp_atk',
    'Defesa': 'def',
    'Defesa Especial': 'sp_def',
    'Velocidade': 'vel',
    'Pseudo/Mítico/ Lendário': 'pml'
})

df['nome'] = df['nome'].str.strip().str.lower()
df['forma'] = df['forma'].str.strip().str.lower()
df['tipo_1'] = df['tipo_1'].str.strip().str.lower()
df['tipo_2'] = df['tipo_2'].str.strip().str.lower()
df['pml'] = df['pml'].str.strip().str.lower()

df['pml'] = df['pml'].map({'pseudoendário': 'pseudo', 'lendário': 'lend', 'mítico': 'mit'})

tipos = {
    'aço': 'aco',
    'dragão': 'dragao',
    'psíquico': 'psiquico',
    'elétrico': 'eletrico',
    'água': 'agua'
}

df['forma'] = df['forma'].fillna('-')
df['estagio'] = df['estagio'].fillna('-')
df['tipo_2'] = df['tipo_2'].fillna('-')
df['pml'] = df['pml'].fillna('-')

df['tipo_1'] = df['tipo_1'].replace(tipos)
df['tipo_2'] = df['tipo_2'].replace(tipos)

saida = Path('../03_processed/pokedex.csv')
df.to_csv(saida, index=False)










































































































