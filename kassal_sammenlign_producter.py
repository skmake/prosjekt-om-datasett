import requests as req
import os
from dotenv import load_dotenv
import time
import json

load_dotenv()

API_KEY = os.getenv('kassal_api_key')
HEADERS = {'Authorization': f'Bearer {API_KEY}'}

'''
Mest relevante ruter:
https://kassal.app/api/v1/products/ean/{ean} - Henter produktet med den angivne EAN-kode i butikkene som har dette
https://kassal.app/api/v1/products/find-by-url/compare?url='url' - Finder produktet med den angivne URL og sammenligner det med de andre produkter i databasen

eksemepel url = 'https://meny.no/varer/middag/pizza/pizza/grandiosa-pizza-7039010019804'

Disse to rutene gjør egentlig det samme, men den ene bruker EAN-kode og den andre bruker URL.

Kanskje fuzzy search blir relevant også... (er en egen rute)
'''

def return_prodct(user_input):
    # Sørger for at brukeren ikke spammer API-et fordi max er 60 requests per minutt
    time.sleep(1)
    # Sjekker om brukeren har skrevet inn en URL eller EAN-kode
    if "https://" in user_input:
        url = user_input
        r = req.get(f"https://kassal.app/api/v1/products/find-by-url/compare?url={url}", headers=HEADERS)
    else:
        ean = user_input
        r = req.get(f"https://kassal.app/api/v1/products/ean/{ean}", headers=HEADERS)
    return r.json()

url = 'https://meny.no/varer/middag/pizza/pizza/grandiosa-pizza-7039010019804'
ean = '7039010019804'
'''
with open('produkter.json', 'a+', encoding='utf-8') as f:
    product_data = return_prodct(url)
    print(json.dumps(product_data, indent=2))
    json.dump(product_data, f, indent=2)
    f.write('\n')
'''
    
with open('produkter.json', 'r', encoding='utf-8-sig') as f:
    product = f.read()
    print(product)