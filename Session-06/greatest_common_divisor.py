def gcd(a, b):

#gcd(2, 12) = 2

#gcd(6, 12) = 6

#gcd(9, 12) = 3

#gcd(17, 12) = 1

    if b == 0:
        return a
    else:
        return gcd(b, a % b)
gcd(2,12)
gcd(8,64)