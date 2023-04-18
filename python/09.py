#square numbers 
def square_list(numbers):
    squared_numbers = [number**2 for number in numbers]
    return squared_numbers


numbers = [1, 2, 3, 4, 5] #Input
squared_numbers = square_list(numbers)
print(squared_numbers) #Output 
