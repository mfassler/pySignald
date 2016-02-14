#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import base64
import json
import time
import tornado.web

import handlers
import config
from lib.basicAuth import basicAuth


class Messages(tornado.web.RequestHandler):
    def get_current_user(self):
        return basicAuth(self.request.headers.get('Authorization'))

    def _setOrigin(self):
        origin = self.request.headers.get('Origin')
        self.add_header('Access-Control-Allow-Origin', origin)

    def options(self, *params):
        print 'options messages:', params
        self.add_header('Access-Control-Allow-Headers',
                        'Content-Type,Authorization,X-Requested-With,'
                        'Content-Length,Accept,Origin,X-Signal-Agent')
        self.add_header('Access-Control-Allow-Credentials', True)
        self._setOrigin()
        self.add_header('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        self.add_header('allow', 'OPTIONS,PUT')
        self.write('OPTIONS, PUT')

    def put(self, dest_number):
        print 'put messages to:', dest_number
        print 'request:', self.request.body
        body = json.loads(self.request.body)
        mbox = config.db.getJSON(dest_number, 'messages.json')
        if not mbox:
            mbox = []
        for msg in body['messages']:
            msg['from'] = self.current_user
            msg['ts'] = int(time.time() * 1000)
            if not handlers.sendPushToUser(dest_number, msg):
                print 'user not online, storing to mailbox'
                mbox.append(msg)
        config.db.setJSON(dest_number, 'messages.json', mbox)
        self._setOrigin()
        self.set_status(200)
        self.finish()
