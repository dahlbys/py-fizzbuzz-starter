import pytest
from fizzbuzz import fizzbuzz, generate_sequence


def test_fizzbuzz_returns_number_for_non_multiple():
    """Test that numbers not divisible by 3 or 5 are returned as strings."""
    assert fizzbuzz(1) == "1"
    assert fizzbuzz(2) == "2"
    assert fizzbuzz(4) == "4"


def test_fizzbuzz_returns_fizz_for_multiple_of_3():
    """Test that multiples of 3 return 'Fizz'."""
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(6) == "Fizz"
    assert fizzbuzz(9) == "Fizz"


def test_fizzbuzz_returns_buzz_for_multiple_of_5():
    """Test that multiples of 5 return 'Buzz'."""
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(10) == "Buzz"
    assert fizzbuzz(20) == "Buzz"


def test_fizzbuzz_returns_fizzbuzz_for_multiple_of_15():
    """Test that multiples of both 3 and 5 return 'FizzBuzz'."""
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(30) == "FizzBuzz"
    assert fizzbuzz(45) == "FizzBuzz"


def test_generate_sequence_returns_list():
    """Test that generate_sequence returns a list."""
    result = generate_sequence(5)
    assert isinstance(result, list)


def test_generate_sequence_length():
    """Test that generate_sequence returns correct number of elements."""
    assert len(generate_sequence(5)) == 5
    assert len(generate_sequence(100)) == 100


def test_generate_sequence_contains_correct_values():
    """Test that generate_sequence contains correct fizzbuzz values."""
    result = generate_sequence(15)
    assert result[0] == "1"
    assert result[2] == "Fizz"
    assert result[4] == "Buzz"
    assert result[14] == "FizzBuzz"


def test_generate_sequence_100_elements():
    """Test that generate_sequence(100) works correctly."""
    result = generate_sequence(100)
    assert len(result) == 100
    assert result[0] == "1"
    assert result[99] == "Buzz"
