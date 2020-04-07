# coding: utf-8

"""
class Category
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
        self.id_category = categories['id']
        self.name = "%s" % categories['name'][:100]
        self.nb_products = categories['products']
        self.url = "%s" % categories['url'][:255]
        self.visible = int(categories['id'] in c.CATEGORIES_VISIBLE)
