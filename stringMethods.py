s = "Hello"
print(len(s))

s = "hello"
print(s.upper())

s = "HELLO"
print(s.lower())

s = "python"
print(s.capitalize())

s = "hello world"
print(s.title())

s = "Hello World"
print(s.swapcase())

s = "  hello  "
print(s.strip())

s = "  hello"
print(s.lstrip())

s = "hello  "
print(s.rstrip())

s = "I like Java"
print(s.replace("Java", "Python"))

s = "Python"
print(s.startswith("Py"))

s = "Python"
print(s.endswith("on"))

s = "Hello World"
print(s.find("o"))

s = "Hello World"
print(s.rfind("o"))

s = "Hello World"
print(s.index("World"))

s = "banana"
print(s.count("a"))

s = "apple,banana,orange"
print(s.split(","))

s = "one two three"
print(s.rsplit(" ", 1))

s_list = ["2025", "08", "11"]
print("-".join(s_list))

s = "Hello"
print(s.isalpha())

s = "12345"
print(s.isdigit())

s = "Hello123"
print(s.isalnum())

s = "   "
print(s.isspace())

s = "hello"
print(s.islower())

s = "HELLO"
print(s.isupper())
