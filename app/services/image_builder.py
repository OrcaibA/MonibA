
import io
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
DEFAULT_LOGO = BASE_DIR / "app" / "assets" / "vis.jpg"

WIDTH, HEIGHT = 1080,1080
BG=(8,26,51)
CARD=(18,42,78)
ACCENT=(255,196,0)
WHITE=(245,245,245)
MUTED=(170,190,220)
GREEN=(46,204,113)
ORANGE=(243,156,18)
RED=(231,76,60)
GRAY=(149, 165, 166)

def _font(size,bold=False):
    names=["DejaVuSans-Bold.ttf","DejaVuSans.ttf"] if bold else ["DejaVuSans.ttf","Arial.ttf"]
    for n in names:
        try:
            return ImageFont.truetype(n,size)
        except: pass
    return ImageFont.load_default()

def round_box(draw,xy,r,fill,outline=None):
    draw.rounded_rectangle(xy,radius=r,fill=fill,outline=outline,width=2 if outline else 1)

def badge(draw, x, y, text, color=None):
    f = _font(22, True)

    # No badge background
    if color is None:
        draw.text(
            (x + 14, y + 8),
            text,
            font=f,
            fill="white"
        )
        return

    w = draw.textbbox((0, 0), text, font=f)[2] + 28

    round_box(
        draw,
        (x, y, x + w, y + 40),
        18,
        color
    )

    draw.text(
        (x + 14, y + 8),
        text,
        font=f,
        fill="white"
    )

def create_image_buffer(data,logo_path=None):
    img=Image.new("RGB",(WIDTH,HEIGHT),BG)
    d=ImageDraw.Draw(img)
    # Load background
    # if background_path is None:
    #     background_path = DEFAULT_LOGO

    # try:
    #     img = (
    #         Image.open(background_path)
    #         .convert("RGB")
    #         .resize((WIDTH, HEIGHT), Image.Resampling.LANCZOS)
    #     )
    # except Exception as e:
    #     print("Background Error:", e)
    #     img = Image.new("RGB", (WIDTH, HEIGHT), BG)

    # d = ImageDraw.Draw(img)

    # Optional: dark overlay for better text visibility
    # overlay = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 90))
    # img = Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")
    # d = ImageDraw.Draw(img)

    # Header
    round_box(d, (30, 30, 1050, 150), 24, (15, 45, 90))

    # Use default logo if none is provided
    # if logo_path is None:
    #     logo_path = DEFAULT_LOGO

    # # Try to load the logo
    # try:
    #     logo = (
    #         Image.open(logo_path)
    #         .convert("RGBA")
    #         .resize((90, 90), Image.Resampling.LANCZOS)
    #     )

    #     img.paste(logo, (50, 45), logo)

    # except Exception as e:
    #     print("Logo Error:", e)

    #     # Fallback placeholder
    #     round_box(d, (50, 45, 140, 135), 18, (35, 80, 160))
    #     d.text((65, 75), "LOGO", font=_font(20, True), fill="white")

    # Header text
    d.text((60, 55), "CASE STATUS", font=_font(42, True), fill=ACCENT)
    d.text((60, 105), "Nagercoil Branch Loan Monitoring", font=_font(20), fill=MUTED)

    # Cards
    round_box(d,(40,190,520,930),20,CARD,(60,120,220))
    round_box(d,(560,190,1040,930),20,CARD,(60,120,220))

    d.text((65,220),"CUSTOMER DETAILS",font=_font(28,True),fill=WHITE)
    d.text((585,220),"CASE STATUS",font=_font(28,True),fill=WHITE)

    left=[
        ("Customer",data.get("CUSTOMER NAME","")),
        ("Mobile",data.get("MOBILE NUMBER","")),
        ("DB Number",data.get("DB NUMBER","")),
        ("Loan Amount","₹ "+str(data.get("LOAN AMOUNT",""))),
        ("Login Date",data.get("LOGIN DATE","")),
        ("CRO",data.get("CRO",""))
    ]
    y=280
    for k,v in left:
        d.text((70,y),k,font=_font(18,True),fill=MUTED)
        d.text((70,y+28),str(v),font=_font(24),fill=WHITE)
        y+=95

    def stat(name,val,y):
        d.text((590,y),name,font=_font(18,True),fill=MUTED)
        txt=(val or "").upper()
        # col=ORANGE
        # if txt=="COMPLETED": col=GREEN
        # elif txt=="RECEIVED": col=GREEN
        # elif txt=="APPROVED": col=GREEN
        # elif txt=="REJECTED": col=RED
        # badge(d,800,y-5,txt or "-",col)
        if txt in ("", "N/A", "NA", "-", "NONE"):
            badge(d, 800, y - 5, "-", None)

        else:
            col = ORANGE

            if txt in ("COMPLETED", "RECEIVED", "APPROVED"):
                col = GREEN

            elif txt == "REJECTED":
                col = RED

            badge(d, 800, y - 5, txt, col)

    stat("Login",data.get("LOGIN STATUS",""),280)
    stat("Legal",data.get("LEGAL STATUS",""),370)
    stat("Valuation",data.get("VALUATION STATUS",""),460)
    stat("Case",data.get("CASE STATUS",""),550)
    stat("Disbursement",data.get("DISBUREMENT STATUS",""),640)

    # Timeline
    d.text((590,760),"PROCESS",font=_font(24,True),fill=WHITE)
    stages = [
        ("LOGIN", data.get("LOGIN STATUS", "")),
        ("LEGAL", data.get("LEGAL STATUS", "")),
        ("VALUATION", data.get("VALUATION STATUS", "")),
        ("APPROVAL", data.get("CASE STATUS", "")),
        ("DISBURSE", data.get("DISBUREMENT STATUS", ""))
    ]

    x = 610

    for i, (title, status) in enumerate(stages):

        status = (status or "").strip().upper()

        if status in ("COMPLETED", "RECEIVED", "APPROVED", "DONE"):
            color = GREEN

        elif status in ("PENDING", "IN-PROGRESS", "IN-PROGESS"):
            color = ORANGE

        elif status in ("REJECTED", "FAILED"):
            color = RED

        
        elif status in ("", "N/A", "NA", "-", "NONE"):
            color = GRAY

        else:
            color = (90, 110, 140)

        print(f"Stage: {title}, Status: [{status}]")

        d.ellipse(
            (x-12, 820-12, x+12, 820+12),
            fill=color
        )

        if i < len(stages) - 1:
            d.line(
                (x+12, 820, x+88, 820),
                fill=(120,140,180),
                width=4
            )

        d.text(
            (x-25, 845),
            title if title else "-",
            font=_font(14),
            fill=WHITE
        )

        x += 100
    completed = []
    pending = []
    rejected = []
    na = []

    for _, status in stages:
        status = (status or "").upper()
        completed.append(status in ("COMPLETED", "RECEIVED", "APPROVED", "DONE"))
        pending.append(status in ("PENDING", "IN-PROGRESS"))
        rejected.append(status == "REJECTED")
        na.append(status in ("N/A",""))

    x = 610

    for i, (title, status) in enumerate(stages):

        # circle = GREEN if completed[i] RED elif rejected[i] else ORANGE
        if completed[i]:
            circle = GREEN

        elif rejected[i]:
            circle = RED

        elif na[i]:
            circle = GRAY

        else:
            circle = ORANGE

        d.ellipse((x-12,808,x+12,832), fill=circle)

        if i < len(stages)-1:
            line_color = GREEN if completed[i] else (120,140,180)
            d.line((x+12,820,x+88,820), fill=line_color, width=5)

        d.text((x-25,845), title, font=_font(14), fill=WHITE)

        x += 100 

    # d.text((540,1015),"Generated by MonibA",anchor="mm",font=_font(20),fill=MUTED)

    buf=io.BytesIO()
    img.save(buf,format="PNG")
    buf.seek(0)
    return buf.read()

if __name__=="__main__":
    sample={
        "CUSTOMER NAME":"SAJINI N",
        "MOBILE NUMBER":"7867843766",
        "DB NUMBER":"DB202607072399765",
        "LOAN AMOUNT":"1000000",
        "LOGIN DATE":"07-Jul-2026",
        "LOGIN STATUS":"COMPLETED",
        "LEGAL STATUS":"PENDING",
        "VALUATION STATUS":"PENDING",
        "CASE STATUS":"IN-PROGRESS",
        "DISBUREMENT STATUS":"PENDING",
        "CRO":"PENIN JOSE"
    }
    with open("preview.png","wb") as f:
        f.write(create_image_buffer(sample))
