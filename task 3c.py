
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
 
def detect_cycle(head):
    slow = head
    fast = head
 
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
 
        if slow == fast:
            return True
 
    return False
 
 
# Create an acyclic list
a = Node("Main Gate")
b = Node("Library")
c = Node("Hostel")
 
a.next = b
b.next = c
 
print("Acyclic list:", detect_cycle(a))
 
 
# Create a cyclic list
x = Node("Gate")
y = Node("Library")
z = Node("Hostel")
 
x.next = y
y.next = z
z.next = x
 
print("Cyclic list:", detect_cycle(x))
