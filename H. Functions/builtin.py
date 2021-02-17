# map: The map() function executes a specified function for each item in an iterable.
# The item is sent to the function as a parameter.

def myfunc(n):
    return len(n)


x = map(myfunc, ('apple', 'banana', 'cherry'))
for el in x:
    print(el)

people = ['Ronaldo', 'Messi', 'Neymar']
peeps = map(lambda name: name.upper(), people)
print(list(peeps))

# filter: The filter() function returns an iterator were the items are filtered through
# a function to test if the item is accepted or not.

l = [1, 2, 3, 4]

evens = list(filter(lambda x: x % 2 == 0, l))
print(evens)

names = ['Lassie', 'Colt', 'Rusty']

# filter_name = [f'Your instructor is {name}' for name in names if len(name) <= 5]
filter_name = list(map(lambda name: f'Your instructor is {name}',
                       filter(lambda name: len(name) <= 5, names)))
print(filter_name)

# all: Return True if all elements of the iterable are truthy (or if the iterable is empty)

nums = [2, 4, 6, 8, 21]
print(all([num % 2 == 0 for num in nums]))

# any: Return True if any element of the iterable is truthy. If the iterable is empty, return False

print(any([num % 2 != 0 for num in nums]))

# Generator Expression

import sys

# A simple comparison of size (in Bytes)
list_comp = sys.getsizeof([x * 10 for x in range(1000)])
gen_exp = sys.getsizeof(x * 10 for x in range(1000))

print("To do the same thing, it takes...")
print(f"List Comprehension: {list_comp} bytes")
print(f"Generator Expression: {gen_exp} bytes")

# sorted: returns a sorted list of the specified iterable object.
nums = [4, 6, 2, 11, 7, 80]
print(sorted(nums))
print(sorted(nums, reverse=True))
print(nums)

users = [
    {"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
    {"username": "katie", "tweets": ["I love my cat"]},
    {"username": "jeff", "tweets": [], "color": "purple"},
    {"username": "bob123", "tweets": [], "num": 10, "color": "teal"},
    {"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
    {"username": "guitar_gal", "tweets": []}
]

for user in users:
    print(len(user))  # count key of dict object

print(sorted(users, key=len))
print(sorted(users, key=lambda user: user['username']))

# max: Return the largest item in an iterable or the largest of two or more arguments

print(max(2, 4, 33, 6))

# min: # max: Return the smallest item in an iterable or the smallest of two or more arguments

print(min(4, 66, 3, 6, 22, 2))

songs = [
    {"title": "happy birthday", "playcount": 1},
    {"title": "Survive", "playcount": 6},
    {"title": "YMCA", "playcount": 99},
    {"title": "Toxic", "playcount": 31}
]

# Finds the song with the lowerest playcount
print(min(songs, key=lambda s: s['playcount']))  # {"title": "happy birthday", "playcount": 1}

# Finds the title of the most played song
print(max(songs, key=lambda s: s['playcount'])['title'])  # YMCA

# reversed: Return a reversed iterator object

alph = ["a", "b", "c", "d"]
ralph = reversed(alph)

for x in ralph:
    print(x)

# len: Return the length (the number of items) of an object

print(len('Phong'))

# abs: Return the absolute value of a number

print(abs(-9))
print(abs(-8.36))

# sum: Return a number, the sum of all items in an iterable.

print(sum([1, 2, 3, 4, 5, 6]))  # 21
print(sum([1, 2, 3, 4, 5, 6], 10))  # 31

# round: Returns a floating point number that is a rounded version of the specified number,
# with the specified number of decimals. The default number of decimals is 0,
# meaning that the function will return the nearest integer.

print(round(5.76543, 2))
print(round(7.5))

# zip:  Returns a zip object, which is an iterator of tuples where the first item in each passed iterator
# is paired together, and then the second item in each passed iterator are paired together etc.
# If the passed iterators have different lengths, the iterator with the least items decides
# the length of the new iterator.

a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica", "Vicky")

print(list(zip(a, b)))
print(tuple(zip(a, b)))

five_by_two = [(0, 1), (1, 2), (2, 3), (3, 4)]
print(list(zip(*five_by_two)))

midterms = [80, 91, 78]
finals = [98, 89, 53]
students = ['dan', 'ang', 'kate']

# returns dict with {student:highest score} USING DICT COMP
# {'dan': 98, 'ang': 91, 'kate': 78}
final_grades = {t[0]: max(t[1], t[2]) for t in zip(students, midterms, finals)}

# returns dict with {student:highest score} (same thing as above) USING MAP+LAMBDA
# {'dan': 98, 'ang': 91, 'kate': 78}
final_grades_dict = dict(
    zip(
        students,
        map(
            lambda pair: max(pair),
            zip(midterms, finals)
        )
    )
)

# returns dict with student:average score
# {'dan': 89.0, 'ang': 90.0, 'kate': 65.5}
avg_grades = dict(
    zip(
        students,
        map(
            lambda pair: ((pair[0] + pair[1]) / 2),
            zip(midterms, finals)
        )
    )
)
