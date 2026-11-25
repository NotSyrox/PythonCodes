from collections.abc import Iterator
from typing import Any

class Node:
    def __init__(self, data: Any) -> None:
        """
        Initializes the Node required for making an object of SinglyLinkedList.
        """
        self.data: Any = data
        self.next: Node | None = None

class SinglyLinkedList:
    def __init__(self) -> None:
        """
        Initializes the required things for a new object of SinglyLinkedList.
        """
        self.head: Node | None = None
        
    def __iter__(self) -> Iterator:
        """
        Allows loops to be used on the objects from SinglyLinkedList data type. For example: for item in singlyLinkedList1, 'item' in this would be node.data instead of the Node object.
        """
        def _in_order(node) -> Iterator:
            if node is not None:
                yield node.data
                yield from _in_order(node.next)

        return _in_order(self.head)
    
    def __str__(self) -> str:
        """
        Returns a string holding all the data of each nodes in the linked list. For example: str(singlyLinkedList1), this could result in 'Type: SinglyLinkedList, Values: 2, 3, 1' if the singlyLinkedList1 is holding values 2, 3, 1 in the exact order.
        """
        values: list[str] = []
        for i in self:
            values.append(str(i))
        return f"Type: SinglyLinkedList, Values: {", ".join(values)}"
    
    def __eq__(self, other: SinglyLinkedList) -> bool:
        """
        Returns a boolean by comparing all the elements from one SinglyLinkedList object to another. For example: if singlyLinkedList1 == singlyLinkedList2, this comparison would check if all the values in the tree are the same from left to right.
        """
        if not isinstance(other, SinglyLinkedList):
            return False

        return list(self) == list(other)
    
    def __contains__(self, item:Any) -> bool:
        """
        Returns a boolean by checking if a given item exists in the linked list or not. For example: if 3 in singlyLinkedList1, this is checking if the linked list 'singlyLinkedList1' has a node with the value of 3.
        """
        return item in list(self)
    
    def __bool__(self) -> bool:
        """
        Returns a boolean value depending on whether the SinglyLinkedList object is empty or not. For example, if singlyLinkedList1, this returns True if the 'singlyLinkedList1' has at least 1 node, or it returns False if the linked list is empty.
        """
        return self.head is not None
    
    def __len__(self) -> int:
        """
        Returns the length of an object of SinglyLinkedList type. For example, len(singlyLinkedList1), this would return the amount of nodes the linked list holds.
        """
        return sum(1 for _ in self)
    
    def __and__(self, other: SinglyLinkedList) -> SinglyLinkedList:
        """
        Returns a new SinglyLinkedList containing only the values present in both lists. For example, print(singlyLinkedList1 & singlyLinkedList2), returns a new SinglyLinkedList containing the values that are found in both singlyLinkedList1 and singlyLinkedList2.
        """
        if not isinstance(other, SinglyLinkedList):
            return NotImplemented
        
        if self.head is None or other.head is None:
            return SinglyLinkedList()

        singlyLinkedList = SinglyLinkedList()
        other_counts = {}
        
        for item in other:
            other_counts[item] = other_counts.get(item, 0) + 1

        for selfData in self:
            if other_counts.get(selfData, 0) > 0:
                singlyLinkedList.append(selfData)
                other_counts[selfData] -= 1

        return singlyLinkedList
    
    def __or__(self, other: SinglyLinkedList) -> SinglyLinkedList:
        """
        Returns a new SinglyLinkedList containing all combined values from both trees. For example, print(singlyLinkedList1 | singlyLinkedList2), returns a new SinglyLinkedList containing every value found in either list1 or list2.
        """
        if not isinstance(other, SinglyLinkedList):
            return NotImplemented

        singlyLinkedList = SinglyLinkedList()
        self_counts = {}

        for selfData in self:
            singlyLinkedList.append(selfData)
            self_counts[selfData] = self_counts.get(selfData, 0) + 1

        for otherData in other:
            if self_counts.get(otherData, 0) > 0:
                self_counts[otherData] -= 1
            else:
                singlyLinkedList.append(otherData)

        return singlyLinkedList

    def __xor__(self, other: SinglyLinkedList) -> SinglyLinkedList:
        """
        Returns a new SinglyLinkedList containing only the values present in one list or the other, but not both. For example, print(singlyLinkedList1 ^ singlyLinkedList2) returns a new SinglyLinkedList containing every value unique to either list1 or list2.
        """
        if not isinstance(other, SinglyLinkedList):
            return NotImplemented
        
        singlyLinkedList = SinglyLinkedList()
        self_counts = {}
        other_counts = {}

        for item in self:
            self_counts[item] = self_counts.get(item, 0) + 1

        for item in other:
            other_counts[item] = other_counts.get(item, 0) + 1

        for item in self:
            if other_counts.get(item, 0) > 0:
                other_counts[item] -= 1
            else:
                singlyLinkedList.append(item)

        for item in other:
            if self_counts.get(item, 0) > 0:
                self_counts[item] -= 1
            else:
                singlyLinkedList.append(item)

        return singlyLinkedList

    def insert(self, idx: int, data: Any) -> SinglyLinkedList:
        """
        Returns the same object, but inserts the given value in the linked list at a specific index. For example, singlyLinkedList1.insert(2, 10), this would make a new node holding the value of 10 and then insert it at the index of 2 in the singlyLinkedList1, and at the end returns the list.
        """
        newNode: Node | None = Node(data)
        if self.head is None:
            self.head = newNode
            return self

        cur: Node | None = self.head
        previous: Node | None = None

        for _ in range(idx):
            if cur is None:
                break
            previous: Node | None = cur
            cur: Node | None = cur.next

        if previous is None:
            newNode.next = cur
            self.head = newNode

        else:
            previous.next = newNode
            newNode.next = cur

        return self

    def append(self, data: Any) -> SinglyLinkedList:
        """
        Returns the same object, but appends the given value at the very end of the list. For example, singlyLinkedList1.append(10), this would add a node holding the value of 10 to the end of the list, and then returns the list.
        """
        newNode: Node = Node(data)
        if self.head is None:
            self.head = newNode
            return self

        cur: Node = self.head

        while cur.next is not None:
            cur = cur.next
        cur.next = newNode

        return self

    def prepend(self, data: Any) -> SinglyLinkedList:
        """
        Returns the same object, but prepends the given value at the very start of the list. For example, singlyLinkedList1.prepend(10), this would add a node holding the value of 10 to the start of the list, and then returns the list.
        """
        newNode: Node = Node(data)
        newNode.next = self.head
        self.head = newNode

        return self

    def pop(self) -> SinglyLinkedList:
        """
        Returns the same object, but removes the last element from the linked list. For example, singlyLinkedList1.pop(), this would get rid of the very last element that exists in the list, and then returns the list.
        """
        if self.head is None:
            return self

        if self.head.next is None:
            self.head = None
            return self

        cur: Node = self.head

        while cur.next is not None and cur.next.next is not None:
            cur = cur.next
        cur.next = None

        return self

    def popFirst(self) -> SinglyLinkedList:
        """
        Returns the same object, but removes the first element from the linked list. For example, singlyLinkedList1.popFirst(), this would get rid of the very first element that exists in the list, and then returns the list.
        """
        if self.head is None:
            return self

        if self.head.next is None:
            self.head = None
            return self

        self.head = self.head.next

        return self

    def remove(self, data: Any) -> SinglyLinkedList:
        """
        Returns the same object, but removes the first given value from the linked list. For example, singlyLinkedList1.remove(10), this would get rid of the first 10 that exists in the list, and then returns the list.
        """
        if self.head is None:
            return self

        previous: Node | None = None
        cur: Node | None = self.head

        while cur is not None:
            if cur.data == data:
                if previous is None:
                    self.head = cur.next
                else:
                    previous.next = cur.next
                return self
            previous = cur
            cur = cur.next

        return self

    def length(self) -> int:
        """
        Returns an integer representing the amount of elements in the linked list. For example, singlyLinkedList1.length(), this would return a number that describes the amount of elements there are in the list.
        """
        return len(list(self))

    def count(self, data: Any) -> int: 
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

    def reverse(self) -> None:
        pass

if __name__ == "__main__":
    newList= SinglelyLinkedList()
    newList.append(10)
    newList.append(20)
    newList.append(30)
    newList.append(30)

    print(newList.length())
    print(newList.count(30))


    newList.printList()