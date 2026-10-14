
def findCommonElements(list1, list2):
    return sorted(set(list1) & set(list2))


list1 = [1, 2, 3, 4]
list2 = [2, 3, 5, 6]

print(findCommonElements(list1, list2))
