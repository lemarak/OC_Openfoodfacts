# coding: utf-8
"""
Create the database from a script sql
And import API data
"""

from db.database import DataBaseOC
from common import config as c


def main():
    """
    main function
    """

    param_connect = {'username': c.USER_NAME,
                     'password': c.PWD,
                     'database': c.DB_NAME}
    my_db = DataBaseOC(**param_connect)

    print(my_db)
    my_db.execute_script('common/create_db.sql')
    print('**** La base est créée ****')


if __name__ == "__main__":
    main()
