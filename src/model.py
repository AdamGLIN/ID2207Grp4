import json
import os

Access = [
    "Customer Service Officer",
    "Senior Customer Service Officer",
    "Production Manager",
    "Service Manager",
    "Financial Manager",
    "HR Manager",
    "Admin"
]

Status = [
    "Initial",
    "Financial Review",
    "Administration Review",
    "Accepted",
    "In Progress",
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


    _SEP_FINANCE_PATH = "db/sep_finance.json"

    def _ensure_finance_file(self):
        if not os.path.exists(self._SEP_FINANCE_PATH):
            os.makedirs("db", exist_ok=True)
            with open(self._SEP_FINANCE_PATH, "w", encoding="utf-8") as f:
                json.dump({}, f, indent=2)

    def _load_finance(self):
        self._ensure_finance_file()
        with open(self._SEP_FINANCE_PATH, "r", encoding="utf-8") as f:
            return json.load(f)

    def _save_finance(self, data):
        os.makedirs("db", exist_ok=True)
        with open(self._SEP_FINANCE_PATH, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    def hasCurrentSeasonBudget(self):
        data = self._load_finance()
        return "Current event season" in data

    def getCurrentSeasonBudget(self):
        data = self._load_finance()
        return data.get("Current event season")

    def createCurrentSeasonBudget(self, amount):
        self._ensure_finance_file()
        try:
            amt = float(amount)
        except (TypeError, ValueError):
            raise ValueError("Budget amount must be numeric.")
        if amt < 0:
            raise ValueError("Budget amount must be non-negative.")

        data = self._load_finance()
        data["Current event season"] = {"budget": amt, "spent": 0.0}
        self._save_finance(data)

    
    def updateSepFinanceOnAcceptance(self, amount, season="Current event season"):
        if not self.hasCurrentSeasonBudget():
            return  # No budget to update
        try:
            amt = float(amount) if amount is not None else 0.0
        except (TypeError, ValueError):
            amt = 0.0

        with open(self._SEP_FINANCE_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)

        row = data.get(season, {"budget": 0, "spent": 0})
        row["spent"] = float(row.get("spent", 0)) + max(0.0, amt)

        data[season] = row

        os.makedirs("db", exist_ok=True)
        with open(self._SEP_FINANCE_PATH, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    _HIRING_PATH = "db/hiring.json"

    def getHiringApplications(self):
        """Return list of hiring applications (minimal)."""
        try:
            with open(self._HIRING_PATH, "r", encoding="utf-8") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def saveHiringApplication(self, application):
        """Append or update a hiring application."""
        data = self.getHiringApplications()
        # assign Id if missing
        if "Id" not in application:
            used_ids = [a.get("Id") for a in data if "Id" in a]
            new_id = 0
            while new_id in used_ids:
                new_id += 1
            application["Id"] = new_id
            data.append(application)
        else:
            for i, a in enumerate(data):
                if a.get("Id") == application["Id"]:
                    data[i] = application
                    break
        os.makedirs("db", exist_ok=True)
        with open(self._HIRING_PATH, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

