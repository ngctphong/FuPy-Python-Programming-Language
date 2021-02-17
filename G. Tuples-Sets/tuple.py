first_tuple = (1, 2, 3, 4, 4)
second_tuple = tuple([5, 1, 2])

print(first_tuple)
print(first_tuple[1]) # 2
print(second_tuple)

for element in first_tuple:
    print(element)

# Returns the number of times a value appears in a tuple
print(first_tuple.count(4))