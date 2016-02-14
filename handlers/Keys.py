#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import base64
import json
import tornado.web

import config
from lib.basicAuth import basicAuth


class Keys(tornado.web.RequestHandler):
    def get_current_user(self):
        return basicAuth(self.request.headers.get('Authorization'))

    def _setOrigin(self):
        origin = self.request.headers.get('Origin')
        self.add_header('Access-Control-Allow-Origin', origin)

    def options(self, *params):
        print 'options keys:', params
        print 'request:', self.request
        self.add_header('Access-Control-Allow-Headers',
                        'Content-Type,Authorization,X-Requested-With,'
                        'Content-Length,Accept,Origin,X-Signal-Agent')
        self.add_header('Access-Control-Allow-Credentials', True)
        self._setOrigin()
        self.add_header('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        self.add_header('allow', 'GET,OPTIONS,HEAD,PUT')
        self.write('GET, OPTIONS, HEAD, PUT')

    def get(self, *params):
        print 'get keys:', params
        print 'request:', self.request
        if self.current_user is None:
            self.send_error(401)
            return
        if len(params) == 2:
            mySelf = False
            number = params[0]
            device_id = params[1]
        elif len(params) == 0:
            mySelf = True
            number = self.current_user
            device_id = '0'
        else:
            self.send_error(404)
            return
        relay = self.get_argument('relay', default=None)
        print 'get keys:', number, device_id, relay

        keys = config.db.getJSON(number, 'keys.json')
        misc = config.db.getJSON(number, 'signalingKeyEtc.json')
        if keys:
            resp = {'identityKey': keys['identityKey'], 'devices': []}
            count = 0
            for oneKey in keys['preKeys']:
                count += 1
                resp['devices'].append({
                    'deviceId': 1,
                    'registrationId': misc['registrationId'],
                    'signedPreKey': keys['signedPreKey'],
                    'preKey': oneKey})
                if not mySelf:
                    break  # only grab the first key, I guess
            resp['count'] = count
            self._setOrigin()
            self.write(json.dumps(resp))
        else:
            self.send_error(404)

    def put(self):
        print 'PUT keys'
        if self.current_user is None:
            self.send_error(401)
            return

        config.db.set(self.current_user, 'keys.json', self.request.body)
        self._setOrigin()
        self.set_status(204)
        self.finish()
