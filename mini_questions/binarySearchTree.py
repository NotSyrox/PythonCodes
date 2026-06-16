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
        if self.root is None:
            return
        queue = [self.root]
        while len(queue) > 0:
            value = queue.pop(0)

            print(value.data)
            if value.left is not None:
                queue.append(value.left)
            if value.right is not None:
                queue.append(value.right)

    def depthFirstSearch(self) -> None:
        self.dfsHelper(self.root)
    
    def dfsHelper(self, cur) -> None:
        if cur is None:
            return 
        print(cur.data)
        self.dfsHelper(cur.left)
        self.dfsHelper(cur.right)
    
    def count(self,) -> int:
        return self._countHelper(self.root)
    
    def _countHelper(self, cur):
        if cur is None:
            return 0
        return 1 + self._countHelper(cur.left) + self._countHelper(cur.right)
    
    def min(self) -> int:
        cur = self.root
        if cur is None:
            return
        while True:
            if cur.left is None:
                break
            cur = cur.left
        return cur.data
    
    def max(self) -> int:
        cur = self.root
        if cur is None:
            return
        while True:
            if cur.right is None:
                break
            cur = cur.right
        return cur.data
    
    def _getLevels(self):
        pass 

    def printTree(self) -> None:
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
print("height: " , binTree.height())
binTree.breathFirstSearch()

print("Count: ", binTree.count())

print(f"Max: {binTree.max()}, Min: {binTree.min()}")

