# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # iterative solution
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        nodeStack = []

        while root or nodeStack:
            while root:
                nodeStack.append(root)
                root = root.left
            root = nodeStack.pop()
            result.append(root.val)
            root = root.right

        return result

    # recursive solution
    # def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     result = []
    #
    #     def inorderTraversal(root: Optional[TreeNode]):
    #         if not root:
    #             return
    #
    #         inorderTraversal(root.left)
    #         result.append(root.val)
    #         inorderTraversal(root.right)
    #
    #     inorderTraversal(root)
    #
    #     return result
