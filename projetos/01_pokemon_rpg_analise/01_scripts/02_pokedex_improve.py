import pandas as pd
from pathlib import Path

entrada = Path('../03_processed/pokedex.csv')

df = pd.read_csv(entrada)

# adicionar BST
df['bst'] = df[['hp', 'atk', 'def', 'sp_atk', 'sp_def', 'vel']].sum(axis=1)

# Média de status por tipo_1 (com pml)

media_status_tipo1_com_pml = df.groupby('tipo_1')[['hp', 'atk', 'sp_atk', 'def', 'sp_def', 'vel']].mean().round(1).reset_index()

saida = Path('../04_output/media_status_tipo_com_pml.csv')
media_status_tipo1_com_pml.to_csv(saida, index=False)


# Média de status por tipo_1 (sem pml)

df_sem_pml = df[df['pml']=='-']
media_status_tipo1_sem_pml = df_sem_pml.groupby('tipo_1')[['hp', 'atk', 'sp_atk', 'def', 'sp_def', 'vel']].mean().round(1).reset_index()

saida = Path('../04_output/media_status_tipo_sem_pml.csv')
media_status_tipo1_sem_pml.to_csv(saida, index=False)


# Poder ofensivo real (foco no melhor atk)
df['best_atk'] = df[['atk', 'sp_atk']].max(axis=1)

# Indice ofensivo (soma do melhor atk com vel)
df['best_atk_vel'] = df[['best_atk', 'vel']].sum(axis=1)

# Poder ofensivo total (soma dos ataques)
df['atk_tot'] = df[['atk', 'sp_atk']].sum(axis=1)

# Defesa total (soma das defesas)
df['def_tot'] = df[['def', 'sp_def']].sum(axis=1)







saida = Path('../03_processed/pokedex_completa.csv')

df.to_csv(saida, index=False)


print(df.head(10).to_string())






































