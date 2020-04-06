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
            'name': data.get('name'),
            'height': data.get('height'),
            'weight': data.get('weight'),
            'image': data.get('sprites', {}).get('front_default'),
            'stats': data.get('stats',{}).get ('0'),
            'base_experiencie': data.get('base_experiencie'),
            'types': data.get('types',{}).get('0')
}
