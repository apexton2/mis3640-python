def linecount(filename):
    count = 0
    for line in open(filename):
        count += 1
    return count


if____name


print(linecount('wc.py'))