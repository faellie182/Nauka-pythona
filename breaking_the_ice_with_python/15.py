# Question 15
# Question:
# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106

users_number = input('Give a number: ')
string = users_number
val_sum = int(users_number)
for i in range(0, 3):
	string += users_number
	val_sum += int(string)
print(val_sum)
