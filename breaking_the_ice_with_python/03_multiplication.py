# 3. With a given integral number n, write a program to generate a dictionary that
# contains (i, i x i) such that is an integral number between 1 and n (both included). and then the program should
# print the dictionary.Suppose the following input is supplied to the program: 8
#
# Then, the output should be:
#
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

given_number = -1


def number_and_output_of_multiplication(number):
	results = {}
	if number <= 0:
		print('Give a positive number')
	for num in range(1, number + 1):
		results.update({num: num * num})
	return results


print(number_and_output_of_multiplication(given_number))
