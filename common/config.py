# coding: utf-8

"""
CONSTANTS for program
"""

# Database
HOST = 'localhost'
USER_NAME = 'oc_projet5'
PWD = 'OC123456'
DB_NAME = 'oc_openfoodfacts'

# Fields
FIELDS_CATEGORY = ['id_category',
                   'name',
                   'nb_products',
                   'url',
                   'visible']
FIELDS_PRODUCTS = ['id_product',
                   'name',
                   'nutriscore_score',
                   'nutriscore_grade',
                   'magasins',
                   'description',
                   'brand']

FIELDS_FROM_API_PRODUCTS = ['_id',
                            'product_name_fr',
                            'nutriscore_score',
                            'nutriscore_grade',
                            'stores',
                            'generic_name_fr',
                            'brands']


# Categories
CATEGORIES_VISIBLE = [
    "en:salted-spreads",
    "en:fruit-jams",
    "en:farming-products",
    "en:legumes-and-their-products",
    "en:pastas"
]
