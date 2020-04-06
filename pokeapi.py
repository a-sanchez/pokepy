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
            'abilities': data.get ('abilities'),
            'height': data.get('heigth'),
            'weight': data.get('weight'),
            'moves': data.get('moves',{}).get('name'),
            'species':data.get('species',{}).get('name'),
            'stats':data.get('stats',{}).get('base_stat'),
            'order':data.get('order')
}

