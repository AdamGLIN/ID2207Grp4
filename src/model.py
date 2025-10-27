import json

Access = [
    "Customer Service Officer",
    "Senior Customer Service Officer",
    "Production Manager",
    "Service Manager",
    "Financial Manager",
    "Admin"
]

Status = [
    "Initial",
    "Financial Review",
    "Accepted",
    "Rejected"
]

class SEPModel :
    
    def __init__(self):
        pass
    
    def getNewId(self, data):
        usedIds = [request["Id"] for request in data]
        id = 0
        while True:
            if not id in usedIds:
                return id
            else:
                id += 1

    def getCredentials(self):
        with open("db/users.json", "r", encoding="utf-8") as f:
            return [tuple(x) for x in json.load(f)]
        
    def getRequests(self):
        try:
            with open("db/request.json", "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
        
    def saveRequest(self, request):
        data = self.getRequests()
        
        if "Id" not in request:
            request["Id"] = self.getNewId(data)
            data.append(request)
        else:
            for i in range(len(data)):
                if data[i]["Id"] == request["Id"]:
                    data[i] = request
                    break
        
        with open("db/request.json", "w") as f:
            json.dump(data, f, indent=4)
            
    
