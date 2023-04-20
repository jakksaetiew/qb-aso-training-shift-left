from typing import List


def reverse_list(lst: List[int]) -> List[int]:
    """
    Reverses the order of elements in a list.

    Args:
        lst: A list of integers.

    Returns:
        A new list with the same elements as `lst`, but in reverse order.
    """
    return lst[::-1]


def sum_squares(n: int) -> int:
    """
    Returns the sum of the squares of the first `n` natural numbers.

    Args:
        n: The number of natural numbers to sum the squares of.

    Returns:
        The sum of the squares of the first `n` natural numbers.
    """
    return sum(i**2 for i in range(1, n + 1))


def is_palindrome(word: str) -> bool:
    """
    Determines whether a word is a palindrome.

    Args:
        word: A string representing a word.

    Returns:
        `True` if `word` is a palindrome, `False` otherwise.
    """
    return word == word[::-1]
