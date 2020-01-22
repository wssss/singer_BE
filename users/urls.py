from django.urls import include, path,re_path
from rest_framework import routers, urls
from django.conf.urls import url

from . import views

urlpatterns = [
    # re_path(r'^user/(?P<pk>\d+/profile/$)', views.account, name='profile'),
    # re_path(r'^user/(?P<pk>\d+/profile/update/$)', views.account_update, name='profile_update'),
    # re_path(r'^user/(?P<pk>\d+/pwdchange/$)', views.pwd_change, name='pwd_change'),
    # re_path(r'^logout/$', views.logout, name='logout')
]

app_name ='[users]' 