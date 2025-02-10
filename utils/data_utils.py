TYPE_WEAKNESSES = {
    "fire": ["water", "rock", "ground"],
    "water": ["electric", "grass"],
    "grass": ["fire", "flying", "ice", "poison"],
    "electric": ["ground"],
    # Add all types and their weaknesses here
}

def calculate_weaknesses(types):
    weaknesses = set()
    for t in types:
        weaknesses.update(TYPE_WEAKNESSES.get(t, []))
    return list(weaknesses)
