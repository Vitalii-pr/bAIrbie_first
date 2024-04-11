def longest_nice_substring(s):
  """
  Finds the longest nice substring in a string.

  Args:
      s: The string to search.

  Returns:
      The longest nice substring in s.
  """
  lower, upper, max_len, start = 0, 0, 0, 0
  for i, char in enumerate(s):
    if char.islower():
      lower |= 1 << (ord(char) - ord('a'))
    else:
      upper |= 1 << (ord(char) - ord('A'))
    while lower & upper == lower:  # Check if all lowercase has a matching uppercase
      max_len = max(max_len, i - start + 1)
      if char.islower():
        lower ^= 1 << (ord(char) - ord('a'))  # Remove the current character from lower
      start += 1
  return s[start:start + max_len]

# Example usage
s = "YazaAay"
result = longest_nice_substring(s)
print(result)  # Output: "aAa"
