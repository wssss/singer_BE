from rest_framework import serializers
from .models import User
import re
from rest_framework_jwt.settings import api_settings

class UserModelSerializer(serializers.ModelSerializer):
    token = serializers.CharField(read_only=True,label="jwt的token字符串")
    class Meta:
        model = User
        fields = ["phone", "password", "token", "id", "username"]
        extra_kwargs = {
            "id":{
                "read_only":True
            },
            "username":{
                "read_only":True,
            },
            "password":{
                "write_only":True
            },
            "phone":{
                "write_only":True
            }
        }

    def validate(self, data):
        phone = data.get("phone")
        password = data.get("password")

        if not re.match("^1[3-7]\d{9}$", phone):
            raise serializers.ValidationError("手机格式不正确！")

        try:
            User.objects.get(phone=phone)
            raise serializers.ValidationError("手机号码已经被注册！")
        except:
            pass

        if len(password) < 6 or len(password) > 16:
            raise serializers.ValidationError("密码必须保持在6-16位字符长度之间！")

        return data

    def create(self, validate_data):
        phone = validate_data.get("phone")
        password = validate_data.get("password")

        user = User.objects.create_user(
            phone=phone,
            username=phone,
            password=password
        )
        payload = api_settings.JWT_PAYLOAD_HANDLER(user)
        user.token = api_settings.JWT_ENCODE_HANDLER(payload)
        return user