# coding: utf-8

import requests

res = requests.get("https://fr.openfoodfacts.org/categories.json")

print(res.status_code)