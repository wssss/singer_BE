from rest_framework.views import APIView
from .serializers import UserModelSerializer
import json
from .models import User

from django.contrib.auth import authenticate, login


from rest_framework import generics
class RegisterView(generics.CreateAPIView):
    serializer_class = UserModelSerializer
    queryset = User.objects.all()
    #接收注册信息


            
