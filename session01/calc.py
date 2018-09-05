print(8 + 30 + 2018)

#EXERCISE 1
#1
import math
print(math.pi)
math.pi  = pi
print(pi)
r = 5
print(r)
x = (4/3) * pi * r **3))
print(x)
print('The Volume of a sphere with radius r is {}'.format(x))

#2 Suppose the cover price of a book is $24.95, but bookstores get a 40\% discount. 
# Shipping costs $3 for the first copy and 75 cents for each additional copy. 
# What is the total wholesale cost for 60 copies?
book = 24.95
discount = .60
c = ((book * discount + 3) + (((book * discount) * 1.75) * 59))
print(c)
print('The total wholesale cost for 60 copies is {}'.format(c))

#If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile)
# , then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again, 
# what time do I get home for breakfast?
start = ((6 * 3600) + (52 * 60))
print(start)
ep = (8.15 * 60)
t = (7.12 * 60)

a = start + (2 * ep + 3 * t)
print (a/3600)
print('You would arrive home by {:.2f}'.format(a/3600))

#If my average grade rises from 82 to 89. What is the percentage of the increase?
#  Format the result as 'xx.x%'. Keep one figure after decimal point.

percent_increase = ((89-82)/82)
print(percent_increase)
print('your percent increase would be {:.2%}'.format(percent_increase))




