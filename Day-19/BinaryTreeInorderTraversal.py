class Solution:
    def inorderTraversal(self, root):
        result = []

        def inorder(node):
            if node is None:
                return

            inorder(node.left)       # Left
            result.append(node.val)  # Root
            inorder(node.right)      # Right

        inorder(root)

        return result

#Iterative Solution
class Solution:
    def inorderTraversal(self, root):
        result = []
        stack = []
        current = root

        while current or stack:
            # Go as far left as possible
            while current:
                stack.append(current)
                current = current.left

            # Visit node
            current = stack.pop()
            result.append(current.val)

            # Move to right subtree
            current = current.right

        return result