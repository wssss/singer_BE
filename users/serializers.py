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
