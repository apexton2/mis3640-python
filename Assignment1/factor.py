# Factoring of integers. Write a program that asks the user for an integer and
#  then prints out all its factors. 
# For example, when the user enters 150, the program should print 2 3 5 5

def factor(n):
    #function takes a number and prints out its factors
    print("the factors for",n,"are:")
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)
n = 999
print(factor(n))