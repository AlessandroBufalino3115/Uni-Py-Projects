class Node(object):
    def __init__(self, Data):
        self.data = Data
        self.next_pos = None  # we set it as default to none because if we add something is going to be overwritten with the next pos anyway


class LinkedList(object):
    def __init__(self):
        self.head = None  # starting a fresh list, therefore we need something to point to the first node

    def print_linked_list(self):
        cur_node = self.head  # current node is equal to the head of the list (the start)
        while cur_node:  # while cur_node is not none
            print(cur_node.data)
            cur_node = cur_node.next_pos

    def append_end(self, Data):  # here is where we add stuff to the end
        new_node = Node(Data)  # we define a new node

        if self.head is None:  # here we check if the head exists, if it doesnt then we create one
            self.head = new_node  # this is the head which contains the data but still no next pos
            return

        # this is where we try to find the spot at the end
        last_node = self.head  # we initially point to the head, we know its been created as it passed the if statement
        while last_node.next_pos:  # while next pos is not null
            last_node = last_node.next_pos  # cycle through the nodes until the while loop is false so have found where it ends
        last_node.next_pos = new_node  # this is equal to the new node location which we made at the start

    def append_start(self, Data):
        new_head = Node(Data)  # we want this to be the new head with the data
        new_head.next_pos = self.head  # here we change the next pos to be the old head
        self.head = new_head  # now we set the positioning of "head" to the new node

    def get_size(self):
        size = 0

        cur_node = self.head
        while cur_node:
            size += 1
            cur_node = cur_node.next_pos

        return size

    def append_specific(self, Data, index):
        place = 0
        new_node = Node(Data)
        if index == 0:  # if the player wants to change the first value we send him to the append_start function
            LinkedList.append_start(self, Data)

        elif index < 0:

            index = LinkedList.get_size(self) + index
            last_node = self.head  # we start from the beginning
            while place != index:
                last_node = last_node.next_pos
                place += 1

            new_node.next_pos = last_node.next_pos
            last_node.next_pos = new_node

        elif index > LinkedList.get_size(self):
            print("index doesnt exist as the list is only " + str(LinkedList.get_size(self)) + " long")

        else:
            last_node = self.head  # we start from the beginning
            while place != index - 1:
                last_node = last_node.next_pos
                place += 1

            new_node.next_pos = last_node.next_pos

            last_node.next_pos = new_node

    def delete_specific(self, index):
        place1 = 0
        place2 = 0

        if index == 0:
            cur_node = self.head
            self.head = cur_node.next_pos

        elif index < 0:
            print("no")

        else:
            last_node = self.head  # we start from the beginning
            unwanted = self.head
            while place1 != index - 1:
                last_node = last_node.next_pos
                place1 += 1

            while place2 != index:
                unwanted = unwanted.next_pos
                place2 += 1

            last_node.next_pos = unwanted.next_pos
            unwanted.next_pos = None #make the unwanted node point to nothing

    def read_specific(self, index):
        place = 0

        if index >= 0:
            cur_node = self.head  # we start from the beginning
            while place != index:  # while cur_node is not none
                cur_node = cur_node.next_pos
                place += 1
            return cur_node.data

    def find_value(self, Data):
        cur_node = self.head

        while cur_node:
            if cur_node.data == Data:
                return True

            cur_node = cur_node.next_pos

        return False

    def replace_specific(self, Data, index):

        if index == 0:
            LinkedList.append_start(self, Data)
            LinkedList.delete_specific(self, 1)

        elif index < 0:
            index = LinkedList.get_size(self) + index
            LinkedList.delete_specific(self, index)
            LinkedList.append_specific(self, Data, index)

        else:
            LinkedList.delete_specific(self, index)
            LinkedList.append_specific(self, Data, index)


class Queue(object):

    def __init__(self):
        self.ll = LinkedList()

    def push(self, Data):
        self.ll.append_end(Data)

    def pop(self):
        data = self.ll.read_specific(0)
        self.ll.delete_specific(0)

        return data

    def printItems(self):

        self.ll.print_linked_list()


class Stack(object):

    def __init__(self):
        self.ll = LinkedList()

    def push(self, Data):
        self.ll.append_start(Data)

    def pop(self):
        data = self.ll.read_specific(0)
        self.ll.delete_specific(0)
        return data

    def printItems(self):

        self.ll.print_linked_list()


if __name__ == '__main__':

    stackList = Stack()  # last in first out

    stackList.push(1)
    stackList.push(2)
    stackList.push(3)
    stackList.push(4)
    stackList.push(5)
    stackList.push(6)
    stackList.push(7)
    stackList.push(8)
    stackList.push(9)
    stackList.push(10)

    stackList.printItems()

    print("we pop 3 values\n")
    print(stackList.pop())
    print(stackList.pop())
    print(stackList.pop())

    print("\n-------------------------\n")
    queueList = Queue()  # first in first out

    queueList.push(1)
    queueList.push(2)
    queueList.push(3)
    queueList.push(4)
    queueList.push(5)
    queueList.push(6)
    queueList.push(7)
    queueList.push(8)
    queueList.push(9)
    queueList.push(10)

    queueList.printItems()

    print("we deque 3 values\n")

    print(queueList.pop())
    print(queueList.pop())
    print(queueList.pop())

    """
    LinkList = LinkedList()  # instantiate a list

    LinkList.append_end("B")  # we add stuff to the end
    LinkList.append_end("B")
    LinkList.append_end("B")
    LinkList.append_end("B")
    LinkList.append_end("B")
    LinkList.append_end("B")

    LinkList.print_linked_list()  # print list
    print("Prints out the whole LinkedList\n\n\n")

    print("The size of the list right now is "+str(LinkList.get_size())) # print the size of the list
    print("Prints out the size of the LinkedList\n\n\n")

    LinkList.append_start("A")  # swaps the head values to a new value
    LinkList.print_linked_list()
    print("Has added A at the start by swapping the 'head' of the LinkedList\n\n\n")

    LinkList.append_specific("F", 2)  # add to specific place in the chain
    LinkList.print_linked_list()
    print("Adds 'F' at index two of the LinkedList\n\n\n")

    LinkList.append_specific("G", 90)  # combining size checking and index placement to give error as the index doesnt exist
    print("Error checking in case the index is not found by using the get.size function\n\n\n")

    LinkList.append_specific("F", -2)  # if the index given is negative it loops back around to add from the back
    LinkList.print_linked_list()
    print("Use of negative number index to add from the back \n\n\n")

    LinkList.delete_specific(2)  # delete the node at the given index
    LinkList.print_linked_list()
    print("Delete a specific node\n\n\n")

    LinkList.replace_specific("K", 2)  # we replace the data at that node, in this case 0 equals to the start
    LinkList.print_linked_list()
    print("Replacing a node at index 2 form B to K, in LinkedList\n\n\n")

    LinkList.read_specific(6)  # we replace the data at that node, in this case 0 equals to the start
    print("Reads a specific node with the use of an index (index 6 in this case)\n\n\n")

    LinkList.replace_specific("Y", 0)  # we replace the data at that node, in this case 0 equals to the start
    LinkList.print_linked_list()
    print("Replacing the data of the first node of LinkedList to Y\n\n\n")

    LinkList.replace_specific("L", -2)  # we replace the data at that node, in this case 0 equals to the start
    LinkList.print_linked_list()
    print("Replacing the data of the second-last node using a negative index, in LinkedList to L\n\n\n")

    if LinkList.find_value("K"):
        print("i have found the value K")
    else:
        print("i have not found the value K")

    if LinkList.find_value("H"):
        print("i have found the value H")
    else:
        print("i have not found the value H")
    print("checking if a value is present in the LinkedList by returning True or False depending on the outcome\n\n\n")

    sys.exit(0)
    """
