import pytest
from src.count_matching_elements import count_matching_elements

def test_basic_matching():
    """Test basic matching of elements"""
    assert count_matching_elements([1, 2, 3], [3, 4, 5]) == 1

def test_multiple_matches():
    """Test multiple matching elements"""
    assert count_matching_elements([1, 2, 3, 2], [2, 3, 4, 5]) == 3

def test_no_matches():
    """Test when no elements match"""
    assert count_matching_elements([1, 2, 3], [4, 5, 6]) == 0

def test_empty_arrays():
    """Test with empty arrays"""
    assert count_matching_elements([], [1, 2, 3]) == 0
    assert count_matching_elements([1, 2, 3], []) == 0

def test_identical_arrays():
    """Test when both arrays are identical"""
    assert count_matching_elements([1, 2, 3], [1, 2, 3]) == 3

def test_invalid_input_types():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        count_matching_elements("not a list", [1, 2, 3])
    with pytest.raises(TypeError):
        count_matching_elements([1, 2, "3"], [1, 2, 3])
    with pytest.raises(TypeError):
        count_matching_elements([1, 2, 3], "not a list")

def test_repeated_elements():
    """Test behavior with repeated elements"""
    assert count_matching_elements([1, 1, 2, 2, 3], [1, 2, 4]) == 4