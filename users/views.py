from django.contrib.auth.models  import User, Group
from rest_framework.views import APIView
import json
from django.contrib.auth.hashers import check_password
from .serializers import UserSerializer, LoginSerializer
from rest_framework.generics import ListAPIView, ListCreateAPIView,CreateAPIView
from django.http import HttpResponse, JsonResponse


# 注册
class Register(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    
# 登录
class Login(APIView):
    authentication_classes = []
    queryset = User.objects.all()
    serializer_class = LoginSerializer
    
    def post(self, request, *args, **kwargs):
        data = request.data
        user = User.objects.filter(username= data['username']).first()
        res = {"success":False, "msg":""}
        if not user:
            res['msg']="用户名不存在"
        else:
            if check_password(data["password"], user.password):
                res['success'] = True
                res['msg']="登陆成功"
            else:
                res['msg']="密码错误"
        return HttpResponse(content=json.dumps(res))
            
            