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
# num = int(input("Enter a number: "))
# def sum_of_numbers(n):
#     sum = 0
#     for i in range(1, n + 1):
#         sum += i
#     return sum

# print("The sum of numbers from 1 to", num, "is:", sum_of_numbers(num))

# write a function to count_vowels in a string using for loop
# def count_vowels(s):
#     count = 0
#     vowels = 'aeiou'
#     for char in s:
#         if char in vowels:
#             count += 1  
#     return count
# print("Number of vowels in the string:", count_vowels("Hello"))

# list square
# def list_square(list1):
#     list2 = []
#     for i in list1:
#         list2.append(i ** 2)
#     print("List of squares:", list2)

# list_square([2,5,6, 7, 8])

# reverse a string using for loop
# def reverse_string(s):
#     reversed_str = ''  
#     for char in s:
#         reversed_str = char + reversed_str # h + "" + e + h, so on
#     return reversed_str

# print("Reversed string:", reverse_string("Hello World"))

# words length
# def words_length(s):
#     revStr = ""
#     for word in s:
#         revStr += str(len(word)) + " "
#     print("Length of each word:", revStr.strip())

# words_length(["Hello", "World", "Python", "Programming"])

# else clause in for loop
for i in range(5):
    if i == 3:
        print("Breaking the loop at i =", i)
        break
    print(i)
else:
    print("Loop completed without break")  # This will execute after the loop finishes normally
