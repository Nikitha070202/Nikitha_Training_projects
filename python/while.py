#i = 0
#while i < 5:
   # print(i)
   # i += 1
    
   # //Demo examples:List comprehension

#// Eg:1
# create a new list of squares of numbers from 1 to 10
'''squares = [i**3 for i in range(0, 12)]
print(squares) '''

# output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#//Eg:2
# create a new list of even numbers from an existing list
'''numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [i for i in numbers if i % 2 == 0]
print(evens)'''


#//Eg:3
# create a new list of strings, where each string is the original string capitalized
'''words = ['apple', 'banana', 'cherry', 'date']
capitalized = [word.capitalize() for word in words]
print(capitalized) '''

#//example of a simple decorator that prints a message before and after 

'''def my_decorator(func):
    def wrapper():
        print("Before function is called.")
        func()
        print("After function is called.")
        
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

# calling the decorated function
say_hello()


numbers = [11, 22, 33, 44, 55, 66, 77, 88, 99, 100]
print("List of numbers:")
print(numbers)
print("\nList of even numbers:")
evenNumbers = list(filter(lambda x: x%2 == 0, numbers))
print(evenNumbers)
print("\nList Odd numbers:")
oddNumbers = list(map(lambfilter(lambda x: x%2 != 0, numbers))
print(oddNumbers)'''

'''lst = [2,3,1,4,7,6,8]
# Use a lambda function to filter out even numbers
Even_num = list(filter(lambda x: x % 2 == 0, lst))


# Use a list comprehension to double the remaining odd numbers
Odd_num = [x * 2 for x in Even_num]

print(Odd_num) '''

'''import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time} seconds to execute.")
        return result
    return wrapper

@time_it
def my_function():
    # the code to be timed goes here
    pass

# call the function to test the decorator
my_function()'''

'''import time

def timer(func):
    def wrapper():
        start_time=time.time()
        func()
        end_time=time.time()
        print("The function ends in",(end_time-start_time)," seconds")
    return wrapper


@timer
def function():
    time.sleep(2)
    
function()'''

file=open('abc.txt','r')




    






