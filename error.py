def get_number():
    "returns a float number"
    number = float(input("enter a float number: "))
    return number

while True:
    try:
        print(get_number())
    except ValueError:
        print("you enter a wrong value.")
