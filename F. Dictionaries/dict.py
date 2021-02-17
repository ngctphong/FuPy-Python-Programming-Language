instructor = {
    'name': 'Phong',
    'favorite_language': 'Python',
    28: 'my favorite number'
}

for value in instructor.values():
    print(value)

for key in instructor.keys():
    print(key)

for key, value in instructor.items():
    print(f'{key} - {value}')

print('name' in instructor)
print('awesome' in instructor)

first = dict(a=1, b=2, c=3, d=4)
print(first)
