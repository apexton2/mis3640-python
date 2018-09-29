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


# def avoids(word, forbidden):
#     for letter in word:
#        if letter == 'e':
#             return False
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

fin = open("Session-09/words.txt")

def is_double_triple(word):
  i = 0 
  count = 0
  while i < len(word)-1:
    if word[i] == word[i+1]:
        count = count + 1
        if count == 3:
          return True
        i = i + 2
    else:
        count = 0
        i = i + 1
  return False

  def find_double_triple(word):
    fin = open("Session-09/words.txt")
    for line in fin:
        word = line.strip()
        if is_double_triple(word):
              print (word)
              find_double_triple(fin)
              print(fin)

# print 'Here are all the words in the list that have'
# print 'three consecutive double letters.'
# find_triple_double()
# print