import io
import base64
import qrcode
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    qr_data_uri = None
    qr_text = ""
    qr_type = request.GET.get("type")
    data = request.GET.get("data")

    if data:
        # Decide what to generate
        if qr_type == "help":
            data = "mailto:dhoniseravath0134@gmail.com?subject=QR%20Help&body=Hello%20Dhonu"
        elif qr_type == "url":
            if not data.startswith("http"):
                data = "https://" + data
        elif qr_type == "text":
            data = data
        else:
            data = "Invalid type"

        qr = qrcode.make(data)
        buffer = io.BytesIO()
        qr.save(buffer, format="PNG")
        img_b64 = base64.b64encode(buffer.getvalue()).decode()
        qr_data_uri = f"data:image/png;base64,{img_b64}"
        qr_text = data

    return render(request, "index.html", {"qr_data_uri": qr_data_uri, "qr_text": qr_text})
