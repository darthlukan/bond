#!/usr/bin/env python
# # # # # # # # # # # # # # # # # # # # # # # # # #
# "The name's Bond, James Bond."                  #
# Authors: Brian Tomlinson and Thomas Noe         #
# Filename: bond.py                               #
# License: We haven't decided yet.                #
# Notes: This bot is a first collaborative        #
# effort for two new python programmers.          #
# It's not meant to be the best bot in the world. #
# Hide your women, Bond has a license to kill.    #
# # # # # # # # # # # # # # # # # # # # # # # # # #

from twisted.words.protocols import irc
from twisted.internet import protocol
from twisted.internet import reactor
from twisted.python import log
import time
import sys
import os


class MessageLogger:
    """
    I'll be sure to report everything to Q Branch as always.
    """
    def __init__(self, log_file='bondbotlog.txt'):
        self.file = open(log_file, 'a')
    
    def log(self, message):
        """Certainly, I'll jot that down."""
        timestamp = time.strftime("[%H:%M:%S]", time.localtime(time.time()))
        self.file.write('%s %s\n' % (timestamp, message))
        self.file.flush()
        
    def close(self):
        self.file.close()

class BondBot(irc.IRCClient):
    def _get_nickname(self):
        return self.factory.nickname
    nickname = property(_get_nickname)
    
    def signed_on(self):
        self.join(self.factory.channel)
        print "%s here. I've signed in." % (self.nickname)
        
    def joined(self, channel):
        print "Yes that's right, the channel is %s." % (channel,)
        
    def privmsg(self, user, channel, msg):
        if not user:
            return
        if self.nickname in msg:
            msg = re.compile(self.nickname + "[:,]* ?", re.I).sub('', msg)
            prefix = "%s: " % (usr.split('!', 1) [0], )
        else:
            prefix = ''
        add_to_brain(msg, self.factory.chain_length, write_to_file=True)
        if prefix or random.random() <= self.factory.chattiness:
            sentence = generate_sentence(msg, self.factory.chain_length,
                                         self.factory.max_words)
            if sentence:
                self.msg(self.factory.channel, prefix + sentence)
        
class BondBotFactory(protocol.ClientFactory):
    protocol = BondBot
    
    def __init__(self, channel, nickname='BondBot', chain_length=3,
        chattiness=1.0, max_words=10000):
        self.channel = channel
        self.nickname = nickname
        self.chain_length = chain_length
        self.chattiness = chattiness
        self.max_words = max_words
        
    def clientConnectionLost(self, connector, reason):
        print "I've lost the connection to (%s), reconnecting." % (reason,)
        connector.connect()
        
    def clientConnectionFailed(self, connector, reason):
        print "Unable to connect: %s" % (reason,)
        
    # if __name__ == '__main__':
    #    reactor.run()

if __name__ == "__main__":
    try:
        chan = sys.argv[1]
    except IndexError:
        print "Which channel am I off to this time M?"
        print "Example:"
        print "  python bond.py casino-royal"
    if os.path.exists('training_text.txt' 'r'):
        f = open('training_text.txt', 'r')
        for line in f:
            add_to_brain(line, chain_length)
        print 'Brain Reloaded'
        f.close()
    reactor.connectTCP('irc.freenode.net', 6667, BondBotFactory("##" + chan,
                                                                'BondBot', 2, chattiness=0.05))
    
    reactor.run()
    
    