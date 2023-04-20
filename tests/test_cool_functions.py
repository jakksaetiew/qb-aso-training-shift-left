from qb_aso_training_shift_left.cool_functions import (
    is_palindrome,
    reverse_list,
    sum_squares,
)


# Test reverse_list function
def test_reverse_list() -> None:
    # Test empty list
    reverse_list([]).should.equal([])

    # Test list with one item
    reverse_list([1]).should.equal([1])

    # Test list with even number of items
    reverse_list([1, 2, 3, 4]).should.equal([4, 3, 2, 1])

    # Test list with odd number of items
    reverse_list([1, 2, 3, 4, 5]).should.equal([5, 4, 3, 2, 1])


# Test sum_squares function
def test_sum_squares() -> None:
    # Test n = 0
    sum_squares(0).should.equal(0)

    # Test n = 1
    sum_squares(1).should.equal(1)

    # Test n = 2
    sum_squares(2).should.equal(5)

    # Test n = 5
    sum_squares(5).should.equal(55)


# Test is_palindrome function
def test_is_palindrome() -> None:
    # Test empty string
    is_palindrome("").should.equal(True)

    # Test single-character string
    is_palindrome("a").should.equal(True)

    # Test even-length palindrome
    is_palindrome("racecar").should.equal(True)

    # Test odd-length palindrome
    is_palindrome("level").should.equal(True)

    # Test non-palindrome
    is_palindrome("hello").should.equal(False)
