# import hashlib

# from app.services.google_sheet import GoogleSheetService
# from app.services.state import StateManager


# class SheetMonitor:

#     def __init__(self):

#         self.sheet = GoogleSheetService()

#     def row_hash(self, row):

#         text = "|".join(
#             str(v) for v in row.values()
#         )

#         return hashlib.md5(text.encode()).hexdigest()

#     def check(self):

#         current_rows = self.sheet.read()

#         previous_state = StateManager.load()

#         new_state = {}

#         new_records = []

#         updated_records = []

#         for row in current_rows:

#             db_number = row["DB NUMBER"]

#             current_hash = self.row_hash(row)

#             new_state[db_number] = current_hash

#             if db_number not in previous_state:

#                 new_records.append(row)

#             elif previous_state[db_number] != current_hash:

#                 updated_records.append(row)

#         StateManager.save(new_state)

#         return {
#             "new": new_records,
#             "updated": updated_records
#         }

import time
import threading
import traceback
from app.services.sheet_engine import SheetEngine
from app.services.formatter import format_message
from app.services.image_builder import create_image_buffer
from app.services.whatsapp import WhatsAppAPI
from app.services.onedrive_sync import OneDriveSync

class SheetMonitor:

    def __init__(self, interval=10):
        self.interval = interval
        self.sync = OneDriveSync()
        self.engine = SheetEngine()
        self.wa = WhatsAppAPI()

    def start(self):
        threading.Thread(target=self.run, daemon=True).start()

    # def run(self):

    #     print("✅ Sheet Monitor Started")

    #     while True:

    #         try:

    #             events = self.engine.scan()

    #             for event in events:

    #                 print("New Event:", event["type"], event["id"])

    #                 msg = format_message(event)

    #                 img = create_image_buffer(event["data"])

    #                 self.wa.send_group_buffer(msg, img)

    #             time.sleep(self.interval)

    #         except Exception as e:

    #             print("Monitor Error:", e)

    #             time.sleep(self.interval)

    def run(self):

        print("✅ Monitor Started")

        while True:

            try:

                print("🔄 Syncing OneDrive...")

                self.sync.sync()

                print("✅ Excel Updated")

                events = self.engine.scan()

                for event in events:
                    print("Events:", events)
                    print("Events type:", type(events))

                    print(
                        f"📢 {event['type']} -> {event['id']}"
                    )

                    # print(event["data"])

                    msg = format_message(event)

                    img = create_image_buffer(
                        event["data"]
                    )

                    result = self.wa.send_group_buffer(
                        msg,
                        img
                    )

                    print(result)

            except Exception as e:
                traceback.print_exc()
                print("Monitor Error:", e)

            time.sleep(self.interval)