first_list = [1, 2, 3, 4]

# Add item to the end of the list
first_list.append(5)
print(first_list)

# Add list all values to the end of the list
first_list.extend([6, 7, 8])
print(first_list)

# Insert an item at a given position
first_list.insert(5, 9)
print(first_list)

# Remove all items from the list
# first_list.clear()
print(first_list)

# Remove the item at the given position. If no index specified, removes and return last item in the list
first_list.pop()
print(first_list.pop(1)) # 2
print(first_list)

# Remove the first item from the list whose value is x. Throws a ValueError if the item is not found
first_list.remove(4)
print(first_list)

# Return the index of the specified item in the list
print(first_list.index(6))
print(first_list.index(6, 1))
print(first_list.index(6, 1, len(first_list) - 1))

# Return the number of times x appears in the list
print(first_list.count(7))

# Reverse the elements of the list
first_list.reverse()
print(first_list)

# Sort the items of the list
first_list.sort()
print(first_list)

# Join
words = ['Coding', 'Is', 'Fun']
print(' '.join(words))
