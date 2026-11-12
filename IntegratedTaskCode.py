import heapq

#  Stack: retain the most recent 10 visited buildings
class Stack:
    def __init__(self, limit=10):
        self.items, self.limit = [], limit
    def push(self, item):
        if len(self.items) == self.limit:
            self.items.pop(0)
        self.items.append(item)
    def pop(self):
        return self.items.pop() if self.items else None
    def peek(self):
        return self.items[-1] if self.items else None
    def is_empty(self):
        return len(self.items) == 0

# Queue: first shuttle request is served first
class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        return self.items.pop(0) if self.items else None
    def front(self):
        return self.items[0] if self.items else None
    def is_empty(self):
        return len(self.items) == 0

# BST: room records ordered by room code 
class BSTNode:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.left = self.right = None

class BST:
    def __init__(self):
        self.root = None
    def insert(self, key, value):
        def add(node):
            if node is None:
                return BSTNode(key, value)
            if key < node.key:
                node.left = add(node.left)
            elif key > node.key:
                node.right = add(node.right)
            else:
                node.value = value
            return node
        self.root = add(self.root)
    def search(self, key):
        node = self.root
        while node:
            if key == node.key:
                return node.value
            node = node.left if key < node.key else node.right
        return None

#  Hash table: division method and linear probing
class RoomHash:
    def __init__(self, size=11):
        self.size, self.table = size, [None] * size
    def insert(self, key, value):
        index = key % self.size
        for _ in range(self.size):
            if self.table[index] is None or self.table[index][0] == key:
                self.table[index] = (key, value)
                return
            index = (index + 1) % self.size
        raise OverflowError("Hash table is full")
    def search(self, key):
        index = key % self.size
        for _ in range(self.size):
            item = self.table[index]
            if item is None:
                return None
            if item[0] == key:
                return item[1]
            index = (index + 1) % self.size
        return None

#Weighted undirected graph
class CampusGraph:
    def __init__(self):
        self.adj = {}
    def add_building(self, name):
        self.adj.setdefault(name, [])
    def add_path(self, a, b, minutes):
        self.add_building(a)
        self.add_building(b)
        self.adj[a].append((b, minutes))
        self.adj[b].append((a, minutes))
    def dfs(self, start):
        visited, order, stack = set(), [], [start]
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            order.append(node)
            for neighbour, _ in reversed(self.adj[node]):
                if neighbour not in visited:
                    stack.append(neighbour)
        return order
    def bfs(self, start):
        visited, order, queue = {start}, [], [start]
        while queue:
            node = queue.pop(0)
            order.append(node)
            for neighbour, _ in self.adj[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)
        return order
    def shortest_path(self, start, goal):
        distances = {v: float("inf") for v in self.adj}
        previous, distances[start] = {}, 0
        heap = [(0, start)]
        while heap:
            distance, node = heapq.heappop(heap)
            if distance != distances[node]:
                continue
            if node == goal:
                break
            for neighbour, weight in self.adj[node]:
                candidate = distance + weight
                if candidate < distances[neighbour]:
                    distances[neighbour] = candidate
                    previous[neighbour] = node
                    heapq.heappush(heap, (candidate, neighbour))
        if distances[goal] == float("inf"):
            return [], float("inf")
        path, current = [], goal
        while current != start:
            path.append(current)
            current = previous[current]
        path.append(start)
        return list(reversed(path)), distances[goal]

def main():
    graph = CampusGraph()
    buildings = ["Main Gate", "Library", "Administration Block",
                 "Lecture Theatre 1", "Lecture Theatre 2", "Hostel 1",
                 "Hostel 2", "Cafeteria", "Computer Laboratory",
                 "Sports Complex"]
    for building in buildings:
        graph.add_building(building)
    paths = [
        ("Main Gate", "Administration Block", 4),
        ("Main Gate", "Library", 6), ("Main Gate", "Hostel 1", 8),
        ("Administration Block", "Library", 3),
        ("Administration Block", "Lecture Theatre 1", 5),
        ("Library", "Lecture Theatre 1", 4),
        ("Library", "Computer Laboratory", 7),
        ("Lecture Theatre 1", "Lecture Theatre 2", 3),
        ("Lecture Theatre 1", "Cafeteria", 6),
        ("Lecture Theatre 2", "Sports Complex", 5),
        ("Hostel 1", "Hostel 2", 2), ("Hostel 1", "Cafeteria", 4),
        ("Hostel 2", "Sports Complex", 7),
        ("Cafeteria", "Sports Complex", 6),
        ("Computer Laboratory", "Sports Complex", 8)
    ]
    for a, b, minutes in paths:
        graph.add_path(a, b, minutes)

    # Sample room directory: numeric room ID -> room description.
    rooms = {205: "Room 205 - Computer Science Office",
             110: "Room 110 - Registry",
             312: "Room 312 - Networking Laboratory"}
    bst, room_hash = BST(), RoomHash(11)
    for code, description in rooms.items():
        bst.insert(code, description)
        room_hash.insert(code, description)

    # Max-heap for ranking: negative counts make heapq return the
    # largest footfall first.
    footfall = [(1200, "Main Gate"), (950, "Library"),
                (780, "Cafeteria"), (650, "Lecture Theatre 1"),
                (590, "Hostel 1"), (420, "Sports Complex"),
                (310, "Administration Block"), (270, "Computer Laboratory")]
    busiest_heap = [(-count, place) for count, place in footfall]
    heapq.heapify(busiest_heap)

    history, shuttle_queue = Stack(), Queue()
    history.push("Main Gate")
    history.push("Library")
    history.push("Lecture Theatre 1")
    shuttle_queue.enqueue("Shuttle 1: Main Gate to Hostels")
    shuttle_queue.enqueue("Shuttle 2: Main Gate to Town Centre")
    shuttle_queue.enqueue("Shuttle 3: Main Gate to Library")

    print("Campus Navigation and Resource Management System")
    print("DFS:", " -> ".join(graph.dfs("Main Gate")))
    print("BFS:", " -> ".join(graph.bfs("Main Gate")))
    path, minutes = graph.shortest_path("Main Gate", "Sports Complex")
    print("Shortest route:", " -> ".join(path), f"({minutes} minutes)")
    room_id = 205
    print("BST room lookup:", bst.search(room_id))
    print("Hash room lookup:", room_hash.search(room_id))
    # Extract the three highest footfall values from the heap.
    print("Top 3 busiest locations:")
    for _ in range(3):
        negative_count, place = heapq.heappop(busiest_heap)
        print(f"  {place}: {-negative_count} people/day")
    print("Navigation history (oldest to newest):", history.items)
    print("Next shuttle:", shuttle_queue.front())
    print("Shuttle queue:", shuttle_queue.items)

if __name__ == "__main__":
    main()