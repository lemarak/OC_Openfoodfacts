# coding: utf-8
"""
script to import data from API
and fill the bdd
"""
import requests
import sys  # to delete

from db.database import DataBaseOC
from openfoodfacts.category import Category
from openfoodfacts.product import Product
from openfoodfacts.category import CatProd

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
    print("Categories - Status code:", res.status_code)
    contents = res.json()
    # delete duplicates
    contents_unique = list({v['id']: v for v in contents['tags']}.values())
    # create list of Category to insert in bdd
    categories = [Category(**content) for content in contents_unique]
    my_db.insert_multi_rows(categories)

    # products by category
    categories = [data for data in categories
                  if data.id_category in c.CATEGORIES_VISIBLE]
    for category in categories:
        str_requests = "https://fr.openfoodfacts.org/cgi/search.pl? \
                          action=process& \
                          tagtype_0=categories& \
                          tag_contains_0=contains& \
                          tag_0=%s& \
                          sort_by=unique_scans_n& \
                          page_size=100& \
                          json=1& \
                          page=1" % (category.id_category)
        res = requests.get(str_requests.replace(" ", ""))
        print("Products from {} - Status code: {}".format(
            category.name,
            res.status_code))
        contents = res.json()
        # delete duplicates
        contents_unique = list(
            {v['_id']: v for v in contents['products']}.values())
        products = [Product(category.id_category, **content)
                    for content in contents_unique
                    if Product.check_all_fields(content)]
        my_db.insert_multi_rows(products)

        # insert into cat_prod
        cat_prod = [CatProd(
            **{"id_category": category.id_category,
               "id_product": product.id_product})
            for product in products]
        my_db.insert_multi_rows(cat_prod)


if __name__ == "__main__":
    main()
