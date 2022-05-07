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

        while root or nodeStack: # whenever current node is not null or node stack is not empty
            while root: # whenever current node is not null push it to stack, iterate its left node
                nodeStack.append(root)
                root = root.left
            # whenever current node is null, pop its parent node
            root = nodeStack.pop()
            # add current node's value to result
            result.append(root.val)
            # iterate its right node
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
