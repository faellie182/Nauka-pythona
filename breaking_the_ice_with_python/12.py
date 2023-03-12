# Question 12 Question: Write a program, which will find all such numbers between 1000 and 3000 (both included) such
# that each digit of the number is an even number.The numbers obtained should be printed in a comma-separated
# sequence on a single line. Hints: In case of input data being supplied to the question, it should be assumed to be
# a console input.


def in_range_if_num_even():
	users_numbers = input(
		'Give a range of numbers to find which numbers in that range have each digit of the number even (numbers must be '
		'comma separated).: '
	)
	users_numbers_even = []
	users_range = users_numbers.split(',')
	for num in range(int(users_range[0]), int(users_range[1]) + 1):
		for n in str(num):
			if int(n) % 2 == 0:
				pass
			else:
				break
		else:
			users_numbers_even.append(num)
	print(users_numbers_even)

# 2ga:
	users_numbers_even = []
	for num in range(int(users_range[0]), int(users_range[1]) + 1):
		is_odd = False
		for n in str(num):
			if int(n) % 2 == 0:
				pass
			else:
				is_odd = True
				break
		if not is_odd:
			users_numbers_even.append(num)
	print(users_numbers_even)


in_range_if_num_even()
