# Question 78
# Question
# Please write a program to shuffle and print the list [3,6,7,8].

import random


def random_shuffle(users_list):
	random.shuffle(users_list)
	print(users_list)


l1 = [3, 6, 7, 8]
random_shuffle(l1)
