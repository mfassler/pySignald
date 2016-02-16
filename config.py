#!/usr/bin/env python
# -*- coding: UTF-8 -*-

httpPort = 8123
udpListenPort = 31337
domainSocketPath = '/tmp/pySignald.sock'

# User's phone number will be base + uid
# (Comment this out to use actual usernames.  Requires a special Signal-Desktop that
#  doesn't validate phone numbers (coming soon))
basePhoneNumber = 2122000000
