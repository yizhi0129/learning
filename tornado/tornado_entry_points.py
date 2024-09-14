import tornado.ioloop
import tornado.web
import tornado.httpserver
from tornado.options import define, options, parse_command_line

# 定义默认的端口
define('port', default=8000, type=int)


class MainHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.name = 'Python'
        print('实例对象的初始化并给name参数赋值')

    def prepare(self):
        print('在执行HTTP行为方法之前被调用')

    def get(self):
        print('执行GET方法')
        self.write("name: %s" % self.name)

    def on_finish(self):
        print('响应后调用此方法，用于清理内存或日志记录等功能')


def make_app():
    return tornado.web.Application(handlers=[
        (r"/", MainHandler),
    ])


if __name__ == "__main__":
    parse_command_line()
    app = make_app()
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()