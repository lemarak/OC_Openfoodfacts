# coding: utf-8


class Entity:

    TABLE = ''
    FIELDS = []
    FIELDS_FROM_API = []

    def __init__(self):
        self.name = ""

    def __repr__(self):
        return "name: {}".format(self.name)

    @property
    def repr_values(self):
        return [getattr(self, field) for field in self.FIELDS]

    @property
    def values_in_sql(self):
        """
            create sql string for insert
        """
        values = [str(value) for value in self.repr_values]
        values = "%s" % values
        values = values[1:-1]
        return "({})".format(values)

    @classmethod
    def check_all_fields(cls, data):
        """
            Check if all the fields of the table
            will be filled by the API element
        """
        for field in cls.FIELDS_FROM_API:
            if field not in data:
                return False
        return True
