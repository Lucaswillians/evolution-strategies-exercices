import numpy as np

# Definindo a função de Rosenbrock
def rosenbrock_function(vector):
    x, y = vector
    a, b = 1, 100
    return (a - x)**2 + b * (y - x**2)**2

# Função principal para executar o algoritmo
def run_rosenbrock():
    problem_size = 2
    search_space = [(-2, 2), (-1, 3)]  # Limites do espaço de busca
    max_gens = 100
    pop_size = 30
    num_children = 20

    # Executa a busca
    best = search(max_gens, search_space, pop_size, num_children)
    
    print(f"Melhor solução encontrada: f = {best['fitness']}, s = {best['vector']}")

# Executa o exercício
if __name__ == "__main__":
    run_rosenbrock()
