# coding: utf-8
"""
script to import data from API
and fill the bdd
"""
import requests

from db.database import DataBaseOC
from openfoodfacts.category import Category
from openfoodfacts.product import Product

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
    categories = [Category(**content) for content in contents['tags']
                  if content['id'] in c.CATEGORIES_VISIBLE]
    print(len(categories))
    my_db.insert_multi_rows(categories)

    # products by category
    for category in categories:
        str_requests = "https://fr.openfoodfacts.org/cgi/search.pl? \
                          action=process& \
                          tagtype_0=categories& \
                          tag_contains_0=contains& \
                          tag_0=%s& \
                          sort_by=unique_scans_n& \
                          page_size=20& \
                          json=1& \
                          page=1" % (category.id_category)
        res = requests.get(str_requests.replace(" ", ""))
        print("Status code:", res.status_code)
        contents = res.json()
        products = [Product(**content) for content in contents['products']
                    if Product.check_all_fields(content)]
        my_db.insert_multi_rows(products)

        # insert into cat_prod



if __name__ == "__main__":
    main()
