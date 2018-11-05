import tkinter as tk

HEADING_FONT = ("Verdana", 18)


class WelcomeWindow(tk.Tk):
    
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        # container.title("Hudibaba Messenger")
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, ChatWindow):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)
            

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        heading_label = tk.Label(self, text ="Welcome to Hudibaba!!", font=HEADING_FONT)
        heading_label.grid(row=0, column=0, columnspan=4, padx=5, pady = 5)
        # heading_label.pack(side="top", fill="y", padx=5, pady=5)

        info_label = tk.Label(self, text="Please fill all fields to register", font=10)
        info_label.grid(row=1, column=0, columnspan=4, padx=5, pady = 5)

        # Username field
        username_lable = tk.Label(self, text="Username:", font=12)
        username_lable.grid(row=2, column=0, sticky="we", padx=5, pady=5)
        self.username = tk.StringVar()
        username_entryBox = tk.Entry(self, textvariable=self.username, font=12)
        username_entryBox.grid(row=2, column=1, columnspan=3, sticky="we", padx=5, pady=5)

        # Password field
        pswd_lable = tk.Label(self, text="Password:", font=12)
        pswd_lable.grid(row=3, column=0, sticky="we", padx=5, pady=5)
        self.password = tk.StringVar()
        password_entryBox = tk.Entry(self, show="*", textvariable=self.password, font=12)
        password_entryBox.grid(row=3, column=1, columnspan=3, sticky="we", padx=5, pady=5)

        self.print_label = tk.Label(self, text="", font=12)
        
        # Register new user
        register_button = tk.Button(self, text="Register", command=self.validateRegistration, font=12)
        register_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        # Login existing user
        login_button = tk.Button(self, text="Login", \
                                    command=lambda: self.loginUser(controller), font=12)
        login_button.grid(row=5, column=2, columnspan=2, padx=5, pady=5)

        # Close the application
        cancel_button = tk.Button(self, text="Close", command=self.quit, font=12)
        cancel_button.grid(row=6, column=1, columnspan=2, padx=5, pady=5)


    def validateRegistration(self):
        self.print_label.destroy()

        if not self.username.get():
            msg = "Username cannot be empty."
        elif not self.password.get():
            msg = "Please enter a valid password."
        else:
            msg = "Registration successful."

        # print(msg)

        self.print_label = tk.Label(self, text=msg, font=12)
        self.print_label.grid(row=7, column=0, columnspan=4)


    def loginUser(self, controller):
        # print(self.username)
        # print(self.password)
        if self.username.get() == "sahil" and self.password.get() == "123":
            controller.show_frame(ChatWindow)



class ChatWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        heading_label = tk.Label(self, text ="Hudibaba Messenger", font=HEADING_FONT)
        heading_label.grid(row=0, column=0, columnspan=4, padx=5, pady = 5, sticky="e")

        online_user = tk.Text(self, height=25, width=20, font=8)
        online_user.grid(row=3, column=0)

        # Logout user
        logout_button = tk.Button(self, text="Logout", \
                                    command=lambda: controller.show_frame(StartPage), font=12)
        logout_button.grid(row=3, column=1, columnspan=2, padx=5, pady=5)
        


if __name__ == '__main__':
    app = WelcomeWindow()
    app.title("Hudibaba Messenger")
    app.mainloop()
    