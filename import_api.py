# coding: utf-8
"""
script to import data from API
and fill the bdd
"""
import requests
import json

from db.database import DataBaseOC
from common import config as c


def main():
    """
    main function
    """

    # connect to the db
    param_connect = {'username': c.USER_NAME,
                     'password': c.PWD,
                     'database': c.DB_NAME}
    my_db = DataBaseOC(**param_connect)

    # all categories
    res = requests.get('https://fr.openfoodfacts.org/categories.json')
    print("Status code:", res.status_code)
    contents = res.json()
    for content in contents['tags']:

        # clean the json for insert
        content['id_category'] = content.pop('id')
        content['nb_products'] = content.pop('products')
        del content['known']
        if 'sameAs' in content:
            del content['sameAs']

        # test if the category must be visible
        if content['id_category'] in c.CATEGORIES_VISIBLE:
            content['visible'] = 1
        my_db.insert_json('categories', content)


if __name__ == "__main__":
    main()
