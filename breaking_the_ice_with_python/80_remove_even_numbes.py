# Question 80
# Question
# Please write a program to print the list after removing even numbers in [5,6,77,45,22,12,24].


def remove_even_num(users_list):
	new_list = []
	for n in users_list:
		if n % 2 != 0:
			new_list.append(n)
	print(new_list)


l1 = [5, 6, 77, 45, 22, 12, 24]
l2 = [6, 7, 87, 46, 23, 13, 25]
remove_even_num(l1)
remove_even_num(l2)
