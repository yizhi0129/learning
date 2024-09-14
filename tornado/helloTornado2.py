import tornado.ioloop
import tornado.web
from tornado.options import define, options, parse_command_line
	
# 定义默认的端口
define('port', default=8000, type=int)

	
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


def make_app():
    return tornado.web.Application(handlers=[
        (r"/hello", MainHandler),
    ])

	
if __name__ == "__main__":
    # 解析命令行
    parse_command_line()
    # 获取Application对象
    app = make_app()
    # 监听端口
    app.listen(options.port)
    # 启动IOLoop实例
    tornado.ioloop.IOLoop.current().start()