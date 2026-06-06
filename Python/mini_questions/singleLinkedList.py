class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next: Node | None = None  # Points to the next node

class SingleLinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None  # Starting point of the list

    def append(self , data) -> None:
        newNode: Node= Node(data)
        if self.head is None:
            self.head = newNode
            return
        cur: Node = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = newNode
        newNode.next = None

    def prepend(self, data) -> None:
        
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def pop(self) -> None:
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        cur = self.head
        while cur.next.next is not None:
            cur = cur.next
        cur.next = None

    def popFirst(self) -> None:
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        self.head = self.head.next

    def remove(self, data) -> None:
        if self.head is None:
            return
        if self.head.next is None and self.head.data == data:
            self.head = None
            return
        previous = None
        cur: Node = self.head
        while cur is not None:
            if cur.data == data:
                if previous is None:
                    self.head = cur
                else:
                    previous.next = cur.next
                return
            previous: Node = cur
            cur = cur.next
        return

    def length(self) -> int:
        if not self.head:
            return 0
        
        count = 0
        cur = self.head
        while cur is not None:
            count+=1
            cur: Node | None = cur.next
        return count

    def count(self, data) -> int: 
        dataCount = 0
        if self.head is None:
            return 0
        cur = self.head
        while cur is not None:
            if cur.data == data:
                dataCount+=1
            cur = cur.next
        return dataCount
    
    def printList(self) -> None:
        if self.head is None:
            print("Singly Linked List is Empty")
            return
        elements:list[any] = []
        cur = self.head

        while cur is not None:
            elements.append(str(cur.data))
            cur: Node | None = cur.next

        print(" -> ".join(elements) + " -> None")

    def insert(self, idx, data) -> None:
        newNode: Node = Node(data)
        if self.head is None:
            self.head = newNode
            return
        cur: Node | None = self.head
        previous: Node | None = None
        for i in range(idx):
            previous: Node | None = cur
            cur: Node | None = cur.next
        if previous is None:
            newNode.next = cur
            self.head = newNode
        else:
            previous.next = newNode
            newNode.next = cur

    def reverse(self) -> None:
        pass

newList= SingleLinkedList()
newList.append(10)
newList.append(20)
newList.append(30)
newList.append(30)

print(newList.length())
print(newList.count(30))


newList.printList()