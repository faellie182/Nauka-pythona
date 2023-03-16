# Question 59
# Question
# Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).
# Example: If the following n is given as input to the program:
# 5
# Then, the output of the program should be:
# 3.55
# In case of input data being supplied to the question, it should be assumed to be a console input.


def equation_result(users_number):
	result = 0
	for n in range(1, users_number + 1):
		result += n / (n + 1)
	print(round(result, 2))


l = 5
equation_result(l)
