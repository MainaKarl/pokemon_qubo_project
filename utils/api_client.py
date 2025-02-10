import requests

BASE_URL = "https://pokeapi.co/api/v2/"

def fetch_pokemon_data(limit=10):
    response = requests.get(f"{BASE_URL}pokemon?limit={limit}")
    if response.status_code != 200:
        raise Exception("Failed to fetch Pokémon list")

    pokemon_list = response.json()["results"]
    pokemon_data = []

    for pokemon in pokemon_list:
        details_response = requests.get(pokemon["url"])
        if details_response.status_code == 200:
            details = details_response.json()
            pokemon_data.append({
                "name": details["name"],
                "types": [t["type"]["name"] for t in details["types"]],
                "hp": details["stats"][0]["base_stat"],
                "attack": details["stats"][1]["base_stat"],
                "defense": details["stats"][2]["base_stat"],
                "speed": details["stats"][5]["base_stat"],
                "weaknesses": []  # Extend to calculate weaknesses
            })
    return pokemon_data
