# coding: utf-8

"""
Model Product
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

    def __init__(self, category=None, **product):
        Entity.__init__(self)
        # _id comes from the API otherwise it is id_product
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
        self.category = category

    def __str__(self):
        str_to_displays = "{}\n({})\nmarque : {}\n \
            nutriscore: {} ({})\nmagasins: {}\n"
        return str_to_displays.format(
            self.name,
            self.generic_name_fr[:100],
            self.brands,
            self.nutriscore_grade.upper(),
            self.nutriscore_score,
            self.stores
        )

    @classmethod
    def get_products_by_category(cls, my_db, id_category):
        """
        collects all products in the category
        """
        query = """
                SELECT * FROM products as p
                INNER JOIN cat_prod as cp
                ON p.id_product = cp.id_product
                WHERE cp.id_category = '%s'
                """ % id_category
        rows = my_db.get_rows('cat_prod',
                              query=query,
                              order_by='product_name_fr')
        products = [Product(id_category, **data) for data in rows]
        return products

    def get_substitutes(self, my_db):
        """
        collects five substitutes from a product
        """

        query = """
                SELECT * FROM products as p
                INNER JOIN cat_prod as cp
                ON p.id_product = cp.id_product
                WHERE cp.id_category = '%s'
                AND p.id_product <> '%s'
                AND p.nutriscore_score <= %s
                ORDER BY p.nutriscore_score DESC
                LIMIT 5
                """ % (self.category, self.id_product, self.nutriscore_score)
        rows = my_db.get_rows('categories',
                              query=query)
        substitutes = [Product(self.category, **data) for data in rows]
        return substitutes
