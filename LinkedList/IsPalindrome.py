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

    def palindrome(self):        

        slow = self.head

        stack = []
        
        ispalin = True

        while slow != None:
            stack.append(slow.data)
            
            slow = slow.next
 
        curr = self.head
        while curr != None:    
            # Get the top most element
            i = stack.pop()            
            # Check if data is not
            # same as popped element
            if curr.data == i:
                ispalin = True
            else:
                ispalin = False
                break    
            # Move the pointer
            curr = curr.next   
        print(ispalin)             
        return ispalin
                
        

llist = LinkedList()
llist.push(40)
llist.push(30)
llist.push(10)
llist.push(20)
llist.push(30)
llist.push(40)
 
llist.palindrome()                    