#!/usr/bin/env python3

import requests

response = requests.get('https://swapi.co/api/starships')
if response.status_code == 200:
    #type dic
    print(type(response.json()))
else:
    print(response.status_code)