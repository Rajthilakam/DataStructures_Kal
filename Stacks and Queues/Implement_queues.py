class Queue:
 
    # Constructor
    def __init__(self):
        self.s1 = []
        self.s2 = []
 
    # Add an item to the queue
    def enqueue(self, data):
        # push item into the first stack
        self.s1.append(data)
 
    # Remove an item from the queue
    def dequeue(self):
        # if both stacks are empty
        if not self.s1 and not self.s2:
            print("Underflow!!")
            exit(0)
 
        # if the second stack is empty, move elements from the first stack to it
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
 
        # return the top item from the second stack
        return self.s2.pop()
 
 
if __name__ == '__main__':
 
    keys = [1, 2, 3, 4, 5]
    q = Queue()
 
    # insert above keys
    for key in keys:
        q.enqueue(key)
 
    print(q.dequeue())        # 1
    print(q.dequeue())        # 2
 