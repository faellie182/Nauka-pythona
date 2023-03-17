# Question 74 Question Please write a program to randomly generate a list with 5 numbers, which are divisible by 5
# and 7 , between 1 and 1000 inclusive. Hints Use random.sample() to generate a list of random values.

from random import sample


def random_5_num_div_by_5_and_7_with_range():
	list_div_by_5 = []
	for i in range(1, 1001):
		if i % 5 == 0 and i % 7 == 0:
			list_div_by_5.append(i)
	print(sample(list_div_by_5, 3))


def random_5_num_div_by_5_and_7(start, stop):
	list_div_by_5 = []
	for i in range(start, stop + 1):
		if i % 5 == 0 and i % 7 == 0:
			list_div_by_5.append(i)
	print(sample(list_div_by_5, 3))


random_5_num_div_by_5_and_7_with_range()
random_5_num_div_by_5_and_7(1, 1000)
