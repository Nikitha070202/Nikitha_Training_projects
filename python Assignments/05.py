#Common elements from the two lists and returns in the another list
def common_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return list(set1 & set2)

# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [3, 5, 7, 9, 11]
common = common_elements(list1, list2)
print(common)  # Output
