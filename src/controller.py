from tkinter import messagebox

class SEPController:
    
    def __init__(self, model):
        self.model = model
    
    def logInController(self, entries):
        username = entries["username"].get()
        password = entries["password"].get()

        if (username, password) in self.model.getCredentials():
            messagebox.showinfo("Ok", f"Welcome, {username} !")
        else:
            messagebox.showerror("Error", "Wrong credentials")
