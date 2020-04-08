# coding: utf-8

from db.database import DataBaseOC
from openfoodfacts.category import Category
from openfoodfacts.product import Product
from common import config as c


def main():
    # connect to database
    param_connect = {'username': c.USER_NAME,
                     'password': c.PWD,
                     'database': c.DB_NAME}
    my_db = DataBaseOC(**param_connect)

    response_menu = int(menu_principal())
    if response_menu == 1:
        category = display_categories(my_db)
        product = display_products(my_db, category.id_category)
        print(product)


def menu_principal():
    print("\n" * 2)
    print("1 - Quel aliment souhaitez-vous remplacer ?")
    print("2 - Retrouver mes aliments substitués.")
    while True:
        response = input("Votre choix : ")

        if response in ('1', '2'):
            return response
        print("Choix incorrect")


def display_categories(my_db):
    print("\n" * 2)
    categories = Category.get_categories(my_db)
    number = 1
    for category in categories:
        print("{} - {} ".format(number, category.name))
        number += 1
    while True:
        try:
            response = int(input("Votre choix : "))
            if response in range(1, len(categories) + 1):
                return categories[response-1]
            print("Choix incorrect")
        except ValueError:
            print("Entrez un nombre.")


def display_products(my_db, id_category):
    print("\n" * 2)
    products = Product.get_products_by_category(my_db, id_category)
    number = 1
    for product in products:
        print("{} - {} ({})".format(number, product.name, product.brands))
        number += 1
    while True:
        try:
            response = int(input("Votre choix : "))
            if response in range(1, len(products) + 1):
                return products[response-1]
            print("Choix incorrect")
        except ValueError:
            print("Entrez un nombre.")


if __name__ == "__main__":
    main()
