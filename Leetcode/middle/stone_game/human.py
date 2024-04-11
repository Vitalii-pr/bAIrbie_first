import functools

class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        xor_total = functools.reduce(lambda x, y: x ^ y, piles)
        return xor_total != 0  