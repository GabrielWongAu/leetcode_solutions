# https://leetcode.com/problems/valid-parentheses/submissions/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping= { "{":"}", "(":")", "[":"]" }
        
        for char in s:
            if char in mapping:
                stack.append(char)
            elif not stack:
                return False
            else:
                opening = stack.pop()
                closing = mapping[opening]
                if char != closing:
                    return False
        
        return not stack


# Time complexity: O(n)
# We simply traverse the given string one character at a 
# time and push and pop operations on a stack take O(1) time.

# Space complexity: O(n) 
# As we push all opening brackets onto the stack and in the 
# worst case, we will end up pushing all the brackets onto 
# the stack. e.g. (((((((((.