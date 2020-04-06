import requests
import json
from random import randrange

class PokeAPI(object):

    def __init__(self):
        self.ENDPOINT = 'https://pokeapi.co/api/v2/pokemon'

    def getPokemon(self, x):
        uri = f'{self.ENDPOINT}/{x}'
        r = requests.get(uri)
        data = r.json()

        return {
            'image': data.get('sprites', {}).get('front_default'),
            'id':data.get('id'),
            'name': data.get('name'),
            'ability': data.get ('ability'),
            'type': data.get('type'),
            'nature': data.get ('nature'),
            'region': data.get('region'),
            'move': data.get('move'),
            'evolution-chain':data.get('evolution-chain'),
            'item':data.get('item'),
            'generation': data.get('generation')
        }


# api = PokeAPI()
# print(json.dumps(api.getPokemon(randrange(10)), indent=2))