from random import randint

random_number = randint(1, 10)

while True:
    guess = int(input('Guess a number between 1 and 10: '))
    if guess < random_number:
        print('Too low, try again!')
    elif guess > random_number:
        print('Too high, try again!')
    else:
        print('You guessed it! You won!')
        keep_playing = input('Do you want to keep playing? (y/n) ')
        if keep_playing == 'y':
            random_number = randint(1, 10)
        elif keep_playing == 'n':
            break
