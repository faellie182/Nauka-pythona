# Question 16 Question: Use a list comprehension to square each odd number in a list. The list is input by a sequence
# of comma-separated numbers. >Suppose the following input is supplied to the program:

# 1,2,3,4,5,6,7,8,9
# Then, the output should be:

# 1,9,25,49,81

users_input = input(
  'Give a sequence of comma-separated numbers to square each odd number in a list. '
)
users_list_str = users_input.split(',')
users_list_int = [int(i) for i in users_list_str]
odd_list = [i for i in users_list_int if i % 2 != 0]
odd_list_square = [i * i for i in odd_list]
print(odd_list_square)
