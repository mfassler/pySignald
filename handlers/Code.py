#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import time
import base64
import json
import tornado.web
import config


class Code(tornado.web.RequestHandler):

    def _setOrigin(self):
        origin = self.request.headers.get('Origin')
        self.add_header('Access-Control-Allow-Origin', origin)

    def options(self, *params):
        print 'options CodeHandler:', params
        self._setOrigin()
        self.add_header('Access-Control-Allow-Credentials', True)
        self.add_header('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        self.add_header('Access-Control-Allow-Headers',
                        'Content-Type,Authorization,X-Requested-With,'
                        'Content-Length,Accept,Origin,X-Signal-Agent')
        self.add_header('Allow', 'OPTIONS,PUT')
        self.write('OPTIONS, PUT')

    def put(self, code):
        print 'PUT codeHandler, code:', code
        auth = self.request.headers.get('Authorization')
        pieces = base64.b64decode(auth.split()[1]).split(':', 1)
        username = pieces[0]
        print 'username:', username
        password = pieces[1]
        print 'password:', password
        register = config.db.getJSON(username, 'register.json')
        print 'register:', register
        if 'code' in register and 'expire' in register:
            # request.body will include a 'signalingKey'
            if int(code) == register['code'] and register['expire'] > time.time():
                print 'code is good'
                config.db.set(username, 'password', password)
                # body is already json
                config.db.set(username, 'signalingKeyEtc.json', self.request.body)
                print '\n ** auth:', auth, '\n\n'
                self._setOrigin()
                self.set_status(204)
                self.finish()
            else:
                print 'a'
                self.send_error(403)
        else:
            print 'b'
            self.send_error(403)
