# Question 11 Question Write a program which accepts a sequence of comma separated 4 digit binary numbers as its
# input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed
# in a comma separated sequence. Example: 0100,0011,1010,1001 Then the output should be: 1010 Notes: Assume the data
# is input by console. Hints: In case of input data being supplied to the question, it should be assumed to be a
# console input.


def input_if_div_by_5():
	users_numbers_input = input(
		'Give  a sequence of comma separated 4 digit binary numbers to be checked if they are divisible by 5: '
	)
	users_numbers = users_numbers_input.split(',')
	for u in users_numbers:
		if int(u, 2) % 5 == 0:  # na 2gim miejscu w incie się podaje, w jakim systemie jest liczba wejściowa
			print(u, end=',')
		else:
			pass


input_if_div_by_5()
