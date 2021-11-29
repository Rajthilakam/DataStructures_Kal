class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
 
 
# Function to print a given linked list
def printList(head):
 
    ptr = head
    while ptr:
        print(ptr.data, end=' —> ')
        ptr = ptr.next
    print('None')
 
def reverse(head):
 
    out = None
    current = head
 
    # traverse the list
    while current:
        
        next = current.next
        # move the current node onto the out
        current.next = out
        out = current
        current = next 
    # fix head
    return out
 
 
# Function to add two lists, `X` and `Y`
def append(X, Y):
 
    head = None 
    # stores the last seen node
    prev = None 
    # initialize carry with 0
    carry = 0 
    # run till both lists are empty
    while X or Y: 
        # sum is X's data + Y's data + carry (if any)
        total = 0
        if X:
            total += X.data
        if Y:
            total += Y.data 
        total += carry 
        # if the sum of a 2–digit number, reduce it and update carry
        carry = total // 10
        total = total % 10 
        # create a new node with the calculated sum
        node = Node(total) 
        # if the output list is empty
        if head is None:
            # update `prev` and `head` to point to the new node
            prev = node
            head = node
        else:
            # add the new node to the output list
            prev.next = node 
            # update the previous node to point to the new node
            prev = node 
        # advance `X` and `Y` for the next iteration of the loop
        X = X.next if X else X
        Y = Y.next if Y else Y 
    if carry:
        prev.next = Node(carry, prev.next)
    return head
 
 
# Function to add two lists, `X` and `Y`
def addLists(X, Y):
 
    # reverse `X` and `Y` to access elements from the end
    X = reverse(X)
    Y = reverse(Y)
 
    return reverse(append(X, Y))
 
 
if __name__ == '__main__':
 
    x = 5734
    y = 946
 
    # construct list `X` (5 —> 7 —> 3 —> 4) from number `x`
    X = None
    while x:
        X = Node(x % 10, X)
        x = x // 10
 
    # construct list `Y` (9 —> 4 —> 6) from number `y`
    Y = None
    while y:
        Y = Node(y % 10, Y)
        y = y // 10
 
    printList(addLists(X, Y))
 

