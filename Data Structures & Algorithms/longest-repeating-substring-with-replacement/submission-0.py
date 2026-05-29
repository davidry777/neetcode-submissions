class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest_rep_char = 0
        n = len(s)
        for i in range(n):
            count = {}
            maxFreq = 0
            for j in range(i, n):
                count[s[j]] = 1 + count.get(s[j], 0)
                maxFreq = max(maxFreq, count[s[j]])
                if (j - i + 1) - maxFreq <= k:
                    longest_rep_char = max(longest_rep_char, j - i + 1)
        return longest_rep_char