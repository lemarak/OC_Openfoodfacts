# coding: utf-8

"""
Model Favorite
"""
from openfoodfacts.entity import Entity
from openfoodfacts.product import Product
from common import config as c


class Favorite(Entity):

    TABLE = 'favorites'
    FIELDS = c.FIELDS_FAVORITES

    def __init__(self, product, user):
        Entity.__init__(self)
        self.product = product
        self.user = user

    def __repr__(self):
        str_to_displays = "user: {} ({}) \nproduit: {}\n"
        return str_to_displays.format(self.user.name,
                                      self.user.login,
                                      self.product.product_name_fr)

    @property
    def id_product(self):
        return self.product.id_product

    @property
    def id_user(self):
        return self.user.id_user

    @classmethod
    def get_favorites_user(cls, my_db, user):
        """
        get all favorites from an user
        and return a list of favorites
        """
        favorites = []
        query = """SELECT * FROM favorites as f
                    INNER JOIN products as p
                    ON f.id_product = p.id_product
                    WHERE f.id_user = %s
                """ % user.id_user
        rows = my_db.get_rows('favorites', query=query)
        favorites = [Favorite(Product(0, **product), user) for product in rows]
        return favorites
