#!/usr/bin/python
# -*- encoding=utf-8 -*-


import os
import django
import time

from django.core.cache import cache

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()


def basic_use():
    cache.set('key', 'value', 5)
    print(cache.get('key'))
    time.sleep(5)
    print(cache.get('key'))


if __name__ == '__main__':
    basic_use()
