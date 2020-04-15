# coding: utf-8
"""
Class to implement database
"""

import mysql.connector
from mysql.connector import Error


class DataBaseOC:
    """
    Class to connect to the database
    and manipulate the data
    """

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
        self.cursor = self._con.cursor(dictionary=True)

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
        """ disconnect to the database """
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

    # obsolète
    def insert_json(self, table, json_to_insert):
        """
            Insert a json in the table
            structure of json :
            {'field_table':'value_to_insert'}
        """
        fields = ",".join(json_to_insert.keys())
        values = [str(value) for key, value in json_to_insert.items()]
        values = "%s" % values
        values = values[1:-1]
        query = "INSERT INTO %s(%s) VALUES (%s)" % (
            table, fields, values
        )
        try:
            self.cursor.execute(query)
            self._con.commit()
        except mysql.connector.Error as err:
            print("Something went wrong in insert table {}: {}".format(
                table,
                err))

    def insert(self, data, table=None):
        """
        insert from an array of objects
        in the associated table
        """
        if not data:
            return "Aucun élément à insérer"
        if table is None:
            table = data[0].TABLE
        sql_values = ",".join(
            [element.values_in_sql for element in data]
        )
        query = "INSERT IGNORE INTO %s VALUES %s" % (table, sql_values)
        try:
            self.cursor.execute(query)
            self._con.commit()
        except mysql.connector.Error as err:
            print("Something went wrong in insert table {}: {}".
                  format(table, err))

    def get_rows(self, table, query=None, order_by=None, clause=None):
        """
        execute a query in table [table] or by executing the query [query]
        fetchall() returns a dictionary
        """
        if query is None:
            query = "SELECT * FROM %s " % table
            if clause is not None:
                query += " WHERE %s" % clause
            if order_by is not None:
                query += " ORDER BY %s" % order_by
        try:
            self.cursor.execute(query)
            records = self.cursor.fetchall()
            return records
        except Error as error_text:
            print("Error reading data from MySQL table", error_text)
            return False


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
