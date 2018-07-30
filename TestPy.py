class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next

    def getNext(self):
        return self.next
        
    def setNext(self,next):
        if self.next != None:
            next.next = self.next
        self.next = next

class linkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def getSize(self):
        return self.size

    def findTail(self):
        curNode = self.head
        while curNode.next != None:
            curNode = curNode.next
        return curNode.data
        
    def addToEnd(self, data):
        lastNode = self.findTail()
        lastNode.setNext(self)

linkList = linkedList()
linkList.addToEnd("james")
linkList.addToEnd("jack")