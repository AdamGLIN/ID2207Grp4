import inspect, sys

def correctCredentials(_model, view, controller):
    view.logInView()
    
    view.entries["username"].insert(0, "admin")
    view.entries["password"].insert(0, "1234")
    
    return controller.logInController(view.entries) is True

def wrongCredentials(_model, view, controller):
    view.logInView()
    
    view.entries["username"].insert(0, "admin")
    view.entries["password"].insert(0, "4321")
    
    return controller.logInController(view.entries) is False

testSet = [
    obj for _, obj in inspect.getmembers(sys.modules[__name__], inspect.isfunction)
    if obj.__module__ == __name__
]