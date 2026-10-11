# Q2. Find Largest, Second Largest, Smallest and Second Smallest

n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))

unique = sorted(set(arr))

if len(unique) < 2:
    print("Enter at least two different elements.")
else:
    print("Largest:", unique[-1])
    print("Second Largest:", unique[-2])
    print("Smallest:", unique[0])
    print("Second Smallest:", unique[1])
