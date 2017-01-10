import textwrap

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web


from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

class ErrorHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(u'you access home page.')

    def write_error(self, status_code, **kwargs):
        self.write(u'you caused a %s error.' % status_code)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[
            (r"/", ErrorHandler),
        ]
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()




