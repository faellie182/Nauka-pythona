import sys
from random import randrange

sys.argv
number = randrange(1, 11)
counter = 0
while True:
	try:
		question = int(input('Guess a number between 1 and 10: '))
	except ValueError:
		print('Please enter just a number between 1 to 10.')
		continue
	counter += 1
	if question < number:
		print('It\'s too low.')
	elif question > number:
		print('It\'s too high.')
	elif question == number:
		print(f'Congrats, you\'re correct!. You\'ve tried to guess {counter} time/s.')
		break
