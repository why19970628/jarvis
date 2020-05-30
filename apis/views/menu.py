#!/usr/bin/python                                                                  
# -*-encoding=utf8 -*-                                                             
# @Author         : imooc
# @Email          : imooc@foxmail.com
# @Created at     : 2018/11/29
# @Filename       : menu.py
# @Desc           :

import os
import yaml

from django.http import JsonResponse

from backend import settings

import utils.response


def init_app_data():
    data_file = os.path.join(settings.BASE_DIR, 'app.yaml')
    with open(data_file, 'r', encoding='utf-8') as f:
        apps = yaml.load(f)
        return apps

def get_menu(request):
    global_app_data = init_app_data()
    published_apps = global_app_data['published']
    # return JsonResponse(data=published_apps, safe=False, status=200)
    response = utils.response.wrap_json_response(data=published_apps)
    return JsonResponse(data=response, safe=False)

