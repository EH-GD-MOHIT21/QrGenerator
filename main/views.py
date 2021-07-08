from django.shortcuts import render,redirect
from .qrcode import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .forms import *
from .models import ImageCollector as ic

# Create your views here.

def home(request):
    return render(request,'index.html')

@csrf_exempt
def generate(request):
    textvalue = request.POST['textvalue']
    path = createqrcode(textvalue)
    message = f"your qr is available {path} please save your qr as we don't keep record of it."
    messages.info(request,f"{message}")
    return redirect('/')

@csrf_exempt
def decode(request):
    form = UploadFileForm(request.POST, request.FILES)
    if form.is_valid():
        image = (request.FILES['file'])
        print(image)
    else:
        messages.error(request,'No files found.')
        return redirect('/')
    temp = ic(image=image)
    temp.save()
    image_path = str(temp.image)
    value = decodeqrcode(image_path)
    messages.info(request,f"Decoded message: {value}")
    return redirect('/')