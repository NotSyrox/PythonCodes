class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, data) -> None:
        newNode = Node(data)
        if self.root is None:
            self.root = newNode
            return
        cur = self.root
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
    
    def search(self, data):
        if self.root is None:
            return False
        cur = self.root
        while cur is not None:
            if data == cur.data:
                return True
            if data < cur.data:
                cur = cur.left
            else:
                cur = cur.right
        return False
    
    def printValues(self) -> str:
        self._printHelper(self.root)

    def _printHelper(self, cur) -> None:
        if cur is None:
            return
        
        self._printHelper(cur.left)
        print(cur.data)
        self._printHelper(cur.right)

    def delete(self, data) -> None:
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
        pass

    def depthFirstSearch(self) -> None:
        pass

    
binTree = BinarySearchTree()
binTree.insert(3)
binTree.insert(1)
binTree.insert(2)
binTree.insert(5)
binTree.insert(4)
binTree.insert(7)
binTree.printValues()
print()
binTree.delete(5)
binTree.printValues()

print()
print(binTree.height())