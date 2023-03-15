# Question 41
# Question:
# Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].


def square(users_list):
	"""Makes a list of square of elements given"""
	result = list(map(lambda x: x * x, users_list))
	return result


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(square(list1))
