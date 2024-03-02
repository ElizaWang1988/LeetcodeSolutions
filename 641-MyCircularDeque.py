"""641-MyCircularDeque

"""
class MyCircularDeque:
    def __init__(self,k:int):
        self.front=0
        self.rear=0
        self.capacity=k+1
        self.arr=[0]*self.capacity

    def insertFront(self,value:int)->bool:
        if self.isFull():
            return False
        self.front=(self.front-1+self.capacity)%self.capacity
        self.arr[self.front]=value
        return True
    
    def insertLast(self,value:int)->bool:
        if self.isFull():
            return False
        self.arr[self.rear]=value
        self.rear=(self.rear+1)%self.capacity
        return True
    
    def deleteFront(self)->bool:
        if self.isEmpty():
            return False    
        self.front=(self.front+1)%self.capacity
        return True
    
    def deleteLast(self)->bool:
        if self.isEmpty():
            return False
        self.rear=(self.rear-1+self.capacity)%self.capacity
        return True
    
    def getFront(self)->int:
        if self.isEmpty():
            return -1
        return self.arr[self.front]
    def getRear(self)->int:
        if self.isEmpty():
            return -1
        return self.arr[(self.rear-1+self.capacity)%self.capacity]
    
    def isEmpty(self)->bool:
        return self.front==self.rear
    
    def isFull(self)->bool:
        return self.front==(self.rear+1)%self.capacity

# 创建一个容量为 3 的双端循环队列
circular_deque = MyCircularDeque(3)

# 在队尾插入元素 1
print(circular_deque.insertLast(1))  # 应该返回 True
# 在队尾插入元素 2
print(circular_deque.insertLast(2))  # 应该返回 True
# 在队尾插入元素 3
print(circular_deque.insertLast(3))  # 应该返回 True
# 在队尾插入元素 4，此时队列已满
print(circular_deque.insertLast(4))  # 应该返回 False

# 获取队头元素
print(circular_deque.getFront())  # 应该返回 1
# 获取队尾元素
print(circular_deque.getRear())   # 应该返回 3

# 在队头插入元素 0
print(circular_deque.insertFront(0))  # 应该返回 True

# 删除队头元素
print(circular_deque.deleteFront())   # 应该返回 True
# 删除队尾元素
print(circular_deque.deleteLast())    # 应该返回 True

# 获取队头元素
print(circular_deque.getFront())  # 应该返回 1
# 获取队尾元素
print(circular_deque.getRear())   # 应该返回 2

