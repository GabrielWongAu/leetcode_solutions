# https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


# Time complexity: O(n)
# We search and insert for n times and each operation takes constant time.

# Space complexity: O(n)
# The space used by a hash table is linear with the number of elements in it.