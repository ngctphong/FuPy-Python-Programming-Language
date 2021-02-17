def colorize(text, color):
    colors = ('cyan', 'blue', 'green')
    if type(color) is not str:
        raise TypeError('color must be instance of str')
    if type(text) != str:
        raise TypeError('text must be instance of str')
    if color not in colors:
        raise ValueError('color is invalid')
    print(f'Printed {text} in {color}')


colorize('hello', 10)
colorize('hi', 'red')
colorize(7, 'red')
