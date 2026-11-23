from collections.abc import Iterator
from typing import Any

class Node:
    def __init__(self, data: Any) -> None:
        self.data: Any = data
        self.left: Node | None= None
        self.right: Node | None = None

class BinarySearchTree:
    def __init__(self) -> None:
        self.root: Node | None = None

    def __iter__(self) -> Iterator:
        def _in_order(node) -> Iterator:
            if node is not None:
                yield from _in_order(node.left)
                yield node.val
                yield from _in_order(node.right)

        return _in_order(self.root)

    def __eq__(self, other: BinarySearchTree) -> bool:
        if not isinstance(other, BinarySearchTree):
            return False

        return list(self) == list(other)

    def __contains__(self, item:Any) -> bool:
        return self.search(item)

    def __bool__(self) -> bool:
        return self.root is not None

    def __len__(self) -> int:
        return self.count()

    def __and__(self, other: BinarySearchTree) -> BinarySearchTree:
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
    
    def search(self, data: Any) -> bool:
        if self.root is None:
            return False
        cur: Node | None = self.root
        while cur is not None:
            if data == cur.data:
                return True
            if data < cur.data:
                cur = cur.left
            else:
                cur = cur.right
        return False
    
    def printValues(self) -> None:
        self._printHelper(self.root)

    def _printHelper(self, cur: Node | None) -> None:
        if cur is None:
            return
        
        self._printHelper(cur.left)
        print(cur.data)
        self._printHelper(cur.right)

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
        return self._heightHelper(self.root)

    def _heightHelper(self, cur: Node | None) -> int:
        if cur is None:
            return 0
        return 1 + max(self._heightHelper(cur.left), self._heightHelper(cur.right))

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
        self.dfsHelper(self.root)
    
    def dfsHelper(self, cur: Node | None) -> None:
        if cur is None:
            return 
        
        print(cur.data)

        self.dfsHelper(cur.left)
        self.dfsHelper(cur.right)
    
    def count(self) -> int:
        return self._countHelper(self.root)
    
    def _countHelper(self, cur: Node | None) -> int:
        if cur is None:
            return 0
        
        return 1 + self._countHelper(cur.left) + self._countHelper(cur.right)
    
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
    
    def _getLevels(self) -> None:
        pass 

    def printTree(self) -> None:
        pass

if __name__ == "__main__":
    binTree = BinarySearchTree()
    binTree.insert(3)
    binTree.insert(1)
    binTree.insert(2)
    binTree.insert(5)
    binTree.insert(4)
    binTree.insert(7)
    binTree.printValues()

    print()
    print("height: " , binTree.height())
    binTree.breathFirstSearch()

    print("Count: ", binTree.count())

    print(f"Max: {binTree.max()}, Min: {binTree.min()}")