from fastapi import APIRouter
from app.services.whatsapp import WhatsAppAPI
from app.services.sheet_engine import SheetEngine
from app.services.formatter import format_message
from app.services.image_builder import create_image_buffer

router = APIRouter()

engine = SheetEngine()
wa = WhatsAppAPI()


@router.get("/scan")
def scan():

    events = engine.scan()

    results = []

    for event in events:

        msg = format_message(event)

        img_buffer = create_image_buffer(event["data"])

        res = wa.send_group_buffer(msg, img_buffer)

        results.append({
            "event": event,
            "whatsapp": res
        })

    return {
        "count": len(events),
        "results": results
    }


@router.post("/send")
def send_test():

    return wa.send(
        group="test",
        message="Hello from FastAPI 🚀"
    )