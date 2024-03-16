# https://leetcode.com/problems/last-stone-weight/

import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)

        stones.append(0)
        return abs(stones[0])
    
# Time complexity: O(n log n)
# where n is the length of stones.

# Space complexity: O(n) or O(log n)
# where n is the length of stones.