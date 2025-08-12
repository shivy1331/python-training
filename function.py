# function declaration
# def fun1():
#     print("Function 1 executed")
# # function calling
# fun1()

# function with parameters
# def add(a, b):
#     return a + b
# print("Addition of a+b is:",add(5, 10))

# take input from user
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# def multiply(x, y):
#     return x * y 
# print("Multiplication of a*b is:", multiply(a, b))

# userName = input("Enter your name: ")
# def greet(name):
#     print("Hello, " + name + "! Welcome to the Python world.")  
# greet(userName)

# types of function 
# 1. Built-in function -> print(), type(), len(), etc.
# 2. User-defined function -> greet()
# 3. Lambda function/anonymous function

# lambda function
x = int(input("Enter a number: "))
square = lambda x: x * x
print("Square of", x, "is:", square(x))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
multiply = lambda x, y: x * y
print("Multiplication of", a, "and", b, "is:", multiply(a, b))
