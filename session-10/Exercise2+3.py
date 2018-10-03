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


