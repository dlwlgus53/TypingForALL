from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('voice', views.voice, name='voice'),
    path('voice/voice_recognize', views.voice_recognize, name='voice_recognize'),


]