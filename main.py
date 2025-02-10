from utils.api_client import fetch_pokemon_data
from qubo_solver.qubo_matrix import generate_qubo_matrix
from qubo_solver.qubo_solver import solve_qubo
from visualization.qubo_heatmap import visualize_qubo_matrix
from visualization.team_distribution import visualize_team_distribution  # Import the team distribution visualization

def main():
    # Step 1: Fetch Pokémon data
    pokemon_dataset = fetch_pokemon_data(limit=10)

    # Step 2: Generate the QUBO matrix
    team_size = 6
    qubo_matrix = generate_qubo_matrix(pokemon_dataset, team_size)

    # Step 3: Visualize the QUBO matrix
    print("Visualizing the QUBO matrix...")
    visualize_qubo_matrix(qubo_matrix, labels=[pokemon["name"] for pokemon in pokemon_dataset])

    # Step 4: Solve the QUBO problem
    selected_team_indices = solve_qubo(qubo_matrix)

    # Step 5: Print the selected Pokémon team
    selected_team = [pokemon_dataset[i] for i in selected_team_indices]
    print("Selected Pokémon Team:")
    for pokemon in selected_team:
        print(f"- {pokemon['name']} ({', '.join(pokemon['types'])})")

    # Step 6: Visualize the team type distribution
    print("Visualizing the team type distribution...")
    visualize_team_distribution(selected_team)

if __name__ == "__main__":
    main()
