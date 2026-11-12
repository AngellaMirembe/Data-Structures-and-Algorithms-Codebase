class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
 
class LinkedList:
    def __init__(self):
        self.head = None
 
    # Insert at the beginning
    def insert_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
 
    # Insert at the end
    def insert_tail(self, data):
        new_node = Node(data)
 
        if self.head is None:
            self.head = new_node
            return
 
        current = self.head
        while current.next:
            current = current.next
 
        current.next = new_node
 
    # Delete a stop by its value
    def delete(self, value):
        current = self.head
 
        if current and current.data == value:
            self.head = current.next
            return
 
        while current and current.next:
            if current.next.data == value:
                current.next = current.next.next
                return
            current = current.next
 
    # Display all shuttle stops
    def traverse(self):
        current = self.head
 
        while current:
            print(current.data, end=" -> ")
            current = current.next
 
        print("None")
 
 
# Test the linked list
shuttle = LinkedList()
 
shuttle.insert_tail("Main Gate")
shuttle.insert_tail("Library")
shuttle.insert_tail("Hostel")
shuttle.insert_head("Town Centre")
 
shuttle.traverse()
 
shuttle.delete("Library")
shuttle.traverse()

