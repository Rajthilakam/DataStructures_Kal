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
    
        
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        n = self.head
        while n.next is not None:
            n= n.next
        n.next = new_node;           
        
n = Node(7) 
ll = LinkedList()
ll.traverse_list()