# Question 81 Question By using list comprehension, please write a program to print the list after removing numbers
# which are divisible by 5 and 7 in [12,24,35,70,88,120,155].


def remov_num_div_by_5_7(users_list):
	list_div = list(filter(lambda n: n % 5 == 0 and n % 7 == 0,
												 users_list))  # sprawdza i zwraca True/False
	print(list_div)
	final_list2 = [n for n in users_list if n % 5 == 0 and n % 7 == 0]
	print(final_list2)


l1 = [12, 24, 35, 70, 88, 120, 155]
remov_num_div_by_5_7(l1)
