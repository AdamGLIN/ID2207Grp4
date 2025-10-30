import inspect, sys, json, os
import tkinter as tk
import tkinter.messagebox as messagebox

def correctCredentials(_model, view, controller):
    view.logInView()
    
    view.entries["Username"].insert(0, "admin")
    view.entries["Password"].insert(0, "1234")
    view.entries["Access"].set("Admin")
    
    return controller.logInController(view.entries) is True

def wrongPassword(_model, view, controller):
    view.logInView()
    
    view.entries["Username"].insert(0, "admin")
    view.entries["Password"].insert(0, "4321")
    view.entries["Access"].set("Admin")
    
    return controller.logInController(view.entries) is False

def wrongUsername(_model, view, controller):
    view.logInView()
    
    view.entries["Username"].insert(0, "admins")
    view.entries["Password"].insert(0, "1234")
    view.entries["Access"].set("Admin")
    
    return controller.logInController(view.entries) is False

def wrongAccess(_model, view, controller):
    view.logInView()
    
    view.entries["Username"].insert(0, "admin")
    view.entries["Password"].insert(0, "1234")
    view.entries["Access"].set("Customer Service Officer")
    
    return controller.logInController(view.entries) is False

def correctRequestSaveFromEmpty(_model, view, controller):
    if os.path.exists("db/request.json"):
        os.remove("db/request.json")
        
    request = {
        "Client Name" : "0",
        "Contact" : "1",
        "Type" : "2",
        "Date" : "3",
        "Budget" : "4",
        "Description" : "5",
        "Status" : "Initial",
        "Id": 0
    }
    
    view.customerServiceOfficerView()
    
    view.entries["Client Name"].insert(0, "0")
    view.entries["Contact"].insert(0, "1")
    view.entries["Type"].insert(0, "2")
    view.entries["Date"].insert(0, "3")
    view.entries["Budget"].insert(0, "4")
    view.entries["Description"].insert(0, "5")
    
    controller.clientCallController(view.entries)
    
    try :
        with open("db/request.json", "r") as f:
            return request in json.load(f)
    except (FileNotFoundError):
        return False
    
def correctRequestSaveFromNotEmpty(model, view, controller):
    data = []
    with open("db/request.json", "w") as f:
        json.dump(data, f, indent=4)
        
    request = {
        "Client Name" : "0",
        "Contact" : "1",
        "Type" : "2",
        "Date" : "3",
        "Budget" : "4",
        "Description" : "5",
        "Status" : "Initial",
        "Id": model.getNewId(data)
    }
            
    view.customerServiceOfficerView()
    
    view.entries["Client Name"].insert(0, "0")
    view.entries["Contact"].insert(0, "1")
    view.entries["Type"].insert(0, "2")
    view.entries["Date"].insert(0, "3")
    view.entries["Budget"].insert(0, "4")
    view.entries["Description"].insert(0, "5")
    
    controller.clientCallController(view.entries)
    
    try :
        with open("db/request.json", "r") as f:
            return request in json.load(f)
    except (FileNotFoundError):
        return False
    
def validInitialClientRequestAnalysis(model, view, controller):
    if os.path.exists("db/request.json"):
        os.remove("db/request.json")
        
    request = {
        "Client Name" : "0",
        "Contact" : "1",
        "Type" : "2",
        "Date" : "3",
        "Budget" : "4",
        "Description" : "5",
        "Status" : "Initial"
    }
    
    model.saveRequest(request)
        
    view.seniorCustomerServiceOfficerView()
    
    view.entries["Senior Customer Service Officer Commentary"].insert(0, "6")
    
    controller.seniorCustomerServiceOfficerReview(view.entries, True)
    
    try :
        with open("db/request.json", "r") as f:
            request["Status"] = "Financial Review"
            request["Senior Customer Service Officer Commentary"] = "6"
            return request in json.load(f)
    except (FileNotFoundError):
        return False
    
def invalidInitialClientRequestAnalysis(model, view, controller):
    if os.path.exists("db/request.json"):
        os.remove("db/request.json")
        
    request = {
        "Client Name" : "0",
        "Contact" : "1",
        "Type" : "2",
        "Date" : "3",
        "Budget" : "4",
        "Description" : "5",
        "Status" : "Initial"
    }
    
    model.saveRequest(request)
        
    view.seniorCustomerServiceOfficerView()
    
    view.entries["Senior Customer Service Officer Commentary"].insert(0, "6")
    
    controller.seniorCustomerServiceOfficerReview(view.entries, False)
    
    try :
        with open("db/request.json", "r") as f:
            request["Status"] = "Rejected"
            request["Senior Customer Service Officer Commentary"] = "6"
            return request in json.load(f)
    except (FileNotFoundError):
        return False
    
def productionManagerTaskDistribution(model, view, controller):
    if os.path.exists("db/request.json"):
        os.remove("db/request.json")
        
    request = {
        "Client Name" : "0",
        "Contact" : "1",
        "Type" : "2",
        "Date" : "3",
        "Budget" : "4",
        "Description" : "5",
        "Status" : "In Progress",
        "Photography Task Description": "6",
        "Audio Task Description" : "7",
        "Graphics Task Description" : "8",
        "Decorating Task Description" : "9",
        "Network Task Description" : "10"
    }
    
    model.saveRequest(request)
        
    view.productionManagerView()
    
    view.entries["Photography Task Description"].insert(0, "6")
    view.entries["Audio Task Description"].insert(0, "7")
    view.entries["Graphics Task Description"].insert(0, "8")
    view.entries["Decorating Task Description"].insert(0, "9")
    view.entries["Network Task Description"].insert(0, "10")
    
    controller.productionManagerController(view.entries)
    
    try :
        with open("db/request.json", "r") as f:
            request["Production Tasks Distributed"] = True
            return request in json.load(f)
    except (FileNotFoundError):
        return False
    
def financialReviewAcceptUpdatesFinance(model, view, controller):
    if os.path.exists("db/request.json"):
        os.remove("db/request.json")
        
    os.makedirs("db", exist_ok=True)
    seed = {
        "Past event season": {"budget": 200000, "spent": 180000},
        "Current event season": {"budget": 200000, "spent": 0},
        "Upcoming event season": {"budget": 200000, "spent": 0}
    }
    with open("db/sep_finance.json", "w", encoding="utf-8") as f:
        json.dump(seed, f, indent=2)

    request = {
        "Client Name": "CLIENT_A",
        "Contact": "john@client.com",
        "Type": "Conference",
        "Date": "2025-11-01",
        "Budget": "1000",
        "Description": "Test event",
        "Status": "Financial Review"
    }
    model.saveRequest(request)

    view.financialManagerView()

    # add commentary and accept
    view.entries["Financial Manager Commentary"].insert(0, "Looks good within budget.")
    controller.financialManagerController(view.entries, True)

    # verify finance spent increased by 1000
    try:
        with open("db/sep_finance.json", "r", encoding="utf-8") as f:
            spent = json.load(f)["Current event season"]["spent"]
    except Exception:
        return None
    finance_ok = (spent == 1000)

    return finance_ok

def financialReviewRejectUpdatesRequest(model, view, controller):
    if os.path.exists("db/request.json"):
        os.remove("db/request.json")

    os.makedirs("db", exist_ok=True)
    seed = {
        "Past event season": {"budget": 200000, "spent": 180000},
        "Current event season": {"budget": 200000, "spent": 0},
        "Upcoming event season": {"budget": 200000, "spent": 0}
    }
    with open("db/sep_finance.json", "w", encoding="utf-8") as f:
        json.dump(seed, f, indent=2)

    request = {
        "Client Name": "CLIENT_B",
        "Contact": "bob@client.com",
        "Type": "Expo",
        "Date": "2025-12-12",
        "Budget": "2500",
        "Description": "Reject path test",
        "Status": "Financial Review"
    }
    model.saveRequest(request)

    view.financialManagerView()
    view.entries["Financial Manager Commentary"].insert(0, "Insufficient allocation this season.")
    controller.financialManagerController(view.entries, False)

    try:
        with open("db/request.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = False

    request["Status"] = "Rejected"
    request["Financial Manager Commentary"] = "Insufficient allocation this season."
    req_ok = request in data

    # spent should remain 0 for current season
    try:
        with open("db/sep_finance.json", "r", encoding="utf-8") as f:
            spent = json.load(f)["Current event season"]["spent"]
    except Exception:
        spent = False
    
    finance_ok = (spent == 0)

    return req_ok and finance_ok

def serviceManagerHiringEmpty(_model, view, controller):
    if os.path.exists("db/hiring.json"):
        os.remove("db/hiring.json")

    entries = {
        "Name": tk.Entry(view.root),
        "Contact": tk.Entry(view.root),
        "Salary": tk.Entry(view.root),
        "Position": tk.Entry(view.root),
        "Start Date": tk.Entry(view.root),
    }
    entries["Name"].insert(0, "Alice Andersson")
    entries["Contact"].insert(0, "alice@example.com")
    entries["Salary"].insert(0, "45000")
    entries["Position"].insert(0, "Event Coordinator")
    entries["Start Date"].insert(0, "2025-11-15")

    # Call controller directly
    controller.serviceManagerHiringController(entries)

    expected = {
        "Name": "Alice Andersson",
        "Contact": "alice@example.com",
        "Salary": "45000",
        "Position": "Event Coordinator",
        "Start Date": "2025-11-15",
        "Status": "Hiring Requested",
        "Id": 0,
    }
    try:
        with open("db/hiring.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []
    return expected in data


def serviceManagerHiringNotEmpty(_model, view, controller):
    # Seed one existing application (Id=0)
    seed = [{
        "Name": "Bobby Bobson",
        "Contact": "bob@example.com",
        "Salary": "40000",
        "Position": "Tech",
        "Start Date": "2025-10-01",
        "Status": "Hiring Requested",
        "Id": 0
    }]
    os.makedirs("db", exist_ok=True)
    with open("db/hiring.json", "w", encoding="utf-8") as f:
        json.dump(seed, f, indent=4)

    # Build entries dict for the new app
    entries = {
        "Name": tk.Entry(view.root),
        "Contact": tk.Entry(view.root),
        "Salary": tk.Entry(view.root),
        "Position": tk.Entry(view.root),
        "Start Date": tk.Entry(view.root),
    }
    entries["Name"].insert(0, "Carla")
    entries["Contact"].insert(0, "carla@mail.com")
    entries["Salary"].insert(0, "48000")
    entries["Position"].insert(0, "Producer")
    entries["Start Date"].insert(0, "2025-12-01")

    controller.serviceManagerHiringController(entries)

    expected = {
        "Name": "Carla",
        "Contact": "carla@mail.com",
        "Salary": "48000",
        "Position": "Producer",
        "Start Date": "2025-12-01",
        "Status": "Hiring Requested",
        "Id": 1,
    }
    try:
        with open("db/hiring.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []
    return expected in data

def ServiceManagerBudgetAccess(model, view, controller):
    os.makedirs("db", exist_ok=True)
    seed = {
        "Current event season": {"budget": 150000, "spent": 30000}
    }
    with open("db/sep_finance.json", "w", encoding="utf-8") as f:
        json.dump(seed, f, indent=2)

    budget = controller.financeGetCurrentSeasonBudget()

    return isinstance(budget, dict) and budget.get("budget") == 150000 and budget.get("spent") == 30000



def hrDeclinesHiringRemovesFromPending(model, view, controller):
    if os.path.exists("db/hiring.json"):
        os.remove("db/hiring.json")
    app = {
        "Name": "dustin",
        "Contact": "d@example.com",
        "Salary": "42000",
        "Position": "Assistant",
        "Start Date": "2026-01-10",
        "Status": "Hiring Requested",
    }
    model.saveHiringApplication(app)

    view.hrHiringView()
    controller.hrUpdateStatus(view.entries, "Declined")

    try:
        with open("db/hiring.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    exists_declined = any(
        d.get("Name") == "dustin" and
        d.get("Contact") == "d@example.com" and
        d.get("Position") == "Assistant" and
        d.get("Status") == "Declined"
        for d in data
    )
    still_pending = any(
        d.get("Name") == "Dina Dahl" and d.get("Status") == "Hiring Requested"
        for d in data
    )
    return exists_declined and not still_pending

def hrStartsProcessRemovesFromPending(model, view, controller):
    if os.path.exists("db/hiring.json"):
        os.remove("db/hiring.json")
    app = {
        "Name": "Erik Ek",
        "Contact": "erik@example.com",
        "Salary": "47000",
        "Position": "Stage Manager",
        "Start Date": "2025-11-20",
        "Status": "Hiring Requested",
    }
    model.saveHiringApplication(app)

    view.hrHiringView()
    controller.hrUpdateStatus(view.entries, "Hiring Process Started")

    try:
        with open("db/hiring.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []
    exists_started = any(
        d.get("Name") == "Erik Ek" and d.get("Status") == "Hiring Process Started"
        for d in data
    )
    still_pending = any(
        d.get("Name") == "Erik Ek" and d.get("Status") == "Hiring Requested"
        for d in data
    )
    return exists_started and not still_pending

testSet = [
    obj for _, obj in inspect.getmembers(sys.modules[__name__], inspect.isfunction)
    if obj.__module__ == __name__
]