class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item): 
        self.stack.append(item)  # add to the end as last on in, first is out, therefore with pop() achieve what we want

    def pop(self):
        return self.stack.pop()  # call pop to get the last item of the array

    def printItems(self):
        for item in self.stack:
            print(item)


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.insert(0,
                          item)  # insert at the start as the first item has to be the last in the array so pop() can retrieve it

    def dequeue(self):
        return self.queue.pop()  # call pop to get the last item of the array

    def printItems(self):
        for item in self.queue:
            print(item)


if __name__ == "__main__":
    stack = Stack()
    print("this works")
    stack.push(1)
    stack.push(2)
    stack.push(3)

    print("Stack contains:")
    stack.printItems()

    print("popping an item from the stack returns: ", stack.pop())

    queue = Queue()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    print("Queue contains:")
    queue.printItems()

    print("dequeue an item from the queue returns: ", queue.dequeue())
