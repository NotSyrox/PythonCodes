class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None

class Stack:
    def __init__(self, data=None):
        if data is not None:
            self.top = Node(data)
            self._count = 1
        else:
            self.top = None
            self._count = 0

    def push(self,data):
        newNode = Node(data)

        if self.top is None:
            self.top = newNode
            self._count+=1
            return
        
        newNode.prev = None
        self.top = newNode
        self._count += 1 