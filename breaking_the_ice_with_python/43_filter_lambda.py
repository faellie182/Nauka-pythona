# Question 43
# Question:
# Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).
# Hints:
# Use filter() to filter elements of a list.Use lambda to define anonymous functions.


def filter_only_even_num_(users_list):
	print(list(filter(lambda i: i % 2 == 0, users_list)))


list1 = [i for i in range(1, 21)]
filter_only_even_num_(list1)
