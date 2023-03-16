# Question 55 Question Write a program which accepts a sequence of words separated by whitespace as input to print
# the words composed of digits only. Example: If the following words is given as input to the program: 2 cats and 3
# dogs. Then, the output of the program should be: ['2', '3'] In case of input data being supplied to the question,
# it should be assumed to be a console input. Hints Use re.findall() to find all substring using regex.

from re import findall


def only_digits(text):
	numbers = findall('[0-9]+', text)
	print(numbers)


l = '2 cats and 3 dogs'
only_digits(l)

# bez sensu, bo findall wyszukuje w całym tekście, więc jakby było d0gs, to by w liście było też '0'
