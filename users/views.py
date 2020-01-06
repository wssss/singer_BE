from django.contrib.auth.models  import User, Group
from rest_framework.views import APIView
import json
from django.contrib.auth.hashers import check_password
from .serializers import UserSerializer, LoginSerializer
from rest_framework.generics import ListAPIView, ListCreateAPIView,CreateAPIView
from django.http import HttpResponse, JsonResponse

from django.contrib.auth import authenticate, login


# 注册
class Register(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
