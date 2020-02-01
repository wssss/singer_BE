from django.urls import include, path,re_path
from rest_framework import routers, urls
from django.conf.urls import url
from .views import GroupAPIView,SongAPIView
from . import views

urlpatterns = [
    path("group/", GroupAPIView.as_view()),
    path("song/",SongAPIView.as_view())
]
