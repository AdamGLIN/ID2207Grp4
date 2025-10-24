import tkinter as tk

class Form :
    
    def __init__(self, name, fields, controller):
        self.name = name
        self.fields = fields
        self.controller = controller
        self.entries = dict()
    
    def view(self, root):
        self.entries = dict()
        
        root.title(f"{self.name} Form Page")
        root.geometry("900x600")
        root.resizable(False, False)
        
        position = 10
        for field in self.fields:
            label = tk.Label(root, text=f"{field} :")
            label.pack(pady=(position, 5))
            
            entry = tk.Entry(root)
            entry.pack()
            
            self.entries[field] = entry
            position += 10

        btn = tk.Button(root, text="Validate", command=lambda : self.controller(self.entries))
        btn.pack(pady=20)

class SEPView :
    
    def __init__(self, controller) :
        self.root = tk.Tk()
        self.controller = controller
        self.entries = dict()
        
    def show(self):
        self.logInView()
        self.root.mainloop()

    def logInView(self):
        self.entries = dict()
        
        self.root.title("Log In Page")
        self.root.geometry("300x200")
        self.root.resizable(False, False)
        
        label_username = tk.Label(self.root, text="Username :")
        label_username.pack(pady=(20, 5))
        entry_username = tk.Entry(self.root)
        entry_username.pack()
        self.entries["username"] = entry_username

        label_password = tk.Label(self.root, text="Password :")
        label_password.pack(pady=(10, 5))
        entry_password = tk.Entry(self.root, show="*")
        entry_password.pack()
        self.entries["password"] = entry_password

        btn_login = tk.Button(self.root, text="Connect", command=lambda : self.controller.logInController(self.entries))
        btn_login.pack(pady=20)
        
    def formView(self, form):
        form.view(self.root)
