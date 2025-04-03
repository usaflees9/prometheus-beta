def reverse_words(input_string: str) -> str:
    """
    Reverse the order of words in a given string.

    Args:
        input_string (str): The input string to reverse.

    Returns:
        str: A new string with words in reverse order, separated by spaces.

    Examples:
        >>> reverse_words("Hello World")
        'World Hello'
        >>> reverse_words("Python is awesome")
        'awesome is Python'
        >>> reverse_words("")
        ''
        >>> reverse_words("SingleWord")
        'SingleWord'
    """
    # Handle empty string or single word cases
    if not input_string or len(input_string.split()) <= 1:
        return input_string
    
    # Split the string into words and reverse their order
    return " ".join(input_string.split()[::-1])