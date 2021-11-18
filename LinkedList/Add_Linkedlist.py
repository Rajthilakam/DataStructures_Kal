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

    #Print the list
    def traverse_list(self):
        if self.head is None:
            print("List has no element")
            return
        else:
            n = self.head
            while n is not None:
                print(n.data , " ")
                n = n.next    

    #Add the two linkedlist
    def sum_list(self,l1,l2):
        dummyNode = Node(0)
        temp = dummyNode
        carry = 0

        while(l1 is not None or l2 is not None or carry ):
            sum = 0
            if(l1 is not None):
                sum+=l1.data
                l1 = l1.next

            if l2:
                sum+=l2.data
                l2 = l2.next

            sum+=carry
            carry = sum//10
            newNode = Node(sum%10)
            temp.next = newNode
            temp = temp.next

        return dummyNode.next

first = LinkedList()
second = LinkedList()
first.push(6)
first.push(4)
first.push(9)
first.push(5)
first.push(7)

second.push(4)
second.push(8)

result = LinkedList()
result.sum_list(first.head,second.head)






