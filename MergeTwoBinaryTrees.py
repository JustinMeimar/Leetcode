class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"Tree:{self.val}"

class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        print(root1.val)


def iterate(root):
    
    print(root)
    if root.left != None:
        iterate(root.left)
    if root.right != None:
        iterate(root.right)
    # iterate(root.right)

one = TreeNode(5)
two = TreeNode(3)
three = TreeNode(1, one, two)
four = TreeNode(4)
root =  TreeNode(9,three,four)

iterate(root)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Stack:
    def __init__(self):
        self.items = []
        
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        self.items.remove(self.items[-1])
    
    def __str__(self):
        return f"{self.items}"
        
class Solution:
    
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        self.stack1 = Stack()
        self.stack2 = Stack()
        
        self.iterate(root1, self.stack1)
        self.iterate(root2, self.stack2)
        
        print(self.stack1)
        print(self.stack2)
        # return TreeNode(sum, None, None)
        
        
    def iterate(self, tree: TreeNode, stack: Stack):
        stack.push(tree.val)
        
        if tree.left != None:
            self.iterate(tree.left, stack)
        if tree.right != None:
            self.iterate(tree.right, stack)
            
        if tree.left == None:
            stack.push(None)
    
"""