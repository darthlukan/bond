from collections import defaultdict

markov = defaultdict(list)
STOP_WORD = "\n"

def add_to_brain(msg, chain_length, write_to_file=False):
    if write_to_file:
        f = open('training_text.text', 'a')
        f.write(msg + '\n')
        f.close()
    buf = [STOP_WORD] * chain_length
    for word in msg.split():
        markov[tuple(buf)].append(word)
        del buf[0]
        buf.append(word)
    markov[tuple(buf)].append(STOP_WORD)
    
def generate_sentence(msg, chain_length, max_words=10000):
    buf = msg.split()[:chain_length]
    if len(msg.split()) > chain_length:
        message = buf[:]
    else:
        message = []
        for i in xrange(chain_length):
            message.append(random.choice(markov[random.choice(markov.keys())]))
        for i in xrange(max_words):
            try:
                next_word = random.choice(markov[tuple(buf)])
            except IndexError:
                continue
            if next_word == STOP_WORD:
                break
            message.append(next_word)
            del buf[0]
            buf.append(next_word)
        return ' '.join(message)
    
                