import math

def decompose(n):
    """
    Finds a strictly increasing sequence of numbers whose squares sum to n^2.

    Args:
        n: A positive integer.

    Returns:
        A list of integers representing the decomposition, or None if no 
        valid solution exists.
    """

    def _find_decomposition(target, current_max, numbers):
        """Recursive helper function to find decompositions."""

        if target == 0:
            return numbers  # Found a solution

        for i in range(current_max, 0, -1):
            square = i * i
            if square <= target:
                result = _find_decomposition(target - square, i - 1, numbers + [i])
                if result:
                    return result  # Pass solution upwards

        return None  # No solution found for this branch

    return _find_decomposition(n * n, n - 1, []) 