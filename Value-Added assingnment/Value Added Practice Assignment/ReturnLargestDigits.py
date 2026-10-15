
def returnLargestDigit(n):
    return max(int(d) for d in str(n))

print(returnLargestDigit(5832))  # Output: 8