import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '14185ffd01e6650e311db69ca62ee35b'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
BODY_REGISTRATION = {
    "trainer_token": "14185ffd01e6650e311db69ca62ee35b",
    "email": "Markovantony763@yandex.ru",
    "password": "A123456"
}
BODY_CONFIRMATION = {
    "trainer_token": "14185ffd01e6650e311db69ca62ee35b"
}
BODY_CREATE_POKEMON = {
    "name": "Бульбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}
BODY_POKEMON_NAME_CHANGE = {
    "pokemon_id": "26999",
    "name": "Бульбашуба",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}
BODY_POKEMON_CATCH_POKEBALL = {
    "pokemon_id": "26999"
}

#response_trainer_registration = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = BODY_REGISTRATION)
#print(response_trainer_registration.text)

#response_trainer_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = BODY_CONFIRMATION)
#print(response_trainer_confirmation.text)


#response_list_of_coaches = requests.get(url = f'{URL}/trainers')
#print(response_list_of_coaches.text)

#responce_create_pokemon = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = BODY_CREATE_POKEMON)
#print(responce_create_pokemon.text)

#responce_pokemon_name_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = BODY_POKEMON_NAME_CHANGE)
#print(responce_pokemon_name_change.text)
responce_pokemon_catch_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = BODY_POKEMON_CATCH_POKEBALL)
print(responce_pokemon_catch_pokeball.text)