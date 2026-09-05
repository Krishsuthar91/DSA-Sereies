# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root):
        def height(node):
            if node is None:
                return 0

            left = height(node.left)
            if left == -1:
                return -1

            right = height(node.right)
            if right == -1:
                return -1

            if abs(left - right) > 1:
                return -1

            return max(left, right) + 1

        return height(root) != -1




class Solution:
    def isBalanced(self, root):
        if root is None:
            return True

        left = self.height(root.left)
        right = self.height(root.right)

        return (
            abs(left - right) <= 1 and
            self.isBalanced(root.left) and
            self.isBalanced(root.right)
        )

    def height(self, node):
        if node is None:
            return 0
        return max(self.height(node.left), self.height(node.right)) + 1