from django.shortcuts import render
import json
from django.http import JsonResponse
import urllib.request
import os

import requests
# Create your views here.
'''
{
  "apikey": "a4FjtzoPaIYwxg-fQ5JQ1jtCZ1b12kYM9zrTR6yO7lbG",
  "iam_apikey_description": "Auto-generated for key c2660c9a-b5f6-40a3-a8e0-83c6687ee43c",
  "iam_apikey_name": "Auto-generated service credentials",
  "iam_role_crn": "crn:v1:bluemix:public:iam::::serviceRole:Manager",
  "iam_serviceid_crn": "crn:v1:bluemix:public:iam-identity::a/c937be21f49740639ae1e579e6ca95b8::serviceid:ServiceId-f8d1840f-0540-48d1-a9b2-1749ad214a0c",
  "url": "https://api.kr-seo.speech-to-text.watson.cloud.ibm.com/instances/a70a5e4d-f62a-4030-93e8-02a88bf454b4"
}
'''


def voice(request):
    # TODO : Remove this part and make IBM version

    url = "https://api.kr-seo.speech-to-text.watson.cloud.ibm.com/instances/a70a5e4d-f62a-4030-93e8-02a88bf454b4/v1/recognize" # 음성인식

    headers = {"Content-Type" : "audio/flac"}
    auth = ( "apikey", "a4FjtzoPaIYwxg-fQ5JQ1jtCZ1b12kYM9zrTR6yO7lbG")
    path  = os.path.dirname(os.path.realpath(__file__)) + '\\voice\\audio.flac'
    data = {"audio" : open(path, "rb")}

    
    response = requests.post(url, data = open(path, "rb"), auth = auth)
    rescode = response.status_code
    if(rescode==200):
        print (response.text)
    else:
        print("Error Code:" + str(rescode))
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
        print("Error Code:" + str(rescode))
    return render(request, 'home/html/home.html', context={"age" : age, "imoji" : "🧑"})