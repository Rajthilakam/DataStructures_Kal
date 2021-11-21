class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None  
        
    def traverse_list(self):
        if self.head is None:
            print("List has no element")
            return
        else:
            n = self.head
            while n is not None:
                print(n.data , " ")
                n = n.next  

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def findLoop(self):
        slow = self.head
        fast = self.head
        # Two pointers slow moves by one and fast moves by two steps
        while(slow and fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        # If both meets then there is a loop in the linkedlist
            if slow == fast:
                return True
        return False           


ll = LinkedList()        