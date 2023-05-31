from random import randint
from time import sleep
computer = randint(0, 10)
total = 0
user = 50
print ('=' * 18)
print ('Try to defeat me!')
print ('=' * 18)
while user != computer:
    user = int(input('Enter an integer: '))
    total += 1
    if user == computer and total == 1:
        print (f'WOW! You are the best, just need {total} tries.')
    if user == computer and total > 1:
        print (f'YOU WON! But you need {total} tries kkkkk')
    if user < computer:
        print ('BIGGER, try again!')
    if user > computer:
        print ('LOWER, try again!')
print('CONGRATULATIONS!')
