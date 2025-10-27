import tkinter as tk
import json

from src.model import Access
from src.model import Status

class Form :
    
    def __init__(self, entries, name, fields, callback, size):
        self.entries = entries
        self.name = name
        self.fields = fields
        self.callback = callback
        self.size = size
    
    def view(self, root):
        root.title(f"{self.name} Form Page")
        root.geometry(self.size)
        root.resizable(False, False)
        
        position = 10
        for field in self.fields:
            label = tk.Label(root, text=f"{field} :")
            label.pack(pady=(position, 5))
            
            entry = tk.Entry(root)
            entry.pack()
            
            self.entries[field] = entry
            position += 10

        btn = tk.Button(root, text="Validate", command=lambda : self.callback(self.entries))
        btn.pack(pady=20)
        
class ClientCallForm(Form) :
    
    def __init__(self, entries, callback):
        super().__init__(entries, "Client Call", [
            "Client Name", 
            "Contact", 
            "Type", 
            "Date", 
            "Budget", 
            "Description"
        ], callback, "900x600")

class ControlPanel() :
    
    def __init__(self, entries, name, size, callbacks):
        self.entries = entries
        self.name = name
        self.size = size
        self.callbacks = callbacks

    def view(self, root, requests):
        root.title(f"{self.name} Control Panel")
        root.geometry(self.size)
        root.resizable(False, False)
        
        for request in requests:
            for status in Status:
                if status in self.callbacks and request["Status"] == status:
                    label = tk.Label(root, text=json.dumps(request, indent=4), justify="left")
                    label.pack(pady=(30, 5))
                    self.entries["Request"] = request
                    
                    label = tk.Label(root, text=f"Commentary :")
                    label.pack(pady=(20, 5))
                    entry = tk.Entry(root)
                    entry.pack()
                    self.entries[f"{self.name} Commentary"] = entry
                    
                    btn_validate = tk.Button(root, text="Validate", command=lambda : self.callbacks[status](self.entries, True))
                    btn_validate.pack(pady=20)
                    
                    btn_reject = tk.Button(root, text="Reject", command=lambda : self.callbacks[status](self.entries, False))
                    btn_reject.pack(pady=10)
                    break

class SeniorCustomerServiceOfficerControlPanel(ControlPanel):
    
    def __init__(self, entries, callbacks):
        super().__init__(entries, "Senior Customer Service Officer", "900x600", callbacks)

class SEPView :
    
    def __init__(self) :
        self.root = tk.Tk()
        self.entries = dict()
    
    def setModel(self, model):
        self.model = model
        
    def setController(self, controller):
        self.controller = controller
        
    def show(self):
        self.logInView()
        self.root.mainloop()
        
    def clearView(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def logInView(self):
        self.entries.clear()
        self.clearView()
        
        self.root.title("Log In Page")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        
        label_username = tk.Label(self.root, text="Username :")
        label_username.pack(pady=(30, 5))
        entry_username = tk.Entry(self.root)
        entry_username.pack()
        self.entries["Username"] = entry_username

        label_password = tk.Label(self.root, text="Password :")
        label_password.pack(pady=(20, 5))
        entry_password = tk.Entry(self.root, show="*")
        entry_password.pack()
        self.entries["Password"] = entry_password
        
        label_access = tk.Label(self.root, text="Access :")
        label_access.pack(pady=(10, 5))
        entry_access = tk.StringVar(value="...")
        option_menu = tk.OptionMenu(self.root, entry_access, *Access)
        option_menu.pack()
        self.entries["Access"] = entry_access

        btn_login = tk.Button(self.root, text="Connect", command=lambda : self.controller.logInController(self.entries))
        btn_login.pack(pady=20)
        
    def customerServiceOfficerView(self):
        self.entries.clear()
        self.clearView()
        
        form = ClientCallForm(self.entries, self.controller.clientCallController)
        form.view(self.root)
        
    def seniorCustomerServiceOfficerView(self):
        self.entries.clear()
        self.clearView()
        
        requests = self.model.getRequests()
        callbacks = {
            "Initial": self.controller.seniorCustomerServiceOfficerReview
        }
        
        controlPanel = SeniorCustomerServiceOfficerControlPanel(self.entries, callbacks)
        controlPanel.view(self.root, requests)
    