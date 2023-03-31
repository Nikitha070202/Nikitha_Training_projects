'''#prints only the palindromes in the list
def palindromes(strings):
    palindromes = []
    for string in strings:
        if string == string[::-1]:
            palindromes.append(string)
    return palindromes


strings = ["window", "level", "python", "madam", "civic"] #Input
palindromes = palindromes(strings)
print(palindromes) #output'''

#//Demo Example of file handling in Python that demonstrates how to open a file, read its contents, and write to it:

# Opening a file
file = open('abc.txt', 'r')
print(file)

# Reading from a file
content = file.read()
print(content)

# Closing a file
file.close()

# Writing to a file
with open('demo.txt', 'a') as file:
    file.write('Nikitha')

# Reading from a file again
with open('demos.txt', 'r') as file:
    content = file.read()
    print(content)
