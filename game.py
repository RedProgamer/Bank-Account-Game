print("\t\t\tWelcome to our Bank")
print("Press 1 to Check your balance.")
print("Press 2 to Check Details.")
print("Press 3 to Withdraw.")
print("Press 4 to Deposit.\n")

class Bank:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def check_balance(self):
        return self.balance

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
        return f'Your current balance is : ${self.balance}'

    def deposit(self, amount):
        self.balance += amount
        return f'Your current balance is : ${self.balance}'

    def __str__(self):
        return f'Owner : {self.name}\nBalance : ${self.balance}'



Condition = input("Do you want to perform any of these ?(y/n) : ").lower()

if Condition == 'y':
    Transaction = True
elif Condition == 'n':
    Transaction = False

while Transaction:
    user_name = input("Enter your name : ")
    balance = int(input("Enter your balance : "))

    Information = Bank(user_name, balance)
    
    user_input = int(input("Enter your requirements : "))

    while user_input not in [1,2,3,4]:
        user_input = int(input("Please! Choose a number : "))
        continue
    else:
        try:
            if user_input == 1:
                print(Information.check_balance())
            elif user_input == 2:
                print(Information)
            elif user_input == 3:
                withdraw = int(input("Enter the amount you want to withdraw : "))
                print(Information.withdraw(withdraw))    
            elif user_input == 4:
                deposit = int(input("Enter the amount you want to deposit : "))
                print(Information.deposit(deposit))
        finally:
            Condition = input("Do you want to do anything else : ").lower()
            if Condition == 'y':
                Transaction = True
            elif Condition == 'n':
                Transaction = False

print("Thanks for visiting the bank.")


