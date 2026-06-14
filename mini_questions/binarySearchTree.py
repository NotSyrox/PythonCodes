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
        while True:
            if data == cur.data:
                return True
            if data < cur.data:
                if cur.left is None:
                    return False
                if cur.left == data:
                    return True
                cur = cur.left
            else:
                if cur.right is None:
                    return None
                if cur.right == data:
                    return True
                cur = cur.right

    def printTree(self) -> None:
        raise NotImplementedError
binTree = BinarySearchTree()
binTree.insert(1)
binTree.insert(2)
binTree.insert(3)
binTree.insert(4)
binTree.insert(5)


binTree.search(4)