from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('voice_recognize', views.voice_recognize, name='voice_recognize'),
    path('face_recognize',views.face_recognize, name='face_Recognize'),
]