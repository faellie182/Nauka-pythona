# Question 13
# Question:
# Write a program that accepts a sentence and calculate the number of letters and digits.

# Suppose the following input is supplied to the program:

# hello world! 123
# Then, the output should be:

# LETTERS 10
# DIGITS 3

users_sentence = input(
	'Give a sentence to sum up number od letters and digits in it. ')
# 1:
digits0 = sum(n.isdigit() for n in users_sentence)
letters0 = sum(n.isalpha() for n in users_sentence)
print(f' LETTERS: {letters0} \n DIGITS {digits0}')

# 2:
digits = 0
letters = 0
for i in users_sentence:
	if i.isdigit():
		digits += 1
	if i.isalpha():
		letters += 1
print(f' LETTERS: {letters} \n DIGITS {digits}')

