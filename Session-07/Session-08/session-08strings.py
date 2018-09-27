# team = 'New England Patriots'
# # letter = team[0] #The expression in brackets is called an index. 
# # len(team)

# # last  = team[len(team)-1]
# # print(last)
# # last = team[-1]
# # print(last)

# for letter in team:
#     print(letter)

# prefixes = 'JKLMNOPQ'
# suffix = 'ack'
# for letter in prefixes:
#     if letter == 'Q' or letter == 'O':
#         print(letter + 'U' + suffix)
# else:
#     print(letter + suffix)

#STRING SLICES- a segment of a string is called a 

team = 'New England Patriots'
# print(team[0:11]) #prints letters 0,1,2
# print(team[20:2])

# new_team = team[:12]+'Nannygoats'
# print(new_team)

# def find(word, letter):
#     index = 0
#     while index < len(word):
#         if word[index] == letter:
#             return index
#         index = index + 1
#     return -1

# print(find(team, 'E'))

# for i in range(len(team)):
#     if team[i] == 'a':
#         print(i)

# for i, letter in enumerate(team):
#     if letter == 'a':
#         print(i, letter)

# word = 'New England Patriots'
# count = 0
# for letter in word:
#     if letter == 'a':
#         count = count + 1
# print(count)

# def count(s, letter):
#     c = 0
#     for each in s:
#         if each == letter:
#             c += 1
#         return c

# print(count(team, 'a'))

# print(count(team, ''))

# team = 'New England Patriots'
# # new_team = team.upper()
# # print(new_team)
# # index = team.find('a')
# # print(index)

# #print(team.find('En'))

# print(team.find('a', 10))

# name = 'bob'
# print(name.find('b', 1, 2))

from string import ascii_lowercase


LETTERS = {letter: str(index) for index, letter in enumerate(ascii_lowercase, start=1)} 

def alphabet_position(text):
    text = text.lower()

    numbers = [LETTERS[character] for character in text if character in LETTERS]

    return ' '.join(numbers)


print(alphabet_position('alden'))

def listsum(numList):
    theSum = 0
    for i in numList:
        theSum = theSum + i
    return theSum

print(listsum([1,3,5,7,9]))

