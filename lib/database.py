#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import json


class Database():
    def set(self, user, keyname, value):
        f = open('db/' + user + ':' + keyname, 'wb')
        f.write(value)
        f.close()

    def setJSON(self, user, keyname, value):
        f = open('db/' + user + ':' + keyname, 'wb')
        json.dump(value, f)
        f.close()

    def get(self, user, keyname):
        try:
            with open('db/' + user + ':' + keyname, 'r') as f:
                return f.read()
        except:
            return None

    def getJSON(self, user, keyname):
        jStr = self.get(user, keyname)
        try:
            return json.loads(jStr)
        except:
            return None
