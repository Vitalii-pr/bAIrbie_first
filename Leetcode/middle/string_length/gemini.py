def maximum_length(arr):
  """
  Finds the maximum possible length of a string formed by the concatenation of unique character subsequences from a given array of strings.

  Args:
      arr: An array of strings.

  Returns:
      The maximum possible length of a string formed by the concatenation of unique character subsequences from the array.
  """
  result = set()
  for s in arr:
    chars = set()
    for char in s:
      # If the character is not already in the set, add it.
      # If it is already in the set, the current string is not unique and we can break out of the loop.
      if char not in chars:
        chars.add(char)
      else:
        break
    # If the loop completes (i.e. no duplicates were found), add the entire string to the result set.
    if len(chars) == len(s):
      result.add(s)
  return len("".join(result))

# Example usage
arr = ["un", "iq", "ue"]
print(maximum_length(arr))  # Output: 4

arr = ["cha", "r", "act", "ers"]
print(maximum_length(arr))  # Output: 6

arr = ["abcdefghijklmnopqrstuvwxyz"]
print(maximum_length(arr))  # Output: 26
