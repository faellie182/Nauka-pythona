# Question: Write a program that computes the net amount of a bank account based a transaction log from console
# input. The transaction log format is shown as following: D 100 W 200 D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program: D 300 D 300 W 200 D 100 Then, the output should be: 500
log_str = []
net_amount = 0
while True:
	users_transaction = input('Transaction log: ')
	if users_transaction == '':
		break
	log_str.append(users_transaction)
log_str_div = []
for l in log_str:
	log_str_div = l.split(' ')
	if log_str_div[0] == 'D':
		net_amount += int(log_str_div[1])
	elif log_str_div[0] == 'W':
		net_amount -= int(log_str_div[1])
print(net_amount)
