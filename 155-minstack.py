"""https://www.jianshu.com/p/d0d29864c83e
https://liweiwei1419.github.io/leetcode-solution-blog/leetcode-problemset/stack/0155-min-stack.html#%E6%96%B9%E6%B3%95%E4%B8%80%EF%BC%9A%E8%BE%85%E5%8A%A9%E6%A0%88%E5%92%8C%E6%95%B0%E6%8D%AE%E6%A0%88%E5%90%8C%E6%AD%A5
"""
class MinStack(object):
    def __init__(self):
        self.stack=[]
        self.mins=[]
    
    def push(self,x):
        self.stack.append(x)
        if not self.mins or x <self.mins[-1]:
            self.mins.append(x)
        else:
            self.mins.append(self.mins[-1])
    
    def pop(self):
        self.mins.pop()
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.mins[-1]

# 创建 MinStack 实例
minStack = MinStack()

# 测试 push、pop、top 和 getMin 方法
minStack.push(3)
minStack.push(2)
minStack.push(5)
print("Current stack:", minStack.stack)  # 应该输出 [3, 2, 5]
print("Current min:", minStack.getMin())  # 应该输出 2
print("Top element:", minStack.top())     # 应该输出 5
minStack.pop()
print("After popping, current stack:", minStack.stack)  # 应该输出 [3, 2]
print("After popping, current min:", minStack.getMin()) # 应该输出 2