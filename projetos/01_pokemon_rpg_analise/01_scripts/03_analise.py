import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

entrada = Path('../03_processed/pokedex_completa.csv')

df = pd.read_csv(entrada)

# Média de status por tipo_1 (com pml)

media_status_tipo1_com_pml = df.groupby('tipo_1')[['hp', 'atk', 'sp_atk', 'def', 'sp_def', 'vel', 'bst', 'best_atk', 'best_atk_vel', 'atk_tot', 'def_tot']].mean().round(1).reset_index()

saida = Path('../04_output/media_status_tipo_com_pml.csv')
media_status_tipo1_com_pml.to_csv(saida, index=False)


# Média de status por tipo_1 (sem pml)

df_sem_pml = df[df['pml']=='-']
media_status_tipo1_sem_pml = df_sem_pml.groupby('tipo_1')[['hp', 'atk', 'sp_atk', 'def', 'sp_def', 'vel', 'bst', 'best_atk', 'best_atk_vel', 'atk_tot', 'def_tot']].mean().round(1).reset_index()

saida = Path('../04_output/media_status_tipo_sem_pml.csv')
media_status_tipo1_sem_pml.to_csv(saida, index=False)


