# *args: Gathers remaining arguments as a tuple

def sum_all_nums(*args):
    total = 0
    for num in args:
        total += num
    return total


print(sum_all_nums(1, 2, 3))


# **kwargs: Gathers remaining arguments as a dictionary

def fav_colors(**kwargs):
    for person, color in kwargs.items():
        print(f"{person}'s favorite number is {color}")


fav_colors(colt='purple', ruby='red', ethel='tears')

# Parameter Ordering
# 1. parameters
# 2. *args
# 3. default parameters
# 4. **kwargs

# Tuple unpacking

print(sum_all_nums(*[1, 2, 3]))
print(sum_all_nums(*(1, 2, 3)))


# Dictionary unpacking

def display_name(first, second, **kwargs):
    print(f'{first} says hello to {second}')
    print(kwargs)


names = {'first': 'Colt', 'second': 'Rusty', 'third': 'Daniel'}
display_name(**names)
