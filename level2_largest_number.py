# Level 2: Find the largest number in a list

def find_largest(numbers):
    """Return the largest number in a list."""
    if not numbers:
        return None
    largest = numbers[0]
    for num in numbers[1:]:
        if num > largest:
            largest = num
    return largest

# Example usage
data = [23, 24, 74, 89, 34]
print(f"Largest number: {find_largest(data)}")
