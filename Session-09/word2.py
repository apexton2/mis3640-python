def uses_only(word, available):
    """
    takes a word and a string of letters, and that returns True if the word
    contains only letters in the list.
    """
    # for letter in word:
    #     if letter not in available:
    #         return False
    # return True

def uses_all(word, required):
    """
    takes a word and a string of required letters, and that returns True if
    the word uses all the required letters at least once.
    """
    for letter in required:
        if letter not in word:
            return False
    return True
  


# print(uses_all('Babson', 'abs'))
# print(uses_all('college', 'abs'))

def find_word_using_all_vowels():
    fin = open("Session-09/words.txt")
    counter = 0
    for line in fin:
        word = line.strip()
        if uses_all(word, 'aeiou'):
            print(word)
            counter += 1
    return counter

print('the number of words that use all the vowels:', find_word_using_all_vowels())


def is_abecedarian(word):
    before = word[0]
    for letter in word:
        if letter < before:
            return False
        before = letter
    return True

# print(is_abecedarian('abs'))
# print(is_abecedarian('college'))

def find_abecedarian_words():
    fin = open("Session-09/words.txt")
    counter = 0
    current_longest_word = ''
    for line in fin:
        word = line.strip()
        if is_abecedarian(word):
            print(word)
            counter += 1
            if len(word)>len(current_longest_word):
                current_longest_word = word

    return counter, current_longest_word


print(find_abecedarian_words())


def is_abecedarian_using_recursion(word):
    if len(word) <= 1:
        return True
    if word[0] > word[0]:
        return False
    return is_abecedarian_using_recursion(word[1:])

def is_abecedarian_using_while(word):

    i = 0 
    while i < len(word)-1:
        if word[i+1] < word[i:]:
            return False
        i = i + 1
    return True