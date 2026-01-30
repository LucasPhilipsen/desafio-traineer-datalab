import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path_alunos = r'C:\Users\ImperadorMaisTemido\Documents\Progamação\Python\datacamp\desafio\dataset_desafio_trainees.csv'
df_alunos = pd.read_csv(path_alunos, sep=";", decimal=",")
notas = df_alunos['nota_final'].to_numpy()

path_dashboard = r'C:\Users\ImperadorMaisTemido\Documents\Progamação\Python\datacamp\desafio\dashboard_alunos.csv'
df_dashboard = pd.read_csv(path_dashboard, sep=";", decimal=",")
valores = df_dashboard['valores'].to_numpy()

ate_dez = df_alunos[df_alunos['horas_estudo'] <= 10]
mais_dez = df_alunos[df_alunos['horas_estudo'] > 10]

plt.boxplot([ate_dez['nota_final'], mais_dez['nota_final']], tick_labels=['estudam até 10h', 'estudam mais de 10h'])

plt.ylabel("Notas Finais")
plt.xlabel("Horas de Estudo")
plt.title("Perfis De esforço")
plt.yticks(np.arange(45, 105, 5))
plt.grid(True, axis="y", linestyle='--', alpha=0.7)

plt.show()
plt.clf()