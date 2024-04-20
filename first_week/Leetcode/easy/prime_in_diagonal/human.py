class Solution(object):
    def diagonalPrime(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: int
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

        for i in range(rows):
            diagonal_value = nums[i][i]
            if is_prime(diagonal_value):
                largest_prime = max(largest_prime, diagonal_value)

        if cols > rows and is_prime(nums[rows - 1][cols - 1]):
            largest_prime = max(largest_prime, nums[rows - 1][cols - 1])

        if cols > rows:
            for i in range(cols):
                diagonal_value = nums[i][cols - i - 1]
                if is_prime(diagonal_value):
                    largest_prime = max(largest_prime, diagonal_value)

        return largest_prime
