import json

Access = [
    "Customer Service Officer",
    "Senior Customer Service Officer",
    "Admin"
]

class SEPModel :
    
    def __init__(self):
        pass

    def getCredentials(self):
        with open("db/users.json", "r", encoding="utf-8") as f:
            return [tuple(x) for x in json.load(f)]
        
    def saveRequest(self, request):
        try:
            with open("db/request.json", "r") as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []
            
        data.append(request)
        
        with open("db/request.json", "w") as f:
            json.dump(data, f, indent=4)
