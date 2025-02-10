import numpy as np

def solve_qubo(qubo_matrix):
    n = len(qubo_matrix)
    best_solution = None
    best_energy = float("inf")

    # Simulated annealing (simplified)
    for _ in range(1000):  # Number of iterations
        solution = np.random.randint(0, 2, size=n)
        energy = solution @ qubo_matrix @ solution.T
        if energy < best_energy:
            best_energy = energy
            best_solution = solution

    # Return indices of selected Pokémon
    selected_indices = [i for i in range(n) if best_solution[i] == 1]
    return selected_indices
