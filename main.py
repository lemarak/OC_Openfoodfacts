# coding: utf-8

"""
main program, User-run program
"""
from db.database import DataBaseOC

from openfoodfacts.user import User

from common import main_terminal
from common import main_interface
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

    response_menu = int(main_menu())

    if response_menu == 1:
        main_terminal.main(my_db, user)
    elif response_menu == 2:
        main_interface.main(my_db, user)


def main_menu():
    """
    displays main menu
    and return the choice
    """

    # displays menu
    print("\n*********** Choix de l'interface *************\n")
    print("1 - Terminal")
    print("2 - Interface graphique")
    print("3 - Quitter")

    # loop until returning 1, 2 or 3
    while True:
        response = input("Votre choix : ")
        if response in ('1', '2', '3'):
            return response
        print("Choix incorrect")


if __name__ == "__main__":
    main()
