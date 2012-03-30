
from tornado.options import options, define, parse_command_line
import django.core.handlers.wsgi
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.wsgi
import os

os.environ['PYTHONPATH'] = "."
os.environ['DJANGO_SETTINGS_MODULE'] = "mcwebadmin.settings"

define ('port', type=int, default=8000)

class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Hello from tornado')

def main():
    static_path = os.path.join(os.path.dirname(__file__), "static")
    wsgi_app = tornado.wsgi.WSGIContainer(
        django.core.handlers.wsgi.WSGIHandler()
    )
    tornado_app = tornado.web.Application(
        [
            ('/static/(.*)', tornado.web.StaticFileHandler, dict(path=static_path)),
            ('.*', tornado.web.FallbackHandler, dict(fallback=wsgi_app)),
        ],
    )
    server = tornado.httpserver.HTTPServer(tornado_app)
    server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()