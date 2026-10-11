"""Small examples for DSA complexity practice."""


def find_max(values):
    """Return the maximum value. Time: O(n); auxiliary space: O(1)."""
    if not values:
        raise ValueError("values must not be empty")

    largest = values[0]
    for value in values[1:]:
        if value > largest:
            largest = value
    return largest


def reverse_copy(values):
    """Return a reversed copy. Time: O(n); extra space: O(n)."""
    return values[::-1]


def contains_value(values, target):
    """Linear search. Worst-case time: O(n); auxiliary space: O(1)."""
    for value in values:
        if value == target:
            return True
    return False


if __name__ == "__main__":
    data = [1, 4, 2, 3]
    print("Values:", data)
    print("Maximum:", find_max(data))
    print("Reversed copy:", reverse_copy(data))
    print("Contains 2:", contains_value(data, 2))
