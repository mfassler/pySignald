#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import sys
import base64
import struct
import math
import time
import hmac
import hashlib
from Crypto.Cipher import AES

import pprint
pp = pprint.PrettyPrinter(indent=4)

import tornado.websocket

sys.path.append('protos_compiled/protos/')
import SubProtocol_pb2 as SubProtocol
import IncomingPushMessageSignal_pb2 as IncomingPushMessageSignal
import DeviceMessages_pb2 as DeviceMessages
import WhisperTextProtocol_pb2 as WhisperTextProtocol

import config


def pad(plaintext):
    '''
    For AES-128, CBC, the plaintext must always be padded to a
    multple of 16 chars (the 128 bit blocksize).  We will always
    have at least 1 pad char.  The pad char is the number of pad
    chars.  (This seems to be from crypto API in Chrome itself.)
    '''
    numBlocks = int(math.ceil((len(plaintext)+1) / 16.0))
    padLen = numBlocks * 16 - len(plaintext)
    paddedPlainText = plaintext + chr(padLen) * padLen
    return paddedPlainText


connFD = 0
clients = {}


class WebSocket(tornado.websocket.WebSocketHandler):
    def get_current_user(self):
        try:
            login = self.get_argument('login')
            username = login.split('.', 1)[0]
            password = self.get_argument('password')
            print 'login:', login
            print 'username:', username
            print 'password:', password
        except:
            return None
        else:
            chkPass = config.db.get(username, 'password')
            if chkPass == password:
                return username

    def check_origin(self, origin):
        print 'origin:', origin
        return True

    def open(self):
        global connFD
        global clients
        connFD += 1
        self.id = connFD
        print 'connected id:', self.id
        self.stream.set_nodelay(True)
        clients[self.id] = {"id": self.id, "object": self}
        # if self.current_user:
        if False:
            mbox = config.db.getJSON(self.current_user, 'messages.json')
            print 'mbox:', mbox
            if mbox:
                for msg in mbox:
                    print 'sending...'
                    self.write_message(base64.b64decode(msg['body']))
        print 'websocket open'
        print ' ************ Websocket user:', self.current_user

    def on_message(self, message):
        print "client: %s  -- rx: %s" % (self.id, message)
        msg = SubProtocol.WebSocketMessage.FromString(message)
        print 'decoded message:', msg
        if msg.request.path == '/v1/keepalive':
            print 'RX keepalive protobuf'
            resp_pb = SubProtocol.WebSocketResponseMessage(
                status=200, message='OK', id=msg.request.id)

            msg_pb = SubProtocol.WebSocketMessage(response=resp_pb)
            self.write_message(msg_pb.SerializeToString(), binary=True)

    def encrypt(self, plaintext):
        misc = config.db.getJSON(self.current_user, 'signalingKeyEtc.json')
        signalingKey = base64.b64decode(misc['signalingKey'])
        aes_key = signalingKey[:32]
        mac_key = signalingKey[32:]
        protoVersion = '\x01'
        iv = os.urandom(16)
        cipher = AES.new(aes_key, AES.MODE_CBC, iv)
        ciphertext = cipher.encrypt(pad(plaintext))
        ivAndCiphertext = protoVersion + iv + ciphertext
        signature = hmac.new(mac_key, ivAndCiphertext, hashlib.sha256).digest()
        # Returns an Encrypted PushMessageSignal
        return ivAndCiphertext + signature[:10]

    def sendCryptoMessage(self, plaintext):
        cryptoMessage = self.encrypt(plaintext)
        randId, = struct.unpack('I', os.urandom(4))

        request = SubProtocol.WebSocketRequestMessage(
            body=cryptoMessage, id=randId, verb='PUT', path='/v1/message')

        msg_pb = SubProtocol.WebSocketMessage(request=request, type=1)
        self.write_message(msg_pb.SerializeToString(), binary=True)
        # the client will return a {status=200, message='OK'} to us

    def on_close(self):
        print "client: %s  close" % (self.id)
        print 'code:', self.close_code
        print 'reason:', self.close_reason
        del clients[self.id]


def sendPush(clientId, mFrom, body, mType, ts):
    for connId in clients:
        client = clients[connId]
        print 'one client:', client['object'].current_user
    if clientId in clients:
        print '...sending...'

        pb_envelope = IncomingPushMessageSignal.Envelope(
            source=mFrom, sourceDevice=1, type=mType, content=body, timestamp=ts)

        clients[clientId]['object'].sendCryptoMessage(pb_envelope.SerializeToString())


def sendPushToUser(toUserName, msgObj):
    for connId in clients:
        client = clients[connId]['object']
        if client.current_user == toUserName:
            print 'Trying to send message:'
            pp.pprint(msgObj)
            print
            body = base64.b64decode(msgObj['body'])

            pb_envelope = IncomingPushMessageSignal.Envelope(source=msgObj['from'],
                                                             sourceDevice=1,
                                                             type=msgObj['type'],
                                                             legacyMessage=body,
                                                             timestamp=msgObj['ts'])

            client.sendCryptoMessage(pb_envelope.SerializeToString())
            return True
    return False
