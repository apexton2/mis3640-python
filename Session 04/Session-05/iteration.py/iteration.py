#print(1 + 2 + 3)
import math
import pandas
# sum = 0
# for i in range(0,10):
#     sum = sum + i
# print (sum)

# sum = 0
# sum = sum + i
# for i in range(0,100):
# if(i%2!=0):
# print (sum)

# def countdown(n):
#     while n > 0:
#         print(n)
#         n = n - 1
#     print('Blastoff')
#     countdown(10)

# iteration = 0
# count = 0
# while iteration < 5:
#     for letter in "Hello, world":
#         count += 1
#     print("Iteration " + str(iteration) +"; count i s: " + str(count))
#     iteration += 1

# iteration = 0
# while iteration < 5:
#     count = 0
#     for letter in "hello, world":
#         count += 1
#     print("Iteration " + str(iteration) +"; count i s: " + str(count))
#     iteration += 1

# iteration = 0
# while iteration < 5:
#     count = 0
#     for letter in "hello, world":
#         count += 1
#         if iteration % 2 == 0:
#             break
#     print("Iteration " + str(iteration) + "; count is: " + str(count))
#     iteration += 1

# mysum = 0
# for i in range(5, 11, 2):
#     mysum += 1
#     if mysum == 5:
#         break
# # print(mysum)


# a = 4
# x = 3
# y = (x + a/x) / 2
# print (y)
# x = y
# y = (x + a/x) / 2
# print(y)
# x = y
# y = (x + a/x) / 2
# print(y)

# while True:
#     print(x)
#     y = (x + a/x) / 2
#     if y == x:
#         break
#     x = y

def mysqrt(a):
    x = a/2
    while True:
        estimated_root = (x + a/x) / 2
        if estimated_root == x:
            return estimated_root
            break
        x = estimated_root
def test_square_root(list_of_a):
    line1a = "a"
    line1b = "mysqrt(a)"
    line1c = "math.sqrt(a)"
    line1d = "diff"

    line2a = "-"
    line2b = "---------"
    line2c = "------------"
    line2d = "----"

    spacing1 = " "
    spacing2 = " " * 3
    spacing3 = ""

    print(line1a, spacing1, line1b, spacing2, line1c, spacing3, line1d)
    print(line2a, spacing1, line2b, spacing2, line2c, spacing3, line2d)
    
    for a in list_of_a:
        col1 = float(a)
        col2 = mysqrt(a)
        col3 = math.sqrt(a)
        col4 = abs(mysqrt(a) - math.sqrt(a))

        print(col1, "{: <13f}".format(col2), "{:<13f}".format(col3), col4)

    test_square_root(range(1,10))



    
