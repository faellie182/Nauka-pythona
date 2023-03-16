# Question 70 Question Please write a program to output a random even number between 0 and 10 inclusive using random
# module and list comprehension.

from random import choice
from random import randrange


def random_num_0_to_10():
	l1 = [n for n in range(0, 11) if n % 2 == 0]
	print(choice(l1))


def random_num(start, end):
	l1 = [n for n in range(start, end + 1) if n % 2 == 0]
	print(choice(l1))


random_num_0_to_10()
random_num(0, 10)
