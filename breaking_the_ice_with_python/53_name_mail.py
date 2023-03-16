# Question 53
# Question
# Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the user name of a given email address. Both user names and company names are composed of letters only.
# Example: If the following email address is given as input to the program:
# john@google.com
# Then, the output of the program should be:
# john
# In case of input data being supplied to the question, it should be assumed to be a console input.
# Hints
# Use \w to match letters.


def extract_name(mail):
	name, rest = mail.split('@')
	company, com = rest.split('.')
	print(name.capitalize())
	print(company.capitalize())


l1 = 'john@google.com'
extract_name(l1)
l2 = input('Give an e-mail: ')
extract_name(l2)
