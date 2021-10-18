from collections import deque
 
 
# Implement stack using two queues
class Stack:
 
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
 
    
    def add(self, data):
        # Push the given item into the first queue
        self.q1.append(data)
 
    # Remove the top item from the stack
    def remove(self):
 
        # if the first queue is empty
        if not self.q1:
            print("Stack Underflow!!")
            exit(0)
 
        # Move all elements except last from the first queue to the second queue
        front = None
        while self.q1:
 
            if len(self.q1) == 1:
                front = self.q1.popleft()
            else:
                self.q2.append(self.q1.popleft())
 
        # Return the last element after moving all elements back to the first queue.
        while self.q2:
            self.q1.append(self.q2.popleft())
 
        return front
 
 
if __name__ == '__main__':
 
    keys = 1, 2, 3, 4, 5
    s = Stack()
 
    for key in keys:
        s.add(key)
    
    while s:
        print(s.remove())
 
    print(s.remove())