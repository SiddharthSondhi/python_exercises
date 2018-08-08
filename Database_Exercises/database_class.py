import sqlite3


class Database:
    def __init__(self, database_name):
        self.conn = sqlite3.connect(database_name)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name, table_contents):
        try:
            query = "CREATE TABLE {0} {1}".format(table_name, table_contents)
            self.cursor.execute(query)
        except:
            print("Table "+table_name+" has already been created.")

    def add_record(self, table_name, number_of_headers, record):
        query = "INSERT INTO {0} VALUES ({1}?)".format(table_name, (number_of_headers-1)*"?,")
        self.cursor.executemany(query, record)

    def remove_record(self, table_name, header, record_value):
        query = "DELETE FROM {0} WHERE {1} = '{2}'".format(table_name, header, record_value)
        self.cursor.execute(query)

    def print_table(self, table_name):
        row_number = 0
        for row in self.cursor.execute("SELECT * FROM "+table_name):
            print("Row", row_number, "=", row)
            row_number = row_number + 1

    def update_record(self, table_name, header_to_change, new_value, identifier_header, identifier):
        """To update a value you need to specify the header that you want to change the value in (header_to_change) and
        that value (new_value), and then specify a column header(identifier_header) and corresponding value(identifier)
        to identify the record which needs to be changed."""
        query = "UPDATE {0} SET {1} = '{2}' WHERE {3} = '{4}'".format\
            (table_name, header_to_change, new_value, identifier_header, identifier)
        self.cursor.execute(query)

    def delete_table(self, table_name):
        query = "DROP TABLE {0}".format(table_name)
        self.cursor.execute(query)

    def delete_record(self, table_name, identifier_header, identifier):
        query = "DELETE FROM {0} WHERE {1} = '{2}'".format(table_name, identifier_header, identifier)
        self.cursor.execute(query)

    def check_exists(self, table_name, identifier):
        '''Checks to see if identifier is in table. If it exists, it returns the row that it is in. If not then None is
        returned.'''
        for row in self.cursor.execute("SELECT * FROM " + table_name):
            if (identifier in row):
                return row
        return None

    def close(self):
        self.conn.commit()
        self.cursor.close()

'''
database_one = Database("database_class_test.db")

database_one.create_table("cartoons", "(first_name text, last_name text, address text)")
database_one.add_record("cartoons", 3, [("micky", "mouse", "1234 disneyland"), ("donald", "trump", "white house")])
database_one.print_table("cartoons")
print('\n')

database_one.update_record("cartoons", "first_name", "chuck", "last_name", "mouse")
database_one.print_table("cartoons")
print('\n')

database_one.delete_record("cartoons", "first_name", "donald")
database_one.print_table("cartoons")
print('\n')

database_one.add_record("cartoons", 3, [("bruce", "wayne", "manor")])
database_one.print_table("cartoons")
print('\n')

database_one.check_exists("cartoons", "chuck")
database_one.check_exists("cartoons", "chkus")

#database_one.close()
'''