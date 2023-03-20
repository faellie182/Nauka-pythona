# Question 79 Question Please write a program to generate all sentences where subject is in ["I", "You"] and verb is
# in ["Play", "Love"] and the object is in ["Hockey","Football"].
import itertools


def all_posible_sentenc():
	subj = ["I", "You"]
	verb = ["Play", "Love"]
	sport = ["Hockey", "Football"]
	sentences = [subj, verb, sport]
	final_list = [
		"{} {} {}".format(*i) for i in itertools.product(*sentences, repeat=1)
	]
	print(final_list)


# def all_posible_sentenc2():
#   subj = ["I", "You"]
#   verb = ["Play", "Love"]
#   sport = ["Hockey", "Football"]
#   sentences = []
#   for s in subj:
#     sentence = []
#     if s not in sentence:
#       sentence.append(s)
#       for v in verb:
#         if v not in sentence:
#           sentence.append(v)
#           for p in sport:
#             if p not in sentence:
#               sentence.append(p)
#             sentences.append(sentence)
#     print(sentences)

all_posible_sentenc()
# all_posible_sentenc2()
