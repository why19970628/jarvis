#!/usr/bin/python                                                                  
# -*-encoding=utf8 -*-                                                             
# @Author         : imooc
# @Email          : imooc@foxmail.com
# @Created at     : 2018/12/4
# @Filename       : service.py
# @Desc           :


import os
import json
import random
import logging
from django.http import JsonResponse

from backend import settings
from utils.response import CommonResponseMixin, ReturnCode
from utils.auth import already_authorized, get_user
from utils import timeutil
from django.core.cache import cache

import thirdparty.juhe


logger = logging.getLogger('django')

all_constellations = ['白羊座', '金牛座', '双子座', '巨蟹座', '狮子座', '处女座', '天秤座', '天蝎座', '射手座', '摩羯座', '水瓶座', '双鱼座']
popular_stocks = [
    {
        'code': '000001',
        'name': '平安银行',
        'market': 'sz'
    },
    {
        'code': '000002',
        'name': '万科A',
        'market': 'sz'
    },
    {
        'code': '600036',
        'name': '招商银行',
        'market': 'sh'
    },
    {
        'code': '601398',
        'name': '工商银行',
        'market': 'sh'
    }
]
joke_cache = []


# 星座运势
def constellation(request):
    data = []
    if already_authorized(request):
        user = get_user(request)
        constellations = json.loads(user.focus_constellations)
    else:
        constellations = all_constellations
    for c in constellations:
        result = cache.get(c)
        if not result:
            result = thirdparty.juhe.constellation(c)
            timeout = timeutil.get_day_left_in_second()
            cache.set(c, result, timeout)
            logger.info('set cache. key=[%s], value=[%s], timeout=[%d]' % (c, result ,timeout))
        data.append(result)

    response = CommonResponseMixin.wrap_json_response(data=data, code=ReturnCode.SUCCESS)
    return JsonResponse(response, safe=False)


# 股票
def stock(request):
    data = []
    stocks = []
    if already_authorized(request):
        user = get_user(request)
        stocks = json.loads(user.focus_stocks)

    else:
        stocks = popular_stocks
    for stock in stocks:
        result = thirdparty.juhe.stock(stock['market'], stock['code'])
        data.append(result)
    response = CommonResponseMixin.wrap_json_response(data=data, code=ReturnCode.SUCCESS)
    return JsonResponse(response, safe=False)


# 笑话
def joke(request):
    global joke_cache
    if not joke_cache:
        joke_cache = json.load(open(os.path.join(settings.BASE_DIR, 'jokes.json'), 'r'))
    # 读缓存
    all_jokes = joke_cache
    limit = 10
    sample_jokes = random.sample(all_jokes, limit)
    response = CommonResponseMixin.wrap_json_response(data=sample_jokes, code=ReturnCode.SUCCESS)
    return JsonResponse(response, safe=False)


# 历史上的今天
def history_today(request):
    data = thirdparty.juhe.history_today()
    data.reverse()
    response = CommonResponseMixin.wrap_json_response(data=data, code=ReturnCode.SUCCESS)
    return JsonResponse(response, safe=False)


