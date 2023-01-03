# is prime

Objective: The objective of this assignment is to write a program that determines whether a number is prime or not. A prime number is a number that is only divisible by itself and 1. For example, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53.

## Problem statement

Define a function named `is_prime` that takes a single integer argument and returns `True` if the argument is a prime number, or `False` otherwise. If the argument is less than 2, the function should return `False`.

```python

def is_prime(n: int) -> bool:
    """
    Return True if n is prime, False otherwise.
    args:
        n: int
    returns:
        bool
    """
    pass

```

Example:

```python
is_prime(2)  # True
is_prime(3)  # True
is_prime(4)  # False
```

## Instructions

1. Fork this repository.
2. Clone your fork.
3. Activate github actions on your fork.
4. Add secret key.

## Constraints

1. 1 <= n <= 1000 (n is an integer)

