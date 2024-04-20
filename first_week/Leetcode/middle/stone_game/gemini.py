import functools

class Solution(object):
    def stoneGame(self, piles):
        """
        This function determines if Alice wins the game given the initial piles of stones.

        Args:
            piles: A list of integers representing the number of stones in each pile.

        Returns:
            True if Alice wins the game, False otherwise.
        """
        xor_total = functools.reduce(lambda x, y: x ^ y, piles)
        return xor_total != 0  # Alice wins if the XOR total of stone counts is not zero