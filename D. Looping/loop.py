# for Loops
for i in range(4):
    print(i)

# While Loops
msg = input('Whats the secret password? ')
while msg != 'bananas':
    print('WRONG!!!')
    msg = input('Whats the secret password? ')

# break keyword
while True:
    command = input('Type \'exit\' to exit: ')
    if command == 'exit':
        break
    else:
        command = input('Type \'exit\' to exit: ')
