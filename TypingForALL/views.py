from django.shortcuts import render
import json
from django.http import JsonResponse
import urllib.request
from django.http import HttpResponseRedirect
import speech_recognition as sr
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import json

import urllib
import time

from django.shortcuts import redirect

import os

import requests
from django.http import HttpResponse
def home(request):



    return HttpResponse("<h1> This is 2020-1 HGU HCI coruse1 project. Attach the /home to see the page</h1>")
