# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root, targetSum):
        if root is None:
            return False

        # Check if it's a leaf node
        if root.left is None and root.right is None:
            return targetSum == root.val

        # Check left or right subtree
        return (self.hasPathSum(root.left, targetSum - root.val) or
                self.hasPathSum(root.right, targetSum - root.val))



#Alternative Iterative Solution (DFS Using Stack)

class Solution:
    def hasPathSum(self, root, targetSum):
        if root is None:
            return False

        stack = [(root, targetSum - root.val)]

        while stack:
            node, remaining = stack.pop()

            if node.left is None and node.right is None and remaining == 0:
                return True

            if node.right:
                stack.append((node.right, remaining - node.right.val))

            if node.left:
                stack.append((node.left, remaining - node.left.val))

        return False