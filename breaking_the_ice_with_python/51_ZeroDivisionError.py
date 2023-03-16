# Question 51
# Question
# Write a function to compute 5/0 and use try/except to catch the exceptions.


def div(num1, num2):
	try:
		print(num1 / num2)
	except ZeroDivisionError:
		print('Cannot divide by zero!')


div(5, 0)
