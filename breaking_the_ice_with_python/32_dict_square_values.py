# Question 32 Question: Define a function which can generate a dictionary where the keys are numbers between 1 and 20
# (both included) and the values are square of keys. The function should just print the keys only.


def dic_square(range1, range2):
	numbers = [n for n in range(range1, range2 + 1)]
	dict1 = {}
	for i in numbers:
		dict1[i] = i * i
	print(dict1.keys())


dic_square(1, 20)
