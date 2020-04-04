from django.shortcuts import render
import json
from django.http import JsonResponse
import urllib.request
import os

import requests
# Create your views here.

# def home(request):
#     if request.method == 'GET':

#         config_secret_debug = json.loads(open(CONFIG_SECRET_DEBUG_FILE).read())
#         client_id = config_secret_debug['NAVER']['CLIENT_ID']
#         client_secret = config_secret_debug['NAVER']['CLIENT_SECRET']

#         q = request.GET.get('q')
#         encText = urllib.parse.quote("{}".format(q))
#         url = "https://openapi.naver.com/v1/search/movie?query=" + encText  # json 결과
#         movie_api_request = urllib.request.Request(url)
#         movie_api_request.add_header("Content-type", “multipart/form-data”)
#         movie_api_request.add_header("X-Naver-Client-Id", client_id)
#         movie_api_request.add_header("X-Naver-Client-Secret", client_secret)
#         response = urllib.request.urlopen(movie_api_request)
#         rescode = response.getcode()
#         if (rescode == 200):
#             response_body = response.read()
#             result = json.loads(response_body.decode('utf-8'))
#             items = result.get('items')
#             pprint(result)  # request를 예쁘게 출력해볼 수 있다.

#             context = {
#                 'items': items
#             }
#             return render(request, 'search/search.html', context=context)

# def home(request):
#     print(request)
#     print("hello")
#     return  render(request, 'home/html/home.html', {'hello' : 'why'})

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