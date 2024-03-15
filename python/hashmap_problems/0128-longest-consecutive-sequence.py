# https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:
            # check if its the start of a sequence
            if (num - 1) not in num_set:
                length = 1
                while (num + length) in num_set:
                    length += 1
                longest = max(length, longest)
        return longest


# Time complexity: O(n)
# On the surface the time complexity appears to be quadratic due to
# the while loop nested within the for loop. However the while loop
# can only run for n iterations throughout the entire runtime of the
# algorithim. This means that despite looking like a O(n x n) complexity,
# the nested loops actually run in O(n + n) = O(n) time.

# Space complexity: O(n)
# in order to set up O(1) lookups, we allocate linear space for a hash
# table to store the O(n) numbers in nums.