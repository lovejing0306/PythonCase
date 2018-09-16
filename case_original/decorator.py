# coding=utf-8

import functools

"""
    在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
    本质上，decorator就是一个返回函数的高阶函数
"""


def log(func):
    """
        wrapper 函数不需要接收参数的装饰器
    """
    @functools.wraps(func)  # 防止修改func函数的名字
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


def logger(text):
    """
        wrapper 函数需要接收参数的装饰器
    """
    def decorator(func):
        @functools.wraps(func)  # 防止修改func函数的名字
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log
def now():
    print('2015-3-25')


@logger('DEBUG')
def today():
    print('2015-3-25')
