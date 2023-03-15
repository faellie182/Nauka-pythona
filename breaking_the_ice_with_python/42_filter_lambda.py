# Question 42 Question: Write a program which can map() and filter() to make a list whose elements are square of even
# number in [1,2,3,4,5,6,7,8,9,10].

# Hints:
# Use map() to generate a list.Use filter() to filter elements of a list.Use lambda to define anonymous functions.


def only_square_of_even_num(item):
	even_num = list(filter(lambda i1: i1 % 2 == 0, item))
	print(even_num)
	final = list(map(lambda i2: i2 * i2, even_num))
	print(final)
	return final


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
only_square_of_even_num(numbers)
