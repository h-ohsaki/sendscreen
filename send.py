#!/usr/bin/env python3
#
#
# Copyright (c) 2019, Hiroyuki Ohsaki.
# All rights reserved.
#
# $Id: $
#

import socket
import time

sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addrport = (('127.0.0.1', 5000))
print(sk)

while True:
    sk.sendto(b'Hello\n'*1000, addrport)
    time.sleep(1)
