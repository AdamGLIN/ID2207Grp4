import tkinter as tk

class SEPView :
    
    def __init__(self, controller) :
        self.root = tk.Tk()
        self.controller = controller
        self.logInView()
        self.root.mainloop()

    def logInView(self):
        entries = dict()
        
        self.root.title("Log In Page")
        self.root.geometry("300x200")
        self.root.resizable(False, False)
        
        label_username = tk.Label(self.root, text="Username :")
        label_username.pack(pady=(20, 5))
        entry_username = tk.Entry(self.root)
        entry_username.pack()
        entries["username"] = entry_username

        label_password = tk.Label(self.root, text="Password :")
        label_password.pack(pady=(10, 5))
        entry_password = tk.Entry(self.root, show="*")
        entry_password.pack()
        entries["password"] = entry_password

        btn_login = tk.Button(self.root, text="Connect", command=lambda : self.controller.logInController(entries))
        btn_login.pack(pady=20)
