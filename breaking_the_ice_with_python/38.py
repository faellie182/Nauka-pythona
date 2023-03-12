# Question 38 Question: With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in
# one line and the last half values in one line.


def tuple_divided(users_tuple):
	list1 = []
	list2 = []
	middle_index = int((len(users_tuple)) / 2)
	for i in list(users_tuple):
		if i < users_tuple[middle_index]:
			list1.append(i)
		else:
			list2.append(i)
	tuple1 = tuple(list1)
	tuple2 = tuple(list2)
	return f'{tuple1} \n{tuple2}'


tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(tuple_divided(tup))
