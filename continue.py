while True:
    n = int(input("Please enter an Integer: "))
    if n < 0:
        continue
    elif n == 0:
        break
    print("square is ", n ** 2)
print("goodbye")
