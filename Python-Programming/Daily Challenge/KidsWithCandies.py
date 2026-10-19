
def kidsWithCandies(candies: list[int], extraCandies: int) -> list[bool]:
    return [c + extraCandies >= max(candies) for c in candies]

print(kidsWithCandies([3, 1, 2, 5, 3], 3))  # Output: [True, False, False, True, True]
print(kidsWithCandies([4, 2, 1, 1, 2], 1))  # Output: [True, False, False, False, False]