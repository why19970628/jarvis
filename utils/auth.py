#!/usr/bin/python                                                                  
# -*-encoding=utf8 -*-                                                             
# @Author         :
# @Email          : imooc@foxmail.com
# @Created at     : 2018/11/2
# @Filename       : auth.py
# @Desc           :


from authorization.models import User

from utils.wx.crypt import WXBizDataCrypt
from utils.wx.code2session import code2session


# 判断是否已经授权
def already_authorized(request):
    is_authorized = False
    print(request.session.items())
    if request.session.get('is_authorized'):
        is_authorized = True
    print('authorized status:', is_authorized)
    return is_authorized


def get_user(request):
    if not already_authorized(request):
        raise Exception('not authorized request')
    open_id = request.session.get('open_id')
    user = User.objects.get(open_id=open_id)
    return user


def c2s(appid, code):
    return code2session(appid, code)
