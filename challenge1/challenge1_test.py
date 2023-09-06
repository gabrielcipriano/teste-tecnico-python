from challenge1 import number_fractions

def test_positive_negative_zeros():
    nums = [-4, 3, -9, 0, 4, 1]
    result = number_fractions(nums)
    expected = {
        "positives": 0.5,
        "negatives": 0.333333,
        "zeros": 0.166667
    }
    assert result == expected

def test_all_zeros():
    nums = [0, 0, 0]
    result = number_fractions(nums)
    expected = {
        "positives": 0.0,
        "negatives": 0.0,
        "zeros": 1.0
    }
    assert result == expected

def test_empty_input():
    nums = []
    result = number_fractions(nums)
    expected = {
        "positives": 0.0,
        "negatives": 0.0,
        "zeros": 0.0
    }
    assert result == expected

def test_large_numbers():
    nums = [10**6, -10**6, 0, 10**6, -10**6]
    result = number_fractions(nums)
    expected = {
        "positives": 0.4,
        "negatives": 0.4,
        "zeros": 0.2
    }
    assert result == expected