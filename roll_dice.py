import random

roll = random.randint(1,6)


guess = int(input('guess the dice roll\n'))

if guess == roll:
    print('correct the computer rolled a ' + str(roll))

else:
    print('nope, the computer rolled a ' + str(roll))
    