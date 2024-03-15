# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Recursive DFS
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# Time complexity: O(n)
# Where n is the number of nodes.

# Space complexity: O(n)
# In the worst case, the tree is completely unbalanced, the recursion
# call would occur n times (the height of the tree). Thus the storage
# to keep the call stack would be O(n).

# In the best case (tree is completely balanced), the height of the tree
# would be log(n). Thus the space complexity would be O(log(n)).


# Iterative DFS
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        stack = [[root, 1]]
        res = 0

        while stack:
            node, depth = stack.pop()

            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res

# Time complexity: O(n)

# Space complexity: O(n)
# In the worst case, the tree is completely unbalanced, the recursion
# call would occur n times (the height of the tree). Thus the storage
# to keep the call stack would be O(n).

# In the best case (tree is completely balanced), the height of the tree
# would be log(n). Thus the space complexity would be O(log(n)).


# BFS
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        q = deque()
        if root:
            q.append(root)

        level = 0

        while q:

            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level

# Time complexity: O(n)

# Space complexity: O(n)