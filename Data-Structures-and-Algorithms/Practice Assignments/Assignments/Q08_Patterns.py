# Q8. Print the Given Patterns

print("Pattern 1:")
for i in range(3):
    print("   *")
print("*  *  *  *  *  *  *")
for i in range(3):
    print("   *")

print("\nPattern 2:")
for i in range(5):
    if i == 0 or i == 4:
        print("* * * * *")
    else:
        print("*       *")

print("\nPattern 3:")
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("*       *")
print(" *     *")
print("  *   *")
print("   * *")
print("    *")

print("\nPattern 4:")
for i in range(1, 6):
    print(" " * (5 - i) + " ".join(str(j) for j in range(1, i + 1)))

print("\nPattern 5:")
for i in range(5):
    print(" ".join(str((i + j) % 2) for j in range(5)))
