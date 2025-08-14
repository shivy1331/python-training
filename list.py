#using square brackets
fruits = {'apple', 'banana', 'chery'}
print(fruits)

# using list function
fruits2 = list(('apple', 'banana', 'chery'))
print(fruits2)

#its supports minuse indexing also

# append method
fruits2.append("kiwi");
print(fruits2)

#add at specific postion
fruits2.insert(1,"orange")
print(fruits2)

#multiple element
fruits2.extend(["pineapple", "watermelon"])
print(fruits2)

#remove elements
#by value
fruits2.remove("apple")
print(fruits2)

#by index
fruits2.pop(2)
print(fruits2)

#by last element
fruits2.pop()
print(fruits2)

#delete entire list
# del fruits2
# print(fruits2)

#useful methods in list
numbers = [5,3,6,2,1,4]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)
