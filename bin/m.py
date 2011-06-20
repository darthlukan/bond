from twisted.internet import reactor
import sys

if __name__ == "__main__":
    try:
        chan = sys.argv[1]
    except IndexError:
        print "Which channel am I off to this time M?"
        print "Example:"
        print "  python bond.py casino-royal"
    if os.path.exists('training_text.txt', 'r')
        f = open('training_text.txt', 'r')
        for line in f:
            add_to_brain(line, chain_length)
        print 'Brain Reloaded'
        f.close()
    reactor.connectTCP('irc.freenode.net', 6667, BondBotFactory('#' + chan,
                                                                'BondBot', 2, chattiness=0.05))
    reactor.run()
    
    