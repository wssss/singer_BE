from django.urls import include, path,re_path
from rest_framework import routers, urls
from django.conf.urls import url
from .views import GroupAPIView,SongAPIView, SongDetailView,groupDeleteView,OrderListView,SongToSingCreateView
from . import views

urlpatterns = [
    path("group/", GroupAPIView.as_view()),
    path("song/",SongAPIView.as_view()),
    re_path("song/(?P<pk>\d+)/$", SongDetailView.as_view()),
    re_path("group/(?P<pk>\d+)/$", groupDeleteView.as_view()),
    re_path("order/(?P<pk>\d+)/$", OrderListView.as_view()),
    re_path("sing/(?P<pk>\d+)/$",SongToSingCreateView.as_view())
]
