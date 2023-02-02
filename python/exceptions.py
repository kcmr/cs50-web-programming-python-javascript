import sys

a = int(input("Number 1: "))
b = int(input("Number 2: "))


def divide():
    try:
        print(f"{a} divided by {b} is: {a/b}")
    except ZeroDivisionError:
        print("0 is not allowed")
        sys.exit(1)


divide()
