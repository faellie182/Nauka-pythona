# Question: Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both
# included) and the values are square of keys

k = [n for n in range(1, 21)]


def square(numbers):
	dict1 = {}
	for i in numbers:
		dict1[i] = i * i
	return dict1


print(square(k))
