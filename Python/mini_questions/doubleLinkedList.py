class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next= None 
        self.prev = None

class DoubleLinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None 
        self.tail: Node | None = None

    def append(self, data:int) -> None:
        newNode: Node = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            return 
        cur: Node = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = newNode
        newNode.prev = cur
        self.tail = newNode

    def prepend(self, data) -> None:
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            return
        self.head.prev = newNode
        newNode.next = self.head
        self.head = newNode
        # No loop needed! The tail node hasn't changed.

    def pop(self) -> None:
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            self.tail = None
            return
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        previous = cur.prev
        previous.next = None
        cur.prev = None
        self.tail = previous

    def popFirst(self) -> None:
        if self.head is None:
            return 
        if self.head.next is None:
            self.head = None
            self.tail = None
            return
        self.head = self.head.next
        self.head.prev = None

    def remove(self, data:int) -> None:
        if self.head is None:
            return
        cur = self.head
        while cur is not None:
            if cur.data != data:
                cur = cur.next
            else:
                break
        if cur is None:
            return
        if cur == self.head:
            after = cur.next
            if after is None:
                self.head = None
                self.tail = None
                return
            self.head = after
            cur.next = None
            after.prev = None
            return
        if cur == self.tail:
            before = cur.prev
            if before is None:
                self.head = None
                self.tail = None
                return
            self.tail = before
            cur.prev = None
            before.next = None
            return
        nex = cur.next
        previous = cur.prev 
        nex.prev = previous
        previous.next = nex

    def length(self) -> int:
        count = 0
        if self.head is None:
            return count
        cur = self.head
        while cur is not None:
            count+=1
            cur = cur.next
        return count

    def count(self, data) -> int: 
        count = 0
        if self.head is None:
            return count
        cur = self.head
        while cur is not None:
            if cur.data == data:
                count+=1
            cur = cur.next
        return count
    
    def printList(self) -> None:
        if self.head is None:
            print("Doubly Linked List is Empty")
            return
        elements:list[str] = []
        cur: Node | None = self.head

        while cur is not None:
            elements.append(str(cur.data))
            cur = cur.next

        print("None <-> " + " <-> ".join(elements) + " <-> None")

    def insert(self, idx, data) -> None:
        newNode: Node = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            return
        
        cur: Node = self.head
        previous: Node | None = None
        for _ in range(idx):
            previous: Node | None = cur
            if cur is not None:
                cur = cur.next
                
        if previous is None:
            newNode.next = self.head
            if self.head is not None:
                self.head.prev = newNode
            self.head = newNode
            return
            
        if cur is None:
            previous.next = newNode
            newNode.prev = previous
            self.tail = newNode
            return
            
        previous.next = newNode
        newNode.prev = previous
        newNode.next = cur
        cur.prev = newNode

    def reverse(self) -> None:
        pass

linList = DoubleLinkedList()
linList.append(1)
linList.append(2)
linList.append(3)
linList.append(4)
linList.append(5)
linList.remove(3)
linList.printList()