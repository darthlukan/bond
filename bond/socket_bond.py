#!/usr/bin/env python
"""
Bond Bot, using sockets.

Now, should we make EVERYTHING irc related happen in here?
Then add functions and set up an if __name__ == "__main__"
with our initial setup? so many options here. can make
config based, etc.
This is all I'll write for tonight, because there's some braindstorming to 
be had tomorrow. -- Thomas
"""

__version__ == 0.1

import socket

class James(object):
    """ Bond, James Bond. """

    def __init__(self, nick):
        """ Set the bot's nick.
            && make a socket"""

        self.nick = nick
        self.socket = socket.socket()
    
    def connect(self, host, port=6667):
        """ Connect to server:
                socket.connect
                send nick
                send ident crap
                get ready to handle PINGs """
        self.socket.connect((host, port))
        
        """ I believe we should brainstorm on how to successfully time out
        when to send everything. Perhaps find out what to wait for before
        we send, set up an event handler, etcetc. """



