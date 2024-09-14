import tornado.ioloop
import tornado.web
from tornado.options import define, options, parse_command_line

# 定义默认的端口
define('port', default=8000, type=int)

class MainHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        # 获取请求URL中传递的name参数
        name = self.get_argument('name', '小明')
        self.write("Hello, %s" % name)

def make_app():
    return tornado.web.Application(handlers=[
        (r"/hello", MainHandler),
    ])

if __name__ == "__main__":
    parse_command_line()
    app = make_app()
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()