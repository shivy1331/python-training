# class Animal:
#     def speak(self):
#         return "Animal Speaks" # overrided method
    
# class Dog:
#     def speak(self):
#         return "woof"
    
# class Cat:
#     def speak(self):
#         return "meow"
    
# # Dogesh1 = Dog()
# # print(Dogesh1.speak()) 

# animals = [Dog(), Cat()]

# for i in animals:
#     print(i.speak());

class Calculator:
    def add(self, a, b):
        print(a + b)
    
    def add(self, a, b, c=0):
        print(a + b + c)
    
    def add(self, a, b, c=0, d=0):
        print(a + b + c + d)

C1 = Calculator()
C1.add(2,4)
