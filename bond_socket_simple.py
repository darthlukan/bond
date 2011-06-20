#!/usr/bin/env python

import sys
import socket
import string

HOST="irc.freenode.net"
PORT=6667
NICK="BondBot"
IDENT="BondBot"
REALNAME="James Bond 007"
OWNER="darthlukan"
CHAN="##blackhats"
CHANNELINIT="##blackhats"
readbuffer=""

s=socket.socket( )
s.connect((HOST, PORT))
s.send("NICK %s\r\n" % NICK)
s.send("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME))
s.send("JOIN :%s\r\n" % CHAN)
s.send("PRIVMSG %s :%s\r\n" % (CHAN, "The name's Bond, James Bond."))
s.send("PRIVMSG %s :%s\r\n" % (CHAN, "What do you say we discuss this in a more private environment?"))
s.send("PRIVMSG %s :%s\r\n" % (CHAN, "Why yes, that would be lovely."))
s.send("PRIVMSG %s :%s\r\n" % (CHAN, "Let's see what Tanaka is really up to."))
s.send("PRIVMSG %s :%s\r\n" % (CHAN, "Hello Money Penny, you're looking as lovely as ever."))

def parsemsg(msg): 
    complete=msg[1:].split(':',1) #Parse the message into useful data 
    info=complete[0].split(' ') 
    msgpart=complete[1] 
    sender=info[0].split('!') 
    if msgpart[0]=='`' and sender[0]==OWNER: #Treat all messages starting with '`' as command 
        cmd=msgpart[1:].split(' ') 
        if cmd[0]=='op': 
            s.send('MODE '+info[2]+' +o '+cmd[1]+'n') 
        if cmd[0]=='deop': 
            s.send('MODE '+info[2]+' -o '+cmd[1]+'n') 
        if cmd[0]=='voice': 
            s.send('MODE '+info[2]+' +v '+cmd[1]+'n') 
        if cmd[0]=='devoice': 
            s.send('MODE '+info[2]+' -v '+cmd[1]+'n') 
        if cmd[0]=='sys': 
            syscmd(msgpart[1:],info[2]) 
         
    if msgpart[0]=='-' and sender[0]==OWNER : #Treat msgs with - as explicit command to send to server 
        cmd=msgpart[1:] 
        s.send(cmd+'n') 
        print 'cmd='+cmd 
        
def syscmd(commandline,channel): 
    cmd=commandline.replace('sys ','') 
    cmd=cmd.rstrip() 
    os.system(cmd+' >temp.txt') 
    a=open('temp.txt') 
    ot=a.read() 
    ot.replace('n','|') 
    a.close() 
    s.send('PRIVMSG '+channel+' :'+ot+'n') 
    return 0 


while 1:
    readbuffer=readbuffer+s.recv(1024)
    temp=string.split(readbuffer, "\n")
    readbuffer=temp.pop( )

for line in temp:
    line=string.rstrip(line)
    line=string.split(line)

if(line[0]=="PING"):
    s.send("PONG %s\r\n" % line[1])