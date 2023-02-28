# Question 10 Question Write a program that accepts a sequence of whitespace separated words as input and prints the
# words after removing all duplicate words and sorting them alphanumerically. Suppose the following input is supplied
# to the program: hello world and practice makes perfect and hello world again Then, the output should be: again and
# hello makes perfect practice world


def remove_dupl_sort_input():
	users_sentence = input('Give sequence of words, separated by whitespace: ')
	words = users_sentence.split()
	words.sort()
	words_sorted = []
	for w in words:
		if w in words_sorted:
			pass
		else:
			words_sorted.append(w)
	for word in words_sorted:
		print(word, end=' ')


remove_dupl_sort_input()
