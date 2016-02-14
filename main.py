#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import tornado.ioloop
import tornado.web

import os

import handlers
import socket_handlers
import config

MY_PATH = os.path.dirname(os.path.realpath(__file__))

import lib.database
config.db = lib.database.Database()

app = tornado.web.Application([
    (r'/v1/websocket/', handlers.WebSocket),
    (r'/v1/websocket/provisioning/', handlers.WebSocket),
    (r'/v1/accounts/sms/code/(.*)', handlers.Sms),

    # The client will create it's own basic_auth here (along with signalingKey):
    (r'/v1/accounts/code/(.*)', handlers.Code),
    # basic_auth is:  toBase64(phone_number + ':' + password)

    (r'/v2/keys/(.*)/(.*)', handlers.Keys),
    (r'/v2/keys', handlers.Keys),

    (r'/v1/messages/(.*)', handlers.Messages)
])


print ' * HTTP+Websockets listening on port:', config.httpPort
app.listen(config.httpPort)

print ' * UDP listening on port:', config.udpListenPort
udp = socket_handlers.Udp(config.udpListenPort)

print ' * Unix Domain socket at:', config.domainSocketPath
domain = socket_handlers.Domain(config.domainSocketPath)

ioLoop = tornado.ioloop.IOLoop.instance()
ioLoop.add_handler(udp.s.fileno(), udp.callback, ioLoop.READ)
ioLoop.add_handler(domain.s.fileno(), domain.callback, ioLoop.READ)
ioLoop.start()
