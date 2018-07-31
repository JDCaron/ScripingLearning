class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

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
        if not self.head:
            return None
        else: 
            curNode = self.head
            while curNode.next != None:
                curNode = curNode.next
            return curNode
    
    def addToEnd(self, value):
        newNode = Node(value)
        lastNode = self.findTail()
        if lastNode != None:
            lastNode.next = newNode
        else:
            self.head = newNode
        self.size += 1

    def items(self):
        list = []
        thisNode = self.head
        while thisNode:
            list.append(thisNode.data)
            thisNode = thisNode.next
        return list

    def itemAt(self, index):
        if index < self.size:
            curNode = self.head
            count = 0
            while count < index:
                curNode = curNode.next
                count += 1
            return curNode
        else:
            return None

    def removeItem(self, index):
        myNode = self.itemAt(index)
        if myNode:
            nextNode = myNode.next
            if index == 0:
                self.head = myNode.next
            else:
                prevNode = self.itemAt(index - 1)
                if myNode.next:
                    prevNode.next = nextNode
                else:
                    prevNode.next = None
            del myNode
        else:
            print "Node", index, "does not exist"
        

l = linkedList()
l.addToEnd("james")
l.addToEnd("jack")
l.addToEnd("gregg")
l.addToEnd("tim")
l.addToEnd("kevin")
l.addToEnd("spam")

itemToDel = 1

print (l.items())
# print (l.itemAt(itemToDel).data)
l.removeItem(itemToDel)
print (l.items())