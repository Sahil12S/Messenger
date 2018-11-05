# This frontend will display registration screen for user.

from tkinter import *

window = Tk()
window.geometry("320x400")
window.title("Hudibaba Messenger")
window.resizable(False, False)

msg = ""
print_label = Label(window, text=msg, font=12)


def validateRegistration():

    global print_label
    global msg

    if print_label:
        print_label.destroy()


    if not username.get():
        msg = "Username cannot be empty."
    elif not password.get():
        msg = "Please enter a valid password."
    else:
        msg = "Registration successful."

    # print(msg)

    print_label = Label(window, text=msg, font=12)
    print_label.grid(row=6, column=0, columnspan=4)



heading_label = Label(window, text ="Welcome to Hudibaba!!", font=("Helvetica 18 bold"))
heading_label.grid(row=0, column=0, columnspan=4, padx=5, pady = 5)

info_label = Label(window, text="Please fill all fields to register", font=10)
info_label.grid(row=1, column=0, columnspan=4, padx=5, pady = 5)

username_lable = Label(window, text="Username:", font=12)
username_lable.grid(row=2, column=0, sticky=W, padx=5, pady=5)
username = StringVar()
username_entryBox = Entry(window, textvariable=username, font=12)
username_entryBox.grid(row=2, column=1, columnspan=3, sticky=W, padx=5, pady=5)

pswd_lable = Label(window, text="Password:", font=12)
pswd_lable.grid(row=3, column=0, sticky=W, padx=5, pady=5)
password = StringVar()
password_entryBox = Entry(window, show="*", textvariable=password, font=12)
password_entryBox.grid(row=3, column=1, columnspan=3, sticky=W, padx=5, pady=5)

blank_label = Label(window, text="")
blank_label.grid(row=4, column=0, columnspan=4)


register_button = Button(window, text="Register", command=validateRegistration, font=12)

# to display button.
# button_refresh_chat.pack()
register_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)


login_button = Button(window, text="Login", command=validateRegistration, font=12)
login_button.grid(row=5, column=2, columnspan=2, padx=5, pady=5)


cancel_button = Button(window, text="Cancel", command=window.destroy, font=12)
cancel_button.grid(row=6, column=1, columnspan=2, padx=5, pady=5)



window.mainloop()