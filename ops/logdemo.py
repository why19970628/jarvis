#!/usr/bin/python
# -*-encoding=utf8 -*-


import os
import django
import logging

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()


def logger_demo():
    logger = logging.getLogger('django')
    logger.info('hello world')
    logger.info('hello world [FILTER FLAG]')

    logger.debug('debug message')

    logger.error('error message')


if __name__ == '__main__':
    logger_demo()
