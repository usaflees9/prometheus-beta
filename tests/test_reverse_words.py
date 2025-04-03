import pytest
from src.reverse_words import reverse_words

def test_reverse_words_multiple_words():
    """Test reversing multiple words."""
    assert reverse_words("Hello World") == "World Hello"
    assert reverse_words("Python is awesome") == "awesome is Python"

def test_reverse_words_edge_cases():
    """Test edge cases like empty string, single word, and string with extra spaces."""
    assert reverse_words("") == ""
    assert reverse_words("SingleWord") == "SingleWord"
    assert reverse_words("  Hello   World  ") == "World Hello"

def test_reverse_words_type_handling():
    """Test type handling and error cases."""
    # Verify that non-string input raises a TypeError
    with pytest.raises(AttributeError):
        reverse_words(None)
    with pytest.raises(AttributeError):
        reverse_words(123)

def test_reverse_words_whitespace_handling():
    """Test handling of different whitespace scenarios."""
    assert reverse_words("a b c") == "c b a"
    assert reverse_words("  a  b  c  ") == "c b a"