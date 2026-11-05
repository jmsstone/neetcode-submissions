# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def equality(self, root, other):
        if not root and not other:
            return True
        if not root:
            return False
        if not other:
            return False
        return root.val == other.val and \
         (self.equality(root.left, other.left)) and \
         (self.equality(root.right, other.right))   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not root:
            return False
        if not subRoot:
            return True
        return self.equality(root,subRoot) or \
        self.isSubtree(root.left,subRoot) or \
        self.isSubtree(root.right,subRoot)
        