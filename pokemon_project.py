# check out this Pokemon API https://pokeapi.co/
# Use the requests package to connect to this API and get and store data for 5 different pokemon.
# Get the pokemons: name, atleast one ability's name, base_experience, and the URL for 
# its sprite (an image that shows up on screen) for the 'front_shiny', attack base_state,
# hp base_stat, defense base_stat


from urllib import response
import requests
# url = "https://pokeapi.co/api/v2/pokemon/ditto"
# renponse  = requests.get(url)
# print(renponse)
# renponse.ok
# renponse.json()
# type(renponse.json())
# data = renponse.json()
# ditto_ability = data['abilities'][1]
# ditto = data['forms'][0]['name']
# ditto_exp = data['base_experience']
# ditto_sprite = 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/132.png'
# ditto_stats_hp = data['stats'][0]
# ditto_stats_attack = data['stats'][1]
# ditto_stats_defense = data['stats'][2]
def pokemon(name):
    get_pokemon_info = f"https://pokeapi.co/api/v2/pokemon/{name}"
    response = requests.get(get_pokemon_info)
    data = response.json()
    
    pokemon_info = {
        'name': data['forms'][0]['name'],
        'abilities': data['abilities'][1]['ability']['name'],
        'base_exp': data['base_experience'],
        'sprite': data['sprites']['front_shiny'],
        'attack': data['stats'][1]['base_stat'],
        'h_p': data['stats'][0]['base_stat'],
        'def': data['stats'][2]['base_stat']
    }
    return pokemon_info
    

print(pokemon('ditto'))
print(pokemon('charmander'))
print(pokemon('squirtle'))
print(pokemon('raichu'))
print(pokemon('salamence'))