# Question 9 Question: Write a program that accepts sequence of lines as input and prints the lines after making all
# characters in the sentence capitalized. Suppose the following input is supplied to the program: Hello world
# Practice makes perfect Then, the output should be: HELLO WORLD PRACTICE MAKES PERFECT


def users_sentence_capit():
	users_sentence = []
	while True:
		users_line = input('Give sequence of lines to be capitalized: ')
		if users_line == '':
			break
		else:
			users_sentence.append(users_line.upper())
	for u in users_sentence:
		print(u)


users_sentence_capit()

# def users_sentence_capit():
#   users_sentence = []
#   while True:
#     try:
#       users_line = input('Give sequence of lines to be capitalized: ')
#       users_sentence.append(users_line)
#     except EOFError:
#       print(users_sentence)
#       break
