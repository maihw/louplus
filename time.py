import sys

def hours(minute):
    if minute < 0:
        raise ValueError("input number cannot be negative")
    else:
        print("{} H, {} M".format(int(minute / 60),minute % 60))

try:
    hours(int(sys.argv[1]))
except:
    print("parameter error")
