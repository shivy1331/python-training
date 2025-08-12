# there are two types of loops in Python:

# 1. for loop
# 2. while loop

# for loop
# for i in range(5):
#     print(i, end=' ')

# fruits = ['apple', 'banana', 'cherry']    
# for fruit in fruits:
#     print(fruit, end=" ")

# for i in range
# for i in range(1, 10):
#     print(i, end=" ")

# while loop
# i = 0
# while i < 5:
#     print(i, end=" ")
#     i += 1

# find the index of an item in a list using for loop
# fruits = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'mango']
# for fruit in fruits:
#     if fruit == 'banana':
#         print("Found banana at index", fruits.index(fruit))

# write a function to use for loop and calculate su of the numbers for 1 to n
num = int(input("Enter a number: "))
def sum_of_numbers(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum

print("The sum of numbers from 1 to", num, "is:", sum_of_numbers(num))

