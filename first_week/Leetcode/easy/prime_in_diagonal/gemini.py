class Solution(object):
    def diagonalPrime(self, nums):
        """
        Finds the largest prime number that lies on at least one of the diagonals of a matrix.

        Args:
            nums: A 0-indexed two-dimensional integer array.

        Returns:
            The largest prime number on a diagonal of nums, or 0 if no prime number is present.
        """

        def is_prime(num):
            """
            Checks if a number is prime.

            Args:
                num: An integer.

            Returns:
                True if num is prime, False otherwise.
            """
            if num <= 1:
                return False
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    return False
            return True

        rows, cols = len(nums), len(nums[0])
        largest_prime = 0

        # Iterate over the top-left to bottom-right diagonal
        for i in range(rows):
            diagonal_value = nums[i][i]
            if is_prime(diagonal_value):
                largest_prime = max(largest_prime, diagonal_value)

        # Handle the case where the bottom-right corner element is not included in the previous loop
        if cols > rows and is_prime(nums[rows - 1][cols - 1]):
            largest_prime = max(largest_prime, nums[rows - 1][cols - 1])

        # Iterate over the top-right to bottom-left diagonal (only applicable if the matrix has more columns than rows)
        if cols > rows:
            for i in range(cols):
                diagonal_value = nums[i][cols - i - 1]
                if is_prime(diagonal_value):
                    largest_prime = max(largest_prime, diagonal_value)

        return largest_prime