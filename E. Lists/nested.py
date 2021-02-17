nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(nested_list[0][1])

for list in nested_list:
    for el in list:
        print(el)

# Nested List Comprehension
[[print(val) for val in l] for l in nested_list]

board = [[num for num in range(1, 4)] for num in range(1, 4)]
print(board) # [[1, 2, 3], [1, 2, 3], [1, 2, 3]]