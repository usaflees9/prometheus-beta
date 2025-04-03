def count_matching_elements(arr1, arr2):
    """
    Count the number of elements in the first array that are also present in the second array.

    Args:
        arr1 (List[int]): The first input array of integers
        arr2 (List[int]): The second input array of integers

    Returns:
        int: Number of elements from arr1 that are also in arr2

    Raises:
        TypeError: If input arguments are not lists of integers
    """
    # Type checking
    if not (isinstance(arr1, list) and isinstance(arr2, list)):
        raise TypeError("Both arguments must be lists")
    
    # Validate input elements are integers
    if not (all(isinstance(x, int) for x in arr1) and 
            all(isinstance(x, int) for x in arr2)):
        raise TypeError("All elements must be integers")
    
    # Use set for efficient membership checking and count matching elements
    arr2_set = set(arr2)
    return sum(1 for x in arr1 if x in arr2_set)