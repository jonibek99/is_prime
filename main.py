def is_prime(n):
    """
    Return True if n is prime, False otherwise.

    Args:
        n: int
    Returns:
        bool
    """
    if n%n!=0 and n%n==1:
        return True
    return False
print(is_prime(int(input())))