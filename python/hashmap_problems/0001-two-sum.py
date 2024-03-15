# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}  # val -> index 
        for index, num in enumerate(nums):
            diff = target - num
            if diff in num_dict:
                return [num_dict[diff],index]
            num_dict[num] = index


# Time complexity: O(n) 
# We traverse the list containing n elements only once.
# Each lookup only takes O(1) time.

# Space complexity: O(n) 
# The extra space required depends on the number of
# items stored in the hash table, which stores at most n elements.