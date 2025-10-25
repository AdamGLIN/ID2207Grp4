import inspect, sys

def correctCredentials(_model, view, controller):
    view.logInView()
    
    view.entries["username"].insert(0, "admin")
    view.entries["password"].insert(0, "1234")
    view.entries["access"].set("Admin")
    
    return controller.logInController(view.entries) is True

def wrongPassword(_model, view, controller):
    view.logInView()
    
    view.entries["username"].insert(0, "admin")
    view.entries["password"].insert(0, "4321")
    view.entries["access"].set("Admin")
    
    return controller.logInController(view.entries) is False

def wrongUsername(_model, view, controller):
    view.logInView()
    
    view.entries["username"].insert(0, "admins")
    view.entries["password"].insert(0, "1234")
    view.entries["access"].set("Admin")
    
    return controller.logInController(view.entries) is False

def wrongAccess(_model, view, controller):
    view.logInView()
    
    view.entries["username"].insert(0, "admin")
    view.entries["password"].insert(0, "1234")
    view.entries["access"].set("Customer Service Officer")
    
    return controller.logInController(view.entries) is False

testSet = [
    obj for _, obj in inspect.getmembers(sys.modules[__name__], inspect.isfunction)
    if obj.__module__ == __name__
]