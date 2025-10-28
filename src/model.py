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


    _SEP_FINANCE_PATH = "db/sep_finance.json"

    def _ensure_sep_finance_seed(self):
        if not os.path.exists(self._SEP_FINANCE_PATH):
            os.makedirs("db", exist_ok=True)
            seed = {
                "Past event season": {"budget": 200000, "spent": 180000},
                "Current event season": {"budget": 200000, "spent": 0},
                "Upcoming event season": {"budget": 200000, "spent": 0}
            }
            with open(self._SEP_FINANCE_PATH, "w", encoding="utf-8") as f:
                json.dump(seed, f, indent=2)

    def _load_sep_finance(self):
        self._ensure_sep_finance_seed()
        with open(self._SEP_FINANCE_PATH, "r", encoding="utf-8") as f:
            return json.load(f)

    def getSepFinanceMonths(self):
        """List of available YYYY-MM strings."""
        data = self._load_sep_finance()
        return sorted(data.keys())

    def getSepMonthlySnapshot(self, month_str: str):
        """
        Return: {'month','budget','spent','left','left_pct'}
        """
        data = self._load_sep_finance()
        row = data.get(month_str)
        if not row:
            return {"month": month_str, "budget": 0, "spent": 0, "left": 0, "left_pct": 0.0}
        budget = float(row.get("budget", 0))
        spent = float(row.get("spent", 0))
        left = budget - spent
        left_pct = (left / budget * 100.0) if budget > 0 else 0.0
        return {
            "month": month_str,
            "budget": budget,
            "spent": spent,
            "left": left,
            "left_pct": round(left_pct, 2)
        }
    
    def updateSepFinanceOnAcceptance(self, amount, season="Current event season"):
        self._ensure_sep_finance_seed()
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

