def compare(varA, varB):
    if isinstance(varA, str) or isinstance(varB, str):
        print('string involved')
        print('string involved')
    else:
        if varA > varB:
            print('bigger')
        elif varA == varB:
            print('equal')
        else:
            print('smaller')

a = 'hello'
b = 3
c = 5

compare(a, b)
compare(b, c)