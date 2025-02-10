import seaborn as sns
import matplotlib.pyplot as plt

def visualize_qubo_matrix(qubo_matrix, labels=None):
    """
    Generates a heatmap visualization of the QUBO matrix.
    
    Args:
        qubo_matrix (list[list[float]]): The QUBO matrix to visualize.
        labels (list[str]): Optional labels for the axes.
    """
    plt.figure(figsize=(10, 8))
    sns.heatmap(
        qubo_matrix,
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        xticklabels=labels,
        yticklabels=labels
    )
    plt.title("QUBO Matrix Heatmap")
    plt.xlabel("Variables")
    plt.ylabel("Variables")
    plt.show()
