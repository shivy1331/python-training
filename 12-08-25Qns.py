# 1. Unique Elements Function

def unique_elements(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

print(unique_elements([1, 2, 2, 3, 4, 1, 5]))  

# 2. List Rotation

def rotate_list(lst, k):
    k = k % len(lst) 
    return lst[-k:] + lst[:-k]

print(rotate_list([1, 2, 3, 4, 5], 2))  

# 3. Find Longest Word

def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)

print(longest_word("Python is an amazing programming language"))  


# 4. Sum of Digits Function

def sum_of_digits(num):
    return sum(int(digit) for digit in str(abs(num)))  

print(sum_of_digits(12345))  

# 5. Character Frequency Counter

def char_frequency(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

print(char_frequency("hello"))

# 1. Numbers Divisible by 3 or 5

for i in range(1, 101):
    if (i % 3 == 0 or i % 5 == 0) and not (i % 3 == 0 and i % 5 == 0):
        print(i, end=" ")

for i in range(1, 16):
    if (i % 3 == 0 or i % 5 == 0) and not (i % 3 == 0 and i % 5 == 0):
        print(i, end=" ")
        
# 2. Reverse Words in a Sentence

sentence = "Python is fun"
word = ""
words = []

for char in sentence:
    if char == " ":
        words.append(word)
        word = ""
    else:
        word += char
words.append(word)


reversed_sentence = ""
for i in range(len(words) - 1, -1, -1):
    reversed_sentence += words[i]
    if i != 0:
        reversed_sentence += " "

print(reversed_sentence)


# 3. Star Diamond Pattern

n = 5

for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
    
# 4. Count Consonants in a String

string = "hello world"
count = 0
vowels = "aeiouAEIOU"

for char in string:
    if char.isalpha() and char not in vowels:
        count += 1

print(count)  


# 5. Number Guessing Game

secret_number = 8

while True:
    guess = int(input("Guess the number: "))
    if guess == secret_number:
        print("Correct! You guessed it.")
        break
    else:
        print("Wrong, try again.")
