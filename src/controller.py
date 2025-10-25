from tkinter import messagebox

class SEPController:
    
    def __init__(self):
        pass
    
    def setModel(self, model):
        self.model = model
        
    def setView(self, view):
        self.view = view
    
    def logInController(self, entries):
        username = entries["Username"].get()
        password = entries["Password"].get()
        access = entries["Access"].get()

        if (username, password, access) in self.model.getCredentials():
            match access:
                case "Customer Service Officer":
                    self.view.customerServiceOfficerView()
                case _:
                    messagebox.showinfo("Ok", f"Welcome, {username} !")
            return True
        else:
            messagebox.showerror("Error", "Wrong credentials")
            return False
        
    def clientCallController(self, entries):
        request = dict()
        for entry in entries :
            request[entry] = entries[entry].get()
        self.model.saveRequest(request)
