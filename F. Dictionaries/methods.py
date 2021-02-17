instructor = {
    'name': 'Phong',
    'favorite_language': 'Python',
    28: 'my favorite number'
}

# Clear all the keys and values in a dict

# instructor.clear()
# print(instructor)

# Makes a copy of a dict

c = instructor.copy()
print(c)
print(c is instructor) # False

# Creates key-value pairs from comma separated values:

fr = {}.fromkeys(["email"], 'unknown')
#fr = {}.fromkeys(["email", "name"], 'unknown')
print(fr)

# Retrieves a key in an object and return None instead of a KeyError if the key does not exist

print(instructor.get('name')) # Phong
print(instructor.get('test')) # None

# Takes a single argument corresponding to a key and removes that key-value pair from the
# dictionary. Returns the value corresponding to the key that was removed

instructor.pop('name')
print(instructor)

# Removes a random key in a dictionary

instructor.popitem()
print(instructor)

# Update keys and values in a dictionary with another set of key value pairs

first = dict(a=1, b=2, c=3, d=4)
second = {'a': 5}

print(second)
second.update(first)
print(second)
