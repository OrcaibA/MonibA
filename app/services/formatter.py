# def format_message(event):

#     if event["type"] == "LOGIN_EVENT":

#         d = event["data"]

#         return (
#             "📢 *CASE LOGIN ALERT*\n\n"
#             f"👤 Customer: {d.get('CUSTOMER NAME')}\n"
#             f"🆔 DB Number: {d.get('DB NUMBER')}\n"
#             f"💰 Loan Amount: ₹{d.get('LOAN AMOUNT')}\n"
#             f"📅 Login Date: {d.get('LOGIN DATE')}\n"
#         )

#     return "Unknown event"

def format_message(event):

    d = event["data"]

    if event["type"] == "LOGIN_EVENT":
        title = "🔐 *CASE LOGIN ALERT*"
        date = d.get("LOGIN DATE", "")
        status = d.get("LOGIN STATUS", "")

    elif event["type"] == "LEGAL_EVENT":
        title = "⚖️ *LEGAL UPDATE*"
        date = d.get("LEGAL DATE", "")
        status = d.get("LEGAL STATUS", "")

    elif event["type"] == "VALUATION_EVENT":
        title = "🏠 *VALUATION UPDATE*"
        date = d.get("VALUATION DATE", "")
        status = d.get("VALUATION STATUS", "")

    elif event["type"] == "CASE_EVENT":
        title = "📋 *CASE STATUS UPDATE*"
        date = d.get("APPROVAL / REJECT DATE", "")
        status = d.get("CASE STATUS", "")

    elif event["type"] == "DISBURSEMENT_EVENT":
        title = "💰 *DISBURSEMENT UPDATE*"
        date = d.get("DISBUREMENT DATE", "")
        status = d.get("DISBUREMENT STATUS", "")

    else:
        title = "📢 *CASE UPDATE*"
        date = ""
        status = ""

    return (
        f"{title}\n\n"
        f"👤 *Customer:* {d.get('CUSTOMER NAME')}\n"
        f"🆔 *DB Number:* {d.get('DB NUMBER')}\n"
        f"📱 *Mobile:* {d.get('MOBILE NUMBER')}\n"
        f"💰 *Loan Amount:* ₹{d.get('LOAN AMOUNT')}\n"
        f"📅 *Date:* {date}\n"
        f"📌 *Status:* {status}\n"
        f"👨‍💼 *CRO:* {d.get('CRO')}"
    )