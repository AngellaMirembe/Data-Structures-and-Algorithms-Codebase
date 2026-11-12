class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, shuttle):
        self.items.append(shuttle)

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.items.pop(0)

    def front(self):
        if self.is_empty():
            return "Queue is empty"
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0


# Creating a queue
schedule = Queue()

# Adding shuttles
schedule.enqueue("Shuttle 1")
schedule.enqueue("Shuttle 2")
schedule.enqueue("Shuttle 3")

print("Shuttle Schedule:", schedule.items)
print("Next shuttle:", schedule.front())
print("Shuttle removed:", schedule.dequeue())
print("Is the queue empty?", schedule.is_empty())