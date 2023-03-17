# Question 71 Question Please write a program to output a random number, which is divisible by 5 and 7, between 10
# and 150 inclusive using random module and list comprehension. Hints Use random.choice() to a random element from a
# list.

import random


def random_div():
	list1 = [n for n in range(10, 151) if n % 5 == 0 and n % 7 == 0]
	print(list1)
	print(random.choice(list1))


random_div()
