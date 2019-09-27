from django.contrib.auth.models import User, Group
from django.contrib.auth.hashers import check_password
from rest_framework import serializers

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
    def validate(self, data):
        user_obj = User.objects.filter(username = data['username']).first()
        if user_obj:
            if check_password(data['password'], user_obj.password):
                return data
        return serializers.ValidationError("用户名或密码错误")
        