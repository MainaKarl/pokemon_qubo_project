# Pokémon Team Selection using QUBO Algorithm

## Overview
This project demonstrates how to use a Quadratic Unconstrained Binary Optimization (QUBO) algorithm to optimize the selection of a balanced Pokémon team. The solution utilizes quantum-inspired computing principles and simulated annealing to solve the problem, while fetching Pokémon data dynamically via the PokéAPI or using an offline dataset.

## Features
- Fetches Pokémon data (types, strengths, weaknesses) from the PokéAPI.
- Processes data to calculate weaknesses and strengths for team balance.
- Utilizes a QUBO matrix to formulate team selection constraints.
- Solves the QUBO problem using simulated annealing for optimal team selection.
- Outputs a balanced Pokémon team based on selected constraints (e.g., type coverage).

## File Structure
```
project-root/
|-- data/
|   |-- pokemon_dataset.json       # Offline dataset for Pokémon data
|
|-- qubo_solver/
|   |-- qubo_matrix.py            # Generates the QUBO matrix
|   |-- qubo_solver.py            # Solves the QUBO problem using simulated annealing
|
|-- utils/
|   |-- api_client.py             # Fetches data from the PokéAPI
|   |-- data_utils.py             # Processes Pokémon data and calculates type weaknesses
|
|-- main.py                       # Orchestrates the entire process
|-- requirements.txt              # Project dependencies
|-- .gitignore                    # Files and folders to be ignored in Git
|-- README.md                     # Project documentation (this file)
```

## Setup Instructions

### Prerequisites
- Python 3.8+
- `pip` (Python package installer)

### Installation
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd project-root
   ```

2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### PokéAPI Setup
If using the PokéAPI to fetch live data, ensure you have internet access.

### Offline Dataset
If using the offline dataset, ensure `data/pokemon_dataset.json` is populated.

## Usage
1. Run the main script:
   ```bash
   python main.py
   ```
2. Follow the prompts to select constraints (e.g., team size, type preferences).
3. The script outputs the optimized Pokémon team.

## How It Works
1. **Fetch or Load Data**: 
   - The `api_client.py` script fetches live data from the PokéAPI.
   - Alternatively, data is loaded from `pokemon_dataset.json`.

2. **Process Data**: 
   - The `data_utils.py` script calculates type strengths and weaknesses.

3. **Generate QUBO Matrix**: 
   - The `qubo_matrix.py` script constructs the QUBO matrix based on constraints such as type diversity, coverage, and balance.

4. **Solve QUBO**: 
   - The `qubo_solver.py` script uses simulated annealing to solve the QUBO problem and output an optimal team.

## Example Output
```
Optimal Team:
1. Pikachu (Electric)
2. Charizard (Fire/Flying)
3. Bulbasaur (Grass/Poison)
4. Squirtle (Water)
5. Gengar (Ghost/Poison)
```

## Customization
- Update the constraints in `qubo_matrix.py` to modify the team selection logic.
- Use different parameters in `qubo_solver.py` to adjust the optimization process.

## Dependencies
- `requests`: For fetching data from the PokéAPI.
- `numpy`: For matrix and numerical computations.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
- [PokéAPI](https://pokeapi.co/): For providing Pokémon data.
- Quantum computing principles and QUBO optimization techniques.

---
Feel free to reach out for any questions or collaboration!