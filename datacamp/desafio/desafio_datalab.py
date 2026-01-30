"""
Análise Estatística dos Alunos Trainees
Desafio DataLab - DataCamp
Neste desafio, foi realizado uma análise estatística descritiva dos dados de desempenho dos alunos trainees de um programa de formação. O objetivo é extrair insights relevantes sobre o desempenho dos alunos com base nas notas finais, horas de estudo e número de aulas assistidas.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path_alunos = r'C:\Users\ImperadorMaisTemido\Documents\Progamação\Python\datacamp\desafio\dataset_desafio_trainees.csv'

df_alunos = pd.read_csv(path_alunos, sep=";", decimal=",")

notas = df_alunos['nota_final'].to_numpy()
print(f'Média: {np.mean(notas):.2f}\nMediana: {np.median(notas):.2f}\nDesvio padrão: {np.std(notas):.2f}\n')
print(f'Quartil 25%: {np.percentile(notas, 25):.2f}')
print(f'Quartil 50%: {np.percentile(notas, 50):.2f}')
print(f'Quartil 75%: {np.percentile(notas, 75):.2f}\n')
print(f'tipos de dados das colunas: \n{df_alunos.dtypes} \n')

path_dashboard = r'C:\Users\ImperadorMaisTemido\Documents\Progamação\Python\datacamp\desafio\dashboard_alunos.csv'

df_dashboard = pd.read_csv(path_dashboard, sep=";", decimal=",")

valores = df_dashboard['valores'].to_numpy()
print(f' Comparativo Estatístico Média, Mediana e Quartis\n\
        excel | python\n\
        {valores[0]:.2f} | {np.mean(notas):.2f}\n\
        {valores[1]:.2f} | {np.median(notas):.2f}\n\
        {valores[3]:.2f} | {np.percentile(notas, 25):.2f}\n\
        {valores[4]:.2f} | {np.percentile(notas, 50):.2f}\n\
        {valores[5]:.2f} | {np.percentile(notas, 75):.2f}\n\
    ')

print(f'correlação: \n\
      Horas de estudo x Nota final: {df_alunos["horas_estudo"].corr(df_alunos["nota_final"]):.4f} \n\
      Aulas assistidas x Nota final: {df_alunos["aulas_assistidas"].corr(df_alunos["nota_final"]):.4f} \n ')

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