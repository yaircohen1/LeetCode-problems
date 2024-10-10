from collections import deque

"""""
Given the root of a binary tree, invert the tree, and return its root.

Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:
Input: root = [2,1,3]
Output: [2,3,1]

Example 3:
Input: root = []
Output: []

# Constraints:
#
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
"""

# Solution:
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(nodes):
    if not nodes:
        return None
    root = TreeNode(nodes[0]) # create the root node
    queue = deque([root]) # use a queue to keep track of the parent nodes
    i = 1
    while i < len(nodes): # while there are nodes to process
        current = queue.popleft() # get the first node in the queue
        if nodes[i] is not None: # if the left child is not None
            current.left = TreeNode(nodes[i])
            queue.append(current.left)
        i += 1
        if i < len(nodes) and nodes[i] is not None: # if there are more nodes to process
            current.right = TreeNode(nodes[i])
            queue.append(current.right)
        i += 1
    return root

def invert_tree(root):
    if not root:
        return None
    root.left, root.right = invert_tree(root.right),invert_tree(root.left)
    return root

def BFS_traversal(root):
    result = []
    if not root:
        return result
    queue = deque([root])
    while queue:
        current = queue.popleft()
        result.append(current.val)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    print(result)

# solutin function
def invert_binary_tree(nodes):
    root = build_tree(nodes)
    inverted_root = invert_tree(root)
    return BFS_traversal(inverted_root)

# Test cases
invert_binary_tree([4,2,7,1,3,6,9]) # [4,7,2,9,6,3,1]
invert_binary_tree([2,1,3])# [2,3,1]
invert_binary_tree([]) # []

# Time complexity: O(n) where n is the number of nodes in the tree
