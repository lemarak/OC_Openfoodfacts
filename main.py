# coding: utf-8

"""
main program
"""

from db.database import DataBaseOC
from openfoodfacts.category import Category
from openfoodfacts.product import Product
from openfoodfacts.favorite import Favorite
from openfoodfacts.user import User
from view.mainapplication import *
from common import config as c


def main():
    """
    main function
    """
    # connect to database
    param_connect = {'username': c.USER_NAME,
                     'password': c.PWD,
                     'database': c.DB_NAME}
    my_db = DataBaseOC(**param_connect)

    # only one user for now
    user = User.get_user(my_db, 'test')
    print("\n", user.name, "est connecté.")

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
            my_db.insert([favorite])
            view_products.frame_comment("Produit enregistré...")
            root.status = 0

        # root.mainloop()
        root.update_idletasks()
        root.update()

    # root.mainloop()


if __name__ == "__main__":
    main()
