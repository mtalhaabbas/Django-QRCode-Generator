from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
import qrcode 
from datetime import datetime
from django.conf import settings


def index(request):
    return render(request,'index.html')


@csrf_exempt
def QRCode(request):
    if request.method == "POST":
        json_data = json.loads(request.body)
        data = json_data['data']
        qr = qrcode.make(data)
        pic='media/QR_Code_'+str(datetime.now().strftime("%f"))+'.png'
        qr.save(pic)
        result=settings.SITE_URL+pic
        dictionary = {
            'result':result
        }
        return JsonResponse(dictionary)
    else:
        dictionary = {
            'result': 'invalid method',
        }
        return JsonResponse(dictionary)