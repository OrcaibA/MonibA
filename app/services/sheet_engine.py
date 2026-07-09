# import hashlib
# from app.services.google_sheet import GoogleSheetService
# from app.services.state import StateManager


# class SheetEngine:

#     def __init__(self):
#         self.sheet = GoogleSheetService()

#     def hash_row(self, row):
#         text = "|".join(f"{k}:{row.get(k,'')}" for k in sorted(row.keys()))
#         return hashlib.md5(text.encode()).hexdigest()

#     def scan(self):

#         rows = self.sheet.read()
#         prev = StateManager.load()

#         new_state = {}
#         events = []

#         for row in rows:

#             db_id = str(row.get("DB NUMBER", "")).strip()
#             if not db_id:
#                 continue

#             login_date = row.get("LOGIN DATE", "").strip()
#             login_status = row.get("LOGIN STATUS", "").strip().upper()

#             h = self.hash_row(row)
#             new_state[db_id] = h

#             # 🔥 LOGIN EVENT RULE
#             if login_date and login_status == "COMPLETED":

#                 event_key = f"{db_id}_LOGIN"

#                 if prev.get(event_key) != "TRIGGERED":

#                     events.append({
#                         "type": "LOGIN_EVENT",
#                         "id": db_id,
#                         "data": row
#                     })

#                     new_state[event_key] = "TRIGGERED"

#         StateManager.save(new_state)

#         return events


import json
from pathlib import Path

from app.services.google_sheet import GoogleSheetService

STATE_FILE = "state.json"


TRACKED_FIELDS = [
    "LOGIN STATUS",
    "LEGAL STATUS",
    "VALUATION STATUS",
    "CASE STATUS",
    "DISBUREMENT STATUS",
]


class SheetEngine:

    def __init__(self):
        self.sheet = GoogleSheetService()

    def load_state(self):

        if not Path(STATE_FILE).exists():
            return {}

        with open(STATE_FILE, "r") as f:
            return json.load(f)

    def save_state(self, state):

        with open(STATE_FILE, "w") as f:
            json.dump(state, f, indent=2)

    def scan(self):

        rows = self.sheet.read()

        old_state = self.load_state()

        new_state = {}

        events = []

        for row in rows:

            db = row["DB NUMBER"]

            current = {}

            for field in TRACKED_FIELDS:
                current[field] = row.get(field, "").strip()

            new_state[db] = current

            # ----------------------
            # NEW RECORD
            # ----------------------
            if db not in old_state:

                if current["LOGIN STATUS"]:

                    events.append({
                        "type": "LOGIN_EVENT",
                        "id": db,
                        "data": row
                    })

                continue

            previous = old_state[db]

            # ----------------------
            # LOGIN
            # ----------------------
            if previous["LOGIN STATUS"] != current["LOGIN STATUS"]:

                events.append({
                    "type": "LOGIN_EVENT",
                    "id": db,
                    "data": row
                })

            # ----------------------
            # LEGAL
            # ----------------------
            if previous["LEGAL STATUS"] != current["LEGAL STATUS"]:

                events.append({
                    "type": "LEGAL_EVENT",
                    "id": db,
                    "data": row
                })

            # ----------------------
            # VALUATION
            # ----------------------
            if previous["VALUATION STATUS"] != current["VALUATION STATUS"]:

                events.append({
                    "type": "VALUATION_EVENT",
                    "id": db,
                    "data": row
                })

            # ----------------------
            # CASE
            # ----------------------
            if previous["CASE STATUS"] != current["CASE STATUS"]:

                events.append({
                    "type": "CASE_EVENT",
                    "id": db,
                    "data": row
                })

            # ----------------------
            # DISBURSEMENT
            # ----------------------
            if previous["DISBUREMENT STATUS"] != current["DISBUREMENT STATUS"]:

                events.append({
                    "type": "DISBURSEMENT_EVENT",
                    "id": db,
                    "data": row
                })

        self.save_state(new_state)

        return events