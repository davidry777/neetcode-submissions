class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substr = 0
        n = len(s)
        for i in range(n):
            charSet = set()
            for j in range(i, n):
                if s[j] in charSet:
                    break
                charSet.add(s[j])
            longest_substr = max(longest_substr, len(charSet))
        return longest_substr