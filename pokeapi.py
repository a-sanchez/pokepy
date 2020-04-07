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
            'pokedex': data.get('id'),            
            'order': data.get('order'),
            'name': data.get('name'),
            'height': data.get('height'),
            'weight': data.get('weight'),
            'image': data.get('sprites', {}).get('front_default'),
            'stats': [i.get('stat',{}).get('name') for i in data.get('stats')],
            'game_indices': [i.get('version',{}).get('name') for i in data.get('game_indices')],
            'types': [i.get('type',{}).get('name') for i in data.get('types')]
            

}
