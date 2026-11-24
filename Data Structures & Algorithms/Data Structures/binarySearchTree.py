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
        Returns a boolean by comparing all the elements from one BinarySearchTree object to another. For example: if binarySearchTree1 == binarySearchTree2, this comparison would check if all the values in the tree are the same from left to right.
        """
        if not isinstance(other, BinarySearchTree):
            return False

        return list(self) == list(other)

    def __contains__(self, item:Any) -> bool:
        """
        Returns a boolean by checking if a given item exists in the binary tree or not. For example: if 3 in binarySearchTree1, this is checking if the binary tree 'binarySearchTree1' has a node with the value of 3.
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
        seen: set = set()

        for selfData in self:
            if selfData in other_set and selfData not in seen:
                binarySearchTree.insert(selfData)
                seen.add(selfData)

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

    def insert(self, data) -> BinarySearchTree:
        """
        Returns the same object, but also inserts the given value in the binary tree in the ascending order. For example, binarySearchTree1.insert(10), this would make a new node holding the value of 10 and then add it to the binarySearchTree1 according to the order, and at the end return the tree.
        """
        newNode: Node = Node(data)
        if self.root is None:
            self.root: Node | None = newNode
            return self
        cur: Node | None = self.root
        while True:
            if data < cur.data:
                if cur.left is None:
                    cur.left = newNode
                    return self
                cur = cur.left
            else:
                if cur.right is None:
                    cur.right = newNode
                    return self
                cur = cur.right
    
    def has(self, data: Any) -> bool:
        """
        Returns a boolean based on if the given data exists in the binary tree or not. For example, binarySearchTree1.has(10), this would return true if there is a node in binarySearchTree1 which holds the value of 10, else it would return False.
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
        """
        Prints the values of the nodes in the binary tree. For example, binarySearchTree1.printValues(), this would print out all the values of the nodes present in the binarySearchTree.
        """
        self.__printHelper(self.root)

    def __printHelper(self, cur: Node | None) -> None:
        """
        Private helper function for printing out each values of the nodes in the binary tree. Helps by recursively calling itself and printing the values.
        """
        if cur is None:
            return
        
        self.__printHelper(cur.left)
        print(cur.data)
        self.__printHelper(cur.right)

    def delete(self, data: Any) -> None:
        """
        Returns the same object, but also deletes the first node it finds from in the binary tree with the given value. For example, binarySearchTree1.delete(10), this would search for the value 10 and delete that node if found and move the other nodes accordingly, finally it would return the tree. 
        """
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
            successor_parent: Node = cur
            successor: Node = cur.right
            while successor.left is not None:
                successor_parent = successor
                successor = successor.left
            cur.data = successor.data
            if successor_parent == cur:
                successor_parent.right = successor.right
            else:
                successor_parent.left = successor.right
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
    
    def height(self) -> int:
        """
        Returns an integer representing the height of the binary tree. For example, binarySearchTree1.height(), this would check the amount of levels the binary tree has and returns that.
        """
        return self.__heightHelper(self.root)

    def __heightHelper(self, cur: Node | None) -> int:
        """
        Private helper function for height() method. This function is used for calculating the height of the binary tree. Helps by recursively calling itself and calculating the height.
        """
        if cur is None:
            return 0
        return 1 + max(self.__heightHelper(cur.left), self.__heightHelper(cur.right))

    def breathFirstSearch(self) -> None:
        """
        Performs a breadth-first search (level-order traversal) on the binary tree and prints out each node's value level by level, from top to bottom and left to right.
        """
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
        """
        Performs a pre-order depth-first search on the binary tree, printing the current node's value before recursively visiting its left and right subtrees.
        """
        self.__dfsHelper(self.root)
    
    def __dfsHelper(self, cur: Node | None) -> None:
        """
        Private helper function for depthFirstSearch() method. This function is used for performing a pre-order traversal of the binary tree. Helps by printing the current node's data and recursively calling itself on the left and right subtrees.
        """
        if cur is None:
            return 
        
        print(cur.data)

        self.__dfsHelper(cur.left)
        self.__dfsHelper(cur.right)
    
    def count(self, data: Any) -> int:
        """
        Returns an integer that represents the amount of a value present in the binary tree. For example, binarySearchTree1.count(10), this counts and returns the total amount of 10s that are present in the entire binary tree.
        """
        return sum(1 for item in self if item == data)
    
    def min(self) -> Any | None:
        """
        Returns the value that is the lowest/minimum in the whole binary tree. For example, binarySearchTree1.min(), this would return the data that is the lowest in the tree, or on the left most side of the tree.
        """
        if self.root is None:
            return None
        
        cur: Node | None = self.root
        
        while True:
            if cur.left is None:
                break
            cur = cur.left
        return cur.data
    
    def max(self) -> Any | None:
        """
        Returns the value that is the highest/maximum in the whole binary tree. For example, binarySearchTree1.max(), this would return the data that is the highest in the tree, or on the right most side of the tree.
        """
        if self.root is None:
            return None
        
        cur: Node = self.root

        while True:
            if cur.right is None:
                break
            cur = cur.right
        return cur.data

    def printTree(self) -> None:
        """
        Prints all the nodes of a binary tree in a binary tree pattern using root, left/right nodes, and arrows.
        """
        pass

if __name__ == "__main__":
    binTree = BinarySearchTree()
    binTree.insert(3).insert(1).insert(2).insert(5).insert(4).insert(3).insert(7)
    binTree.printValues()

    print()
    print("height: " , binTree.height())
    binTree.breathFirstSearch()
    print()
    binTree.depthFirstSearch()

    print("Count of 3: ", binTree.count(3))

    print(f"Max: {binTree.max()}, Min: {binTree.min()}")