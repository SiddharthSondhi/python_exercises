import tkinter
import tkinter.messagebox
from database_class import Database


class UserLogin:
    def __init__(self):
        self.screen = tkinter.Tk()
        self.screen.title("User Login")
        self.screen.geometry("300x150")

        self.username_label = tkinter.Label(self.screen, text="Username:", width=10)
        self.username_entry = tkinter.Entry(self.screen)

        self.password_label = tkinter.Label(self.screen, text="Password:", width=10)
        self.password_entry = tkinter.Entry(self.screen)

        self.login_button = tkinter.Button(self.screen, text="Login", command=self.login)

        self.create_account_button = tkinter.Button(self.screen, text="Create New Account", command=self.create_account)
        self.sign_up_button = tkinter.Button(self.screen, text="Sign Up", command=self.sign_up)

        self.username_label.grid(row=0, column=0)
        self.username_entry.grid(row=0, column=1)
        self.password_label.grid(row=1, column=0)
        self.password_entry.grid(row=1, column=1)
        self.login_button.grid(row=2, column=1)
        self.create_account_button.grid(row=3, column=1)

        # creates database
        self.user_login_database = Database("user_login_database.db")

        # creates table in user_login_database
        self.user_login_database.create_table("user_data_table", "(username, password)")

        self.user_login_database.print_table("user_data_table")

    def login(self):
        self.username = self.username_entry.get()
        self.password = self.password_entry.get()

        self.user_info = self.user_login_database.check_exists("user_data_table", self.username)

        if self.user_info:
            if self.password in self.user_info:
                tkinter.messagebox.showinfo(message="Success!")
                self.username_entry.delete(0, tkinter.END)
                self.password_entry.delete(0, tkinter.END)

            else:
                tkinter.messagebox.showwarning(message="Incorrect password.")
                self.password_entry.delete(0, tkinter.END)

        else:
            tkinter.messagebox.showwarning(message="Username does not exist.")

    def create_account(self):
        self.login_button.grid_forget()
        self.create_account_button.grid_forget()

        self.sign_up_button.grid(row=2, column=1)

    def sign_up(self):
        self.username = self.username_entry.get()
        self.password = self.password_entry.get()

        self.username_entry.delete(0, tkinter.END)
        self.password_entry.delete(0, tkinter.END)

        self.user_login_database.add_record("user_data_table", 2, [(self.username, self.password)])

        self.sign_up_button.grid_forget()
        self.login_button.grid(row=2, column=1)
        self.create_account_button.grid(row=3, column=1)

    def run(self):
        self.screen.mainloop()


user_login = UserLogin()

user_login.run()
