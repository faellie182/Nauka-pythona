# Question 25 Question: Define a class, which have a class parameter and have a same instance parameter. Hints:
# Define an instance parameter, need add it in __init__ method.You can init an object with construct parameter or set
# the value later


class Costam():
	name = 'Imie'

	def __init__(self, name=None):
		if name:
			self.name = name



cokolwiek = Costam()
print(cokolwiek.name)
cokolwiek2 = Costam('Fvfkdninv')
print(cokolwiek2.name)
