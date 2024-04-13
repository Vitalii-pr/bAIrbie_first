class Solution(object):
    def checkOnesSegment(self, s):
        """
        Checks if a binary string has at most one contiguous segment of ones.

        Args:
            s: The binary string to check.

        Returns:
            True if the string has at most one contiguous segment of ones, False otherwise.
        """
        return "01" not in s  # Key Change