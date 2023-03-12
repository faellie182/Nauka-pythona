# Question 35 Question: Define a function which can generate a list where the values are square of numbers between 1
# and 20 (both included). Then the function needs to print the last 5 elements in the list.


def gen_list_last_5(list):
	list_of_numbers = []
	for num in list:
		list_of_numbers.append(num * num)
	print(list_of_numbers[-5:])


def gen_list_last_5_a(begin, end):
	list_of_numbers = list(range(begin, end + 1))
	list_of_numbers_square = list(map(lambda num: num * num, list_of_numbers))
	print(list_of_numbers_square[-5:])


l1 = [k for k in range(1, 21)]
gen_list_last_5(l1)

gen_list_last_5_a(1, 20)
