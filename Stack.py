class Node :
    def __init__(self,value):
        self.data = value
        self.next = None
class Stack :
    def __init__(self):
        self.top = None
    
    def is_empty(self):
        return self.top == None
    def push(self,value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
    def pop(self):
        if(self.is_empty()):
            return "Stack Is Empty"
        else:
            data = self.top.data
            self.top = self.top.next
            return data
    def peek(self):
        if (self.is_empty()):
            return "stack is empty"
        else:
            return self.top.data

