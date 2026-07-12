from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    GOOGLE_SHEET_ID: str
    GOOGLE_WORKSHEET: str = "Sheet1"
    
    WHATSAPP_GROUP: str

    POLL_INTERVAL: int = 10

    CHROME_PROFILE: str = "./sessions/chrome"

    HEADLESS: bool = False

    WHATSAPP_NODE_URL: str 
    STATE_FILE: str

    ONEDRIVE_REMOTE: str
    EXCEL_LOCAL_DIR: str
    EXCEL_FILE: str

    class Config:
        env_file = ".env"


settings = Settings()