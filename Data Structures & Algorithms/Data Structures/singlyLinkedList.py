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
        cur: Node | None = self.head

        while cur is not None:
            yield cur.data
            cur = cur.next

    def __str__(self) -> str:
        """
        Returns a string holding all the data of each nodes in the linked list. For example: str(singlyLinkedList1), this could result in 'Type: SinglyLinkedList, Values: 2, 3, 1' if the singlyLinkedList1 is holding values 2, 3, 1 in the exact order.
        """
        values: list[str] = []
        for i in self:
            values.append(str(i))
        return f"Type: SinglyLinkedList, Values: {", ".join(values)}"

    def __eq__(self, other: object) -> bool:
        """
        Returns a boolean by comparing all the elements from one SinglyLinkedList object to another. For example: if singlyLinkedList1 == singlyLinkedList2, this comparison would check if all the values in the list are the same from left to right.
        """
        if not isinstance(other, SinglyLinkedList):
            return NotImplemented

        return list(self) == list(other)

    def __contains__(self, item:Any) -> bool:
        """
        Returns a boolean by checking if a given item exists in the linked list or not. For example: if 3 in singlyLinkedList1, this is checking if the linked list 'singlyLinkedList1' has a node with the value of 3.
        """
        return self.has(item)

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
        Returns a new SinglyLinkedList containing all combined values from both lists. For example, print(singlyLinkedList1 | singlyLinkedList2), returns a new SinglyLinkedList containing every value found in either list1 or list2.
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
        newNode: Node = Node(data)

        if self.head is None:
            self.head = newNode
            return self

        cur: Node | None = self.head
        previous: Node | None = None

        for _ in range(idx):
            if cur is None:
                break
            previous = cur
            cur = cur.next

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

    def pop(self) -> Any:
        """
        Removes the last element from the linked list and returns its value, or None if the list is empty. For example, singlyLinkedList1.pop(), this would remove the very last element in the list and return the value that was removed.
        """
        if self.head is None:
            return None

        if self.head.next is None:
            data: Any = self.head.data
            self.head = None
            return data

        cur: Node = self.head
        last: Node = self.head.next

        while last.next is not None:
            cur = last
            last = last.next

        cur.next = None
        return last.data

    def popFirst(self) -> Any:
        """
        Removes the first element from the linked list and returns its value, or None if the list is empty. For example, singlyLinkedList1.popFirst(), this would remove the very first element in the list and return the value that was removed.
        """
        if self.head is None:
            return None

        data: Any = self.head.data
        self.head = self.head.next
        return data

    def remove(self, data: Any) -> SinglyLinkedList:
        """
        Returns the same object, but removes the first given value from the linked list. For example, singlyLinkedList1.remove(10), this would get rid of the first 10 that exists in the list, and then returns the list.
        """
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
        return len(self)

    def count(self, data: Any) -> int:
        """
        Returns an integer representing the amount of times a given value exists in the linked list. For example, singlyLinkedList1.count(10), this would return a number that describes how many times the value 10 exists in the list.
        """
        return sum(1 for item in self if item == data)

    def has(self, data: Any) -> bool:
        """
        Returns a boolean by checking if a given value exists in the linked list or not. For example, singlyLinkedList1.has(10), this would return True if the value 10 exists in the list, or it would return False if the value 10 does not exist in the list.
        """
        cur: Node | None = self.head

        while cur is not None:
            if cur.data == data:
                return True
            cur = cur.next
        return False

    def copy(self) -> SinglyLinkedList:
        """
        Returns a new SinglyLinkedList object that is a copy of the current linked list. For example, singlyLinkedList1.copy(), this would create a new linked list with the same values in the same order as singlyLinkedList1.
        """
        new_list: SinglyLinkedList = SinglyLinkedList()

        for item in self:
            new_list.append(item)
        return new_list

    def clear(self) -> None:
        """
        Clears the linked list, removing all nodes. For example, singlyLinkedList1.clear(), this would remove all elements from the linked list, leaving it empty.
        """
        self.head = None

    def reverse(self) -> SinglyLinkedList:
        """
        Reverses the linked list in place. For example, singlyLinkedList1.reverse(), this would reverse the order of the nodes in the linked list, so if the original order was 10 -> 20 -> 30, after calling reverse() it would become 30 -> 20 -> 10.
        """
        previous: Node | None = None
        current: Node | None = self.head

        while current is not None:
            next_node: Node | None = current.next
            current.next = previous
            previous = current
            current = next_node

        self.head = previous
        return self

    def asString(self) -> str:
        """
        Returns a string with all the values of the nodes found in the linked list in order. For example, singlyLinkedList1.asString(), this would return a string with all the values of the nodes present in the singlyLinkedList.
        """
        values = []
        for i in self:
            values.append(str(i))
        return ", ".join(values)

    def asList(self) -> list:
        """
        Returns a list representation of the linked list, showing the values of each node in order. For example, singlyLinkedList1.asList(), this would return a list like [10, 20, 30] if the linked list contains those values in that order.
        """
        return list(self)

    def asTuple(self) -> tuple:
        """
        Returns a tuple representation of the linked list, showing the values of each node in order. For example, singlyLinkedList1.asTuple(), this would return a tuple like (10, 20, 30) if the linked list contains those values in that order.
        """
        return tuple(self)

    def asSet(self) -> set:
        """
        Returns a set representation of the linked list, showing the unique values of each node. For example, singlyLinkedList1.asSet(), this would return a set like {10, 20, 30} if the linked list contains those values.
        """
        return set(self)

    @staticmethod
    def fromList(values: list) -> SinglyLinkedList:
        """
        Creates a new SinglyLinkedList from a given list of values. For example, SinglyLinkedList.fromList([10, 20, 30]), this would create a new linked list with nodes containing the values 10, 20, and 30.
        """
        singlyLinkedList = SinglyLinkedList()

        for value in values:
            singlyLinkedList.append(value)
        return singlyLinkedList

    @staticmethod
    def fromTuple(values: tuple) -> SinglyLinkedList:
        """
        Creates a new SinglyLinkedList from a given tuple of values. For example, SinglyLinkedList.fromTuple((10, 20, 30)), this would create a new linked list with nodes containing the values 10, 20, and 30.
        """
        singlyLinkedList = SinglyLinkedList()

        for value in values:
            singlyLinkedList.append(value)
        return singlyLinkedList

    @staticmethod
    def fromSet(values: set) -> SinglyLinkedList:
        """
        Creates a new SinglyLinkedList from a given set of values. For example, SinglyLinkedList.fromSet({10, 20, 30}), this would create a new linked list with nodes containing the values 10, 20, and 30.
        """
        singlyLinkedList = SinglyLinkedList()

        for value in values:
            singlyLinkedList.append(value)
        return singlyLinkedList

if __name__ == "__main__":
    newList= SinglyLinkedList()
    newList.append(10).append(20).append(30).append(30)
    print(newList.length())
    print(newList.count(30))
    print(newList.asList())
    print(newList.reverse().asList())
