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
                case "Production Manager":
                    self.view.productionManagerView()
                case "Financial Manager":
                    self.view.financialManagerView()
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

    def productionManagerController(self, entries):
        request = entries["Request"]
        for key in entries.keys():
            if key != "Request":
                request[key] = entries[key].get()
        request["Production Tasks Distributed"] = True
        self.model.saveRequest(request)
        self.view.productionManagerView()

    def financialManagerController(self, entries, valid):
        request = entries["Request"]

        comment_widget = entries.get("Financial Manager Commentary")
        commentary = comment_widget.get().strip() if comment_widget else ""

        if not commentary:
            messagebox.showwarning("Missing commentary", "Please add a commentary before proceeding.")
            return

        request["Financial Manager Commentary"] = commentary

        # Decision (validate or reject)
        if valid:
            request["Status"] = "Administration Review"
        else:
            request["Status"] = "Rejected"
            self.model.saveRequest(request)

        self.view.financialManagerView()
