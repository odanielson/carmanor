from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

from handler import Handler

class UDPReader(DatagramProtocol, Handler):

    def __init__(self, source_name, port, dest=[]):
        Handler.__init__(self, dest=dest)
        reactor.listenUDP(port, self)
        self.name = source_name

    def datagramReceived(self, data, (host, port)):
        self.debug("received %r from %s:%d" % (data, host, port))
        Handler.push(self, {'raw': data,
                            'source': self.name })

