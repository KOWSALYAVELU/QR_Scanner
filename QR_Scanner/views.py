from django.shortcuts import render
from .forms import QRCodeForm
import qrcode
import base64                                  
from io import BytesIO


def generate_qr_code(request):
    if request.method == "POST":
        form = QRCodeForm(request.POST)
        if form.is_valid():
            restaurant_name = form.cleaned_data['restaurant_name']
            url = form.cleaned_data['url']

            #Genrate QR code 
            qr = qrcode.make(url)
            file_name= restaurant_name.replace(" ", "_").lower() + "_menu.png"

            buffer = BytesIO()
            qr.save(buffer, format="PNG")
            qr_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")
        
            #Image URL  Create
            qr_url = "data:image/png;base64," + qr_base64           
            context = {
                 'restaurant_name': restaurant_name,
                 'qr_url': qr_url,
                 'file_name' : file_name,

            }
            return render(request, 'qr_success.html',context)
    else:
        form = QRCodeForm()
        context = {
            'form': form
            }
        return render(request, 'generate_qr_code.html',context)