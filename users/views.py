from django.contrib.auth.models  import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer
from rest_framework.generics import ListAPIView, ListCreateAPIView,CreateAPIView


class Register(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    
    
