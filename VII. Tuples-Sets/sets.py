s1 = set({1, 2, 3, 4, 5, 6, 5, 7})
s2 = {1, 4, 5}

print(s1)
print(s2)

for number in s1:
    print(number)

# Add an element to a set

s1.add(8)
print(s1)

# Removes a value from the set

s1.remove(8)
# s1.discard(56)
print(s1)

# Creates a copy of the set

s3 = s1.copy()
print(s3)
print(s3 == s1) # True
print(s3 is s1) # False

# Removes all the contents of the set

s3.clear()
print(s3) # set()

# Set Math

math_students = {'Matthew', 'Helen', 'Prashant', 'James', 'Aparna'}
biology_students = {'Jane', 'Matthew', 'Charlotte', 'Mesut', 'Oliver', 'James'}

# Union (|): all elements from both sets
print(math_students | biology_students)

# Intersection (&): set of elements that are common in both the sets
print(math_students & biology_students)

# Comprehension

print({x ** 2 for x in range(10)})

string = 'hello hahaha'
print({char for char in string if char in 'aeiou' })