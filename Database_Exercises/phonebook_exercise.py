from database_class import Database


class Phonebook:

    def __init__(self):
        self.database = Database("phonebook_database.db")
        self.database.create_table("phonebook", "(first_name, last_name, phone_number)")

    def print(self):
        self.database.print_table("phonebook")
        print()

    def add_entry(self):
        print("please enter your first name")
        first_name = input()
        print()

        print("please enter your last name")
        last_name = input()
        print()

        print("please enter your phone number")
        phone_number = input()
        print()

        self.database.add_record("phonebook", 3, [(first_name, last_name, phone_number)])
        print("successfully created \n")

    def delete_entry(self):
        while True:
            print("Please enter the first name of the entry that you want to delete. Type exit to leave.\n")
            entry_to_delete = input()

            if self.database.check_exists("phonebook", entry_to_delete):
                self.database.delete_record("phonebook", "first_name", entry_to_delete)
                print("successfully deleted \n")
                break

            elif entry_to_delete == "exit":
                print()
                break

            else:
                print("that entry does not exist \n")

    def close(self):
        self.database.close()

phonebook = Phonebook()

while True:
    print("Type [0] to look at phone book \nType [1] to add entry to phonebook \nType [2] to delete entry \n"
          "Type [3] to exit \n")

    user_input = input()

    if user_input == '0':
        phonebook.print()

    if user_input == '1':
        phonebook.add_entry()

    if user_input == '2':
        phonebook.delete_entry()

    if user_input == '3':
        break

    if user_input not in ['0', '1', '2', '3']:
        print("please type either 0, 1 , 2, or 3 ", '\n')

phonebook.close()
