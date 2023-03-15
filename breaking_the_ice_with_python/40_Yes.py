# Question 40 Question: Write a program which accepts a string as input to print "Yes" if the string is "yes" or
# "YES" or "Yes", otherwise print "No".


def yes_or_no(users_input):
	if users_input == 'yes' or users_input == 'YES' or users_input == 'Yes':
		return 'Yes'
	else:
		return 'No'


users_unput1 = input(': ')
print(yes_or_no(users_unput1))
