# %%
## 1022. Sum of Root To Leaf Binary Numbers
## author: Greysuki
from typing import Optional
from functools import lru_cache
import math

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_complete_binary_tree(nodes):
    root = TreeNode(nodes[0])
    row = [root]

    node_counter = 1
    h = math.ceil(math.log2(len(nodes) + 1))
    for i in range(1, h):
        new_row = []
        for node in row:
            if node_counter >= len(nodes):
                break

            node.left = TreeNode(nodes[node_counter])

            if node_counter + 1 >= len(nodes):
                break

            node.right = TreeNode(nodes[node_counter + 1])

            new_row.append(node.left)
            new_row.append(node.right)

            node_counter += 2

        row = new_row

    return root


def traverse_tree(node):
    if node == None:
        return
    else:
        print(node.val)
        traverse_tree(node.left)
        traverse_tree(node.right)


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        return self.helper(root, 0)

    def helper(self, node, prefix):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            # print(node.val, prefix)
            return prefix * 2 + node.val
        else:
            prefix = prefix * 2 + node.val
            a = self.helper(node.left, prefix)
            b = self.helper(node.right, prefix)

            # print(a + b)

            return a + b


# Your Solution object will be instantiated and called as such:
obj = Solution()
root = build_complete_binary_tree([1, 0, 1, 0, 1, 0, 1, 1, 0])

# traverse_tree(root)

obj.sumRootToLeaf(root)
# print(obj.addBinary(a="1010", b="1011"))

# %%
