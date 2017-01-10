# -*- coding: utf-8 -*-

from tornado import httpserver, ioloop, options, web
from tornado.options import define, options

define('port', default=8000, help='run on port', type=int)

class DbHandler(web.RequestHandler):
    def get(self):
        desc = self.get_argument('desc', 'nothing')
        print desc
        self.write(desc)


if __name__ == '__main__':
    options.parse_command_line()
    app = web.Application(handlers=[
        (r'db/', DbHandler)
    ])
    httpserver.HTTPServer(app).listen(options.port)
    ioloop.IOLoop.instance().start()
