import math
ratio = 100
math.log10(ratio)
def print_lyrics():
    print("Hey Jude. Don't make it bad")
    print("Take a sad song and make it better")

Print_lyrics()

print(type(print_lyrics))

def repeat_lyrics():
    print_lyrics()
    print('na- na- na- na!')
    print_lyrics()

repeat_lyrics()

def print_twice(Alden):
print('first time:')
print(Alden)
print('the second time:')
print(Alden)

#print_twice('name')
name = input('please enter your name:')
print_twice(name)
print(Alden)


def my_abs(n):
if n < 0:
    print(-n)
else:
    print(n)

my_abs(-5)
my_abs(-4)


def give_a_break():
    return 'break'

    print(give_a_break())

def give_me_another_break():
    str1 = 'break'
    print('another break')
    return = str1

print(give_me_another_break())