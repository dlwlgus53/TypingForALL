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
    #voice_result = json.loads(speech_recognition_results)
    voice = speech_recognition_results["results"][0]["alternatives"][0]["transcript"]
    args = {'voice': voice}
    url = build_url('http://127.0.0.1:8000/home?', args)


    return redirect(url)


def home(request):
    row_url = ('http://127.0.0.1:8000'+request.get_full_path())
    url = urllib.parse.urlparse(row_url) 
    args = urllib.parse.parse_qs(url.query)
    print(args)
    voice = " "
    emoji_list = []
    try:
        voice = args['voice'][0]
        print(voice)
    except:
        pass
    try:
        gender = args['gender'][0]
        emotion = args['emotion'][0]
        print(gender)
        print(emotion)
        emoji_list = emotionToEmoji(emotion, gender)
    except:
        pass

        


 

    return render(request, 'home/html/home.html', context={"voice" : voice, "emoji_list" : emoji_list})



def face_recognize(request):

    client_id = "salwDsOe8RoUMKEKAKMh"
    client_secret = "A8_2T9SxK_"
    url = "https://openapi.naver.com/v1/vision/face" # ?柤甑挫澑?嫕
    # Imagepath= open(os.path.dirname(os.path.realpath(__file__)) + '../image/IU.png', "rb")
    # print(Imagepath)
    
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
    #age = json_data['faces'][0]['age']["value"] # 나이 
    emotion = json_data['faces'][0]['emotion']["value"] # 감정 

    args = {'emotion': emotion, 'gender':gender}
    url = build_url('http://127.0.0.1:8000/home?', args)

    return redirect(url)


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


def build_url(baseurl, args_dict):
    # Returns a list in the structure of urlparse.ParseResult
    url = baseurl + urllib.parse.urlencode(args_dict)
    print("url" + baseurl)
    return url
