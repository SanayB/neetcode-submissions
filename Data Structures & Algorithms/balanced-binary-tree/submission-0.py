class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def height(node):

            if not node:
                return 0

            left = height(node.left)
            right = height(node.right)

            # If already unbalanced
            if left == -1 or right == -1:
                return -1

            # Check balance condition
            if abs(left - right) > 1:
                return -1

            return 1 + max(left, right)

        return height(root) != -1