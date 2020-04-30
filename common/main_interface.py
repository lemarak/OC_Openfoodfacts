# coding: utf-8

"""
main program
"""

from openfoodfacts.category import Category
from openfoodfacts.product import Product
from openfoodfacts.favorite import Favorite
from view.mainapplication import *


def main(my_db, user):
    """
    main function
    """

    root = MainApplication()

    view_categories = root.frame_categories
    categories = Category.get_categories(my_db)
    if categories:
        view_categories.display(categories)

    view_favorites = root.frame_favorites
    favorites = Favorite.get_favorites_user(my_db, user)
    view_favorites.refresh_favorites(favorites)

    view_products = root.frame_products

    while True:
        # display categories
        if root.status == 1:
            if root.category is not None:
                products = Product.get_products_by_category(
                    my_db,
                    root.category
                )
                view_products.refresh_products(products)
                root.display_frame(view_products)
                root.category = None
        # display favorites
        elif root.status == 2:
            favorites = Favorite.get_favorites_user(my_db, user)
            view_favorites.refresh_favorites(favorites)
            root.display_frame(view_favorites)
            root.status = 0
        # display substitutes
        elif root.status == 3:
            product = root.product
            substitutes = product.get_substitutes(my_db)
            view_products.refresh_substitutes(substitutes)
            root.status = 0
        # save substitute
        elif root.status == 4:
            favorite = Favorite(root.product, user)
            clause_where = "id_product = {} AND id_user = {}".format(
                favorite.id_product, favorite.id_user
            )
            if not my_db.get_rows("favorites", clause=clause_where):
                my_db.insert([favorite])
                view_products.frame_comment("Produit enregistré...")
            else:
                view_products.frame_comment("!!! Produit déjà enregistré !!!")
            root.status = 0

        # root.mainloop()
        root.update_idletasks()
        root.update()

    # root.mainloop()
