# Question 21 Question: A robot moves in a plane starting from the original point (0,0). The robot can move toward
# UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following: UP 5 DOWN 3
# LEFT 3 RIGHT 2 The numbers after the direction are steps. Please write a program to compute the distance from
# current position after a sequence of movement and original point. If the distance is a float, then just print the
# nearest integer. Example: If the following tuples are given as input to the program: UP 5 DOWN 3 LEFT 3 RIGHT 2
# Then, the output of the program should be: 2 Hints: In case of input data being supplied to the question,
# it should be assumed to be a console input. Here distance indicates to euclidean distance. Import math module to
# use sqrt function.
from math import sqrt

point = [0, 0]
moves = []
while True:
	console = input(
		'Move: which way and after space number of steps in this direction. ')
	if console == '':
		break
	moves.append(console)
# print(moves)
for m in moves:
	m_div = m.split(' ')
	if m_div[0] == 'UP':
		point[0] += int(m_div[1])
	elif m_div[0] == 'DOWN':
		point[0] -= int(m_div[1])
	elif m_div[0] == 'LEFT':
		point[1] += int(m_div[1])
	elif m_div[0] == 'RIGHT':
		point[1] -= int(m_div[1])
# print(point)
distance = sqrt(point[0] ** 2 + point[1] ** 2)
print(int(distance))
