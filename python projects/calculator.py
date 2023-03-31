#Simple Calculator

#function to add two  numbers
def add(x, y):
    return x + y

#function to subtract two numbers
def subtract(x, y):
    return x - y

#function to find the product of two numbers
def multiply(x, y):
    return x * y

#function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Error: division by zero"
    else:
        return x / y

print("Simple Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

while True:
    choice = input("Enter your choice (1-4): ") #user selects the choice 

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: ")) #input from the user 
        num2 = float(input("Enter second number: "))  #input from the user 

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2)) # prints addition result

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2)) #prints subtraction result

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2)) #prints multiplication result

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))  #prints division result
        
        break
    else:
        print("Invalid input") #Prints invalid input if none of above conditons are satisfied
