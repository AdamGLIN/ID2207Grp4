import inspect, sys, json, os

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
    
    view.customerServiceOfficerView()
    
    request = {
        "Client Name" : "0",
        "Contact" : "1",
        "Type" : "2",
        "Date" : "3",
        "Budget" : "4",
        "Description" : "5",
        "Status" : "Initial"
    }
    
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
    
def correctRequestSaveFromNotEmpty(_model, view, controller):
    data = []
    with open("db/request.json", "w") as f:
            json.dump(data, f, indent=4)
            
    view.customerServiceOfficerView()
    
    request = {
        "Client Name" : "0",
        "Contact" : "1",
        "Type" : "2",
        "Date" : "3",
        "Budget" : "4",
        "Description" : "5",
        "Status" : "Initial"
    }
    
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

testSet = [
    obj for _, obj in inspect.getmembers(sys.modules[__name__], inspect.isfunction)
    if obj.__module__ == __name__
]