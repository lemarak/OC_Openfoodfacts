# coding: utf-8

"""
class Category and CatProd
"""

from openfoodfacts.entity import Entity
from common import config as c


class Category(Entity):
    """
    class Category
    """

    TABLE = 'categories'
    FIELDS = c.FIELDS_CATEGORY

    def __init__(self, **categories):
        Entity.__init__(self)
        # id comes from the API otherwise it is id_category
        if 'id' in categories:
            self.id_category = categories['id'][:250]
        else:
            self.id_category = categories['id_category']
        self.name = "%s" % categories['name'][:100]
        self.products = categories['products']
        self.url = "%s" % categories['url'][:255]
        self.visible = int(self.id_category in c.CATEGORIES_VISIBLE)

    @classmethod
    def get_categories(cls, my_db):
        """
        retrieve categories
        and return an array of Category instances
        """
        rows = my_db.get_rows('categories',
                              order_by='name',
                              clause="visible = 1")
        categories = [Category(**data) for data in rows]
        return categories


class CatProd(Entity):
    """
    class CatProd
    """

    TABLE = 'cat_prod'
    FIELDS = ['id_category', 'id_product']

    def __init__(self, **cat_prod):
        Entity.__init__(self)
        self.id_category = cat_prod['id_category']
        self.id_product = cat_prod['id_product']
