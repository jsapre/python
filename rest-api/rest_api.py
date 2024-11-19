import json


class RestAPI:

    def __init__(self, database):
        self.database = database

    def find_user(self, name) -> dict | None:
        user_list = self.database["users"]
        for user in user_list:
            if user["name"] == name:
                return user
        return None

    def get_all_user_list(self):
        result = {"users": []}
        for user in self.database["users"]:
            result["users"].append(user["name"])

        result["users"].sort()
        return result

    def get(self, url, payload: str | None = None):
        if url == "/users":
            if not payload:
                data = self.get_all_user_list()
            else:
                data = json.loads(payload)

            response_list = {"users": []}
            for name in sorted(data["users"]):
                response_list["users"].append(self.find_user(name))
            return json.dumps(response_list)

        else:
            return '{"error":"no api on this path"}'

    def post(self, url, payload):
        if url == "/add":
            return self.create_user(payload)
        elif url == "/iou":
            return self.create_iou(payload)
        else:
            return '{"error":"no api on this path"}'

    def create_user(self, payload):
        data = json.loads(payload)
        new_user = data["user"]
        if not self.find_user(new_user):
            user = {
                "name": new_user,
                "owes": {},
                "owed_by": {},
                "balance": 0.0,
            }
            self.database["users"].append(user)
            return json.dumps(user)
        return None

    def create_iou(self, payload):
        data = json.loads(payload)
        lender_name = data["lender"]
        borrower_name = data["borrower"]
        amount = data["amount"]
        lender, borrower = self.find_user(lender_name), self.find_user(borrower_name)
        if lender and borrower:
            if borrower_name in lender["owed_by"]:
                lender["owed_by"][borrower_name] += amount
            else:
                lender["owed_by"][borrower_name] = amount

            lender["balance"] += amount

            if lender_name in borrower["owes"]:
                borrower["owes"][lender_name] += amount
            else:
                borrower["owes"][lender_name] = amount

            borrower["balance"] -= amount

            # Case of mutual borrow - lend
            if borrower_name in lender["owed_by"] and borrower_name in lender["owes"]:
                correction = min(
                    lender["owed_by"][borrower_name], lender["owes"][borrower_name]
                )
                lender["owed_by"][borrower_name] = (
                    lender["owed_by"][borrower_name] - correction
                )
                if lender["owed_by"][borrower_name] == 0.0:
                    del lender["owed_by"][borrower_name]

                lender["owes"][borrower_name] = (
                    lender["owes"][borrower_name] - correction
                )
                if lender["owes"][borrower_name] == 0.0:
                    del lender["owes"][borrower_name]

                correction = min(
                    borrower["owed_by"][lender_name], borrower["owes"][lender_name]
                )
                borrower["owed_by"][lender_name] = (
                    borrower["owed_by"][lender_name] - correction
                )
                if borrower["owed_by"][lender_name] == 0.0:
                    del borrower["owed_by"][lender_name]

                borrower["owes"][lender_name] = (
                    borrower["owes"][lender_name] - correction
                )
                if borrower["owes"][lender_name] == 0.0:
                    del borrower["owes"][lender_name]

            if lender_name < borrower_name:
                return json.dumps({"users": [lender, borrower]})
            else:
                return json.dumps({"users": [borrower, lender]})

        return None
