def countdown(n):
    if n <= 0:
        print('blastoff!')
    else:
        print(n)
        countdown(n-1)
countdown(3)

def print_n(s, n):
    if n <= 0:
        return
    print(s)
    print_n(s, n-1)
