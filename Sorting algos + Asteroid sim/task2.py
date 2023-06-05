import random

class BinarySearchTree:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def add(self, node):

        if node.value < self.value:
            if self.left is not None:
                self.left.add(node)
            else:
                self.left = node

        else:
            if self.right is not None:
                self.right.add(node)
            else:
                self.right = node

    def print(self, curr_node):
        if curr_node is not None:   # Added lines
            self.print(curr_node.left)
            print(str(curr_node.value))
            self.print(curr_node.right)


if __name__ == "__main__":
    values = [random.randint(1, 100) for i in range(20)]
    tree = BinarySearchTree(values[0])
    for value in values[1:]:
        node = BinarySearchTree(value)
        tree.add(node)

    tree.print(tree)










'''
class BinarySearchTree:
    def __init__(self, value):  # Constructor initialises this as a node contains some data
        self.left = None
        self.right = None  # every node is a start of a branch the left and right
        self.value = value

    def add(self, node):  # Recursively add a node into the correct place in the tree

        if node.value < self.value:  # if the value of the node that has been sent is smaller then the "main node" being compared to then
            if self.left is not None:  # if something is there we recursively send that "main node" back to be checked again, calling the function again
                self.left.add(node)
            else:  # lesser value go to the left, therefore if nothing is there then that is its place
                self.left = node

        else:  # if the "main node" is bigger then
            if self.right is not None:  # if on the right there is something /// same as above
                self.right.add(node)
            else:
                self.right = node

    def print(self, curr_node):
        if curr_node is not None:   # if the node doesnt exist then just do nothing
            self.print(curr_node.left)  # want to sort from the smallest tot he biggest therefore the left comes first
            print(str(curr_node.value))
            self.print(curr_node.right)


if __name__ == "__main__":
    values = [random.randint(1, 100) for i in range(20)]  # Initial random values in an array
    tree = BinarySearchTree(values[0])  # Create the root node of the binary search tree
    for value in values[1:]:  # Iterate over the other random values in the list starting from index 1 as the index 0 is taken at the node
        node = BinarySearchTree(value)  # Create a node with the random value index (from loop)
        #initialises this node and save it
        #sends the node to be sorted out
        tree.add(node)  # Add to the correct position in the tree

    tree.print(tree)
'''