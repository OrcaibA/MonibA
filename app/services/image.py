import io
from PIL import Image, ImageDraw, ImageFont


def create_image_buffer(data):

    img = Image.new("RGB", (900, 450), (25, 25, 25))
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("DejaVuSans.ttf", 20)
    except:
        font = None

    text = (
        "🚨 CASE LOGIN ALERT\n\n"
        f"Customer: {data.get('CUSTOMER NAME')}\n"
        f"DB: {data.get('DB NUMBER')}\n"
        f"Loan: {data.get('LOAN AMOUNT')}\n"
        f"Date: {data.get('LOGIN DATE')}"
    )

    draw.multiline_text((50, 50), text, fill="white", font=font)

    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    return buffer.read() i need to add logo and other deatails