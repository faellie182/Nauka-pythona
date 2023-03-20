# Question 77
# Question
# Please write a program to print the running time of execution of "1+1" for 100 times.
from time import time


def time_add_100_times():
	start = time()
	for n in range(101):
		return 1 + 1
	stop = time()
	print(stop - start)


time_add_100_times()
