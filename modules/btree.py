from btnode import BTNode


class LinkedBinaryTree:
    def __init__(self, root):
        self.key = root
        self.left = None
        self.right = None

    def insert_left(self, new_node):
        if self.left == None:
            self.left = LinkedBinaryTree(new_node)
        else:
            t = LinkedBinaryTree(new_node)
            t.left = self.left
            self.left = t

    def insert_right(self, new_node):
        if self.right == None:
            self.right = LinkedBinaryTree(new_node)
        else:
            t = LinkedBinaryTree(new_node)
            t.right = self.right
            self.right = t

    def get_right_child(self):
        return self.right

    def get_left_child(self):
        return self.left

    def set_root_val(self, obj):
        self.key = obj

    def get_root_val(self):
        return self.key

    def preorder(self):
        print(self.key)
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.key)
        if self.right:
            self.right.inorder()

    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.key)
