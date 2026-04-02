import time

""" 
EPOCH = 1970-01-01T00:00:00Z, the point where the time starts and is represented as the number of seconds that have elapsed since then, ignoring leap seconds.
    a date time from which a computer system measures system time. It is used as a reference point for calculating time and is commonly used in programming and computing to represent dates and times as a single number (the number of seconds since the epoch).
"""

print(time.time())  # current time in seconds since the epoch
print(time.ctime())  # current time in a human-readable format
print(time.ctime(0))  # epoch time in a human-readable format
print(time.localtime())  # current time as a struct_time in local time
print(time.gmtime())  # current time as a struct_time in UTC
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))  # current time formatted as a string