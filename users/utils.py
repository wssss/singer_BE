# 设置多个返回值

def jwt_response_payload_handler(token, user=None, request=None):
    '''
    param token 在登录信息通过验证以后，生成都jwt字符串
    param user 在登陆信息通关验证后用户的登陆信息
    request 请求信息
    
    '''
    return {
        'token':token,
        'user_id':user.id,
        'user_name':user.username
    }


from django.contrib.auth.backends import ModelBackend
import re
from .models import User

#多条件登陆
def get_account_by_username(account):
    try:
        if re.match('^1[3-9]\d{9}$', account):
            user = User.objects.get(phone=account)
        else:
            user = User.objects.get(username=account)
    except User.DoesNotExist:
        return None
    else:
        return user

#自定义用户认证
class UsernameMobileAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user = get_account_by_username(username)
        
        if user is None:
            return None
        
        if user.check_password(password) and self.user_can_authenticate(user):
            return user