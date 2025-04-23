class BinaryTree:
    def __init__(self, value):
        self.key = value
        self.left_child = None
        self.right_child = None

    def insert_left(self, value):
        if self.left_child == None:
            self.left_child = BinaryTree(value)
        else:
            bin_tree = BinaryTree(value)
            bin_tree.left_child = self.left_child
            self.left_child = bin_tree

    def insert_right(self, value1):

        if self.right_child == None:
            self.right_child = BinaryTree(value1)
        else:
            bin_tree = BinaryTree(value1)
            bin_tree.right_child = self.right_child
            self.right_child = bin_tree

    def invert(self):
        current = [self]
        next = []
        while current:
            for node in current:
                if node.left_child:
                    next.append(node.left_child)
                if node.right_child:
                    next.append(node.right_child)
                tmp = node.left_child
                node.left_child = node.right_child
                node.right_child = tmp
                current = next
                next = []


tree = BinaryTree(1)
tree_2 = BinaryTree(2)


tree.insert_left(2)
tree.insert_right(3)
tree.insert_right(8)
tree.insert_left(4)
tree.insert_left(12)
tree.insert_left(13)
tree.left_child.insert_right(6)
tree.insert_right(5)

tree.invert()
