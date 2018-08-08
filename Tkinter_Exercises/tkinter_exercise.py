import tkinter

screen = tkinter.Tk()
screen.title("Screen Title")

def button_0_function():
    user_entry = entry_0.get()
    print(user_entry)
    entry_0.delete(0, tkinter.END)
    entry_0.insert(0, "entry text")


label_0 = tkinter.Label(screen, text="this is label text")
button_0 = tkinter.Button(screen, text="this is a button", command=button_0_function)
entry_0 = tkinter.Entry(screen)

label_0.grid(row=0, column=0)
button_0.grid(row=1, column=0)
entry_0.grid(row=2, column=0)

screen.mainloop()
