#byte is 8-bits used in situations of multilanguage to avoid problems#
#IDENTIFIERS:
# for class roster
#alden, *b = class_roster (this prints everything in the list after alden)
# *a, b = class_roster, only gives you the first item on the list)

#This is how we do variable assignments

#set Prints  no repeat items in a list

# a = [1,2, 3, 4, 1, 4]
# print(set(a))
# print(chr(64))
# print(ord('!'))
# x = 'dog'
# (repr(x)

#boolean practice with conditionals#

# def a(b):
#     if b > 10:
#         return True
    
#     else:
#         return False
    
#     return b > 10
# print(a(11))

# group=['apple', 'orange', 'banana', 'kiwi']

# roster = {name: len(name) for name in group}

# print(roster)
import random

class_roster = {'Jonathan Beltran': 0, 'Allison Fernandez': 1,
 'Siddhanth Goyal': 0,'Jingyu He': 0, 'Defne Ikiz': 0, 
'Zirui Jiao': 0, 'Pranjal Joshi': 0, 'Dong Hyun Kim': 0,
 'Ha Min Ko': 0, 'Kyle Lawson': 0,'Christine Lee': 1, 'Connie Li': 1,
'Qinyi Li': 0, 'Matthew Michalke': 0, 'Ho Wang Alastair Ng': 1, 'Jonghyun Park': 0,
 'Alden Pexton': 2, 'Shriya Rathi': 2, 'Waylon Ryan': 1, 'Christian Thompson': 3,
  'Angela Tsung': 2, 'Aaron Wendell': 0, 'Sarah Zazyczny': 0, 'Shiyue (Shirley) Zong': 0}

# min_times = min(class_roster.values())

# print(min_times)

# pool = []

# for name in class_roster:
#     if class_roster[name] == min_times:
#         pool.append(name)
# random_name = random.choice(pool)
# print(random_name)

# #update a value on the dictionary#
# class_roster['Dong Hyun Kim'] += 1

# print(class_roster)


class_roster.update({"Alden Pexton":99})

print(class_roster)

#TODO: store the data



  