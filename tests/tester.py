from tests.unitTest import testSet

class SEPTester:
    
    def __init__(self, model, view, controller):
        self.model = model
        self.view = view
        self.controller = controller
        
    def start(self):
        nb = len(testSet)
        valid = 0
        print(f"Execution of {nb} unit tests :")
        for test in testSet:
            print(f"Test of {test.__name__}")
            if not test(self.model, self.view, self.controller):
                print("Error")
            else:
                valid += 1
                print("Ok")
        print(f"Results : {valid} / {nb}")
        
