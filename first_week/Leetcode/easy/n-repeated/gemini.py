class Solution(object):
    def repeatedNTimes(self, nums):
        """
        Finds the element that appears n times in an array where the length is 2n and contains n+1 unique elements using a hash map.

        Args:
            nums: An integer array.

        Returns:
            The element that appears n times in nums.
        """

        counts = {}
        for num in nums:
            if num in counts:
                return num
            counts[num] = 1
        return None

    def find_repeated_element_pointers(self, nums):
        """
        Finds the element that appears n times in an array where the length is 2n and contains n+1 unique elements using two pointers.

        Args:
            nums: An integer array.

        Returns:
            The element that appears n times in nums.
        """

        i, j = 0, 1
        while i < len(nums) and j < len(nums):
            if nums[i] == nums[j]:
                return nums[i]
            i += 1
            j = (j + 1) % len(nums)  # Wrap around if j reaches the end of the array

        return None
