def jwt_response_payload_handler(token, user=None, request=None):
    """
    自定义jwt认证成功返回数据
    :param token 在登陆信息通过以后，生成的jwt字符串
    :param user 在登陆信息通过验证以后，从数据库查询出来的登陆用户模型对象
    :param request 在本次客户端提交数据时，发送火来的请求
    
    """

    return {
        "token": token,
        "user_id":user.id,
        "user_name":user.username
    }