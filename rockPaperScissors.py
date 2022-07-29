from importlib import import_module
from multiprocessing import parent_process
from random import random



import random

computer_choice = random.choice(['scissors', 'rock', 'paper'])

user_choice = input('do you want - rock, paper, or scissors?\n')

if computer_choice == user_choice:
    print('TIE!')

elif user_choice == 'rock' and computer_choice == 'scissors':
    print(' you win!')

elif user_choice == 'paper' and computer_choice == 'rock' :
    print('You Win!')

elif user_choice == 'scissors' and computer_choice == 'paper' :
    print('You Win!')

else:
    print('you lose :( computer wins  with' + computer_choice + ' :D')

