class Solution(object):
    def minAddToMakeValid(self, s):
        """
        Returns the minimum number of parentheses needed to make the string valid.

        Args:
            s: A string containing only '(' and ')' characters.

        Returns:
            The minimum number of parentheses needed to make the string valid.
        """

        open_count = 0  # Count of currently open parentheses
        unmatched = 0   # Count of parentheses needing a match

        for ch in s:
            if ch == '(':
                open_count += 1
            else:  # It's a closing parenthesis
                if open_count > 0: 
                    open_count -= 1  # We found a match
                else:
                    unmatched += 1   # Need to add an opening parenthesis

        return open_count + unmatched  
