# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # recursive solution
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        def isSymmetric(leftNode, rightNode) -> bool:
            if not leftNode and not rightNode:
                return True

            if not leftNode or not rightNode:
                return False

            return (leftNode.val == rightNode.val) and isSymmetric(leftNode.left, rightNode.right) and isSymmetric(leftNode.right, rightNode.left)

        rootLeft, rootRight = root.left, root.right

        return isSymmetric(rootLeft, rootRight)

    # iterative solution
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        stack = [root.right, root.left]

        while stack:
            leftNode = stack.pop()
            rightNode = stack.pop()
            if not leftNode and not rightNode:
                continue
            if not leftNode or not rightNode or leftNode.val != rightNode.val:
                return False
            stack.append(leftNode.left)
            stack.append(rightNode.right)
            stack.append(leftNode.right)
            stack.append(rightNode.left)

        return True
