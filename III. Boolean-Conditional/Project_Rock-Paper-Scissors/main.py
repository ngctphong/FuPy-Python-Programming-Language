from random import randint

print("Rock...")
print("Paper...")
print("Scissors...")

# Basic version

# player1 = input("Player 1, make your move: ")
# player2 = input("Player 2, make your move: ")

# rps = ['rock', 'paper', 'scissors']

# if player1.lower() not in rps or player2.lower() not in rps:
#     print('Wrong input')
# elif player1.lower() == player2.lower():
#     print('Draw')
# elif player1.lower() == 'rock' and player2.lower() == 'scissors' \
#         or player1.lower() == 'paper' and player2.lower() == 'rock' \
#         or player1.lower() == 'scissors' and player2.lower() == 'paper':
#     print('Player 1 wins')
# else:
#     print('Player 2 wins')

# AI version

player1 = input("Player 1, make your move: ")
rps = ['rock', 'paper', 'scissors']

computer = ''
random_number = randint(1, 3)

if random_number == 1:
    computer = 'rock'
    print('The computer plays: rock')
elif random_number == 2:
    computer = 'paper'
    print('The computer plays: paper')
else:
    computer = 'scissors'
    print('The computer plays: scissors')

if player1.lower() not in rps:
    print('Wrong input')
elif player1.lower() == computer:
    print('Draw')
elif player1.lower() == 'rock' and computer == 'scissors' \
        or player1.lower() == 'paper' and computer == 'rock' \
        or player1.lower() == 'scissors' and computer == 'paper':
    print('Player 1 wins')
else:
    print('Computer wins')