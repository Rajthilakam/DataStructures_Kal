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

    def printMiddle(self):
       
        slow = self.head
        fast = self.head
 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
               
        print("The middle element is ", slow.data)    


llist = LinkedList()
   
for i in range(5, 0, -1):
    llist.insert_at_start(i)
    llist.traverse_list()
    llist.printMiddle()         