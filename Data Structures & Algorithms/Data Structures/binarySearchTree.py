from collections.abc import Iterator
from typing import Any

class Node:
    def __init__(self, data: Any) -> None:
        """
        Initializes the Node required for making an object of BinarySearchTree.
        """
        self.data: Any = data
        self.left: Node | None= None
        self.right: Node | None = None

class BinarySearchTree:
    def __init__(self) -> None:
        """
        Creates a brand new object of BinarySearchTree.
        """
        self.root: Node | None = None

    def __iter__(self) -> Iterator:
        """
        Allows loops to be used on the objects from BinarySearchTree data type. For example: for item in binarySearchTree1, 'item' in this would be node.data instead of the Node object.
        """
        def _in_order(node) -> Iterator:
            if node is not None:
                yield from _in_order(node.left)
                yield node.data
                yield from _in_order(node.right)

        return _in_order(self.root)

    def __eq__(self, other: BinarySearchTree) -> bool:
        """
        Allows comparisions to exist for the objects from BinarySearchTree data type. For example: if binarySearchTree1 == binarySearchTree2, this comparison would check if all the values in the tree are the same from left to right.
        """
        if not isinstance(other, BinarySearchTree):
            return False

        return list(self) == list(other)

    def __contains__(self, item:Any) -> bool:
        """
        Checks if a given item exists in an object of BinarySearchTree. For example: if 3 in binarySearchTree1, this is checking if the binary tree 'binarySearchTree1' has a node with the value of 3.
        """
        return item in list(self)

    def __bool__(self) -> bool:
        """
        Returns a boolean value depending on whether the object is empty or not. For example, if binarySearchTree1, this returns True if the 'binarySearchTree1' has at least 1 node, or it returns False if the binary tree is empty.
        """
        return self.root is not None

    def __len__(self) -> int:
        """
        Returns the length of an object of BinarySearchTree type. For example, len(binarySearchTree1), this would return the amount of nodes binary tree holds.
        """
        return sum(1 for _ in self)

    def __and__(self, other: BinarySearchTree) -> BinarySearchTree:
        """
        Returns a new BinarySearchTree containing only the values present in both trees. For example, print(binarySearchTree1 & binarySearchTree2), displays a new BinarySearchTree containing the values that are found in both binarySearchTree1 and binarySearchTree2.
        """
        if not isinstance(other, BinarySearchTree):
            return NotImplemented
        
        if self.root is None or other.root is None:
            return BinarySearchTree()

        binarySearchTree = BinarySearchTree()
        other_set: set = set(other)

        for selfData in self:
            if selfData in other_set:
                binarySearchTree.insert(selfData)

        return binarySearchTree
    
            
    def __or__(self, other: BinarySearchTree) -> BinarySearchTree:
        """
        Returns a new BinarySearchTree containing all combined values from both trees. For example, print(binarySearchTree1 | binarySearchTree2), displays a new BinarySearchTree containing every value found in either tree1 or tree2.
        """
        if not isinstance(other, BinarySearchTree):
            return NotImplemented

        binarySearchTree:BinarySearchTree = BinarySearchTree()
        seen: set = set()

        for selfData in self:
            if selfData not in seen:
                binarySearchTree.insert(selfData)
                seen.add(selfData)

        for otherData in other:
            if otherData not in seen:
                binarySearchTree.insert(otherData)
                seen.add(otherData)
                
        return binarySearchTree
    
    def __xor__(self, other: BinarySearchTree) -> BinarySearchTree:
        """
        Returns a new BinarySearchTree containing only the values present in one tree or the other, but not both. For example, print(binarySearchTree1 ^ binarySearchTree2) displays a new BinarySearchTree containing every value unique to either tree1 or tree2.
        """
        if not isinstance(other, BinarySearchTree):
            return NotImplemented
        
        binarySearchTree = BinarySearchTree()

        selfSet: set = set(self)
        otherSet: set = set(other)

        for item in selfSet:
            if item not in otherSet:
                binarySearchTree.insert(item)

        for item in otherSet:
            if item not in selfSet:
                binarySearchTree.insert(item)


        return binarySearchTree

    def insert(self, data) -> None:
        """
        Inserts the given value in the binary tree in the ascending order. For example, binarySearchTree1.insert(10), this would make a new node holding the value of 10 and then add it to the binarySearchTree1 according to the order.
        """
        newNode: Node = Node(data)
        if self.root is None:
            self.root: Node | None = newNode
            return
        cur: Node | None = self.root
        while True:
            if data < cur.data:
                if cur.left is None:
                    cur.left = newNode
                    return
                cur = cur.left
            else:
                if cur.right is None:
                    cur.right = newNode
                    return
                cur = cur.right
    
    def has(self, data: Any) -> bool:
        """
        Checks whether the given data exists in the binary tree or not. For example, binarySearchTree1.has(10), this would check whether there is a node in binarySearchTree1 which holds the value of 10.
        """
        # if self.root is None:
        #     return False
        # cur: Node | None = self.root
        # while cur is not None:
        #     if data == cur.data:
        #         return True
        #     if data < cur.data:
        #         cur = cur.left
        #     else:
        #         cur = cur.right
        # return False

        return data in self

    def printValues(self) -> None:
        self.__printHelper(self.root)

    def __printHelper(self, cur: Node | None) -> None:
        if cur is None:
            return
        
        self.__printHelper(cur.left)
        print(cur.data)
        self.__printHelper(cur.right)

    def delete(self, data: Any) -> None:
        if self.root is None:
            return
        cur: Node | None = self.root
        parent = None
        is_left = False
        while cur is not None:
            if data == cur.data:
                break
            parent = cur
            if data < cur.data:
                cur = cur.left
                is_left = True
            else:
                cur = cur.right
                is_left = False
        if cur is None:
            return

        if cur.left is not None and cur.right is not None:
            successor: Node = cur.right
            while successor.left is not None:
                successor = successor.left
            successor_data: Any = successor.data
            self.delete(successor_data)
            cur.data = successor_data
            return

        if parent is None:
            if cur.left is None and cur.right is None:
                self.root = None
            elif cur.left is None:
                self.root = cur.right
            elif cur.right is None:
                self.root = cur.left
            return

        if cur.left is None and cur.right is None:
            if is_left:
                parent.left = None
            else:
                parent.right = None
        else:
            child: Node | None = cur.left if cur.left is not None else cur.right
            if is_left:
                parent.left = child
            else:
                parent.right = child

        if self.root is None:
            return
        cur = self.root
        parent:None | Node = None
        is_left:bool = False
        while cur is not None:
            if data == cur.data:
                break
            parent = cur
            if data < cur.data:
                cur = cur.left
                is_left = True
            else:
                cur = cur.right
                is_left = False
        if cur is None:
            return
        if parent is None:
            # deleting the root
            if cur.left is None and cur.right is None:
                self.root = None
            elif cur.left is None:
                self.root = cur.right
            elif cur.right is None:
                self.root = cur.left
            return
        

        if cur.left is None and cur.right is None:
            if is_left:
                parent.left = None
            else:
                parent.right = None
        

        elif cur.left is None or cur.right is None:
            child = cur.left if cur.left is not None else cur.right
            if is_left:
                parent.left = child
            else:
                parent.right = child
        
        
        else:
            successor = cur.right
            while successor.left is not None:
                successor= successor.left
            successor_data = successor.data
            self.delete(successor.data) 
            cur.data = successor.data
    
    def height(self) -> int:
        return self.__heightHelper(self.root)

    def __heightHelper(self, cur: Node | None) -> int:
        if cur is None:
            return 0
        return 1 + max(self.__heightHelper(cur.left), self.__heightHelper(cur.right))

    def breathFirstSearch(self) -> None:
        if self.root is None:
            return
        queue: list[Node] = [self.root]
        while len(queue) > 0:
            value: Node = queue.pop(0)

            print(value.data)
            if value.left is not None:
                queue.append(value.left)
            if value.right is not None:
                queue.append(value.right)

    def depthFirstSearch(self) -> None:
        self.__dfsHelper(self.root)
    
    def __dfsHelper(self, cur: Node | None) -> None:
        if cur is None:
            return 
        
        print(cur.data)

        self.__dfsHelper(cur.left)
        self.__dfsHelper(cur.right)
    
    def count(self, data: Any) -> int:
        return sum(1 for item in self if item == data)
    
    def min(self) -> Any | None:
        if self.root is None:
            return None
        
        cur: Node | None = self.root
        
        while True:
            if cur.left is None:
                break
            cur = cur.left
        return cur.data
    
    def max(self) -> Any | None:
        if self.root is None:
            return None
        
        cur: Node = self.root

        while True:
            if cur.right is None:
                break
            cur = cur.right
        return cur.data

    def printTree(self) -> None:
        pass

if __name__ == "__main__":
    binTree = BinarySearchTree()
    binTree.insert(3)
    binTree.insert(1)
    binTree.insert(2)
    binTree.insert(5)
    binTree.insert(4)
    binTree.insert(3)
    binTree.insert(7)
    binTree.printValues()

    print()
    print("height: " , binTree.height())
    binTree.breathFirstSearch()

    print("Count of 3: ", binTree.count(3))

    print(f"Max: {binTree.max()}, Min: {binTree.min()}")