s = input("please enter a string: ")
z = s[::-1]
if s == z:
    print("the string is a palindrome")
else:
    print("the string is not a palindrome")
    print("s is a :",type(s))
    print("z is a :",type(z))
