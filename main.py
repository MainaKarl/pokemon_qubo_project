from utils.api_client import fetch_pokemon_data
from utils.data_utils import calculate_weaknesses
from qubo_solver.qubo_matrix import generate_qubo_matrix
from qubo_solver.qubo_solver import solve_qubo

def main():
    # Step 1: Fetch Pokémon data
    pokemon_data = fetch_pokemon_data(limit=10)

    # Step 2: Add weaknesses to data
    for pokemon in pokemon_data:
        pokemon["weaknesses"] = calculate_weaknesses(pokemon["types"])

    # Step 3: Generate QUBO matrix
    team_size = 6
    qubo_matrix = generate_qubo_matrix(pokemon_data, team_size)

    # Step 4: Solve QUBO
    selected_indices = solve_qubo(qubo_matrix)
    selected_team = [pokemon_data[i] for i in selected_indices]

    # Step 5: Display results
    print("Selected Pokémon Team:")
    for pokemon in selected_team:
        print(f"- {pokemon['name']} ({', '.join(pokemon['types'])})")

if __name__ == "__main__":
    main()
