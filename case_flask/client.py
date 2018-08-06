# coding=utf-8

import requests


if __name__ == '__main__':
    user_info = {'username':'moxiaobei'}
    response = requests.post('http://127.0.0.1:5000/index3', data=user_info)
    print(response.text)
