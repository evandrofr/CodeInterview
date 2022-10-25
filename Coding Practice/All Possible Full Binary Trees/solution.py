from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def allPossibleFBT(self, N):
        memory = {0: [], 1: [TreeNode(0)]}
        def rec(N):
            if N not in memory:
                solution = []
                for x in range(N):
                    y = N - 1 - x
                    for left in rec(x):
                        for right in rec(y):
                            node = TreeNode(0)
                            node.left = left
                            node.right = right
                            solution.append(node)
                memory[N] = solution

            return memory[N]
        return rec(N)

if __name__ == "__main__":
    print(Solution().allPossibleFBT(5))