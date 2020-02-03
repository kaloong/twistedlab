from twisted.internet import protocol, reactor

class Echo(protocol.Protocol):
    def dataReceived(self, data):
        self.transport.write(data)
    def connectionLost(self, reason):
        self.transport.loseConnection()

class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Echo()
