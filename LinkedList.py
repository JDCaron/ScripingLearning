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


class linkedList(object):
    def __init__(self, items):
        self.size = 0
        self.head = None
        for each in items:
            self.append(each)

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
    
    def append(self, value):
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

    def deleteAt(self, index):
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
            print ("Node", index, "does not exist")

    def insertAt(self, value, index):
        newNode = Node(value)
        nextNode = self.itemAt(index)
        if index != 0:
            prevNode = self.itemAt(index - 1)
            if prevNode:
                prevNode.next = newNode
                if nextNode:
                    newNode.next = nextNode
                self.size += 1
            else:
                print index, 'is out of range'
                print 'Current list length range is:', "0 -", self.getSize()
        else:
            self.head = newNode
            if nextNode:
                newNode.next = nextNode
            self.size += 1
            
    def replaceAt(self, value, index):
        newNode = Node(value)
        oldNode = self.itemAt(index)
        if oldNode:
            newNode.next = oldNode.next
            oldNode.next = None
            if index != 0:
                prevNode = self.itemAt(index - 1)
                prevNode.next = newNode
            else:
                self.head = newNode                
            del oldNode
        else:
            print 'Node',index,'does not exist'


l = linkedList(["james", "jack", "gregg", "tim", "kevin", "spam"])

l.insertAt("julia", 6)
print (l.items())

l.replaceAt("stacey", 2)
print (l.items())


# itemToDel = 1
# l.deleteAt(itemToDel)
# print (l.items())
