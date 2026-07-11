import requests
from app.core.config import settings


class WhatsAppAPI:

    BASE_URL = settings.WHATSAPP_NODE_URL

    def send_group_buffer(self, message: str, image_bytes: bytes):

        try:
            res = requests.post(
                f"{self.BASE_URL}/send-image",
                json={
                    "message": message,
                    "image": list(image_bytes)   # convert bytes → JSON safe
                },
                timeout=20
            )
            print("dd")

            return res.json()

        except Exception as e:
            return {"error": str(e)}

    def send_group(self, message: str, image_path: str):

        try:
            res = requests.post(
                f"{self.BASE_URL}/send-group",
                json={
                    "message": message,
                    "imagePath": image_path
                },
                timeout=15
            )

            res.raise_for_status()

            return res.json()

        except Exception as e:
            return {"error": str(e)}

    def send(self, group: str, message: str):

        try:
            res = requests.post(
                f"{self.BASE_URL}/send",
                json={
                    "group": group,
                    "message": message
                },
                timeout=15
            )

            res.raise_for_status()

            return res.json()

        except Exception as e:
            return {"error": str(e)}