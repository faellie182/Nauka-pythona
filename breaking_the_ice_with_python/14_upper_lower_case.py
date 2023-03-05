# Question 14
# Question:
# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

# Suppose the following input is supplied to the program:

# Hello world!
# Then, the output should be:

# UPPER CASE 1
# LOWER CASE 9

users_sentence = input(
	'Give a sentence to calculate numbers of upper case letters and lower case letters. '
)
upper = 0
lower = 0
for l in users_sentence:
	if l.isupper():
		upper += 1
	if l.islower():
		lower += 1
print(f'UPPER CASE {upper} \n LOWER CASE {lower}')
