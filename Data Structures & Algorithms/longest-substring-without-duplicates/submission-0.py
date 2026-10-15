from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        count = defaultdict(int)
        res = 0
        while right < len(s):
            character = s[right]
            count[character] += 1
            while count[character] > 1:
                count[s[left]] -= 1
                left += 1
            res = max(res, (right - left + 1))
            right += 1

        return res