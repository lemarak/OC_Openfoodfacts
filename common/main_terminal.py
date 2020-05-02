# coding: utf-8

"""
main program
"""

from openfoodfacts.category import Category
from openfoodfacts.product import Product
from openfoodfacts.favorite import Favorite


def main(my_db, user):
    """
    main function
    """
    menu_next = 0

    while True:
        response_menu = int(main_menu())
        menu = 1
        if response_menu == 1:  # Menu find a substitute
            while True:
                if menu == 1:
                    # displays, select and return a category
                    category, menu_next = select_categories(my_db)
                elif menu == 2:
                    # displays, select and return a product
                    product, menu_next = select_products(my_db,
                                                         category.id_category)
                elif menu == 3:
                    # display substitutes, select and return a substitute
                    substitute, menu_next = display_substitutes(my_db, product)
                    if substitute:
                        favorite = Favorite(substitute, user)
                        my_db.insert([favorite])
                        menu = 2
                else:
                    break
                # menu_next = -1 if back else 1
                menu += menu_next
        elif response_menu == 2:  # menu, displays favorites
            favorites = Favorite.get_favorites_user(my_db, user)
            print("\n*********** Favoris *************\n")
            if favorites:
                for favorite in favorites:
                    print(favorite.product)
            else:
                print('Pas de favoris !')
        else:
            break
    print("\nBye !\n")


def main_menu():
    """
    displays main menu
    and return the choice
    """

    # displays menu
    print("\n*********** Menu principal *************\n")
    print("1 - Quel aliment souhaitez-vous remplacer ?")
    print("2 - Retrouver mes aliments substitués.")
    print("3 - Quitter")

    # loop until returning 1, 2 or 3
    while True:
        response = input("Votre choix : ")
        if response in ('1', '2', '3'):
            return response
        print("Choix incorrect")


def select_categories(my_db):
    """
    Displays the categories
    and returns the chosen category
    (category instance)
    """
    print("\n*********** Catégories *************\n")
    categories = Category.get_categories(my_db)
    number = 1
    # displays categories
    for category in categories:
        print("{} - {} ".format(number, category.name))
        number += 1
    return loop_menu(categories)


def select_products(my_db, id_category):
    """
    Displays the products of a category
    and returns the selected product
    (product instance)
    """
    print("\n*********** Produits *************\n")
    # collects all products in the category
    products = Product.get_products_by_category(my_db, id_category)
    number = 1
    # displays products
    for product in products:
        print("{} - {} ({})".format(number, product.name, product.brands))
        number += 1
    return loop_menu(products)


def display_substitutes(my_db, product):
    """
    Displays the substitutes of a product (5 products max)
    and returns the selected product
    (product instance)
    """

    print("\n" * 2)
    substitutes = product.get_substitutes(my_db)
    number = 1
    # displays substitutes
    for substitute in substitutes:
        print(number, '-', substitute)
        number += 1
    return loop_menu(substitutes)


def loop_menu(data):
    """
    loop until the entry is correct
    and return the selected object
    """
    print("0 - <--- menu précédent <---")
    while True:
        try:
            response = int(input("Votre choix : "))
            if response in range(1, len(data) + 1):
                return data[response-1], 1
            elif response == 0:
                return None, -1
            print("Choix incorrect")
        except ValueError:
            print("Entrez un nombre.")
