import gspread

gc = gspread.service_account(filename="credentials.json")

sheet = gc.open_by_key("1MOBkrRuvqiQPy6ip_obRGAmOTDeNRTsHUyl8yGm6VSg").worksheet("Sheet1")

rows = sheet.get_all_values()

headers = rows[1]      # Row 2
data = rows[2:]         # Data starts at Row 3

records = []

for row in data:
    if any(cell.strip() for cell in row):  # Skip empty rows
        records.append(dict(zip(headers, row)))

print(records)