def sumOfSquares(nums):
    total = 0
    n = len(nums)

    for i in range(n):
        if n % (i + 1) == 0:
            total += nums[i] ** 2

    return total

print(sumOfSquares([2,4,8,5])) #Output: 4%1==0, 4%2==0, 4%3!=0, 4%4==0 => 2^2 + 4^2 + 5^2 = 4 + 16 + 25 = 45