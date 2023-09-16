#Single Linked List in Python
class Node:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
    
class LinkedList:
    def __init__(self, headNode=None):
        self.headNode = headNode

    def setHead(self, headNode):
        self.headNode = headNode

    def traverse(self):
        nextLink = self.headNode

        while (nextLink != None):
            print(nextLink.head)
            nextLink = nextLink.tail
    
    def size(self):
        count = 0
        nextLink = self.headNode

        while (nextLink != None):
            nextLink = nextLink.tail
            
            count += 1

        return count
    
linkedList = LinkedList()

node1 = Node('firstNode')
node2 = Node('secondNode')
node3 = Node('thirdNode')
node4 = Node('fourthNode')
node5 = Node('fifthNode')

linkedList.setHead(node1)
node1.tail = node5
node5.tail = node4
node4.tail = node2
node2.tail = node3

linkedList.traverse()

print(f'\nsize of linked list: {linkedList.size()}')
