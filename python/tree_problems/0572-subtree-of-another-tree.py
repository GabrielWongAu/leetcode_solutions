# https://leetcode.com/problems/subtree-of-another-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        if self.sameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def sameTree(self, root, subRoot):
        if not root and not subRoot:
            return True
        if root and subRoot and root.val == subRoot.val:
            return self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right)
        return False


# Time complexity: O(m * n)
# Where m is the size of the subtree (subRoot) and n is the size of the 
# main tree (root). This is because for each node in the main tree, 
# the solution checks if the subtree is identical to the subtree rooted at that node. 

# Space complexity: O(n)
# Where n is the size of the main tree (root). This is because the maximum depth of the 
# recursive call stack is proportional to the height of the main tree. In the worst case, 
# this could be the height of the entire tree, leading to a linear space complexity.