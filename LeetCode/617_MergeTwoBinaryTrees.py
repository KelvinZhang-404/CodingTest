# You are given two binary trees root1 and root2.
#
# Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others
# are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum
# node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new
# tree.
#
# Return the merged tree.
#
# Note: The merging process must start from the root nodes of both trees.
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/merge-two-binary-trees
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root2:
            return root1

        if not root1:
            return root2

        return TreeNode(root1.val + root2.val, self.mergeTrees(root1.left, root2.left), self.mergeTrees(root1.right, root2.right))