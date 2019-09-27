from django.contrib.auth.models  import User, Group
from rest_framework.views import APIView
from .serializers import UserSerializer, LoginSerializer
from rest_framework.generics import ListAPIView, ListCreateAPIView,CreateAPIView
from django.http import HttpResponse


# 注册
class Register(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    
# 登录
class Login(APIView):
    queryset = User.objects.all()
    serializer_class = LoginSerializer
    
    def post(self, request, *args, **kwargs):
        data = request.data
        res = LoginSerializer(data=data)
        if res.is_valid():
            return HttpResponse(res.validated_data)
        return HttpResponse(res.errors)
            