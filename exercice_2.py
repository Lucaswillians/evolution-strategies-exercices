import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# Função que gera um conjunto de dados de exemplo
def generate_data(n_samples=100):
    X = np.random.rand(n_samples, 1) * 10  # Característica aleatória
    y = 2 * X.flatten() + np.random.randn(n_samples) * 2  # Criando um alvo linear
    return X, y

# Função para avaliar o modelo com os parâmetros dados
def evaluate_model(params, X_train, y_train):
    alpha, learning_rate = params
    model = LinearRegression()  # Modelo de Regressão Linear
    model.fit(X_train, y_train)
    
    # Fazendo previsões e avaliando o modelo
    predictions = model.predict(X_train)
    return mean_squared_error(y_train, predictions)  # Retorna o MSE

# Função principal para executar o algoritmo
def run_parameter_optimization():
    # Gerando dados de exemplo
    X, y = generate_data()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Definindo limites para os hiperparâmetros
    search_space = [(0.01, 1.0), (0.001, 0.1)]  # [alpha, learning_rate]
    max_gens = 100
    pop_size = 30
    num_children = 20

    # Executa a busca
    best = search(max_gens, search_space, pop_size, num_children)
    
    print(f"Melhor solução encontrada: MSE = {best['fitness']}, parâmetros = {best['vector']}")

# Executa o exercício
if __name__ == "__main__":
    run_parameter_optimization()
