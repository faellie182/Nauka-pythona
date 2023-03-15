# Question 44
# Question:
# Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).

# Hints:
# Use map() to generate a list. Use lambda to define anonymous functions.


def gen_list_square(users_range1, users_range2):
	return list(map(lambda i: i*i, range(users_range1, users_range2)))


print(gen_list_square(1, 21))