import matplotlib.pyplot as plt
from collections import Counter

def visualize_team_distribution(selected_team):
    """
    Visualizes the type distribution of the selected Pokémon team.
    
    Args:
        selected_team (list[dict]): List of selected Pokémon with their details.
    """
    # Count Pokémon types
    type_counts = Counter()
    for pokemon in selected_team:
        type_counts.update(pokemon["types"])

    # Plot the type distribution
    plt.figure(figsize=(8, 6))
    plt.bar(type_counts.keys(), type_counts.values(), color="skyblue")
    plt.title("Selected Team Type Distribution")
    plt.xlabel("Pokémon Types")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
