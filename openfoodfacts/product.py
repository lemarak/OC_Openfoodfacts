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
        Entity.__init__(self)
        if '_id' in product:
            self.id_product = str(product['_id'])
        else:
            self.id_product = str(product['id_product'])
        self.product_name_fr = product['product_name_fr']
        self.nutriscore_score = product['nutriscore_score']
        self.nutriscore_grade = product['nutriscore_grade']
        self.stores = product['stores']
        self.generic_name_fr = product['generic_name_fr']
        self.brands = product['brands']
        self.name = product['product_name_fr']
        # self.url = product['']

    @classmethod
    def get_products_by_category(cls, db, id_category):
        query = """
                SELECT * FROM products as p
                INNER JOIN cat_prod as cp
                ON p.id_product = cp.id_product
                WHERE cp.id_category = '%s'
                """ % id_category
        rows = db.get_rows('cat_prod', query=query, order_by='product_name_fr')
        products = [Product(**data) for data in rows]
        return products
