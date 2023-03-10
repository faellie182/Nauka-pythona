# Question 18 Question: A website requires the users to input username and password to register. Write a program to
# check the validity of password input by users. Following are the criteria for checking the password: At least 1
# letter between [a-z] At least 1 number between [0-9] At least 1 letter between [A-Z] At least 1 character from [
# $#@] Minimum length of transaction password: 6 Maximum length of transaction password: 12 Your program should
# accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that
# match the criteria are to be printed, each separated by a comma. Example If the following passwords are given as
# input to the program: ABd1234@1,a F1#,2w3E*,2We3345 Then, the output of the program should be: ABd1234@1

users_passwords = input(
	'Give your pottential passwords, ones that match our criteria will be shown. '
)


def password_checker(input_pot_pass):
	symbols = ['$', '#', '@']
	list_of_pot_pass = input_pot_pass.split(',')
	for password in list_of_pot_pass:
		symbol_counter = 0
		letter_counter = 0
		number_counter = 0
		upper_counter = 0
		for letter in password:
			if letter.isalpha():
				letter_counter += 1
				if letter.isupper():
					upper_counter += 1
				else:
					pass
			elif letter.isdigit():
				number_counter += 1
			elif letter in symbols:
				symbol_counter += 1
		if symbol_counter != 0 and letter_counter != 0 and number_counter != 0 and upper_counter != 0 and 6 <= len(
						password) <= 12:
			print(password)


password_checker(users_passwords)

# a = ['A', 'b', 'C']
# counter = 0
# for i in a:
#   for l in i:
#     if l == l.upper():
#       counter += 1
# print(counter)
