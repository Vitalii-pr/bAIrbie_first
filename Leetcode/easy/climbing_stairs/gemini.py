def climb_stairs_dp(n):
  """
  Calculates the number of ways to climb n stairs using dynamic programming.

  Args:
      n: The number of stairs.

  Returns:
      The number of ways to climb n stairs.
  """
  if n <= 1:
    return 1

  dp = [0 for _ in range(n + 1)]
  dp[0] = 1
  dp[1] = 1

  for i in range(2, n + 1):
    dp[i] = dp[i-1] + dp[i-2]

  return dp[n]

# Example usage
n = 4
result = climb_stairs_dp(n)
print(f"Number of ways to climb {n} stairs (dynamic programming): {result}")
