import io
import base64
import qrcode
from django.shortcuts import render

def home(request):
    qr_data_uri = None
    qr_text = ""
    qr_type = request.GET.get("type")
    data = request.GET.get("data")

    if data:
        # ✅ Choose what to generate
        if qr_type == "help":
            data = "mailto:dhoniseravath0134@gmail.com?subject=Need%20Help&body=Hi%20Dhonu%2C%20I%20need%20some%20help%20regarding%20the%20QR%20project."
            qr_text = "SCAN AND REPORT YOUR ISSUE ON ABOVE GMAIL QR CODE"
        elif qr_type == "url":
            if not data.startswith("http://") and not data.startswith("https://"):
                data = "https://" + data
            qr_text = f"Website: {data}"
        elif qr_type == "text":
            qr_text = f"Text: {data}"
        else:
            qr_text = "Invalid input type!"

        # ✅ Generate QR
        qr = qrcode.make(data)
        buffer = io.BytesIO()
        qr.save(buffer, format="PNG")
        img_b64 = base64.b64encode(buffer.getvalue()).decode()
        qr_data_uri = f"data:image/png;base64,{img_b64}"

    return render(request, "index.html", {"qr_data_uri": qr_data_uri, "qr_text": qr_text})
