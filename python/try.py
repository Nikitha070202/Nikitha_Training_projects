#while True:
   # try:
       # numerator = float(input("Enter the numerator: "))
       # denominator = float(input("Enter the denominator: "))
      #  result = numerator / denominator
       # print(f"{numerator} / {denominator} = {result}")
      #  break
   # except ZeroDivisionError:
    #    print("Error: Denominator cannot be zero. Please enter a non-zero value for the denominator.")'''
     #  ''' //A simple example of a lambda function that squares a number:'''

#square = lambda x: x**2
#result1=int(input("Enter a number"))
# call the lambda function
#result = square(result1)

# print the result
#print(result)
#//Python program that defines a class to represent a bank account:
#//This is just a simple example, and you can modify and customize the class and its methods to suit your needs.

class BankAccount:
    
    def __init__(self):
        self.balance = 0
    
    def deposit(self, amount):
        self.balance += amount
        print("Deposit of", amount, "completed.")
        
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("Withdrawal of", amount, "completed.")
        else:
            print("Insufficient balance.")
    
    def print_balance(self):
        print("Current balance:", self.balance)
#//Here, we define a class called BankAccount with an __init__ method to initialize the balance to 0. We then define three methods:

#deposit(amount): Adds the specified amount to the balance and prints a message confirming the deposit.
#withdraw(amount): Subtracts the specified amount from the balance if there is enough balance, and prints a message confirming the withdrawal. If there is not enough balance, it prints an error message.
#print_balance(): Prints the current balance.

#//We can create an instance of the BankAccount class and call its methods like this:
# create an instance of BankAccount
account = BankAccount()

# deposit some money
account.deposit(1000)

# withdraw some money
account.withdraw(500)

# try to withdraw more money than the balance
account.withdraw(300)

# print the balance
account.print_balance()






