import pytest
from src.string_reversal import reverse_string_inplace

def test_basic_reversal():
    """Test reversing a typical string."""
    chars = list("hello")
    reverse_string_inplace(chars)
    assert chars == list("olleh")

def test_empty_list():
    """Test empty list handling."""
    chars = []
    reverse_string_inplace(chars)
    assert chars == []

def test_single_character():
    """Test single character list."""
    chars = ['a']
    reverse_string_inplace(chars)
    assert chars == ['a']

def test_even_length_string():
    """Test string with even number of characters."""
    chars = list("python")
    reverse_string_inplace(chars)
    assert chars == list("nohtyp")

def test_palindrome():
    """Test palindrome string remains unchanged when reversed."""
    chars = list("racecar")
    reverse_string_inplace(chars)
    assert chars == list("racecar")

def test_mixed_characters():
    """Test string with mixed case and special characters."""
    chars = list("A!b@C")
    reverse_string_inplace(chars)
    assert chars == list("C@b!A")

def test_invalid_input_type():
    """Test that TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list of characters"):
        reverse_string_inplace("not a list")
    
    with pytest.raises(TypeError, match="Input must be a list of characters"):
        reverse_string_inplace(123)

def test_mutability():
    """Ensure the function modifies the original list."""
    original = list("modify")
    chars = original.copy()
    reverse_string_inplace(chars)
    assert chars != original  # Ensure the list was modified
    assert chars == list("yfidom")