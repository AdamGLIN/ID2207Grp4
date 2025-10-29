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
                case "Service Manager":
                    self.view.serviceManagerView()
                case "HR Manager":
                    self.view.hrHiringView()
                case "Admin":
                    self.view.administrationManagerView()
                case _:
                    messagebox.showinfo("Ok", f"Welcome, {username} !")
            return True
        else:
            messagebox.showerror("Error", "Wrong credentials")
            return False
        
    def financeGetPeriods(self):
        return self.model.getSepFinancePeriods()

    def financeGetMonthlySnapshot(self, month_str: str):
        return self.model.getSepFinanceSnapshot(month_str)
        
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
        if "Request" not in entries:
            messagebox.showerror("Error", "No request selected.")
            return

        request = entries["Request"]
        commentary = entries.get("Financial Manager Commentary").get().strip() if entries.get("Financial Manager Commentary") else ""

        if not commentary:
            messagebox.showwarning("Missing commentary", "Please add a commentary before proceeding.")
            return

        request["Financial Manager Commentary"] = commentary

        if valid:
            request["Status"] = "Administration Review"
            try:
                self.model.updateSepFinanceOnAcceptance(request.get("Budget"))
            except Exception as e:
                messagebox.showwarning("Finance update", f"Saved request, but failed to update SEP finance: {e}")
        else:
            request["Status"] = "Rejected"

        self.model.saveRequest(request)
        try:
            self.view.financialManagerView()
        except AttributeError:
            messagebox.showinfo("Saved", "Decision recorded.")

    def serviceManagerHiringController(self, entries):
        """Create a minimal hiring application from the form fields."""
        name = entries["Name"].get().strip()
        contact = entries["Contact"].get().strip()
        salary = entries["Salary"].get().strip()
        position = entries["Position"].get().strip()
        start_date = entries["Start Date"].get().strip()

        if not name or not salary or not position or not start_date:
            messagebox.showwarning("Missing fields", "Please fill Name, Salary, Position and Start Date.")
            return

        application = {
            "Name": name,
            "Contact": contact,
            "Salary": salary,
            "Position": position,
            "Start Date": start_date,
            "Status": "Hiring Requested"
        }

        self.model.saveHiringApplication(application)
        messagebox.showinfo("Saved", "Hiring application created.")
        # stay on page for rapid entry
        try:
            self.view.serviceManagerView()
        except AttributeError:
            pass

    def hrUpdateStatus(self, entries, new_status: str):
        """HR sets status for the selected hiring application, then refreshes the HR page."""
        if "Application" not in entries:
            messagebox.showerror("Error", "No hiring application selected.")
            return

        app = entries["Application"]
        app["Status"] = new_status
        self.model.saveHiringApplication(app)
        messagebox.showinfo("Saved", f"Application status set to: {new_status}")
        try:
            self.view.hrHiringView()
        except AttributeError:
            pass

    def administrationManagerController(self, entries, valid):
        request = entries["Request"]
        commentary = entries["Administration Manager Commentary"].get()
        request["Senior Customer Service Officer Commentary"] = commentary
        if valid :
            request["Status"] = "Accepted"
        else :
            request["Status"] = "Rejected"
        self.model.saveRequest(request)
        self.view.administrationManagerView()
