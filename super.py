# super() keyword is used to access method or variable from a parent class
# without directly naming the parent class
# it supports multiple inheritance through python mro

# super().method_name(arguments)

class parent:
    def __init__(self, name):
        self.name = name
        print("Parent__init__called")
    
class child(parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
        print("Chiled__it__called")

p1 = child("shivi", 25)
