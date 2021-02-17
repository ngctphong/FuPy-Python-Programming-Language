d = {"name": "Mbappe"}


def get(d, key):
    try:
        return d[key]
    except KeyError:
        return None


print(get(d, "name"))
print(get(d, "city"))

while True:
    try:
        num = int(input("please enter a number: "))
    except ValueError:
        print("That's not a number!")
    else:
        print("Good job, you entered a number!")
        break
    finally:
        print("RUNS NO MATTER WHAT!")
print("REST OF GAME LOGIC RUNS!")


def divide(a, b):
    try:
        result = a / b
    except (ZeroDivisionError, TypeError) as err:
        print("Something went wrong!")
        print(err)
    else:
        print(f"{a} divided by {b} is {result}")


# print(divide(1,2))
print(divide(1, 'a'))
print(divide(1, 0))
print(divide(1, 2))
