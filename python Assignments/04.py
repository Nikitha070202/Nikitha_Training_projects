#Median number in the list 
def median(data): 
    sorted_data = sorted(data)
    data_len = len(sorted_data)

    middle = (data_len - 1) // 2

    if middle % 2:
        return sorted_data[middle]
    else:
        return (sorted_data[middle] + sorted_data[middle + 1]) / 2.0
numbers = [1, 2, 3, 4, 5, 6, 7]
med = median(numbers)
#prints the median value
print(med)