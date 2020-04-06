# coding: utf-8
"""
Class to implement database
"""

import mysql.connector


class DataBaseOC:

    def __init__(self, **connect_params):
        self._con = None
        if 'host' in connect_params:
            self._host = connect_params['host']
        else:
            self._host = 'localhost'
        self._username = connect_params['username']
        self._password = connect_params['password']
        self._dbname = connect_params['database']

        self.connect()
        self.cursor = self._con.cursor()

    def __repr__(self):
        string_format = "Host:{}, db:{}, user:{}".format(self._host,
                                                         self._dbname,
                                                         self._username)
        return string_format

    def __del__(self):
        self.disconnect()

    def connect(self):
        """
        connect to the database
        """
        self._con = mysql.connector.connect(
            host=self._host,
            user=self._username,
            password=self._password,
            database=self._dbname)

    def disconnect(self):
        if self._con:
            self._con.close()

    def execute_script(self, file_name):
        """
        execute a sql script from a file
        """

        with open(file_name, 'r') as file:
            content_sql = file.read()

        sql_commands = content_sql.split(';')

        for sql in sql_commands:
            # print(sql)
            try:
                if sql.rstrip() != '':
                    self.cursor.execute(sql)
            except ValueError:
                print("Command skipped:", sql)


def main():
    """
    main function
    """
    param_connect = {'username': 'oc_projet5',
                     'password': 'OC123456',
                     'database': 'oc_openfoodfacts'}
    my_db = DataBaseOC(**param_connect)
    print(my_db)


if __name__ == "__main__":
    main()
