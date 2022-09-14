from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        count = 0
        if root is None:
            return count
        def sum_path(node: TreeNode, acc_list: List[int]):
            nonlocal count
            if acc_list[-1] == targetSum:
                count += 1
            for acc in acc_list[:-1]:
                if acc_list[-1] - acc == targetSum:
                    count += 1 
            if node.left:
                sum_path(node=node.left, acc_list=acc_list.copy() + [acc_list[-1] + node.left.val])
            if node.right:
                sum_path(node=node.right, acc_list=acc_list.copy() + [acc_list[-1] + node.right.val])
                
        sum_path(root, [root.val])
        return count