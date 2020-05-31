#!/usr/bin/python
# -*-encoding=utf8 -*-


class TestMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print('TestMiddleWare before request.')
        response = self.get_response(request)
        print('TestMiddleWare after request.')
        return response
