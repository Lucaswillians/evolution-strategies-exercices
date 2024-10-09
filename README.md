## Exercícios sobre estratégias evolutivas

## Exercício 1: Problema Clássico - Função de Rosenbrock

Descrição
- A função de Rosenbrock, frequentemente chamada de "função do banana", é um problema de otimização bem conhecido na literatura. A função é definida como:
- ![Captura de Tela 2024-10-08 às 22 07 03](https://github.com/user-attachments/assets/c5615cb6-577a-4412-945a-538bdbe3a8cc)

Objetivo
- Utilizar o algoritmo de Estratégias Evolutivas para encontrar o ponto mínimo da função de Rosenbrock.

Documentação
- Função objetivo: A função de Rosenbrock é uma função contínua que apresenta um mínimo global em um vale estreito. O objetivo é encontrar esse mínimo utilizando o algoritmo de Estratégias Evolutivas.
- Espaço de busca: O espaço de busca foi escolhido como (-2, 2) para x e (-1, 3) para y, permitindo que o algoritmo explore a região ao redor do mínimo global.
- Resultado esperado: O algoritmo deve convergir para a solução, (1, 1), (1,1) ao longo das gerações.

##

## Exercício 2: Problema Prático - Otimização de Parâmetros de um Modelo de Machine Learning

Descrição
- Neste exercício, os alunos devem otimizar os hiperparâmetros de um modelo de regressão linear, como a regularização (parâmetro α (alpha)) e a taxa de aprendizado. O objetivo é minimizar o erro quadrático médio (MSE) de um conjunto de dados de treinamento.

Objetivo
- Utilizar o algoritmo de Estratégias Evolutivas para otimizar os hiperparâmetros de um modelo de machine learning.

Documentação
- Objetivo do exercício: Os alunos devem otimizar os hiperparâmetros de um modelo de regressão linear para minimizar o erro quadrático médio em um conjunto de dados sintéticos.
- Espaço de busca: O espaço de busca foi definido com limites para a regularização α (alpha) e a taxa de aprendizado, permitindo que o algoritmo explore combinações desses parâmetros.
- Resultado esperado: O algoritmo deve encontrar uma combinação de parâmetros que minimize o MSE no conjunto de treinamento, resultando em um modelo de regressão linear mais eficiente.
