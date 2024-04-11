def compareVersion(version1: str, version2: str) -> int:
  """
  Compares two version numbers and returns -1 if the first one is smaller, 1 if it's larger, and 0 if they are equal.

  Args:
      version1: The first version number.
      version2: The second version number.

  Returns:
      -1 if version1 is smaller than version2, 1 if it's larger, and 0 if they are equal.
  """

  # Split the version strings into lists of integers.
  v1_list = [int(x) for x in version1.split(".")]
  v2_list = [int(x) for x in version2.split(".")]

  # Add zeros to the shorter list to make them the same length.
  for i in range(max(len(v1_list), len(v2_list))):
    if i >= len(v1_list):
      v1_list.append(0)
    if i >= len(v2_list):
      v2_list.append(0)

  # Compare the corresponding elements of the lists.
  for i in range(len(v1_list)):
    if v1_list[i] < v2_list[i]:
      return -1
    elif v1_list[i] > v2_list[i]:
      return 1

  # If all elements are equal, the versions are equal.
  return 0

# Example usage
version1 = "1.01"
version2 = "1.001"
print(compareVersion(version1, version2))  # Output: 0

version1 = "1.0"
version2 = "1.0.0"
print(compareVersion(version1, version2))  # Output: 0

version1 = "0.1"
version2 = "1.1"
print(compareVersion(version1, version2))  # Output: -1
