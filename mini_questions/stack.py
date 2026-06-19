class Node:
    def __init__(self, data):
        self.data = data
        self.down = None

class Stack:
    def __init__(self, data=None):
        if data is not None:
            self.top = Node(data)
            self._count = 1
        else:
            self.top = None
            self._count = 0

    def __len__(self):
        return self.size()

    def __repr__(self):
        datas = []
        cur = self.top
        while cur is not None:
            datas.append(str(cur.data))
            cur = cur.down
        return "\n↓\n".join(datas)
        
    def push(self,data):
        newNode = Node(data)

        if self.top is None:
            self.top = newNode
            self._count+=1
            return
        top = self.top
        self.top = newNode
        self.top.down = top
        self._count += 1

    def pop(self):
        if self.top is None:
            return
        top  = self.top
        self.top = self.top.down
        self._count -= 1
        return top.data

    def isEmpty(self) -> bool:
        return True if self.top is None else False

    def peek(self) -> None:
        if self.top is None:
            return
        return self.top.data

    def size(self) -> int:
        return self._count
    
    def clear(self):
        if self.isEmpty():
            return
        
        self.top = None
        self._count= 0

stack1 = Stack()

stack1.push(1)
stack1.push(2)
stack1.push(3)
print(stack1)
print()
print(stack1.pop())
print(stack1)
print()
print(stack1.peek())
print(stack1.size())
stack1.clear()
print(stack1.isEmpty())
print(stack1)