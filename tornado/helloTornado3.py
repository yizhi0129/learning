import tornado.ioloop
import tornado.web
import tornado.httpserver
from tornado.options import define, options, parse_command_line

define('port', default=8000, type=int)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

def make_app():
    return tornado.web.Application(handlers=[
        (r"/hello", MainHandler),
    ])

if __name__ == "__main__":
	# 取消日志打印
    # options.logging=None
    # 解析命令行
    parse_command_line()
	# 获取Application对象
    app = make_app()
	# 获取httpserver对象
    server = tornado.httpserver.HTTPServer(app)
	# 监听端口
    server.bind(options.port)
    # 启动进程数n<=0自动根据cpu核数创建子进程, n>0创建n个子进程
    server.start(0)
	# 启动IOLoop实例
    tornado.ioloop.IOLoop.current().start()