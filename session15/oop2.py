class Time:
    """represents time of day. 
    attributes: hour, minute, second
    """

time = Time()
time.hour = 11
time.minute = 59
time.second = 30

later = Time()
later.hour = time.hour
later.minute = time.minute + 5
later.second = time.second

print(time.hour, time.minute, time.second)

#excersize 1

def print_time(t):
    """prints time in a string
    t: time object
    """
    print('{:2d}:{:2d}:{:2d}'.format(t.hour,t.minute,t.second))
    
    print_time(time)

def is_after(t1, t2):
    """returns true if t1 is after t2. returns false otherwise"""
    if t1.hour > t2.hour:
        return True
    elif t1.hour < t2.hour:
        return False
    elif t1.minute > t2.minute:
        return True

print(is_after(time, later))

# Here is a simple prototype of add_time:
# def add_time(t1, t2):
#     sum = Time()
#     sum.hour = t1.hour + t2.hour
#     sum.minute = t1.minute + t2.minute
#     sum.second = t1.second + t2.second
#     return sum

# start = Time()
# start.hour = 9
# start.minute = 45
# start.second =  0

# duration = Time()
# duration.hour = 1
# duration.minute = 35
# duration.second = 0

# done = add_time(start, duration)
# print_time(done)

def increment(time, seconds):
    time.second += seconds

    if time.second >= 60:
        time.second -= 60
        time.minute += 1

    if time.minute >= 60:
        time.minute -= 60
        time.hour += 1

def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def add_time_2(t1, t2):
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)

def valid_time(time):
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False
    if time.minute >= 60 or time.second >= 60:
        return False
    return True


def add_time_2(t1, t2):
    if not valid_time(t1) or not valid_time(t2):
        raise ValueError('invalid Time object in add_time')
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)

def add_time(t1, t2):
    assert valid_time(t1) and valid_time(t2)
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)

    #excerises 4 and 5 WIP