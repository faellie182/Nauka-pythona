# 1. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a
# single line.

def all_num_div_by_7_not_multip_of_5(start, stop):
	for n in range(start, stop + 1):
		if n % 7 and n % 5 != 0:
			print(n, end=', ')


all_num_div_by_7_not_multip_of_5(2000, 3200)
