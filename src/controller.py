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
                case "Senior Customer Service Officer":
                    self.view.seniorCustomerServiceOfficerView()
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
        request["Status"] = "Initial"
        self.model.saveRequest(request)
        
    def seniorCustomerServiceOfficerReview(self, entries, valid):
        request = entries["Request"]
        commentary = entries["Senior Customer Service Officer Commentary"].get()
        request["Senior Customer Service Officer Commentary"] = commentary
        if valid :
            request["Status"] = "Financial Review"
        else :
            request["Status"] = "Rejected"
        self.model.saveRequest(request)
        self.view.seniorCustomerServiceOfficerView()
