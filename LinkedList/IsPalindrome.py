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
        fast = self.head
        slow = self.head
        
        #Find middle element in the linkedlist
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        #Reverse Second half
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            print(prev.data)
            slow = tmp                

        #Check Palindrome
        left,right = self.head,prev
        while right:
            if left.data != right.data:
                print ("False")
                return False
                
        return True

llist = LinkedList()
llist.push(40)
llist.push(30)
llist.push(20)
llist.push(30)
llist.push(40)
 
llist.palindrome()                    