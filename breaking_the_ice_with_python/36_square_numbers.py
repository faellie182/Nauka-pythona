# Question 36 Question: Define a function which can generate a list where the values are square of numbers between 1
# and 20 (both included). Then the function needs to print all values except the first 5 elements in the list.


def gen_list_square(numbers):
	list_square = []
	for num in numbers:
		list_square.append(num * num)
	# print(list_square)
	print(list_square[5:])


l1 = [i for i in range(1, 21)]
gen_list_square(l1)
