import sys
print("first value", sys.argv[0])
print("all values")
for i, x in enumerate(sys.argv):
    print(i, x)

