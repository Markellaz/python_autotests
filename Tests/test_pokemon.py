import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '14185ffd01e6650e311db69ca62ee35b'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '2396'
TRAINER_NAME = 'Markzy'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID})
    assert response.status_code == 200

def test_trainer_name():
    response_get_trainer_name = requests.get (url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID})
    assert response_get_trainer_name.json()['data'][0]['trainer_name'] == 'Markzy'