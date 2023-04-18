#sum of all even numbers in the list 
numbers = input("Enter a list of numbers : ") #Enter the list from the user
num_list = numbers.split()
sum_even = 0
for num in num_list:
    if int(num) % 2 == 0:
        sum_even += int(num)
print("The sum of all even numbers in the list is:", sum_even) #prints the output
