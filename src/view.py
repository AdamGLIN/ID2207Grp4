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

class ReviewPage() :
    
    def __init__(self, entries, name, size, callbacks):
        self.entries = entries
        self.name = name
        self.size = size
        self.callbacks = callbacks

    def view(self, root, requests):
        root.title(f"{self.name} Review Page")
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

class SeniorCustomerServiceOfficerReviewPage(ReviewPage):
    def __init__(self, entries, callbacks):
        super().__init__(entries, "Senior Customer Service Officer", "900x600", callbacks)

class FinancialManagerReviewPage(ReviewPage):
    def __init__(self, entries, callbacks):
        super().__init__(entries, "Financial Manager", "900x600", callbacks)

class HiringApplicationForm(Form):
    def __init__(self, entries, callback):
        super().__init__(
            entries,
            "Hiring Application",
            ["Name", "Contact", "Salary", "Position", "Start Date"],
            callback,
            "750x500"
        )


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
        
        controlPanel = SeniorCustomerServiceOfficerReviewPage(self.entries, callbacks)
        controlPanel.view(self.root, requests)
    
    def productionManagerView(self):
        self.entries.clear()
        self.clearView()
        
        requests = self.model.getRequests()
        
        self.root.title(f"Production Manager Page")
        self.root.geometry("900x900")
        self.root.resizable(False, False)
        
        for request in requests:
            if request["Status"] == "Accepted" and "Production Tasks Distributed" not in request:
                label = tk.Label(self.root, text=json.dumps(request, indent=4), justify="left")
                label.pack(pady=(60, 5))
                self.entries["Request"] = request
                
                label_photo = tk.Label(self.root, text="Photography Task Description :")
                label_photo.pack(pady=(50, 5))
                entry_photo = tk.Entry(self.root)
                entry_photo.pack()
                self.entries["Photography Task Description"] = entry_photo
                
                label_audio = tk.Label(self.root, text="Audio Task Description :")
                label_audio.pack(pady=(40, 5))
                entry_audio = tk.Entry(self.root)
                entry_audio.pack()
                self.entries["Audio Task Description"] = entry_audio
                
                label_graphics = tk.Label(self.root, text="Graphics Task Description :")
                label_graphics.pack(pady=(30, 5))
                entry_graphic = tk.Entry(self.root)
                entry_graphic.pack()
                self.entries["Graphics Task Description"] = entry_graphic
                
                label_decorating = tk.Label(self.root, text="Decorating Task Description :")
                label_decorating.pack(pady=(20, 5))
                entry_decorating = tk.Entry(self.root)
                entry_decorating.pack()
                self.entries["Decorating Task Description"] = entry_decorating
                
                label_network = tk.Label(self.root, text="Network Task Description :")
                label_network.pack(pady=(10, 5))
                entry_network = tk.Entry(self.root)
                entry_network.pack()
                self.entries["Network Task Description"] = entry_network
                
                btn_validate = tk.Button(self.root, text="Validate", command=lambda : self.controller.productionManagerController(self.entries))
                btn_validate.pack(pady=20)
                break

    def financialManagerView(self):
        self.entries.clear()
        self.clearView()

        btn = tk.Button(self.root, text="Show Monthly Budgets", command=self.showFinanceBudgets)
        btn.pack(pady=(10, 5))

        requests = self.model.getRequests() or []
        finance_reqs = [r for r in requests if r.get("Status") == "Financial Review"]

        if not finance_reqs:
            self.root.title("Financial Manager Review Page")
            self.root.geometry("900x600")
            self.root.resizable(False, False)
            tk.Label(self.root, text="No requests awaiting Financial Review.", font=("TkDefaultFont", 12)).pack(pady=30)
            tk.Button(self.root, text="Back", command=self.logInView).pack(pady=10)
            return

        callbacks = {
            "Financial Review": self.controller.financialManagerController
        }
        panel = FinancialManagerReviewPage(self.entries, callbacks)
        panel.view(self.root, finance_reqs)

    def showFinanceBudgets(self):
        win = tk.Toplevel(self.root)
        win.title("SEP Budgets")
        win.geometry("650x300")
        win.resizable(False, False)

        months = self.controller.financeGetMonths() or []
        if not months:
            tk.Label(win, text="No finance data.", font=("TkDefaultFont", 11)).pack(pady=20)
            return

        wrap = tk.Frame(win)
        wrap.pack(fill="both", expand=True, padx=10, pady=10)

        for m in months:
            snap = self.controller.financeGetMonthlySnapshot(m)
            tk.Label(
                wrap,
                text=f"{snap['month']}:  Budget {int(snap['budget'])}  |  Spent {int(snap['spent'])}  |  Left {int(snap['left'])}  ({snap['left_pct']}%)",
                anchor="w", justify="left"
            ).pack(anchor="w", pady=2)

        tk.Button(wrap, text="Close", command=win.destroy).pack(pady=8)

    def serviceManagerView(self):
        self.entries.clear()
        self.clearView()

        self.root.title("Service Manager – Hiring Application")
        self.root.geometry("500x360")
        self.root.resizable(False, False)

        form = HiringApplicationForm(self.entries, self.controller.serviceManagerHiringController)
        form.view(self.root)

    def hrHiringView(self):
        self.entries.clear()
        self.clearView()

        self.root.title("HR – Hiring Requests")
        self.root.geometry("700x500")
        self.root.resizable(False, False)

        applications = self.model.getHiringApplications() or []
        pending = [a for a in applications if a.get("Status") == "Hiring Requested"]

        if not pending:
            tk.Label(self.root, text="No hiring requests awaiting HR.", font=("TkDefaultFont", 12)).pack(pady=30)
            tk.Button(self.root, text="Back", command=self.logInView).pack(pady=10)
            return

        app = pending[0]
        self.entries["Application"] = app

        tk.Label(self.root, text="Hiring application:", font=("TkDefaultFont", 11, "bold")).pack(pady=(16, 6))
        tk.Label(self.root, text=json.dumps(app, indent=4), justify="left", anchor="w").pack(padx=10, pady=(0, 16))

        # Action buttons
        btns = tk.Frame(self.root)
        btns.pack(pady=10)

        tk.Button(btns, text="Decline",
                  command=lambda: self.controller.hrUpdateStatus(self.entries, "Declined")).pack(side="left", padx=6)

        tk.Button(btns, text="Start Hiring Process",
                  command=lambda: self.controller.hrUpdateStatus(self.entries, "Hiring Process Started")).pack(side="left", padx=6)

        tk.Button(self.root, text="Back", command=self.logInView).pack(pady=16)
