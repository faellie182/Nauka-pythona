# 5. Question:
# Define a class which has at least two methods:
#
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.


class Smth:

  def __init__(self):
    self.name = self
    self.users_input = str(input('Please enter a string: '))

  def get_string(self, users_input):
    self.users_input = str(input('Please enter a string: '))

  def print_String(self):
    str_uppercase = self.users_input.upper()
    return str_uppercase


smth = Smth()
print(smth.print_String())
somth = str(smth.print_String())


def test(sm):
  print(f'Test: is every letter in uppercase? {sm.isupper()}')


test(somth)
