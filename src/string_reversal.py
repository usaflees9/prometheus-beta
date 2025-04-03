def reverse_string_inplace(s: list[str]) -> None:
    """
    Reverse a string in-place with O(1) space complexity.
    
    This function modifies the input list of characters directly,
    swapping characters from the start and end of the list until 
    the entire string is reversed.
    
    Args:
        s (list[str]): A mutable list of characters to be reversed in-place.
    
    Time Complexity: O(n/2) = O(n), where n is the length of the string
    Space Complexity: O(1), as the reversal is done without additional space
    
    Raises:
        TypeError: If input is not a list
    
    Examples:
        >>> chars = list("hello")
        >>> reverse_string_inplace(chars)
        >>> chars
        ['o', 'l', 'l', 'e', 'h']
    """
    # Check for invalid input 
    if not isinstance(s, list):
        raise TypeError("Input must be a list of characters")
    
    # Handle empty or single-character lists
    if len(s) <= 1:
        return
    
    # Two-pointer approach to swap characters
    left, right = 0, len(s) - 1
    
    while left < right:
        # Swap characters
        s[left], s[right] = s[right], s[left]
        
        # Move pointers towards center
        left += 1
        right -= 1