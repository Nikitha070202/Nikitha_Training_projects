
#Arranging the words in alphabetical order
my_str = "Hello ,Good Afternoon everyone" #Input
words = [word.lower() for word in my_str.split()]
words.sort()
print("The sorted words are:") 
for word in words:
   print(word) #prints the sorting order
