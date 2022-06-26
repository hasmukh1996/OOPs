# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
'''''''''''
# OOPs

class Percentage:
    "SSC 2022 Result"
    def __init__(self,Name,Maths,SS,Science,English):
        self.Name = Hasmukh
        self.Maths = Maths
        self.SS = SS
        self.Science = Science
        self.English = English

Result = SSC("Hasmukh",90,85,90,31)


print(Hasmukh)
'''''''''''
class Fruit:
    def __init__(self):
        self.name = "apple"
        self.color = "red"
my_fruit = Fruit()
print(my_fruit.color)


class Fruit:
    def __init__(self,name,color):
        self.name = name
        self.color = color
    def details(self):
        exp_date = "26.06.2022"
        print("my " + self.name + "  is  " + self.color)
        print("expires on " + exp_date)
apple = Fruit("apple","red")
apple.details()


# define parent class
class Guitar:
    def __init__(self, n_strings=6):
        self.n_strings = n_strings
        self.play()
        self.__cost = 50 #private member
    def play(self):
        print("pam pam pam pam pam pam pam")

# use parent class to make a child class
class BassGuitar(Guitar):
    pass

# use parent class to make a child class
# make adjustments
class ElectricGuitar(Guitar):
    def __init__(self):
        # access __init__ method of parent function
        super().__init__(n_strings = 8)
        self.colour = ("#000000", "#FFFFFF")
    def playLouder(self):
        print("pam pam pam pam pam pam pam".upper())
    # private method
    def __secret(self):
        # access private member of the parent class
        print("this guitar actually cost me $", self._Guitar__cost, "only!")

# create an object
my_guitar = ElectricGuitar()
# call a class method
my_guitar.playLouder()
# call a private class method
my_guitar._ElectricGuitar__secret()
# verify n_strings across different objects
print("my bass guitar has", BassGuitar(4).n_strings, "strings")
print("my electric guitar has", my_guitar.n_strings, "strings")