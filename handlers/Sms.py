#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import tornado.web


class Sms(tornado.web.RequestHandler):

    def _setOrigin(self):
        origin = self.request.headers.get('Origin')
        self.add_header('Access-Control-Allow-Origin', origin)

    def options(self, *params):
        print 'options SmsHandler:', params
        print 'request:', self.request
        self.add_header('Access-Control-Allow-Headers',
                        'Content-Type,Authorization,X-Requested-With,'
                        'Content-Length,Accept,Origin,X-Signal-Agent')
        self.add_header('Access-Control-Allow-Credentials', True)
        self._setOrigin()
        self.add_header('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        self.add_header('allow', 'GET,OPTIONS,HEAD,PUT')
        self.write('GET, OPTIONS, HEAD, PUT')

    def get(self, number):
        pass
