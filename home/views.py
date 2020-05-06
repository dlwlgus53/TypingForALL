from django.shortcuts import render
import json
from django.http import JsonResponse
import urllib.request
from django.http import HttpResponseRedirect
import speech_recognition as sr
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import json



import os

import requests

#from collections import OrderedDict
#from pprint import pprint
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
def recognize(request):
    
    r = sr.Recognizer()
    speech = sr.Microphone()
    #authenticator -> apikey
    authenticator = IAMAuthenticator("RJwfHoc632pKWuv2uoMrNG0VXJoHWP2qxvlpvlFqJz8E")
    speechToText = SpeechToTextV1(
        authenticator=authenticator
        )
    #url link
    speechToText.set_service_url("https://api.kr-seo.speech-to-text.watson.cloud.ibm.com/instances/6414f5a4-9b16-4e26-a9fe-948c5bcac106")

    with speech as source:
        print("say something!!…")
        audio_file = r.adjust_for_ambient_noise(source)
        audio_file = r.listen(source)
    speech_recognition_results = speechToText.recognize(audio=audio_file.get_wav_data(), content_type='audio/wav').get_result()
    print(json.dumps(speech_recognition_results, indent=2))

    return render(request, 'home/html/voice.html', context={"response" : json.dumps(speech_recognition_results, indent=2)})

def voice(request):
    # TODO : Remove this part and make IBM version


    url = "https://api.kr-seo.speech-to-text.watson.cloud.ibm.com/instances/a70a5e4d-f62a-4030-93e8-02a88bf454b4/v1/recognize" # 鞚岇劚鞚胳嫕

    headers = {"Content-Type" : "audio/wav"}
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
    url = "https://openapi.naver.com/v1/vision/face" # ?柤甑挫澑?嫕
    # Imagepath= open(os.path.dirname(os.path.realpath(__file__)) + '../image/IU.png', "rb")
    # print(Imagepath)
    files = {'image':open(os.path.dirname(os.path.realpath(__file__)) + '\\image\\IU.png', "rb")}
    headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret }
    response = requests.post(url,  files=files, headers=headers)
    rescode = response.status_code

    age = 0# 20's 30's
    sex = 0
    emotion = 0



    if(rescode==200):
        print (response.text)
        print ("HEllo~")
    else:

        print("Error Code:" + str(rescode))

    age = 3
    return render(request, 'home/html/home.html', context={"age" : age, "imoji" : "🧑"})
