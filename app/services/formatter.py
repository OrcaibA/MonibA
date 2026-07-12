def format_message(event):

    d = event["data"]

    title = "📢 *CASE UPDATE*"
    date = ""
    status = ""
    received = None
    reason = None

    if event["type"] == "LOGIN_EVENT":
        title = "🔐 *CASE LOGIN ALERT*"
        date = d.get("LOGIN DATE", "").split(" ")[0]
        status = d.get("LOGIN STATUS", "")

    elif event["type"] == "LEGAL_EVENT":
        title = "⚖️ *LEGAL UPDATE*"
        date = d.get("LEGAL INITIATED", "").split(" ")[0]
        received = (d.get("LEGAL RECEVIED") or "NOT RECEIVED").split(" ")[0]
        status = d.get("LEGAL STATUS", "")

    elif event["type"] == "VALUATION_EVENT":
        title = "🏠 *VALUATION UPDATE*"
        date = d.get("VALUATION DATE", "").split(" ")[0]
        received = (d.get("VALUATION RECEVIED") or "NOT RECEIVED").split(" ")[0]
        status = d.get("VALUATION STATUS", "")

    elif event["type"] == "CASE_EVENT":
        title = "📋 *CASE STATUS UPDATE*"
        date = d.get("APPROVAL / REJECT DATE", "").split(" ")[0]
        status = d.get("CASE STATUS", "")

        if status.upper() == "REJECTED":
            reason = d.get("REJECT REASON")
        # else:
        #     reason = d.get("CASE APPROVED")

    elif event["type"] == "DISBURSEMENT_EVENT":
        title = "💰 *DISBURSEMENT UPDATE*"
        date = d.get("DISBUREMENT DATE", "").split(" ")[0]
        received = (d.get("DISBUREMENT PLAN DATE") or "NOT PLANNED").split(" ")[0]
        status = d.get("DISBUREMENT STATUS", "")

    message = (
        f"{title}\n\n"
        f"👤 *Customer:* {d.get('CUSTOMER NAME', '')}\n"
        f"🆔 *DB Number:* {d.get('DB NUMBER', '')}\n"
        f"📱 *Mobile:* {d.get('MOBILE NUMBER', '')}\n"
        f"💰 *Loan Amount:* ₹{d.get('LOAN AMOUNT', '')}\n"
        f"📅 *Date:* {date}\n"
        f"📌 *Status:* {status}\n"
        # f"📌 *Status:* {status}\n"
    )

    if received:
        message += f"📥 *Received:* {received}\n"
        print("Received:", received)

    if reason:
        message += f"❌ *Reject Reason:* {reason}\n"

    message += f"👨‍💼 *CRO:* {d.get('CRO', '')}"

    return message