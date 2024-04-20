def find_min_crossed_bricks(wall):
    """
    This function takes a 2D list representing a brick wall as input 
    and returns the minimum number of bricks that can be crossed by a 
    vertical line drawn from the top to the bottom of the wall.
    
    Args:
      wall: A 2D list where each sublist represents a row of bricks in the wall. 
            The value at each index in the sublist represents the width of a brick in that row.
    Returns:
    The minimum number of bricks that can be crossed by a vertical line.
    """
    prefix_sums = {}
    min_crossed_bricks = float('inf')

    for row in wall:
        current_prefix_sum = 0
    for brick_width in row:
        current_prefix_sum += brick_width
    if current_prefix_sum - 1 in prefix_sums:
        min_crossed_bricks = min(min_crossed_bricks, prefix_sums[current_prefix_sum - 1] + 1)
    prefix_sums[current_prefix_sum] = current_prefix_sum

    return min_crossed_bricks

# Example usage
wall = [[1, 2, 2, 1], [3, 1, 2], [1, 3, 2], [2, 4], [3, 1, 2], [1, 3, 1, 1]]
min_bricks_crossed = find_min_crossed_bricks(wall)
print(f"Minimum number of bricks crossed: {min_bricks_crossed}")
