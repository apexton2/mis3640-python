import random
import string


def process_file(filename, skip_header):
    """Makes a histogram that contains the words from a file.
    filename: string
    skip_header: boolean, whether to skip the Gutenberg header
    returns: map from each word to the number of times it appears.
    """
    hist = {}
    fp = open(filename, encoding='UTF8')

    if skip_header:
         skip_gutenberg_header(fp)

    for line in fp:
        if line.startswith('*** END OF THIS PROJECT'):
            break
        for word in line.split(): #converts into list of words
            word = word.lower()

            #update the histogram
            hist[word] = hist.get(word, 0) + 1

        # INSERT CODE BELOW
        

    return hist

print(process_file('session13/test_file.txt', skip_header=False))

def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.
    fp: open file object
    """
    for line in fp:
        if line.startswith('*** START OF THIS PROJECT'):
            break

def total_words(hist):
    """Returns the total of the frequencies in a histogram."""
    return sum(hist.values())

hist = process_file('session13/test_file.txt', skip_header=False)
print(total_words(hist))

def different_words(hist):
    """Returns the number of different words in a histogram."""
    return len(hist)
print(different_words(hist))

def most_common(hist):
    """Makes a list of word-freq pairs in descending order of frequency.
    hist: map from word to frequency
    returns: list of (frequency, word) pairs
    """
    temp = []
    for word, frequency in hist.items():
        temp.append((frequency, word))

    temp.sort()
    temp.reverse()
    return temp

common_wordlist= most_common(hist)
print(common_wordlist[:10])

def print_most_common(hist, num=0):
    """Prints the most commons words in a histgram and their frequencies.
    hist: histogram (map from word to frequency)
    num: number of words to print
    """
    t =most_common(hist)
    for frequency, word in t[:num]:
        print(word,'\t', freq)

def subtract(d1, d2):
    """Returns a dictionary with all keys that appear in d1 but not d2.
    d1, d2: dictionaries
    """
    res = {}
    for key in d1:
        if key not in d2:
            res[key] = None
    return res

def random_word(hist):
    """Chooses a random word from a histogram.
    The probability of each word is proportional to its frequency.
    """
    t= []
    for word, frequency in hist.items():
    
    return random.choice(t)


def main():
    hist = process_file('session13/test_file.txt', skip_header=True)
    print('Total number of words:', total_words(hist))
    print('Number of different words:', different_words(hist))

    t = most_common(hist)
    print('The most common words are:')
    for freq, word in t[0:20]:
        print(word, '\t', freq)

    words = process_file('session13/words.txt', skip_header=False)

    diff = subtract(hist, words)
    print("The words in the book that aren't in the word list are:")
    for word in diff.keys():
        print(word, end=' ')

    print("\n\nHere are some random words from the book")
    for i in range(100):
        print(random_word(hist), end=' ')


if __name__ == '__main__':
    main()
    pass