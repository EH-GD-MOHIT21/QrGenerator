from qrproject.settings import BASE_DIR
import qrcode
from datetime import datetime
import cv2
from django.conf import settings
from pathlib import os
from PIL import *

def abspath(path):
    return os.path.join(BASE_DIR,f'media/{path}')

def createqrcode(data):
    ctime = str(datetime.now())
    ctime = ctime.replace('.','-')
    ctime = ctime.replace(':','-')
    ctime = ctime.replace(' ','_')
    img = qrcode.make(data)
    path = os.path.join(BASE_DIR,f"media/{ctime}.png")
    img.save(path)
    return settings.URL + f"media/{ctime}.png"

def decodeqrcode(image):
    image = abspath(image)
    decoder = cv2.QRCodeDetector()
    val,points,staqr = decoder.detectAndDecode(cv2.imread(image))
    return val