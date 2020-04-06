from django.shortcuts import render
import json
from django.http import JsonResponse
import urllib.request
import os

import requests
# Create your views here.



def voice(request):
    client_id = "salwDsOe8RoUMKEKAKMh"
    client_secret = "A8_2T9SxK_"
    url = "https://openapi.naver.com/v1/vision/face" # 얼굴인식
    # Imagepath= open(os.path.dirname(os.path.realpath(__file__)) + '../image/IU.png', "rb")
    # print(Imagepath)
    files = {'image':open(os.path.dirname(os.path.realpath(__file__)) + '\\image\\IU.png', "rb")}
    headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret }
    response = requests.post(url,  files=files, headers=headers)
    rescode = response.status_code
    if(rescode==200):
        print (response.text)
    else:
        print("Error Code:" + rescode)
    return render(request, 'home/html/voice.html', context={"response" : response.text})


def home(request):
    client_id = "salwDsOe8RoUMKEKAKMh"
    client_secret = "A8_2T9SxK_"
    url = "https://openapi.naver.com/v1/vision/face" # 얼굴인식
    # Imagepath= open(os.path.dirname(os.path.realpath(__file__)) + '../image/IU.png', "rb")
    # print(Imagepath)
    files = {'image':open(os.path.dirname(os.path.realpath(__file__)) + '\\image\\IU.png', "rb")}
    headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret }
    response = requests.post(url,  files=files, headers=headers)
    rescode = response.status_code
    if(rescode==200):
        print (response.text)
    else:
        print("Error Code:" + rescode)
    return render(request, 'home/html/home.html', context={"response" : response.text})