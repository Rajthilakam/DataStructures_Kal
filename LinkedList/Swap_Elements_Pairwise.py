class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
 
 
# Helper function to print a given linked list
def printList(msg, head):
 
    print(msg, end='')
    ptr = head
    while ptr:
        print(ptr.data, end=' —> ')
        ptr = ptr.next
 
    print('None')
 
 
# Function to pairwise swap adjacent nodes of a linked list
def rearrange(head):
 
    # if the list is empty or contains just one node
    if head is None or head.next is None:
        return head
 
    curr = head
    prev = None
 
    # consider two nodes at a time and swap their links
    while curr and curr.next:
 
        temp = curr.next
        curr.next = temp.next
        temp.next = curr
 
        if prev is None:
            head = temp
        else:
            prev.next = temp
 
        prev = curr
        curr = curr.next
 
    return head
 
 
if __name__ == '__main__':
 
    head = None
    for i in reversed(range(8)):
        head = Node(i + 1, head)
 
    printList('Before : ', head)
    head = rearrange(head)
    printList('After : ', head)
 