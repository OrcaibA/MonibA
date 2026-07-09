from fastapi import FastAPI

from app.services.google_sheet import GoogleSheetService

from app.services.monitor import SheetMonitor

from app.api.routes import router

app = FastAPI()

monitor = SheetMonitor(interval=10)


@app.get("/")
def home():
    return {"status": "running"}


@app.get("/check")
def check():

    result = monitor.check()

    return result


@app.get("/sheet")
def read_sheet():

    sheet = GoogleSheetService()

    return sheet.read()

app.include_router(router)

@app.on_event("startup")
def startup():

    monitor.start()