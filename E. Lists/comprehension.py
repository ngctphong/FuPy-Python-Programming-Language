numbers = [1, 2, 3, 4, 5, 6]

evens = [num for num in numbers if num % 2 == 0]
odds = [num for num in numbers if num % 2 != 0]

result = [num * 2 if num % 2 == 0 else num / 2 for num in numbers]

print(evens)
print(odds)
print(result)