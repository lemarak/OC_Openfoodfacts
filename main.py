# coding: utf-8

"""
main program
"""

from db.database import DataBaseOC
from openfoodfacts.category import Category
from openfoodfacts.product import Product
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

    response_menu = int(main_menu())
    if response_menu == 1:
        # select and return a category
        category = select_categories(my_db)
        # select and return a product
        product = select_products(my_db, category.id_category)
        # display substitutes
        display_substitutes(my_db, product)
    else:
        pass


def main_menu():
    """
    displays main menu
    and return the choice
    """

    # displays menu
    print("\n" * 2)
    print("1 - Quel aliment souhaitez-vous remplacer ?")
    print("2 - Retrouver mes aliments substitués.")

    # loop until returning 1 or 2
    while True:
        response = input("Votre choix : ")
        if response in ('1', '2'):
            return response
        print("Choix incorrect")


def select_categories(my_db):
    """
    Displays the categories
    and returns the chosen category
    (category instance)
    """
    print("\n" * 2)
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
    print("\n" * 2)
    # collects all products in the category
    products = Product.get_products_by_category(my_db, id_category)
    number = 1
    # displays products
    for product in products:
        print("{} - {} ({})".format(number, product.name, product.brands))
        number += 1
    return loop_menu(products)


def display_substitutes(my_db, product):
    print("\n" * 2)
    substitutes = product.get_substitutes(my_db)
    number = 1
    # displays substitutes
    for substitute in substitutes:
        print("""
            {} - {}
            {}
            nutriscore: {}({})
            magasins: {}""".format(number,
                                   substitute.name,
                                   substitute.generic_name_fr,
                                   substitute.nutriscore_grade.upper(),
                                   substitute.nutriscore_score,
                                   substitute.stores
                                   )
              )
        number += 1


def loop_menu(data):
    """
    loop until the entry is correct
    and return the selected object
    """
    while True:
        try:
            response = int(input("Votre choix : "))
            if response in range(1, len(data) + 1):
                return data[response-1]
            print("Choix incorrect")
        except ValueError:
            print("Entrez un nombre.")


if __name__ == "__main__":
    main()
