t = ['a', 'b', 'c', 'd']
# t.append('d')
# print(t)

# t.extend('f')

# t.insert(0,'z')
# print(t)

# t.pop(1)

# print(t)
# t.clear()
# print(t)

# t.index('a')
# print(t.index('a'))

# print(t.sort())
# t.reverse()
# print(t)

# t.copy
# print(t)


# EXERCISE 3

# def capitalize_all(t):
#     res = []
#     for s in t:
#         res.append(s.capitalize())
#     return res
# print(capitalize_all(t))

# # print(sum(t))

# def only_upper(t):
#     res = []
#     for s in t:
#         if s.isupper():
#             res.append(s)
#     return res

# t = ['a', 'b', 'c', 'd']
# x = t.pop(1)

# print(x)
# print(t)

# x = t.pop()
# print(x)

# del t[1:3]
# print(t)

# t.remove('a')
# print(t)

team = 'patriots'
t = list(team)
print(t)

team = 'New England Patriots'
t = team.split()
print(t)

s = 'spam-spam-spam'
delimiter = '-'
t = s.split(delimiter)
print(t)

t = ['New', 'England', 'Patriots']
team = ' '.join(t)
print(team)

a = 'banana'
b = 'banana'

a is b 

a = [1, 2, 3]
b = [1, 2, 3]
a is b

a = [1, 2, 3]
b = a
b is a 
b[0] = 'something else'
print(a)

# t.append(x)
# t = t + x [x]
# t += [x]

t = [3, 1, 2]
t2 = t[:]
t2.sort()
print(t)
print(t2)


def is_sorted(t):
    """Checks whether a list is sorted.
    t: list
    returns: boolean
    Expected output:
    >>> is_sorted([1, 2, 2])
    True
    >>> is_sorted(['b', 'a'])
    False
    """
    return

def is_sorted(t):
    previous = t[0]
    for c in t:
        if c < previous:
            return False
        previous = c
    return True

    return t == sorted(t)

print(is_sorted(['a', 'b', 'b', 'c']))
print(is_sorted(['a', 'b', 'c', 'b']))


def is_anagram(word1, word2):
    """Checks whether two words are anagrams
    Two words are anagrams if you can rearrange the letters from one to 
    spell the other.
    word1: string or list
    word2: string or list
    returns: boolean
    Expected output:
    >>> is_anagram('stop', 'pots')
    True
    >>> is_anagram('different', 'letters')
    False
    >>> is_anagram([1, 2, 2], [2, 1, 2])
    Ture
    """
    return sorted(word1) == sorted(word2)
    
print(is_anagram('stop', 'pots'))
print(is_anagram([1, 2, 2], [2, 1, 2]))

def has_duplicates(s):
    """Returns True if any element appears more than once in a sequence.
    s: string or list
    returns: bool
    output:
    >>> print(has_duplicates('cba'))
    False
    >>> print(has_duplicates('abba'))
    True
    """

def has_adjacent_duplicates(s):
    """Returns True if there are two same adjacent elements.
    s: string or list
    returns: bool
    output:
    >>> print(has_adjacent_duplicates('cba'))
    False
    >>> print(has_adjacent_duplicates('abca'))
    Flase
    >>> print(has_adjacent_duplicates('abbc'))
    True
    """
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return True
    return false