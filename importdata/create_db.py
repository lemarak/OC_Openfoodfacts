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
    # Connection information
    param_connect = {'username': c.USER_NAME,
                     'password': c.PWD,
                     'database': c.DB_NAME}
    my_db = DataBaseOC(**param_connect)

    my_db.execute_script('importdata/create_db.sql')
    print('**** La base est créée ****')

    my_db.disconnect()


if __name__ == "__main__":
    main()
