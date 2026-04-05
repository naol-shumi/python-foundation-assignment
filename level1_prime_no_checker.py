# Level 1: Check if a number is prime

def is_prime(n):
    """
    Return True if n is a prime number, else False.
    A prime number is greater than 1 and divisible only by 1 and itself.
    """

    # Step 1: Handle numbers less than or equal to 1
    # These are not prime by definition
    if n <= 1:
        return False

    # Step 2: Check divisors from 2 up to sqrt(n)
    # If n has a divisor in this range, it's not prime
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:  # If divisible evenly, not prime
            return False

    # Step 3: If no divisors found, n is prime
    return True

# Example usage
num = 45  # Test number
print(f"{num} is prime? {is_prime(num)}")
