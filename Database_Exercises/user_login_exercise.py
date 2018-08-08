from database_class import Database

# creates database
user_login_database = Database("user_login_database.db")

# creates table in user_login_database
user_login_database.create_table("user_data_table", "(username, password)")

user_login_database.print_table("user_data_table")
print('\n')


print("Please enter your username.")
user_info = user_login_database.check_exists("user_data_table", input())
print(user_info)

if user_info:
    print("Please enter your password.")
    if input() == user_info[1]:
        print("Success!")
    else:
        print("incorrect password")


else:
    print("This username does not exist. Would you like to create a new account? [yes, no]")
    while True:
        create = input()
        if create in ["yes", "Yes"]:
            print("Please enter a new username.")
            new_username = input()
            print("Please enter a new password.")
            new_password = input()
            user_login_database.add_record("user_data_table", 2, [(new_username, new_password)])
            break
        elif create in ["no", "No"]:
            break
        else:
            print("please type yes or no")

user_login_database.close()
