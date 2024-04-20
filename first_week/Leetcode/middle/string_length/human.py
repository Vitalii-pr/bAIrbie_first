class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        validSubsets = [set()]
        for word in arr:
            if len(set(word)) < len(word):
                continue
            wordSet = set(word)
            for existingSet in validSubsets: 
                if wordSet & existingSet:
                    continue
                validSubsets.append(wordSet | existingSet)

        maxLen = 0 
        for subset in validSubsets:
            maxLen = max(maxLen, len(subset)) 
        return maxLen

