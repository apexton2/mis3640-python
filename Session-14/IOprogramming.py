# import os
# print(os.getcwd())

# fout = open('output.txt', 'a')

# line1 = 'How many roads must a man walk down\n"
# fout.write(line1)
# line2 = "Before you call him a man?\n"
# fout.write(line2)
# fout.close()

# print(os.path.abspath('Session-14/output.txt'))

# print(os.path.exists('Session-14/output.txt'))
# print(os.path.exists('Session-14/input.txt'))
import pickle

# t1 = [1, 2, 3]

# f = open('save.p', 'wb')
# s = pickle.dump(t1, f)
# f.close()

t2 = pickle.loads(open('save.p', 'rb'))
print(t2)


