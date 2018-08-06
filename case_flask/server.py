# coding=utf-8

from flask import Flask, request

app = Flask(__name__)


# 将url和函数进行绑定
@app.route('/')
@app.route('/index', methods=['GET'])
def hello_world():
    """
        响应GET方式的请求
    """
    return 'hello world'


@app.route('/index2/<user>', methods=['GET'])
def hello_world2(user):
    """
        在url中添加变量
    """
    return 'hello %s' % user


@app.route('/index3', methods=['POST'])
def hello_world3():
    """
        响应POST方式的请求
    """
    username = request.form.get('username', default='xiaobei')
    return 'hello %s' % username


if __name__ == '__main__':
    # 配置host使公网用户或者局域网用户可以访问
    # 在局域网中需要关闭服务器的防火墙
    app.run(host='0.0.0.0', port=5000)