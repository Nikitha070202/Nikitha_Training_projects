#Removing the vowels from the words
string=input("Enter the string") #Enter the string 
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
result = ""

for i in range(len(string)): #using for loop
    if string[i] not in vowels:
        result = result + string[i]
#prints the result
print("\nAfter removing Vowels: ", result)