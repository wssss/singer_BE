from django.urls import include, path,re_path
from rest_framework import routers, urls
from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token

from . import views

urlpatterns = [
    url(r'^register', views.Register.as_view(), name='register'),
        
    path("login/", obtain_jwt_token)
]

app_name ='[users]' 