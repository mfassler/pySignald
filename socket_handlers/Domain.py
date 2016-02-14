#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
This unix-domain socket handler is how users request verification codes.
'''

import os
import pwd
import time
import random
import socket

from lib.getpeercred import getpeerid  # TODO: inconsistent naming

import config


class Domain():
    def __init__(self, path):
        try:
            os.unlink(path)
        except:
            pass
        self.path = path
        self.s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.s.setblocking(1)
        self.s.bind(self.path)
        os.chmod(self.path, 0777)
        self.s.listen(128)

    def callback(self, fd, events):

        conn, addr = self.s.accept()
        uid, gid = getpeerid(conn)
        userinfo = pwd.getpwuid(uid)

        conn.send('Hello, %s\n' % (userinfo.pw_name))

        phoneNumber = config.basePhoneNumber + uid
        username = '+1' + str(phoneNumber)
        register = {
            'code': random.randrange(100000, 999999),
            'expire': time.time() + 300
        }
        config.db.setJSON(username, 'register.json', register)
        conn.send('Your phone number is: %s\n' % phoneNumber)
        conn.send('Your verification code is: %s' % register['code'])
        conn.send('  (expires in 5 minutes)\n')
        conn.close()
