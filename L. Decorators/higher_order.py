def sum(n, func):
    total = 0
    for num in range(n):
        total += func(num)
    return total


def square(x):
    return x * x


print(sum(3, square))