class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
 
class CircularLinkedList:
    def __init__(self):
        self.head = None
 
    def insert(self, data):
        new_node = Node(data)
 
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return
 
        current = self.head
 
        while current.next != self.head:
            current = current.next
 
        current.next = new_node
        new_node.next = self.head
 
    # Display the route from any starting stop
    def traverse_from(self, start):
        if self.head is None:
            return
 
        current = self.head
 
        # Find the requested starting stop
        while current.data != start:
            current = current.next
 
            if current == self.head:
                print("Stop not found")
                return
 
        # Display the route once
        first = current
 
        while True:
            print(current.data, end=" -> ")
            current = current.next
 
            if current == first:
                break
 
        print("(back to starting stop)")
 
 
# Test the circular linked list
route = CircularLinkedList()
 
route.insert("Main Gate")
route.insert("Library")
route.insert("Hostel")
route.insert("Cafeteria")
 
route.traverse_from("Main Gate")
route.traverse_from("Hostel")
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
 
class CircularLinkedList:
    def __init__(self):
        self.head = None
 
    def insert(self, data):
        new_node = Node(data)
 
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return
 
        current = self.head
 
        while current.next != self.head:
            current = current.next
 
        current.next = new_node
        new_node.next = self.head
 
    # Display the route from any starting stop
    def traverse_from(self, start):
        if self.head is None:
            return
 
        current = self.head
 
        # Find the requested starting stop
        while current.data != start:
            current = current.next
 
            if current == self.head:
                print("Stop not found")
                return
 
        # Display the route once
        first = current
 
        while True:
            print(current.data, end=" -> ")
            current = current.next
 
            if current == first:
                break
 
        print("(back to starting stop)")
 
 
# Test the circular linked list
route = CircularLinkedList()
 
route.insert("Main Gate")
route.insert("Library")
route.insert("Hostel")
route.insert("Cafeteria")
 
route.traverse_from("Main Gate")
route.traverse_from("Hostel")
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
 
class CircularLinkedList:
    def __init__(self):
        self.head = None
 
    def insert(self, data):
        new_node = Node(data)
 
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return
 
        current = self.head
 
        while current.next != self.head:
            current = current.next
 
        current.next = new_node
        new_node.next = self.head
 
    # Display the route from any starting stop
    def traverse_from(self, start):
        if self.head is None:
            return
 
        current = self.head
 
        # Find the requested starting stop
        while current.data != start:
            current = current.next
 
            if current == self.head:
                print("Stop not found")
                return
 
        # Display the route once
        first = current
 
        while True:
            print(current.data, end=" -> ")
            current = current.next
 
            if current == first:
                break
 
        print("(back to starting stop)")
 
 
# Test the circular linked list
route = CircularLinkedList()
 
route.insert("Main Gate")
route.insert("Library")
route.insert("Hostel")
route.insert("Cafeteria")
 
route.traverse_from("Main Gate")
route.traverse_from("Hostel")
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
 
class CircularLinkedList:
    def __init__(self):
        self.head = None
 
    def insert(self, data):
        new_node = Node(data)
 
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return
 
        current = self.head
 
        while current.next != self.head:
            current = current.next
 
        current.next = new_node
        new_node.next = self.head
 
    # Display the route from any starting stop
    def traverse_from(self, start):
        if self.head is None:
            return
 
        current = self.head
 
        # Find the requested starting stop
        while current.data != start:
            current = current.next
 
            if current == self.head:
                print("Stop not found")
                return
 
        # Display the route once
        first = current
 
        while True:
            print(current.data, end=" -> ")
            current = current.next
 
            if current == first:
                break
 
        print("(back to starting stop)")
 
 
# Test the circular linked list
route = CircularLinkedList()
 
route.insert("Main Gate")
route.insert("Library")
route.insert("Hostel")
route.insert("Cafeteria")
 
route.traverse_from("Main Gate")
route.traverse_from("Hostel")
