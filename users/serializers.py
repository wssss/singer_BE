from django.contrib.auth.models import User, Group
from django.contrib.auth.hashers import check_password
from rest_framework import serializers
from rest_framework.exceptions import ErrorDetail, ValidationError

#注册
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


#登录
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
    def vadildate(self, data):
        user_obj = User.objects.filter(username = data['username']).first()
        if not user_obj:
            raise serializers.ValidationError("用户名不存在")
        else:
            if user_obj.check_password(data['password']):
                return data
            else:
                raise serializers.ValidationError("用户名或密码错误")
