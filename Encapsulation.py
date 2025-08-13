# class BankAccount:
#     def __init__(self, name, balance, pin):
#         self.AccountHolderName = name
#         self.__balance = balance #private
#         self.__pin = pin

#     def __str__(self):
#         return f"Account Holder Name:{self.AccountHolderName}"
    
#     # getter
#     def getBalance(self, pin):
#         if pin == self.__pin:
#             return self.__balance
#         return "Invalid pin or BankAccount"
    
#     # setter
#     def depositBalance(self, amount):
#         if amount >= 0:
#             self.__balance += amount
#             return "Balance has been updated"
#         return "Invalid Amount"

# b1 = BankAccount("shivi", 50000, 12345)

# print(b1.getBalance(12345))


# By myself
# class BankAccount:
#     def __init__(self, name, balance, AccountNo):
#         self.name = name
#         self.balance = balance
#         self.AccountNo = AccountNo
    
#     def __str__(self):
#         return f"Account Holder Name{self.name}, balance:{self.balance}, Account No: {self.AccountNo}"
    
# b1 = BankAccount('shivam', 6000000, 12345)
# print(b1.name)
# print(b1.balance)
# print(b1.AccountNo)


# ChatGpt
class Customer:
    def __init__(self, name, age, address, phone, email, account_number, balance=0):
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone
        self.email = email
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully. New balance: ₹{self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"₹{amount} withdrawn successfully. New balance: ₹{self.balance}")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    def display_details(self):
        print("\n--- Customer Details ---")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")
        print(f"Phone: {self.phone}")
        print(f"Email: {self.email}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: ₹{self.balance}")


# Create customer from user input
print("Enter Customer Details:")
name = input("Name: ")
age = int(input("Age: "))
address = input("Address: ")
phone = input("Phone: ")
email = input("Email: ")
account_number = input("Account Number: ")
balance = float(input("Initial Balance: "))

customer = Customer(name, age, address, phone, email, account_number, balance)

# Menu for operations
while True:
    print("\n--- Bank Menu ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. View Details")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        customer.deposit(amount)

    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))
        customer.withdraw(amount)

    elif choice == "3":
        customer.display_details()

    elif choice == "4":
        print("Thank you for banking with us!")
        break

    else:
        print("Invalid choice. Please try again.")
