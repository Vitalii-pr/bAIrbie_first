def minimum_deletion_score(s, t):
  """Finds the minimum deletion score to make t a subsequence of s.

  Args:
    s: The original string.
    t: The string to be transformed into a subsequence of s.

  Returns:
    The minimum deletion score required.
  """

  if not t:
      return 0

  m, n = len(s), len(t)
  dp = [[0] * (n + 1) for _ in range(m + 1)]

  for i in range(m + 1):
    for j in range(n + 1):
      if i == 0 or j == 0:
        dp[i][j] = 0
      elif s[i - 1] == t[j - 1]:
        dp[i][j] = dp[i - 1][j - 1] + 1
      else:
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

  return len(t) - dp[m][n]

# Example usage
s = "abacaba"
t = "bzaa"
result = minimum_deletion_score(s, t)
print(result)
