from django.urls import include, path,re_path
from rest_framework import routers, urls
from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from .views import RegisterView

from . import views

urlpatterns = [
    path("login/", obtain_jwt_token),
    path("register/", RegisterView.as_view())
]
