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

class Trial:
    @staticmethod
    def greet():
        print("hello ji")

    def speak(self):
        print("speak ji")

# obj = Trial();
Trial.speak("hello");
# obj.speak();
