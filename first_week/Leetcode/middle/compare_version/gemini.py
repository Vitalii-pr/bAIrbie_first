class Solution(object):
    def compareVersion(self, version1, version2):
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