# Question 72
# Question
# Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive.
# Hints
# Use random.sample() to generate a list of random values.
from random import sample


def gen_5_rand_num_betw_100_200():
	random_list = [n for n in range(100, 201)]
	# print(random_list)
	print(sample(random_list, 5))


gen_5_rand_num_betw_100_200()
