
def removeDuplicatesPreserveOrder(nums):
    return list(dict.fromkeys(nums))

print(removeDuplicatesPreserveOrder([1,2,3,2,1,4])) #[1, 2, 3, 4]