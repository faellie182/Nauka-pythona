# 2. Write a program which can compute the factorial of a given numbers.The results should be
# printed in a comma-separated sequence on a single line.Suppose the following input is supplied to the program: 8
# Then, the output should be:40320
import math

given_number = 8


def factorial(number):
	return math.factorial(number)


def factorial2(number):
	fact = 1
	for num in range(2, number + 1):
		fact *= num
	return fact


print(factorial(given_number))
print(factorial2(given_number))
