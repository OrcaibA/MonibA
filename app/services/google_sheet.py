import gspread

from app.core.config import settings


class GoogleSheetService:

    def __init__(self):
        self.client = gspread.service_account(
            filename="credentials.json"
        )

        self.sheet = (
            self.client
            .open_by_key(settings.GOOGLE_SHEET_ID)
            .worksheet(settings.GOOGLE_WORKSHEET)
        )

    def read(self):

        rows = self.sheet.get_all_values()

        headers = rows[1]
        data = rows[2:]

        records = []

        for row in data:

            # Make sure row length matches header length
            row += [""] * (len(headers) - len(row))

            record = {}

            for h, v in zip(headers, row):

                h = h.strip()

                # Skip empty header
                if h == "":
                    continue

                record[h] = v.strip()

            # Skip empty records
            if not record.get("DB NUMBER"):
                continue

            records.append(record)

        return records