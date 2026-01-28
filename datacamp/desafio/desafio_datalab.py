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
print(f' Média: {np.mean(notas):.2f}')
print(f' Mediana: {np.median(notas):.2f}')
print(f'Desvio padrão: {np.std(notas):.2f}')
print(f'Quartil 25%: {np.percentile(notas, 25):.2f}')
print(f'Quartil 50%: {np.percentile(notas, 50):.2f}')
print(f'Quartil 75%: {np.percentile(notas, 75):.2f}\n')
print(f'tipos de dados das colunas: \n {df_alunos.dtypes} \n')

path_dashboard = r'C:\Users\ImperadorMaisTemido\Documents\Progamação\Python\datacamp\desafio\dashboard_alunos.csv'
df_dashboard = pd.read_csv(path_dashboard, sep=";", decimal=",")
valores = df_dashboard['valores'].to_numpy()
media_excel = valores[0].round(2)
print(f' Comparativo Estatístico Média, Mediana e Quartis\n\
        excel | python\n\
        {valores[0]:.2f} | {np.mean(notas):.2f}\n\
        {valores[1]:.2f} | {np.median(notas):.2f}\n\
        {valores[3]:.2f} | {np.percentile(notas, 25):.2f}\n\
        {valores[4]:.2f} | {np.percentile(notas, 50):.2f}\n\
        {valores[5]:.2f} | {np.percentile(notas, 75):.2f}\n\
    ')

print(f'correlação: Horas de estudo x Nota final \n {df_alunos["horas_estudo"].corr(df_alunos["nota_final"]):.4f} \n ')
print(f'correlação: Aulas assistidas x Nota final \n {df_alunos["aulas_assistidas"].corr(df_alunos["nota_final"]):.4f} \n ')

# A Correlção mais proxima do valor 1 é a que possui mais impacto/efetividade. Após analisar os resultados das correlações é possivel notar que as 'Horas de estudo' tem maior relação com a nota final, ou seja quanto mais tempo estuda maior a nota final será, este é o pensamento estatistico correto, entretanto a diferença de 0.002 é insignificante, acredito que seja necessário mais dados para se tirar uma melhor conclusão.
# Horas de estudo: 0.996
# Aulas assistidas: 0.994

ate_dez = df_alunos[df_alunos['horas_estudo'] <= 10]
mais_dez = df_alunos[df_alunos['horas_estudo'] > 10]

print(f'{len(ate_dez)} alunos estudam ate 10h e a media de suas notas eh: {ate_dez['nota_final'].mean():.2f}')
print(f'{len(mais_dez)} alunos estudam mais de 10h e a media de suas notas eh: {mais_dez['nota_final'].mean():.2f}')

notas_ate_dez = ate_dez['nota_final']
notas_mais_dez = mais_dez['nota_final']

plt.boxplot([notas_ate_dez, notas_mais_dez], labels=['até 10h', 'mais de 10h'])

plt.ylabel("Notas Finais")
plt.xlabel("Horas de Estudo")
plt.title("Perfis De esforço")
plt.yticks(np.arange(45, 100, 5))
plt.grid(True, axis="y", linestyle='--', alpha=0.7)

plt.show()
plt.clf()

# Apos a visualização do grafico fica mais evidente que nenhum aluno que estuda até 10h tirou uma nota superior a um aluno que estuda mais de 10h, e a escolha de grafico foi priorizando a clareza nessa diferença como se pode ver