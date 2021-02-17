# Declare function

def sing_happy_birthday():
    print('Happy Birthday To You')


sing_happy_birthday()


def square_of_7():
    return 7 * 7


print(square_of_7())


# Parameters

def square(num):
    return num * num


print(square(8))


def is_odd_number(num):
    return num % 2 != 0


print(is_odd_number(4))
print(is_odd_number(9))


# Default Parameters

def exponent(num, power=2):
    return num ** power


print(exponent(2, 3))
print(exponent(4))
print(exponent(power=5, num=8))


def full_name(first='Phong', last='Nguyen'):
    return f'Your name is {first} {last}'


print(full_name())

# global

total = 0


def increment():
    global total
    total += 1
    return total


increment()
print(total)


# nonlocal: Lets modify a parent's variables in a child (nested) function

def outer():
    count = 0

    def inner():
        nonlocal count
        count += 1
        return count

    return inner()


print(outer())


# Documenting functions

def say_hello():
    """A simple function that returns the string hello"""
    return 'Hello!'


print(say_hello.__doc__)
