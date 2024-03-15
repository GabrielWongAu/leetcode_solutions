# https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_count, t_count = {}, {}

        for i in range(len(s)):
            s_count[s[i]] = 1 + s_count.get(s[i], 0)
            t_count[t[i]] = 1 + t_count.get(t[i], 0)
        return s_count == t_count


# Time complexity: O(s + t)
# where s is the number of characters in s string 
# and t is the number of characters in t string

# Space complexity: O(s + t)
