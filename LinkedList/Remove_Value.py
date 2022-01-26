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
                prev = n.data
                print(prev)
                print(n.data, " ")
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

            n = n.next
        n.next = new_node

    def remove(self, data):
        #Create a dummy node
        dummy_node = Node(0)
        #Point the dummy node to head
        dummy_node.next = self.head
        
        current_head = dummy_node
        while(current_head.next != None):
            if (current_head.next.data == data):
                current_head.next = current_head.next.next
            else:
                current_head = current_head.next


#n = Node(7)
ll = LinkedList()
ll.insert_at_start(7)
ll.insert_at_start(17)
ll.insert_at_start(27)
ll.insert_at_start(37)
ll.remove(17)
ll.traverse_list()
