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

    def printNthNode(self,n):
        main_ptr = self.head
        ref_ptr = self.head
        count = 0

        if(self.head is not None):
            while(count < n ):
                if(ref_ptr is None):
                    print (n,"is greater than the no of nodes in the list")
                    return
   
                ref_ptr = ref_ptr.next
                count += 1
                  
  
        while(ref_ptr is not None):
           main_ptr = main_ptr.next 
           ref_ptr = ref_ptr.next
                       
        print ("Node no.",n,"from last is",main_ptr.data)
                       
  
# Driver program to test above function
llist = LinkedList()
llist.insert_at_start(20)
llist.insert_at_start(4)
llist.insert_at_start(15)
llist.insert_at_start(35)
  
llist.printNthNode(5) 

