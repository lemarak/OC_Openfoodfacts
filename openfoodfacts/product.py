# coding: utf-8

"""
class Product
"""

from openfoodfacts.entity import Entity
from common import config as c


class Product(Entity):
    """
    class Product
    """
    TABLE = 'products'
    FIELDS = c.FIELDS_PRODUCTS
    FIELDS_FROM_API = c.FIELDS_FROM_API_PRODUCTS

    def __init__(self, **product):
        self.id_product = str(product['_id'])
        self.name = product['product_name_fr']
        self.nutriscore_score = product['nutriscore_score']
        self.nutriscore_grade = product['nutriscore_grade']
        self.magasins = product['stores']
        self.description = product['generic_name_fr']
        self.brand = product['brands']
        # self.url = product['']
