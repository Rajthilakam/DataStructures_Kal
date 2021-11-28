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
    tail = dummyNode

    while True:
# If any of the list gets completely empty
# directly join all the elements of the other list
        if l1 is None:
            tail.next = l2
            break
        if l2 is None:
            tail.next = l1
            break

        # Compare both the data of the lists and whichever is smaller is
        # appended to the new node of the merged list and the head is changed
        if l1.data <= l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next

        # Advance the tail
        tail = tail.next

    return dummyNode.next



l1 = LinkedList()
l1.insert_at_start(12)
l1.insert_at_start(8)
l1.insert_at_start(6)
l1.insert_at_start(4)
l1.insert_at_start(2)

l2 = LinkedList()
l2.insert_at_start(7)
l2.insert_at_start(5)
l2.insert_at_start(3)
l2.insert_at_start(1)


l3 = LinkedList()
l3.head = merge_sorted_List(l1.head,l2.head)
l3.traverse_list()




          
