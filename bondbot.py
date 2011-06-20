from twisted.words.protocols import irc
from twisted.internet import protocol, reactor
from twisted.python import log
from fnmatch import fnmatch
import sys
import time

class Logger:
    def __init__(self, log_file='log.txt'):
        self.file = open(log_file, 'a')

    def log(self, message):
        """Write a message to the file."""
        timestamp = time.strftime("[%H:%M:%S]", time.localtime(time.time()))
        self.file.write('%s %s\n' % (timestamp, message))
        self.file.flush()

    def close(self):
        self.file.close()


class BondBot(irc.IRCClient):
        
    @property
    def nickname(self):
        return self.factory.nickname

    @property
    def logger(self):
        return self.factory.logger

    def connectionMade(self):
        irc.IRCClient.connectionMade(self)
        self.logger.log("[connected at %s]" % time.asctime(time.localtime(time.time())))

    def connectionLost(self, reason):
        irc.IRCClient.connectionLost(self, reason)
        self.logger.log("[disconnected at %s]" % time.asctime(time.localtime(time.time())))
        self.logger.close()

    def signedOn(self):
        self.setNick(self.nickname)
        self.join(self.factory.channel)

    def joined(self, channel):
        self.logger.log("[I have joined %s]" % channel)

    # Security and commands down here    
    # Thanks to zeekay for this!
    owners = ['darthlukan', 'iAmerikan']

    def is_owner(self, channel, user):
        denied = [
            "I'm sorry there chap, I belong to Great Britain.",
            "I don't beleive we've met."
            "Some people never learn."
            "Come now darling, I have other things in mind for us."
            "You didn't think that was actually going to work, did you?"
            ]
        nick, host = user.split('!')
        for pattern in self.owners:
            if fnmatch(nick, pattern):
                return True
            elif fnmatch(host, pattern):
                return True
        return self.msg(channel, random.choice(denied))
         

    def privmsg(self, user, channel, msg):
        slappy = [
            'slaps %s with reckless abandon.',
            'slaps %s with a gold finger.',
            'slaps %s with an unequaled pimp hand.'
            ]
        huggy = [
            'hugs %s.'
            'cuddles %s.'
            'holds %s a little too long for comfort.'
            'Shows %s his pedobear.'
            ]
        killy = [
            'kills %s.'
            'makes a title song credit out of %s.'
            'busts out with the muy thai all up in %s\'s face.'
            'takes %s down faster than a nameless henchmen.'
            ]
        def repeat(*args):
            self.msg(channel, ' '.join(args))

        def hug(*args):
            self.me(channel, random.choice(huggy) % args[0])
            
        def slap(*args):
            self.me(channel, random.choice(slappy) % args[0])
        
        def kill(*args):
            self.me(channel, random.choice(killy) % args[0])

        def error(*args):
            self.msg(channel, 'Not a valid command')

        commands = {
            'kill': kill,
            'slap': slap,
            'hug': hug,
            'repeat': repeat
        }

        if msg.startswith('!'):
            if self.is_owner(channel, user):
                msg = msg.split()
                command, args = msg[0][1:], msg[1:]
                commands.get(command, error)(*args)

        
            
class BondBotFactory(protocol.ClientFactory):
    protocol = BondBot
    logger = Logger()

    def __init__(self, channel, nickname='BondBot'):
        self.channel = channel
        self.nickname = nickname

    def clientConnectionLost(self, connector, reason):
        self.logger.log("I've lost the connection to (%s), reconnecting." % reason)
        connector.connect()

    def clientConnectionFailed(self, connector, reason):
        self.logger.log("Unable to connect: %s" % reason)
        reactor.stop


def run_bot(network='irc.freenode.net', channel="##blackhats"):
    log.startLogging(sys.stdout)
    factory = BondBotFactory(channel)
    try:
        from twisted.internet import ssl
        context = ssl.ClientContextFactory()
        reactor.connectSSL(network, 6697, factory, context)
    except:
        reactor.connectTCP(network, 6667, factory)
    reactor.run()

if __name__ == '__main__':
    run_bot()