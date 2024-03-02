"""232-Implement queue using stack

"""
class Stack(object):
    def __init__(self):
        self.stack=[]

    def push(self,x):
        self.stack.append(x)

    def pop(self):
        if self.is_empty:
            return None
        return self.stack.pop()

    @property
    def length(self):               # 获取栈中元素
        return len(self.stack)
    
    @property                      
    def is_empty(self):            # 获取栈的状态：是否为空
        return self.length == 0

class MyQueue(object):
    def __init__(self):
        self.stack1=Stack()
        self.stack2=Stack()

    def push(self,x):
        self.stack1.push(x)

    def pop(self):
        while self.stack1.length>1:
            self.stack2.push(self.stack1.pop())
            res=self.stack1.pop()
            while not self.stack2.is_empty:
                self.stack1.push(self.stack2.pop())
            return res

    def peek(self):
        while self.stack1.length>1:
            self.stack2.push(self.stack1.pop())
        res=self.stack1.pop()
        self.stack1.push(res)
        while not self.stack2.is_empty:
            self.stack1.push(self.stack2.pop())
        return res
    
    def empty(self):
        return self.stack1.is_empty




