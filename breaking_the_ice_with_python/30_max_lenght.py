# Question 30 Question: Define a function that can accept two strings as input and print the string with maximum
# length in console. If two strings have the same length, then the function should print all strings line by line.


def longer_string(text1, text2):
	print(
		'The output will be longer text, if they have the same lengh, then both of them will be shown.'
	)
	if len(text1) > len(text2):
		return text1
	elif len(text1) < len(text2):
		return text1
	else:
		return f'{text1} \n{text2}'


str1 = input('Give first text: ')
str2 = input('Give second text: ')
print(longer_string(str1, str2))
