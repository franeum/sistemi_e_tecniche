#!/usr/bin/env python3

import time 
from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

host = "127.0.0.1"
port = 8000

class Echo(DatagramProtocol):
    def datagramReceived(self, data, addr):
        print("received", data)
        #self.transport.write(data, (host, port))

reactor.listenUDP(8000, Echo())
reactor.listenUDP(9000, Echo())
reactor.run()
