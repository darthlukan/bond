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
        
