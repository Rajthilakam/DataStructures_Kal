#create a node with data and next
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#Create Linkend list with head pointer 
class LinkedList:
    def __init__(self):
        self.head = None  

    #Method to traverse the list    
    def traverse_list(self):
        if self.head is None:
            print("List has no element")
            return
        else:
            n = self.head
            while n is not None:
                print(n.data , " ")
                n = n.next  

    #Method to insert element at the beginning of the list
    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    #Method to merge sorted list
    def merge_sorted_List(l1,l2):
        dummyNode = Node(0)
        sorting = dummyNode

        if not l1:
            return l2
        if not l2:
            return l1
    #Point  sorting to the low value    
        if(l1.data <= l2.data):
            sorting = l1
            l1 = sorting.next

        else:
           sorting = l2
           l2 = sorting.next 

    #Check l1 is less than l2 and change the pointers acccording to that
        while (l1 and l2):
            if(l1.data <= l2.data):
                sorting.next = l1
                sorting = l1
                l1 = sorting.next
            else:
                sorting.next = l2
                sorting = l2
                l2 = sorting.next  

        if (l1.next is None):
            sorting.next = l2

        if (l2.next is None):
            sorting.next = l1    

        return dummyNode.next
