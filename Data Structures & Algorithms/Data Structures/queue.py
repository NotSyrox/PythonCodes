class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self, data=None) -> None:
        if data is not None:
            self.front = Node(data)
            self._count = 1
        else:
            self.front = None
            self._count = 0
    
    def __len__(self):
        return self.size()

    def __repr__(self):
        if self.isEmpty():
            return "The queue is empty!"
        queue = []
        cur = self.front
        while cur is not None:
            queue.append(str(cur.data))
            cur = cur.next
        return " <- ".join(queue)

    def enqueue(self, data) -> None:
        newNode = Node(data)

        if self.front is None:
            self.front = newNode
            self._count += 1
            return
        
        cur = self.front
        while cur.next is not None:
            cur = cur.next
        cur.next = newNode
        
        self._count += 1
    
    def peek(self) -> None:
        print(self.front.data if self.front is not None else "The queue is empty!")

    def dequeue(self) -> None:
        cur = self.front
        if cur is None:
            return
        
        next = self.front.next
        self.front.next = None
        self.front = next
        self._count -= 1

    def size(self):
        return self._count
    
    def isEmpty(self) -> bool:
        return True if self.front is None else False


if __name__ == "__main__":

    queue1 = Queue()

    queue1.enqueue(4)
    queue1.enqueue(4)
    queue1.enqueue(4)

    print(queue1)