from django.shortcuts import render
import json
from django.http import JsonResponse
import urllib.request
from django.http import HttpResponseRedirect
import speech_recognition as sr
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import json
import cv2 
import urllib
from django.shortcuts import redirect

import os

import requests

voice =""
emoji_list=[]
from_voice = False
from_face = False

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


def voice_recognize(request):
    global voice
    global from_voice
    from_voice = True
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
    voice = speech_recognition_results["results"][0]["alternatives"][0]["transcript"]



    return redirect('http://127.0.0.1:8000/home')


def home(request):
    global emoji_list
    global voice
    global from_voice
    global from_face

    if(not from_voice and not from_face):
        voice = ""
        emoji_list = []
    from_voice =False
    from_face =False


    return render(request, 'home/html/home.html', context={"voice" : voice, "emoji_list" : emoji_list})



def face_recognize(request):
    global emoji_list
    global from_face

    from_face = True
    client_id = "salwDsOe8RoUMKEKAKMh"
    client_secret = "A8_2T9SxK_"
    url = "https://openapi.naver.com/v1/vision/face" 

    
    cap = cv2.VideoCapture(0)   # 0: default camera
    while cap.isOpened():
        success, frame = cap.read()
        if success:
            cv2.imshow('Camera Window', frame)
            cv2.imwrite('home/image/user.png', frame)
            key = cv2.waitKey(1) & 0xFF
            
            if (key == 27): 
                break
    cap.release()
    cv2.destroyAllWindows()

    files = {'image':open(os.path.dirname(os.path.realpath(__file__)) + '\\image\\user.png', "rb")}
    headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret }
    response = requests.post(url,  files=files, headers=headers)
    rescode = response.status_code

    if(rescode==200):
        print (response.text)


    else:
        print("Error Code:" + str(rescode))

    json_data = json.loads(response.text)
    gender = json_data['faces'][0]['gender']["value"]# 성별 

    emotion = json_data['faces'][0]['emotion']["value"] # 감정 


    emoji_list = emotionToEmoji(emotion, gender)

    print(emoji_list)
    return redirect('http://127.0.0.1:8000/home')


def emotionToEmoji(emotion, gender):
    if(emotion == "angry"  ): emoji_list = ["😠","😡","👿","😤","😾","😕","💢"]
    if(emotion == "disgust"): emoji_list = ["😩","😒","😫","😣"]
    if(emotion == "fear" ): emoji_list = ["😱","😨","😰","😖","🙀","😬"]
    if(emotion == "laugh"): emoji_list = ["😆","😁","😄","😂","😹"]
    if(emotion == "neutral" ): emoji_list = ["😐","😶","😌","😑"]
    if(emotion == "sad" ): emoji_list = [ "😭","😥","😢","😿","😟","😔","😞","💧"]
    if(emotion == "suprise" ): emoji_list = ["😳","😲","😮","😦","😵"]
    if(emotion == "smile" and gender =="female"): emoji_list = ["😊","😀","😉","😎","😸","😺","😇","😙","👩","👧","👵"]
    if(emotion == "smile" and gender =="male"): emoji_list = ["😊","😀","😉","😎","😸","😺","😇","😙","👦","👱","👴","👨"]
    if(emotion == "talking" ): emoji_list = ["😀","😄","😮"]

    return emoji_list