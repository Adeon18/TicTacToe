"""
Tree node which I did not use but it is here nontheless :/
"""
class BTNode:
    """
    A simple node for the binary tree
    """
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    
    def __repr__(self):
        return f"BTNode(data={self.data}, left={self.left}, right={self.right})"