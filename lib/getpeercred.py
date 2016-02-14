#!/usr/bin/env python
#
#    <one line to give the program's name and a brief idea of what it does.>
#    Copyright (C) 2002  Michael Urman
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program; if not, write to the Free Software
#    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#

import socket
import struct

try:
    SO_PEERCRED = socket.SO_PEERCRED
except:
    SO_PEERCRED = 17

sizeof_ucred = 12
format_ucred = 'III'  # pid_t, uid_t, gid_t


def getpeerid(sock):
    """getpeerid(sock) -> uid, gid

    Return the effective uid and gid of the remote connection.  Only works on
    UNIX sockets."""

    ucred = sock.getsockopt(socket.SOL_SOCKET, SO_PEERCRED, sizeof_ucred)
    pid, uid, gid = struct.unpack(format_ucred, ucred)

    return uid, gid
