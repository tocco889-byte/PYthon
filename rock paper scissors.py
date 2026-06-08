import random
options = ['rock','paper','scissors']
computer = random.choice(options)

a = input('choose rock paper scissors :')
print('the computer chooses : ' + computer)
if computer == a:
    print('draw')
elif a == 'paper' and computer == 'rock':
    print('you win')
elif a == 'rock' and computer == 'scissors':
    print('you win')
elif a == 'scissors' and computer == 'paper':
    print('you win')
else:
        print("you loose")