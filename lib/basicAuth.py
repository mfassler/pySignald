#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import base64

import config


def basicAuth(auth_header):
    if auth_header.startswith('Basic '):
        pieces = base64.b64decode(auth_header.split('asic ')[1]).split(':', 1)
        username = pieces[0].split('.', 1)[0]
        password = pieces[1]
        chkPass = config.db.get(username, 'password')
        if chkPass == password:
            print ' ** current_user:', username
            return username

    print ' ** No current user'
    return None
