# **Desafio Trainee: Análise de Desempenho Estudantil**
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/Lucas-Philipsen-Borges/)
![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=flat&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=flat&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=flat&logo=Matplotlib&logoColor=black)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=flat&logo=scikit-learn&logoColor=white)
![Status](https://img.shields.io/badge/Status-Em_Desenvolvimento-yellow)

Este projeto consiste na análise estatística e preditiva de dados de alunos em uma plataforma de educação online. O objetivo principal é identificar padrões de estudo que impactam a nota final e construir um modelo de regressão para prever o desempenho acadêmico.

## Tecnologias Utilizadas
* **Python 3**.
* **Pandas**: Manipulação e limpeza de dados.
* **NumPy**: Cálculos estatísticos avançados.
* **Matplotlib**: Visualização de dados e análise de distribuição.
* **Scikit-Learn**: Implementação de modelos de Machine Learning.



## Etapas do Projeto

### 1. Exploração e Validação (Excel vs Python)
fiz uma validação entre os cálculos manuais feitos em Excel e o processamento automatizado em Python.

| Métrica  | Resultado Excel | Resultado Python | 
| :--- | :---: | :---: |
| Média    |      73.67      |       73.67      | 
| Mediana  |      74.50      |       74.50      | 
| Q1 (25%) |      62.75      |       62.75      |

### 2. Estatísticas Descritivas
Desvio Padrão: Com um desvio padrao da nota final sendo 13,95 e a média 73,67 de acordo com o Coeficiente de Variação (CV) é considerado um grau de dispersão médio/baixo, ou seja, a turma não é muito homogênea.
Mediana vs. Média: Se a média for muito menor que a mediana, poucos alunos com notas muito baixas estão "puxando" o desempenho do grupo para baixo, como a diferença entre estes é pouca não há com oque se preocupar com alunos que despencam a média.

### 3. Análise de Correlação
A Correlção mais proxima a 1 mostra uma associação linear fortíssima entre as variáveis, a forte relação linear sugere que as variáveis são bons preditores, mas não isolam a causa raiz da nota final. Devido à diferença mínima (0.002), nota-se uma redundância entre as variáveis. Para modelos futuros, recomenda-se a simplificação ou a inclusão de variáveis ainda não contabilizadas (como histórico escolar) para capturar nuances que as horas de estudo sozinhas não explicam.
* **Horas de Estudo vs Nota Final**: 0.9965 
* **Aulas Assistidas vs Nota Final**: 0.9942

### 4. Teste de Hipótese e Escolha de Amostras
**Hipótese:** Alunos que estudam mais de 10 horas por semana apresentam média superior.

**Metodologia de Amostragem:**
* Apos a visualização do grafico fica mais evidente que nenhum aluno que estuda até 10h tirou uma nota superior a um aluno que estuda mais de 10h, e a escolha de grafico foi priorizando a clareza nessa diferença como se pode ver, coloquei o gráfico aqui para melhor visualização:

![Gráfico](https://github.com/user-attachments/assets/68719a25-5706-4684-8b90-19db4df02f0b)


---

## Etapa 5: Regressão Linear (Em desenvolvimento)
O próximo passo é a implementação de um modelo preditivo para estimar a `nota_final`.
1. Treinamento do modelo via `LinearRegression`. 
2. Avaliação por métricas de erro (MSE, MAE e R²).
