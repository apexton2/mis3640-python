# name = ['defne', 'jack', 'angela']
# scores = [95, 75, 85]

# grades = dict()
# print(grades)

# grades['defne'] = 90
# print(grades)

# grades = {'defne': 90, 'jack': 75, 'Angela': 85}
# print(grades)

# print(grades['jack'])

# print(len(grades))

# print('jack' in grades)

# 90 in grades.value()

def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

h = histogram('bookkeeper')
print(h)

number_of_e = h.get('e', 0)
number_of_z = h.get('z', 0)
print(number_of_e)
print(number_of_z)

# def print_hist(h):
#     for c in h:
#         print(c, h[c])

# h = histogram('massachusettes')
# print_hist(h)

# f = open("Session-09/words.txt")

# def create_word_dict():
#     word_dict = dict()
#     for line in f:
#         word = line.strip()
#         word_dict[word] = word
#     return word_dict

grades = {'a':3}
# import random
# for name in class_roster:
#     if name[0] == 'A':
#            grades{name} = random.randint(90, 100)
 
#     grades{name} = random.randint(90, 100)
print(grades)


