# https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # mapping character count to list of anagrams
        res = collections.defaultdict(list) 

        for string in strs:
            count = [0] * 26 # a ... z

            for char in string:
                count[ord(char) - ord("a")] += 1

            res[tuple(count)].append(string)

        return res.values()

# Time complexity: O(m * n)
# Where m is the number of strings we are given
# and n is the average length of each string

# Space complexity: O(m * n)
# The total information content stored in res