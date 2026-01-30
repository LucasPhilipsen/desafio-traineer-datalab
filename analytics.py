import numpy as np
from data_loader import valores, notas, df_alunos

show_statistics = print(f'\
Média: {np.mean(notas):.2f}\nMediana: {np.median(notas):.2f}\nDesvio padrão: {np.std(notas):.2f}\n\
Quartil 25%: {np.percentile(notas, 25):.2f}\n\
Quartil 50%: {np.percentile(notas, 50):.2f}\n\
Quartil 75%: {np.percentile(notas, 75):.2f}\n\n\
tipos de dados das colunas: \n{df_alunos.dtypes} \n\n\
    ')

show_comparasions = print(f'\
 Comparativo Estatístico Média, Mediana e Quartis\n\
        excel | python\n\
        {valores[0]:.2f} | {np.mean(notas):.2f}\n\
        {valores[1]:.2f} | {np.median(notas):.2f}\n\
        {valores[3]:.2f} | {np.percentile(notas, 25):.2f}\n\
        {valores[4]:.2f} | {np.percentile(notas, 50):.2f}\n\
        {valores[5]:.2f} | {np.percentile(notas, 75):.2f}\n\
    ')

show_correlations = print(f'\
correlação: \n\
      Horas de estudo x Nota final: {df_alunos["horas_estudo"].corr(df_alunos["nota_final"]):.4f} \n\
      Aulas assistidas x Nota final: {df_alunos["aulas_assistidas"].corr(df_alunos["nota_final"]):.4f} \n ')