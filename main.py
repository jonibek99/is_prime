def is_prime(n):
    """
    Return True if n is prime, False otherwise.

    Args:
        n: int
    Returns:
        bool
    """
    if not n%2!=0:
        return False

    return True
print(is_prime(int(input())))