from django.contrib.auth.models  import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer
from rest_framework.generics import ListAPIView, ListCreateAPIView,CreateAPIView


class Register(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    
    

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    
