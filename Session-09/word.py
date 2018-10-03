# fin = open("Session-09/words.txt")
# # line = fin.readline()
# # word = line.strip()
# # print(word)

# # counter = 0
# # for line in fin:
# #   word = line.strip()
# #   counter += 1
# #   # print(word)
# # print(counter)
# line = fin.readline()


# def read_long_words(list):
#   for line in list:
#     word = line.strip()
#     if len(word) > 20:
#       print(word)
# read_long_words(fin)
#     """
#     prints only the words with more than 20 characters
#     """




# def has_no_e(word):
#   # for letter in word:
#   #     if letter == 'e':
#   #       return False
#   # return True
#   return not 'e' in word.lower()


#     # """
#     # returns True if the given word doesn’t have the letter “e” in it.
#     # """


# print(has_no_e('Babson'))
# print(has_no_e('College'))


def avoids(word, forbidden):
    for letter in word:
       if letter == 'e':
            return False
#     return True
#     """
#     takes a word and a string of forbidden letters, and that returns True
#     if the word doesn’t use any of the forbidden letters.
#     """
    


# print(avoids('Babson', 'ab'))
# print(avoids('College', 'ab'))


# def uses_only(word, available):
#     for letter in word: 
#         if letter not in available:
#             return False
#     return True

#     """
#     takes a word and a string of letters, and that returns True if the word
#     contains only letters in the list.
#     """
#     pass


# print(uses_only('Babson', 'aBbsonxyz'))
# print(uses_only('college', 'aBbsonxyz'))


# def uses_all(word, required):
#     for letter in required:
#         if letter not in word:
#             return False
#     return True
#     """
#     takes a word and a string of required letters, and that returns True if
#     the word uses all the required letters at least once.
#     """
#     pass


# print(uses_all('Babson', 'abs'))
# print(uses_all('college', 'abs'))


# def is_abecedarian(word):
#     previous = word[0]
#     for c in word:
#         if c < previous:
#             return False
#         previous = c
#     return True
#     """
#     returns True if the letters in a word appear in alphabetical order
#     (double letters are ok).
#     """
#     pass


# print(is_abecedarian('abs'))
# print(is_abecedarian('college'))

# fin = open("Session-09/words.txt")

# def is_double_triple(word):
#   i = 0 
#   count = 0
#   while i < len(word)-1:
#     if word[i] == word[i+1]:
#         count = count + 1
#         if count == 3:
#           return True
#         i = i + 2
#     else:
#         count = 0
#         i = i + 1
#   return False

#   def find_double_triple(word):
#     fin = open("Session-09/words.txt")
#     for line in fin:
#         word = line.strip()
#         if is_double_triple(word):

#           print(find_double_triple)
#               print (word)
#               find_double_triple(fin)
#               print(fin)

# print 'Here are all the words in the list that have'
# print 'three consecutive double letters.'
# find_triple_double()
# print

# def avoids(word, forbidden):
#   for letter in word:
#     if letter in forbidden:
#       return False
#     return True


#   print(avoids('baboson, abdce'))

def uses_only(word, available):
    """
    takes a word and a string of letters, and that returns True if the word
    contains only letters in the list.
    """
    for letter in word:
        if letter not in available:
            return False
    return True


def uses_all(word, required):
    # fin = open("Session-09/words.txt")
    # for letter in required:
    #   if letter not in word:
    #     return False
    # return True
    return uses_only(required, word)

print(uses_all('Babson', 'abs'))
print(uses_all('college', 'abs'))

def find_words_using_all_vowels():
    fin = open("Session-09/words.txt")
    counter = 0
    for line in fin:
      word = line.strip()
      # if ...
      return counter

      print('the number of words that use all the vowels:',find_words_using_all_vowels())
    

    def find_words_no_vowels():
        fin = open("Session-09/words.txt")
        counter_no_vowel = 0
        counter_total = 0
        for line in fin:
          counter_total += 1
          word = line.strip()
          if avoids(word, 'aeiouy'):
           print(word)
          counter_no_vowel += 1
        return counter_no_vowel/counter_total
    