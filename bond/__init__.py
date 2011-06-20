from twisted.internet import reactor
import bond

def run_bot(network='irc.freenode.net', port=6667, channel='##blackhats'):
    reactor.connectTCP(network, port, BondBotFactory, channel)
    reactor.run()
    
    