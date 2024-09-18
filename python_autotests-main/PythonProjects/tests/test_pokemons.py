import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'daedd5902bd43ea650c3b3d8716f9bbc'
HEADER = {'Content-Type': 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '5170'



def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    print(response.text)
    print(requests)
    assert response.status_code == 200
    assert response.json()["data"][0]["id"] == '5170'
    assert response.json()["data"][0]["trainer_name"] == 'Knot'
