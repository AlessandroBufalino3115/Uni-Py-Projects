import random

SCN = 0
found = True


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

    def find_min(self, curr_node):

        if curr_node is not None:
            if curr_node.left is not None:
                num = self.find_min(curr_node.left)
            else:
                return curr_node.value
            return num

    def find_max(self, curr_node):

        if curr_node is not None:
            if curr_node.right is not None:
                num = self.find_max(curr_node.right)
            else:
                return curr_node.value
            return num

    def find_value(self, curr_node, target):
        global found

        if curr_node is not None:
            if curr_node.value != target:
                if curr_node.value > target:
                    self.find_value(curr_node.left, target)
                elif curr_node.value < target:
                    self.find_value(curr_node.right, target)
            else:
                found = True
        else:
            found = False

    def close_value(self, curr_node, target):
        global SCN
        if curr_node != None:
            self.close_value(curr_node.left, target)

            midd = (curr_node.value + SCN) // 2

            if(target >= midd):
                SCN = curr_node.value

            self.close_value(curr_node.right, target)


if __name__ == "__main__":
    values = [random.randint(1, 100) for i in range(20)]
    tree = BinarySearchTree(values[0])
    for value in values[1:]:
        node = BinarySearchTree(value)
        tree.add(node)

    print("Lets now play guess the number, the bounds are " + str(tree.find_min(tree)) + " (as the minimum value) " + str(tree.find_max(tree)) + " (as the maximum value)")  # main menu

    while True:

        player_input = input("\nWhat is your number: ")

        tree.find_value(tree, int(player_input))

        if (found):
            print("i have found the value you inputted well done")
            break
        else:
            print("unfortunately that is wrong")
            tree.close_value(tree, int(player_input))
            diff = abs(int(player_input) - SCN)
            print(str(diff) + " is how far away from the closest value you are")
