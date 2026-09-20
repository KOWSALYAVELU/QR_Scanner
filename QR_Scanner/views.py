from django.shortcuts import render
from .forms import QRCodeForm
import qrcode
import os
from django.conf import settings

def generate_qr_code(request):
    if request.method == "POST":
        form = QRCodeForm(request.POST)
        if form.is_valid():
            restaurant_name = form.cleaned_data['restaurant_name']
            url = form.cleaned_data['url']

            #Genrate QR code 
            qr = qrcode.make(url)
            file_name= restaurant_name.replace(" ", "_").lower() + "_menu.png"
            file_path = os.path.join(settings.MEDIA_ROOT, file_name)
            # Save the QR code image to the media folder
            qr.save(file_path)

            #Image URL  Create
            qr_url = settings.MEDIA_URL + file_name            
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