#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
This UDP handler is only for development / troubleshooting.
(I can use socat->udp to inject push messages)
'''
import socket
import json
import base64
import handlers


class Udp():
    def __init__(self, port):
        self.port = port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.bind(('localhost', self.port))

    def callback(self, fd, events):
        rxUdpMsg = self.s.recv(5000)
        pieces = rxUdpMsg.split(':', 1)
        print 'pieces:', pieces

        '''
        if len(pieces) == 2:
            clientId = int(pieces[0])
            jsonMsg = pieces[1]
            msg = json.loads(jsonMsg)
            body = base64.b64decode(msg['body'])
            handlers.sendPush(clientId, msg['from'], body, msg['type'], msg['ts'])
        '''
