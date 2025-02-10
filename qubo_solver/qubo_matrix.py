import numpy as np

def generate_qubo_matrix(pokemon_data, team_size):
    n = len(pokemon_data)
    qubo_matrix = np.zeros((n, n))

    # Team size constraint: Enforce exactly `team_size` Pokémon
    for i in range(n):
        qubo_matrix[i, i] -= (2 * team_size - 1)

    # Type diversity constraint: Penalize overlapping types
    for i in range(n):
        for j in range(i + 1, n):
            if set(pokemon_data[i]["types"]) & set(pokemon_data[j]["types"]):
                qubo_matrix[i, j] += 2
                qubo_matrix[j, i] += 2

    return qubo_matrix
