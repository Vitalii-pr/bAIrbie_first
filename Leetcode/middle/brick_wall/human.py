class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        border_counts = {}
        highest_count = 0

        for layer in wall:
            current_position = 0  

            for brick_index in range(len(layer) - 1):
                brick_width = layer[brick_index]
                current_position += brick_width

                border_counts[current_position] = border_counts.get(current_position, 0) + 1
                highest_count = max(highest_count, border_counts[current_position])

        return len(wall) - highest_count