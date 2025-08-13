# oops ->
# Oops is programming paradigm that structures code around ob

# classes ->
# class is a blueprint for creating objects

# objects ->
# object is an instance of a class

# methods ->
# method is a function defined inside a class

# variables/attributes ->
# variable is a named storage for data
# attribute is a variable that belongs to an object

# encapsulation ->
# encapsulation is the bundling of data with methods that operate on that data

# inheritance ->
# inheritance is a mechanism where a new class can inherit 

# polymorphism ->
# polymorphism is the ability to present the same interface for different data types

# abstracting ->
# abstracting is the process of hiding the complex implementation details and showing only the essential features of the object

# class student
# student1 = {'name': 'rohan', 'age': 17, 'course': 'Mern'}
# student2 = {'name': 'amit', 'age': 18, 'course': 'Mern'}
# student3 = {'name': 'rav', 'age': 19, 'course': 'Mern'}
# student4 = {'name': 'rak', 'age': 16, 'course': 'Mern'}

# inheritance
#parent class and child class
#class ParentClass:
 #   pass
#class ChildClass(ParentClass):
  #  pass
class Grandfather:
    def _init_(self):
        self.hobby = "Reading the news"
    def speak(self):
        print("I am Grandfather. Hobby:", self.hobby)

class Father(Grandfather):
    def _init_(self):
        super()._init_()
        self.job = "Engineer"
    def speak(self):
        print("I am Father. Job:", self.job)

class Child(Father):
    def _init_(self):
        super()._init_()
        self.school = "ABC School"
    def speak(self):
        print("I am Child. School:", self.school)

# Create objects and call methods
gf = Grandfather()
gf.speak()

ft = Father()
ft.speak()

ch = Child()
ch.speak()
