class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
         # Create a trie to store the words efficiently
        n = len(people)
        dp = [[float('inf')] * (1 << len(required_skills)) for _ in range(n + 1)]
        dp[0][0] = 0

        # Skill presence bitmask for each person
        skill_sets = [0] * n
        for i, person_skills in enumerate(people):
            for skill in person_skills:
                skill_sets[i] |= 1 << required_skills.index(skill)

        for i in range(1, n + 1):
            for prev_mask in range((1 << len(required_skills)) - 1):
            # Consider adding the current person
                curr_mask = prev_mask | skill_sets[i - 1]
            # Update dp if adding the current person is beneficial
            if curr_mask not in (prev_mask, float('inf')):
                dp[i][curr_mask] = min(dp[i][curr_mask], dp[i - 1][prev_mask] + 1)
            # Keep the minimum team size for the current mask (without adding the current person)
            dp[i][prev_mask] = min(dp[i][prev_mask], dp[i - 1][prev_mask])

        # Backtrack to find the team members
        team = []
        mask = (1 << len(required_skills)) - 1
        for i in range(n, 0, -1):
            if dp[i][mask] != dp[i - 1][mask]:
                team.append(i - 1)
                mask ^= skill_sets[i - 1]
        return team[::-1]