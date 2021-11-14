class Node:  
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None
  
class LinkedList:  
    # Function to initialize head
    def __init__(self):
        self.head = None
  
    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        
    # Function to print the list        
    def traverse_list(self):
        if self.head is None:
            print("List has no element")
            return
        else:
            n = self.head
            while n is not None:
                print(n.data , " ")
                n = n.next
                
    # Rotate the list by n places            
    def rotate_list(self,k):
        
        if not self.head:
            return self.head
            
    # Get the length of the list
        length,tail = 1,self.head
        while tail.next:
            tail = tail.next
            length+=1
            
    # Get the length of the k if its greater than length of the list
        k = k % length
        if k == 0:
            return self.head
            
    # Move the pointer to the pivot(k) and rotate
        cur = self.head
        for i in range(length-k-1):
            cur = cur.next
        tail.next = self.head
        self.head = cur.next
        cur.next = None
         
# Driver program to test above function
llist = LinkedList()
llist.push(40)
llist.push(30)
llist.push(20)
llist.push(10)
llist.rotate_list(2)  
llist.traverse_list()