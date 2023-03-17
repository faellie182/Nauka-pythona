# Question 73
# Question
# Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.
# Hints
# Use random.sample() to generate a list of random values.

from random import sample


def rand_5_even_num_betw_100_200():
	random_list = [n for n in range(100, 201) if n % 2 == 0]
	print(sample(random_list, 5))


rand_5_even_num_betw_100_200()
