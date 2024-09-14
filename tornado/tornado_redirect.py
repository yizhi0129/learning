import tornado.ioloop
import tornado.web
from tornado.options import define, options, parse_command_line

# 定义默认的端口
define('port', default=8000, type=int)

class HelloHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("hello tornado")
        self.write('<br/>')
        self.write("实现从路由'/redirect/'跳转到本方法中")

class RedirectHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        # 使用redirect方法，跳转到根路径"/"地址
        self.redirect('/')

def make_app():
    return tornado.web.Application(handlers=[
        (r"/redirect/", RedirectHandler),
        (r"/", HelloHandler),
    ])

if __name__ == "__main__":
    parse_command_line()
    app = make_app()
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()