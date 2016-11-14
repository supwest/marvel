import pandas as pd
import requests
import json
import os
from datetime import datetime
import hashlib

url ='https://gateway.marvel.com/v1/public/stories?apikey='
public_key = os.environ['MARVEL_PUBLIC_KEY']
private_key = os.environ['MARVEL_PRIVATE_KEY']
base_url = 'https://gateway.marvel.com/v1/public/'

# http://gateway.marvel.com/v1/comics?ts=1&apikey=1234&hash=ffd275c5130566a2916217b101f26150

if __name__ == '__main__':
    ts = str(datetime.utcnow().microsecond)
    full_hash = hashlib.md5(ts+private_key+public_key).hexdigest()
    payload = {
        'ts':ts,
        'apikey':public_key,
        'hash':full_hash
    }
    stuff = requests.get(base_url+'comics', params=payload)
    things = json.loads(stuff.content)
    data = things['data']
    results = data['results']

    character_stuff = requests.get(base_url+'characters', params=payload)
    character_things = json.loads(character_stuff.content)
    character_data = character_things['data']
    c_results = character_data['results']
    
    c_dict = {}

    for res in c_results:
        c_dict[res['id']] = res['name']
