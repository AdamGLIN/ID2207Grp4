import json

Access = [
    "Customer Service Officer",
    "Senior Customer Service Officer",
    "Admin"
]

class SEPModel :
    
    def __init__(self):
        pass

    def getCredentials(self) :
        with open("db/users.json", "r", encoding="utf-8") as f:
            return [tuple(x) for x in json.load(f)]
