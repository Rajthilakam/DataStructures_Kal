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

    def swap_elements_pairwise(self):
        dummy = Node(0)
        prev, curr = dummy, self.head
        
        while curr and curr.next:
            # store pointers
            newHead = curr.next
            nextCurr = newHead.next
            
            # swap
            prev.next = newHead
            newHead.next = curr
            curr.next = nextCurr

            if (nextCurr is None or nextCurr.next is None):
                curr.next = nextCurr
                break
            
            # move to next pair
            prev = curr
            curr = nextCurr
        
        return dummy.next
        

