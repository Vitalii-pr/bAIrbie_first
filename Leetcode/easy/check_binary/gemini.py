def check_ones(s):
    """
    Checks if a binary string has at most one contiguous segment of ones.

    Args:
        s: The binary string to check.

    Returns:
        True if the string has at most one contiguous segment of ones, False otherwise.
    """
    return "01" not in s  # Key Change

# Examples
print(check_ones("1001"))  # Output: False
print(check_ones("110"))   # Output: True
print(check_ones("111000"))  # Output: True
print(check_ones("10001"))  # Output: False
