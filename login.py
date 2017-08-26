#!/usr/bin/python
# -*- coding:utf-8 -*-

from tornado import web
from tornado import httpserver
from tornado import ioloop
import check_node
import io

# 逻辑模块
class IndexHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write('hello world!')

class LoginHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('login.html')

    def post(self, *args, **kwargs):
        username = self.get_argument('username')
        password = self.get_argument('password')
        code = self.get_argument('code')
        # print password, username
        # CheckCodeHandler = CheckCodeHandler.get()
        # print CheckCodeHandler
        if str(CODE).lower() == str(code).lower():
            if username == 'admin' and password == '111111':
                self.write('登陆成功')
            else:
                self.write('用户名或密码错误')
        else:
            self.write('验证码错误')

# class ImageHandler(web.RequestHandler):
#     def get(self, *args, **kwargs):
#         with open('111.jpg', 'rb') as f:
#             image_data = f.read()
#             self.write(image_data)
#             self.set_header("Content-Type", "image/jpeg")

class CheckCodeHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        global CODE
        image, CODE = check_node.create_validate_code()
        mstream = io.BytesIO()
        image.save(mstream, 'GIF')
        self.write(mstream.getvalue())

# url路由
application = web.Application([
        (r"/index", IndexHandler),
        (r"/login", LoginHandler),
        # (r"/image", ImageHandler),
        (r"/check_code.*", CheckCodeHandler),
    ])

if __name__ == '__main__':
    http_server = httpserver.HTTPServer(application)
    http_server.listen(8000)
    ioloop.IOLoop.current().start()
