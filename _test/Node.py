# 实现链表的一个节点
class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None    
    
    def getDate(self):
        return self.data
    def getNext(self):
        return self.next
    
    def setData(self, newdata):
        self.data = newdata
    def setNext(self, newnext):
        self.next = newnext
